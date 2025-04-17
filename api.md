# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/aymara_ai/resources/health.py">check</a>() -> None</code>

# IntegrationTest

Types:

```python
from aymara_ai.types import IntegrationTestRunResponse
```

Methods:

- <code title="post /v1/integration-test/">client.integration_test.<a href="./src/aymara_ai/resources/integration_test.py">run</a>() -> <a href="./src/aymara_ai/types/integration_test_run_response.py">IntegrationTestRunResponse</a></code>

# Tests

Types:

```python
from aymara_ai.types import (
    ContentType,
    ExampleType,
    Question,
    TestOut,
    TestRetrieveQuestionsResponse,
)
```

Methods:

- <code title="post /v1/tests/">client.tests.<a href="./src/aymara_ai/resources/tests/tests.py">create</a>(\*\*<a href="src/aymara_ai/types/test_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/test_out.py">TestOut</a></code>
- <code title="get /v1/tests/{test_uuid}">client.tests.<a href="./src/aymara_ai/resources/tests/tests.py">retrieve</a>(test_uuid, \*\*<a href="src/aymara_ai/types/test_retrieve_params.py">params</a>) -> <a href="./src/aymara_ai/types/test_out.py">TestOut</a></code>
- <code title="get /v1/tests/">client.tests.<a href="./src/aymara_ai/resources/tests/tests.py">list</a>(\*\*<a href="src/aymara_ai/types/test_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/test_out.py">SyncOffsetPage[TestOut]</a></code>
- <code title="delete /v1/tests/{test_uuid}">client.tests.<a href="./src/aymara_ai/resources/tests/tests.py">delete</a>(test_uuid, \*\*<a href="src/aymara_ai/types/test_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/tests/{test_uuid}/questions">client.tests.<a href="./src/aymara_ai/resources/tests/tests.py">retrieve_questions</a>(test_uuid, \*\*<a href="src/aymara_ai/types/test_retrieve_questions_params.py">params</a>) -> <a href="./src/aymara_ai/types/test_retrieve_questions_response.py">TestRetrieveQuestionsResponse</a></code>

## Multiturn

Types:

```python
from aymara_ai.types.tests import MultiturnContinueResponse
```

Methods:

- <code title="post /v1/tests/multiturn/continue">client.tests.multiturn.<a href="./src/aymara_ai/resources/tests/multiturn.py">continue\_</a>(\*\*<a href="src/aymara_ai/types/tests/multiturn_continue_params.py">params</a>) -> <a href="./src/aymara_ai/types/tests/multiturn_continue_response.py">MultiturnContinueResponse</a></code>

# Scores

Types:

```python
from aymara_ai.types import AnswerIn, AnswerOut, ScoreRunOut, ScoreGetAnswersResponse
```

Methods:

- <code title="post /v1/scores/">client.scores.<a href="./src/aymara_ai/resources/scores/scores.py">create</a>(\*\*<a href="src/aymara_ai/types/score_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/score_run_out.py">ScoreRunOut</a></code>
- <code title="get /v1/scores/{score_run_uuid}">client.scores.<a href="./src/aymara_ai/resources/scores/scores.py">retrieve</a>(score_run_uuid, \*\*<a href="src/aymara_ai/types/score_retrieve_params.py">params</a>) -> <a href="./src/aymara_ai/types/score_run_out.py">ScoreRunOut</a></code>
- <code title="delete /v1/scores/{score_run_uuid}">client.scores.<a href="./src/aymara_ai/resources/scores/scores.py">delete</a>(score_run_uuid, \*\*<a href="src/aymara_ai/types/score_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/scores/{score_run_uuid}/answers">client.scores.<a href="./src/aymara_ai/resources/scores/scores.py">get_answers</a>(score_run_uuid, \*\*<a href="src/aymara_ai/types/score_get_answers_params.py">params</a>) -> <a href="./src/aymara_ai/types/score_get_answers_response.py">ScoreGetAnswersResponse</a></code>

## Image

Types:

```python
from aymara_ai.types.scores import ImageUploadRequestIn, ImageGetPresignedURLsResponse
```

Methods:

- <code title="post /v1/scores/image/get-presigned-urls">client.scores.image.<a href="./src/aymara_ai/resources/scores/image.py">get_presigned_urls</a>(\*\*<a href="src/aymara_ai/types/scores/image_get_presigned_urls_params.py">params</a>) -> <a href="./src/aymara_ai/types/scores/image_get_presigned_urls_response.py">ImageGetPresignedURLsResponse</a></code>

## Summary

Types:

```python
from aymara_ai.types.scores import ScoreRunSuiteSummaryOut
```

Methods:

- <code title="delete /v1/scores/summary/{summary_uuid}">client.scores.summary.<a href="./src/aymara_ai/resources/scores/summary.py">delete_summary</a>(summary_uuid, \*\*<a href="src/aymara_ai/types/scores/summary_delete_summary_params.py">params</a>) -> None</code>
- <code title="get /v1/scores/summary/{summary_uuid}">client.scores.summary.<a href="./src/aymara_ai/resources/scores/summary.py">retrieve_summary</a>(summary_uuid, \*\*<a href="src/aymara_ai/types/scores/summary_retrieve_summary_params.py">params</a>) -> <a href="./src/aymara_ai/types/scores/score_run_suite_summary_out.py">ScoreRunSuiteSummaryOut</a></code>

# Workspaces

Types:

```python
from aymara_ai.types import WorkspaceIn, WorkspaceOut
```

Methods:

- <code title="get /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_ai/resources/workspaces.py">retrieve</a>(workspace_uuid) -> <a href="./src/aymara_ai/types/workspace_out.py">WorkspaceOut</a></code>
- <code title="put /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_ai/resources/workspaces.py">update</a>(workspace_uuid, \*\*<a href="src/aymara_ai/types/workspace_update_params.py">params</a>) -> <a href="./src/aymara_ai/types/workspace_out.py">WorkspaceOut</a></code>
- <code title="delete /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_ai/resources/workspaces.py">delete</a>(workspace_uuid) -> None</code>

# Webhooks

Methods:

- <code title="post /v1/webhooks/propel">client.webhooks.<a href="./src/aymara_ai/resources/webhooks.py">propel</a>() -> None</code>

# Accounts

Types:

```python
from aymara_ai.types import User
```

Methods:

- <code title="get /v1/accounts/me">client.accounts.<a href="./src/aymara_ai/resources/accounts.py">retrieve_me</a>() -> <a href="./src/aymara_ai/types/user.py">User</a></code>

# Usage

Types:

```python
from aymara_ai.types import UsageListResponse
```

Methods:

- <code title="get /v1/usage/">client.usage.<a href="./src/aymara_ai/resources/usage.py">list</a>(\*\*<a href="src/aymara_ai/types/usage_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/usage_list_response.py">UsageListResponse</a></code>

# Policies

Types:

```python
from aymara_ai.types import PolicyListResponse
```

Methods:

- <code title="get /v1/policies/">client.policies.<a href="./src/aymara_ai/resources/policies.py">list</a>(\*\*<a href="src/aymara_ai/types/policy_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/policy_list_response.py">SyncOffsetPage[PolicyListResponse]</a></code>

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
- <code title="post /v2/eval-runs/{eval_run_uuid}/continue">client.evals.<a href="./src/aymara_ai/resources/evals.py">continue_run</a>(path_eval_run_uuid, \*\*<a href="src/aymara_ai/types/eval_continue_run_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_run_result.py">EvalRunResult</a></code>
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
