# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    evals,
    usage,
    health,
    reports,
    accounts,
    policies,
    webhooks,
    eval_types,
    workspaces,
    integration_test,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AymaraAIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.tests import tests
from .resources.scores import scores

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
    "production": "https://api.example.com",
    "staging": "https://staging-api.example.com",
    "development": "http://localhost:8000",
}


class AymaraAI(SyncAPIClient):
    health: health.HealthResource
    integration_test: integration_test.IntegrationTestResource
    tests: tests.TestsResource
    scores: scores.ScoresResource
    workspaces: workspaces.WorkspacesResource
    webhooks: webhooks.WebhooksResource
    accounts: accounts.AccountsResource
    usage: usage.UsageResource
    policies: policies.PoliciesResource
    evals: evals.EvalsResource
    eval_types: eval_types.EvalTypesResource
    reports: reports.ReportsResource
    with_raw_response: AymaraAIWithRawResponse
    with_streaming_response: AymaraAIWithStreamedResponse

    # client options
    api_key: str
    bearer_token: str | None

    _environment: Literal["production", "staging", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "staging", "development"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.health = health.HealthResource(self)
        self.integration_test = integration_test.IntegrationTestResource(self)
        self.tests = tests.TestsResource(self)
        self.scores = scores.ScoresResource(self)
        self.workspaces = workspaces.WorkspacesResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.usage = usage.UsageResource(self)
        self.policies = policies.PoliciesResource(self)
        self.evals = evals.EvalsResource(self)
        self.eval_types = eval_types.EvalTypesResource(self)
        self.reports = reports.ReportsResource(self)
        self.with_raw_response = AymaraAIWithRawResponse(self)
        self.with_streaming_response = AymaraAIWithStreamedResponse(self)

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "staging", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    health: health.AsyncHealthResource
    integration_test: integration_test.AsyncIntegrationTestResource
    tests: tests.AsyncTestsResource
    scores: scores.AsyncScoresResource
    workspaces: workspaces.AsyncWorkspacesResource
    webhooks: webhooks.AsyncWebhooksResource
    accounts: accounts.AsyncAccountsResource
    usage: usage.AsyncUsageResource
    policies: policies.AsyncPoliciesResource
    evals: evals.AsyncEvalsResource
    eval_types: eval_types.AsyncEvalTypesResource
    reports: reports.AsyncReportsResource
    with_raw_response: AsyncAymaraAIWithRawResponse
    with_streaming_response: AsyncAymaraAIWithStreamedResponse

    # client options
    api_key: str
    bearer_token: str | None

    _environment: Literal["production", "staging", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "staging", "development"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.health = health.AsyncHealthResource(self)
        self.integration_test = integration_test.AsyncIntegrationTestResource(self)
        self.tests = tests.AsyncTestsResource(self)
        self.scores = scores.AsyncScoresResource(self)
        self.workspaces = workspaces.AsyncWorkspacesResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.usage = usage.AsyncUsageResource(self)
        self.policies = policies.AsyncPoliciesResource(self)
        self.evals = evals.AsyncEvalsResource(self)
        self.eval_types = eval_types.AsyncEvalTypesResource(self)
        self.reports = reports.AsyncReportsResource(self)
        self.with_raw_response = AsyncAymaraAIWithRawResponse(self)
        self.with_streaming_response = AsyncAymaraAIWithStreamedResponse(self)

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "staging", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: AymaraAI) -> None:
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.integration_test = integration_test.IntegrationTestResourceWithRawResponse(client.integration_test)
        self.tests = tests.TestsResourceWithRawResponse(client.tests)
        self.scores = scores.ScoresResourceWithRawResponse(client.scores)
        self.workspaces = workspaces.WorkspacesResourceWithRawResponse(client.workspaces)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.usage = usage.UsageResourceWithRawResponse(client.usage)
        self.policies = policies.PoliciesResourceWithRawResponse(client.policies)
        self.evals = evals.EvalsResourceWithRawResponse(client.evals)
        self.eval_types = eval_types.EvalTypesResourceWithRawResponse(client.eval_types)
        self.reports = reports.ReportsResourceWithRawResponse(client.reports)


class AsyncAymaraAIWithRawResponse:
    def __init__(self, client: AsyncAymaraAI) -> None:
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.integration_test = integration_test.AsyncIntegrationTestResourceWithRawResponse(client.integration_test)
        self.tests = tests.AsyncTestsResourceWithRawResponse(client.tests)
        self.scores = scores.AsyncScoresResourceWithRawResponse(client.scores)
        self.workspaces = workspaces.AsyncWorkspacesResourceWithRawResponse(client.workspaces)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.usage = usage.AsyncUsageResourceWithRawResponse(client.usage)
        self.policies = policies.AsyncPoliciesResourceWithRawResponse(client.policies)
        self.evals = evals.AsyncEvalsResourceWithRawResponse(client.evals)
        self.eval_types = eval_types.AsyncEvalTypesResourceWithRawResponse(client.eval_types)
        self.reports = reports.AsyncReportsResourceWithRawResponse(client.reports)


class AymaraAIWithStreamedResponse:
    def __init__(self, client: AymaraAI) -> None:
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.integration_test = integration_test.IntegrationTestResourceWithStreamingResponse(client.integration_test)
        self.tests = tests.TestsResourceWithStreamingResponse(client.tests)
        self.scores = scores.ScoresResourceWithStreamingResponse(client.scores)
        self.workspaces = workspaces.WorkspacesResourceWithStreamingResponse(client.workspaces)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.usage = usage.UsageResourceWithStreamingResponse(client.usage)
        self.policies = policies.PoliciesResourceWithStreamingResponse(client.policies)
        self.evals = evals.EvalsResourceWithStreamingResponse(client.evals)
        self.eval_types = eval_types.EvalTypesResourceWithStreamingResponse(client.eval_types)
        self.reports = reports.ReportsResourceWithStreamingResponse(client.reports)


class AsyncAymaraAIWithStreamedResponse:
    def __init__(self, client: AsyncAymaraAI) -> None:
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.integration_test = integration_test.AsyncIntegrationTestResourceWithStreamingResponse(
            client.integration_test
        )
        self.tests = tests.AsyncTestsResourceWithStreamingResponse(client.tests)
        self.scores = scores.AsyncScoresResourceWithStreamingResponse(client.scores)
        self.workspaces = workspaces.AsyncWorkspacesResourceWithStreamingResponse(client.workspaces)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.usage = usage.AsyncUsageResourceWithStreamingResponse(client.usage)
        self.policies = policies.AsyncPoliciesResourceWithStreamingResponse(client.policies)
        self.evals = evals.AsyncEvalsResourceWithStreamingResponse(client.evals)
        self.eval_types = eval_types.AsyncEvalTypesResourceWithStreamingResponse(client.eval_types)
        self.reports = reports.AsyncReportsResourceWithStreamingResponse(client.reports)


Client = AymaraAI

AsyncClient = AsyncAymaraAI
