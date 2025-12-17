# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library, maybe_coerce_boolean
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AymaraAIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import evals, files, health, reports, eval_types
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.reports import ReportsResource, AsyncReportsResource
    from .resources.eval_types import EvalTypesResource, AsyncEvalTypesResource
    from .resources.evals.evals import EvalsResource, AsyncEvalsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "AymaraAI",
    "AsyncAymaraAI",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.aymara.ai",
    "staging": "https://staging-api.aymara.ai",
    "development": "http://localhost:8000",
}


class AymaraAI(SyncAPIClient):
    # client options
    api_key: str
    bearer_token: str | None
    use_sandbox: bool | None

    _environment: Literal["production", "staging", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        use_sandbox: bool | None = None,
        environment: Literal["production", "staging", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous AymaraAI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `AYMARA_AI_API_KEY`
        - `bearer_token` from `AYMARA_AI_BEARER_TOKEN`
        - `use_sandbox` from `AYMARA_AI_USE_SANDBOX`
        """
        if api_key is None:
            api_key = os.environ.get("AYMARA_AI_API_KEY")
        if api_key is None:
            raise AymaraAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the AYMARA_AI_API_KEY environment variable"
            )
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("AYMARA_AI_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if use_sandbox is None:
            use_sandbox = maybe_coerce_boolean(os.environ.get("AYMARA_AI_USE_SANDBOX")) or False
        self.use_sandbox = use_sandbox

        self._environment = environment

        base_url_env = os.environ.get("AYMARA_AI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `AYMARA_AI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def evals(self) -> EvalsResource:
        from .resources.evals import EvalsResource

        return EvalsResource(self)

    @cached_property
    def eval_types(self) -> EvalTypesResource:
        from .resources.eval_types import EvalTypesResource

        return EvalTypesResource(self)

    @cached_property
    def reports(self) -> ReportsResource:
        from .resources.reports import ReportsResource

        return ReportsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def with_raw_response(self) -> AymaraAIWithRawResponse:
        return AymaraAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AymaraAIWithStreamedResponse:
        return AymaraAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._auth_bearer}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    def _auth_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Use-Sandbox": str(self.use_sandbox) if self.use_sandbox is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        use_sandbox: bool | None = None,
        environment: Literal["production", "staging", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            use_sandbox=use_sandbox or self.use_sandbox,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAymaraAI(AsyncAPIClient):
    # client options
    api_key: str
    bearer_token: str | None
    use_sandbox: bool | None

    _environment: Literal["production", "staging", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        use_sandbox: bool | None = None,
        environment: Literal["production", "staging", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAymaraAI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `AYMARA_AI_API_KEY`
        - `bearer_token` from `AYMARA_AI_BEARER_TOKEN`
        - `use_sandbox` from `AYMARA_AI_USE_SANDBOX`
        """
        if api_key is None:
            api_key = os.environ.get("AYMARA_AI_API_KEY")
        if api_key is None:
            raise AymaraAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the AYMARA_AI_API_KEY environment variable"
            )
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("AYMARA_AI_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if use_sandbox is None:
            use_sandbox = maybe_coerce_boolean(os.environ.get("AYMARA_AI_USE_SANDBOX")) or False
        self.use_sandbox = use_sandbox

        self._environment = environment

        base_url_env = os.environ.get("AYMARA_AI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `AYMARA_AI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def evals(self) -> AsyncEvalsResource:
        from .resources.evals import AsyncEvalsResource

        return AsyncEvalsResource(self)

    @cached_property
    def eval_types(self) -> AsyncEvalTypesResource:
        from .resources.eval_types import AsyncEvalTypesResource

        return AsyncEvalTypesResource(self)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        from .resources.reports import AsyncReportsResource

        return AsyncReportsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAymaraAIWithRawResponse:
        return AsyncAymaraAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAymaraAIWithStreamedResponse:
        return AsyncAymaraAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._auth_bearer}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    def _auth_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Use-Sandbox": str(self.use_sandbox) if self.use_sandbox is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        use_sandbox: bool | None = None,
        environment: Literal["production", "staging", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            use_sandbox=use_sandbox or self.use_sandbox,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AymaraAIWithRawResponse:
    _client: AymaraAI

    def __init__(self, client: AymaraAI) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def evals(self) -> evals.EvalsResourceWithRawResponse:
        from .resources.evals import EvalsResourceWithRawResponse

        return EvalsResourceWithRawResponse(self._client.evals)

    @cached_property
    def eval_types(self) -> eval_types.EvalTypesResourceWithRawResponse:
        from .resources.eval_types import EvalTypesResourceWithRawResponse

        return EvalTypesResourceWithRawResponse(self._client.eval_types)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        from .resources.reports import ReportsResourceWithRawResponse

        return ReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)


class AsyncAymaraAIWithRawResponse:
    _client: AsyncAymaraAI

    def __init__(self, client: AsyncAymaraAI) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def evals(self) -> evals.AsyncEvalsResourceWithRawResponse:
        from .resources.evals import AsyncEvalsResourceWithRawResponse

        return AsyncEvalsResourceWithRawResponse(self._client.evals)

    @cached_property
    def eval_types(self) -> eval_types.AsyncEvalTypesResourceWithRawResponse:
        from .resources.eval_types import AsyncEvalTypesResourceWithRawResponse

        return AsyncEvalTypesResourceWithRawResponse(self._client.eval_types)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        from .resources.reports import AsyncReportsResourceWithRawResponse

        return AsyncReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)


class AymaraAIWithStreamedResponse:
    _client: AymaraAI

    def __init__(self, client: AymaraAI) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def evals(self) -> evals.EvalsResourceWithStreamingResponse:
        from .resources.evals import EvalsResourceWithStreamingResponse

        return EvalsResourceWithStreamingResponse(self._client.evals)

    @cached_property
    def eval_types(self) -> eval_types.EvalTypesResourceWithStreamingResponse:
        from .resources.eval_types import EvalTypesResourceWithStreamingResponse

        return EvalTypesResourceWithStreamingResponse(self._client.eval_types)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        from .resources.reports import ReportsResourceWithStreamingResponse

        return ReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)


class AsyncAymaraAIWithStreamedResponse:
    _client: AsyncAymaraAI

    def __init__(self, client: AsyncAymaraAI) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def evals(self) -> evals.AsyncEvalsResourceWithStreamingResponse:
        from .resources.evals import AsyncEvalsResourceWithStreamingResponse

        return AsyncEvalsResourceWithStreamingResponse(self._client.evals)

    @cached_property
    def eval_types(self) -> eval_types.AsyncEvalTypesResourceWithStreamingResponse:
        from .resources.eval_types import AsyncEvalTypesResourceWithStreamingResponse

        return AsyncEvalTypesResourceWithStreamingResponse(self._client.eval_types)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        from .resources.reports import AsyncReportsResourceWithStreamingResponse

        return AsyncReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)


Client = AymaraAI

AsyncClient = AsyncAymaraAI
