# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/aymara_ai/resources/health.py">check</a>() -> None</code>

# Evals

Types:

```python
from aymara_ai.types import (
    Eval,
    EvalPrompt,
    EvalResponse,
    EvalRunRequest,
    EvalRunResult,
    PromptExample,
    Status,
    EvalListResponsesResponse,
)
```

Methods:

- <code title="post /v2/evals">client.evals.<a href="./src/aymara_ai/resources/evals.py">create</a>(\*\*<a href="src/aymara_ai/types/eval_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">Eval</a></code>
- <code title="get /v2/evals">client.evals.<a href="./src/aymara_ai/resources/evals.py">list</a>(\*\*<a href="src/aymara_ai/types/eval_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">SyncOffsetPage[Eval]</a></code>
- <code title="delete /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals.py">delete</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_delete_params.py">params</a>) -> None</code>
- <code title="post /v2/eval-runs/{eval_run_uuid}/continue">client.evals.<a href="./src/aymara_ai/resources/evals.py">continue_run</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/eval_continue_run_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_run_result.py">EvalRunResult</a></code>
- <code title="post /v2/eval-runs">client.evals.<a href="./src/aymara_ai/resources/evals.py">create_run</a>(\*\*<a href="src/aymara_ai/types/eval_create_run_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_run_result.py">EvalRunResult</a></code>
- <code title="delete /v2/eval-runs/{eval_run_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals.py">delete_run</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/eval_delete_run_params.py">params</a>) -> None</code>
- <code title="get /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals.py">get</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_get_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">Eval</a></code>
- <code title="get /v2/eval-runs/{eval_run_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals.py">get_run</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/eval_get_run_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_run_result.py">EvalRunResult</a></code>
- <code title="get /v2/evals/{eval_uuid}/prompts">client.evals.<a href="./src/aymara_ai/resources/evals.py">list_prompts</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_list_prompts_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_prompt.py">SyncOffsetPage[EvalPrompt]</a></code>
- <code title="get /v2/eval-runs/{eval_run_uuid}/responses">client.evals.<a href="./src/aymara_ai/resources/evals.py">list_responses</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/eval_list_responses_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_list_responses_response.py">SyncOffsetPage[EvalListResponsesResponse]</a></code>
- <code title="get /v2/eval-runs">client.evals.<a href="./src/aymara_ai/resources/evals.py">list_runs</a>(\*\*<a href="src/aymara_ai/types/eval_list_runs_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_run_result.py">SyncOffsetPage[EvalRunResult]</a></code>

# EvalTypes

Types:

```python
from aymara_ai.types import EvalType, EvalTypeListResponse
```

Methods:

- <code title="get /v2/eval-types">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">list</a>() -> <a href="./src/aymara_ai/types/eval_type_list_response.py">EvalTypeListResponse</a></code>
- <code title="get /v2/eval-types/{eval_type_uuid}">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">get</a>(eval_type_uuid) -> <a href="./src/aymara_ai/types/eval_type.py">EvalType</a></code>

# Reports

Types:

```python
from aymara_ai.types import EvalSuiteReport
```

Methods:

- <code title="post /v2/eval-reports">client.reports.<a href="./src/aymara_ai/resources/reports.py">create</a>(\*\*<a href="src/aymara_ai/types/report_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_suite_report.py">EvalSuiteReport</a></code>
- <code title="get /v2/eval-reports">client.reports.<a href="./src/aymara_ai/resources/reports.py">list</a>(\*\*<a href="src/aymara_ai/types/report_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_suite_report.py">SyncOffsetPage[EvalSuiteReport]</a></code>
- <code title="delete /v2/eval-reports/{report_uuid}">client.reports.<a href="./src/aymara_ai/resources/reports.py">delete</a>(report_uuid, \*\*<a href="src/aymara_ai/types/report_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/eval-reports/{report_uuid}">client.reports.<a href="./src/aymara_ai/resources/reports.py">get</a>(report_uuid, \*\*<a href="src/aymara_ai/types/report_get_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_suite_report.py">EvalSuiteReport</a></code>

# Files

Types:

```python
from aymara_ai.types import FileCreateResponse
```

Methods:

- <code title="post /v2/files">client.files.<a href="./src/aymara_ai/resources/files.py">create</a>(\*\*<a href="src/aymara_ai/types/file_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/file_create_response.py">FileCreateResponse</a></code>
