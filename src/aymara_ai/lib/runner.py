"""
EvalRunner & AsyncEvalRunner: Simple orchestrators for Aymara SDK evals (sync and async).

"""

import asyncio
from typing import Any, Dict, List, Union, Callable, Optional, Awaitable
from pathlib import Path

from aymara_ai import AymaraAI, AsyncAymaraAI
from aymara_ai.lib.async_utils import wait_until_complete
from aymara_ai.types.eval_prompt import EvalPrompt
from aymara_ai.types.shared_params import FileReference
from aymara_ai.types.eval_response_param import EvalResponseParam
from aymara_ai.types.evals.eval_run_result import EvalRunResult


class EvalRunner:
    """
    Orchestrates the evaluation process for Aymara SDK using a user-provided model callable.
    Stores all state internally. For synchronous (blocking) use with AymaraClient.
    """

    def __init__(
        self,
        client: AymaraAI,
        model_callable: Callable[..., Any],
    ):
        """
        Args:
            client: An instance of AymaraClient.
            model_callable: Callable for model inference (prompt, system_prompt) -> str or Path (for image).
        """
        self.client = client
        self.model_callable = model_callable
        self.eval_id: Optional[str] = None
        self.run_id: Optional[str] = None
        self.eval_run_result: Optional[Any] = None

    @staticmethod
    def _default_response_adapter(model_output: Union[str, Path], prompt: EvalPrompt) -> EvalResponseParam:
        """
        Adapts model output to EvalResponseParam or FileReferenceParam based on type.
        """

        if isinstance(model_output, (str, bytes)):
            return EvalResponseParam(content=model_output, prompt_uuid=prompt.prompt_uuid)
        elif isinstance(model_output, Path):  # type: ignore
            # For image, wrap in FileReferenceParam
            return EvalResponseParam(
                content=FileReference(local_file_path=str(model_output.absolute)),
                prompt_uuid=prompt.prompt_uuid,
                content_type="image",
            )
        else:
            raise ValueError("Unsupported model output type for response adapter.")

    def run_eval(
        self,
        eval_params: Dict[str, Any],
        system_prompt: Optional[str] = None,
        timeout: float = 120.0,
        poll_interval: float = 5.0,
    ) -> EvalRunResult:
        """
        Orchestrate the full eval flow (sync).
        """
        # 1. Create eval
        eval_obj = self.client.evals.create(**eval_params)
        self.eval_id = eval_obj.eval_uuid

        # 2. Wait for eval readiness

        eval_obj = wait_until_complete(self.client.evals.get, resource_id=str(self.eval_id))

        # 3. Fetch prompts
        prompts_response = self.client.evals.list_prompts(self.eval_id)
        prompts = prompts_response.items

        # 4. Model inference and response adaptation
        responses: List[EvalResponseParam] = []
        for prompt in prompts:
            model_output = self.model_callable(prompt.content, system_prompt)
            response = self._default_response_adapter(model_output, prompt)
            responses.append(response)

        # 5. Create eval run
        eval_run = self.client.evals.runs.create(eval_uuid=self.eval_id, responses=responses)
        self.run_id = eval_run.eval_run_uuid

        # 6. Wait for eval run completion
        eval_run = wait_until_complete(self.client.evals.runs.get, resource_id=str(self.run_id))
        self.eval_run_result = eval_run
        return eval_run


class AsyncEvalRunner:
    """
    Orchestrates the evaluation process for Aymara SDK using a user-provided async model callable.
    Stores all state internally. For asynchronous use with AsyncAymaraClient.
    """

    def __init__(
        self,
        client: AsyncAymaraAI,
        model_callable: Callable[..., Awaitable[Any]],
    ):
        """
        Args:
            client: An instance of AsyncAymaraClient.
            model_callable: Async callable for model inference (prompt, system_prompt) -> str or Path (for image).
        """
        self.client = client
        self.model_callable = model_callable
        self.eval_id: Optional[str] = None
        self.run_id: Optional[str] = None
        self.eval_run_result: Optional[Any] = None

    @staticmethod
    def _default_response_adapter(model_output: Any, prompt: Any) -> Any:
        """
        Adapts model output to EvalResponseParam or FileReferenceParam based on type.
        """

        if isinstance(model_output, str):
            return EvalResponseParam(content=model_output, prompt_uuid=prompt.prompt_uuid)
        elif isinstance(model_output, Path):
            # For image, wrap in FileReference
            # Try both possible FileReference imports for compatibility
            file_ref = FileReference(remote_file_path=str(model_output))
            return EvalResponseParam(content=file_ref, prompt_uuid=prompt.prompt_uuid, content_type="image")
        else:
            raise ValueError("Unsupported model output type for response adapter.")

    async def run_eval(
        self,
        eval_params: Dict[str, Any],
        system_prompt: Optional[str] = None,
        timeout: float = 120.0,
        poll_interval: float = 5.0,
    ) -> EvalRunResult:
        """
        Orchestrate the full eval flow (async).
        """
        # 1. Create eval
        eval_obj = await self.client.evals.create(**eval_params)
        self.eval_id = eval_obj.eval_uuid

        # 2. Wait for eval readiness
        async def wait_until_complete_async(
            get_fn: Callable[..., Awaitable[Any]], resource_id: str, poll_interval: float, timeout: float
        ) -> Any:
            start = asyncio.get_event_loop().time()
            while True:
                obj = await get_fn(resource_id=resource_id)
                if getattr(obj, "status", None) == "ready":
                    return obj
                if asyncio.get_event_loop().time() - start > timeout:
                    raise TimeoutError("Eval did not become ready in time.")
                await asyncio.sleep(poll_interval)

        eval_obj = await wait_until_complete_async(
            self.client.evals.get, resource_id=str(self.eval_id), poll_interval=poll_interval, timeout=timeout
        )

        # 3. Fetch prompts
        prompts_response = await self.client.evals.list_prompts(self.eval_id)
        prompts = prompts_response.items

        # 4. Model inference and response adaptation
        responses: List[EvalResponseParam] = []
        for prompt in prompts:
            model_output = await self.model_callable(prompt.content, system_prompt)
            response = self._default_response_adapter(model_output, prompt)
            responses.append(response)

        # 5. Create eval run
        eval_run = await self.client.evals.runs.create(eval_uuid=self.eval_id, responses=responses)
        self.run_id = eval_run.eval_run_uuid

        # 6. Wait for eval run completion
        eval_run = await wait_until_complete_async(
            self.client.evals.runs.get, resource_id=str(self.run_id), poll_interval=poll_interval, timeout=timeout
        )
        self.eval_run_result = eval_run
        return eval_run
