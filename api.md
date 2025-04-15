# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/aymara_sdk/resources/health.py">check</a>() -> None</code>

# IntegrationTest

Types:

```python
from aymara_sdk.types import IntegrationTestRunResponse
```

Methods:

- <code title="post /v1/integration-test/">client.integration_test.<a href="./src/aymara_sdk/resources/integration_test.py">run</a>() -> <a href="./src/aymara_sdk/types/integration_test_run_response.py">IntegrationTestRunResponse</a></code>

# Tests

Types:

```python
from aymara_sdk.types import (
    ContentType,
    ExampleType,
    Question,
    TestOut,
    TestRetrieveQuestionsResponse,
)
```

Methods:

- <code title="post /v1/tests/">client.tests.<a href="./src/aymara_sdk/resources/tests/tests.py">create</a>(\*\*<a href="src/aymara_sdk/types/test_create_params.py">params</a>) -> <a href="./src/aymara_sdk/types/test_out.py">TestOut</a></code>
- <code title="get /v1/tests/{test_uuid}">client.tests.<a href="./src/aymara_sdk/resources/tests/tests.py">retrieve</a>(test_uuid, \*\*<a href="src/aymara_sdk/types/test_retrieve_params.py">params</a>) -> <a href="./src/aymara_sdk/types/test_out.py">TestOut</a></code>
- <code title="get /v1/tests/">client.tests.<a href="./src/aymara_sdk/resources/tests/tests.py">list</a>(\*\*<a href="src/aymara_sdk/types/test_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/test_out.py">SyncOffsetPage[TestOut]</a></code>
- <code title="delete /v1/tests/{test_uuid}">client.tests.<a href="./src/aymara_sdk/resources/tests/tests.py">delete</a>(test_uuid, \*\*<a href="src/aymara_sdk/types/test_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/tests/{test_uuid}/questions">client.tests.<a href="./src/aymara_sdk/resources/tests/tests.py">retrieve_questions</a>(test_uuid, \*\*<a href="src/aymara_sdk/types/test_retrieve_questions_params.py">params</a>) -> <a href="./src/aymara_sdk/types/test_retrieve_questions_response.py">TestRetrieveQuestionsResponse</a></code>

## Multiturn

Types:

```python
from aymara_sdk.types.tests import MultiturnContinueResponse
```

Methods:

- <code title="post /v1/tests/multiturn/continue">client.tests.multiturn.<a href="./src/aymara_sdk/resources/tests/multiturn.py">continue\_</a>(\*\*<a href="src/aymara_sdk/types/tests/multiturn_continue_params.py">params</a>) -> <a href="./src/aymara_sdk/types/tests/multiturn_continue_response.py">MultiturnContinueResponse</a></code>

# Scores

Types:

```python
from aymara_sdk.types import AnswerIn, AnswerOut, ScoreRunOut, ScoreGetAnswersResponse
```

Methods:

- <code title="post /v1/scores/">client.scores.<a href="./src/aymara_sdk/resources/scores/scores.py">create</a>(\*\*<a href="src/aymara_sdk/types/score_create_params.py">params</a>) -> <a href="./src/aymara_sdk/types/score_run_out.py">ScoreRunOut</a></code>
- <code title="get /v1/scores/{score_run_uuid}">client.scores.<a href="./src/aymara_sdk/resources/scores/scores.py">retrieve</a>(score_run_uuid, \*\*<a href="src/aymara_sdk/types/score_retrieve_params.py">params</a>) -> <a href="./src/aymara_sdk/types/score_run_out.py">ScoreRunOut</a></code>
- <code title="delete /v1/scores/{score_run_uuid}">client.scores.<a href="./src/aymara_sdk/resources/scores/scores.py">delete</a>(score_run_uuid, \*\*<a href="src/aymara_sdk/types/score_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/scores/{score_run_uuid}/answers">client.scores.<a href="./src/aymara_sdk/resources/scores/scores.py">get_answers</a>(score_run_uuid, \*\*<a href="src/aymara_sdk/types/score_get_answers_params.py">params</a>) -> <a href="./src/aymara_sdk/types/score_get_answers_response.py">ScoreGetAnswersResponse</a></code>

## Image

Types:

```python
from aymara_sdk.types.scores import ImageUploadRequestIn, ImageGetPresignedURLsResponse
```

Methods:

- <code title="post /v1/scores/image/get-presigned-urls">client.scores.image.<a href="./src/aymara_sdk/resources/scores/image.py">get_presigned_urls</a>(\*\*<a href="src/aymara_sdk/types/scores/image_get_presigned_urls_params.py">params</a>) -> <a href="./src/aymara_sdk/types/scores/image_get_presigned_urls_response.py">ImageGetPresignedURLsResponse</a></code>

## Summary

Types:

```python
from aymara_sdk.types.scores import ScoreRunSuiteSummaryOut
```

Methods:

- <code title="delete /v1/scores/summary/{summary_uuid}">client.scores.summary.<a href="./src/aymara_sdk/resources/scores/summary.py">delete_summary</a>(summary_uuid, \*\*<a href="src/aymara_sdk/types/scores/summary_delete_summary_params.py">params</a>) -> None</code>
- <code title="get /v1/scores/summary/{summary_uuid}">client.scores.summary.<a href="./src/aymara_sdk/resources/scores/summary.py">retrieve_summary</a>(summary_uuid, \*\*<a href="src/aymara_sdk/types/scores/summary_retrieve_summary_params.py">params</a>) -> <a href="./src/aymara_sdk/types/scores/score_run_suite_summary_out.py">ScoreRunSuiteSummaryOut</a></code>

# Workspaces

Types:

```python
from aymara_sdk.types import WorkspaceIn, WorkspaceOut
```

Methods:

- <code title="get /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_sdk/resources/workspaces.py">retrieve</a>(workspace_uuid) -> <a href="./src/aymara_sdk/types/workspace_out.py">WorkspaceOut</a></code>
- <code title="put /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_sdk/resources/workspaces.py">update</a>(workspace_uuid, \*\*<a href="src/aymara_sdk/types/workspace_update_params.py">params</a>) -> <a href="./src/aymara_sdk/types/workspace_out.py">WorkspaceOut</a></code>
- <code title="delete /v1/workspaces/{workspace_uuid}">client.workspaces.<a href="./src/aymara_sdk/resources/workspaces.py">delete</a>(workspace_uuid) -> None</code>

# Webhooks

Methods:

- <code title="post /v1/webhooks/propel">client.webhooks.<a href="./src/aymara_sdk/resources/webhooks.py">propel</a>() -> None</code>

# Accounts

Types:

```python
from aymara_sdk.types import User
```

Methods:

- <code title="get /v1/accounts/me">client.accounts.<a href="./src/aymara_sdk/resources/accounts.py">retrieve_me</a>() -> <a href="./src/aymara_sdk/types/user.py">User</a></code>

# Usage

Types:

```python
from aymara_sdk.types import UsageListResponse
```

Methods:

- <code title="get /v1/usage/">client.usage.<a href="./src/aymara_sdk/resources/usage.py">list</a>(\*\*<a href="src/aymara_sdk/types/usage_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/usage_list_response.py">UsageListResponse</a></code>

# Policies

Types:

```python
from aymara_sdk.types import PolicyListResponse
```

Methods:

- <code title="get /v1/policies/">client.policies.<a href="./src/aymara_sdk/resources/policies.py">list</a>(\*\*<a href="src/aymara_sdk/types/policy_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/policy_list_response.py">SyncOffsetPage[PolicyListResponse]</a></code>

# Evals

Types:

```python
from aymara_sdk.types import EvalOut, EvalPrompt, PromptExampleIn, Status, EvalGetPromptsResponse
```

Methods:

- <code title="post /v2/evals/">client.evals.<a href="./src/aymara_sdk/resources/evals.py">create</a>(\*\*<a href="src/aymara_sdk/types/eval_create_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_out.py">EvalOut</a></code>
- <code title="get /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_sdk/resources/evals.py">retrieve</a>(eval_uuid, \*\*<a href="src/aymara_sdk/types/eval_retrieve_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_out.py">EvalOut</a></code>
- <code title="get /v2/evals/">client.evals.<a href="./src/aymara_sdk/resources/evals.py">list</a>(\*\*<a href="src/aymara_sdk/types/eval_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_out.py">SyncOffsetPage[EvalOut]</a></code>
- <code title="delete /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_sdk/resources/evals.py">delete</a>(eval_uuid, \*\*<a href="src/aymara_sdk/types/eval_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/evals/{eval_uuid}/prompts">client.evals.<a href="./src/aymara_sdk/resources/evals.py">get_prompts</a>(eval_uuid, \*\*<a href="src/aymara_sdk/types/eval_get_prompts_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_get_prompts_response.py">EvalGetPromptsResponse</a></code>

# EvalTypes

Types:

```python
from aymara_sdk.types import EvalType, EvalTypeListResponse
```

Methods:

- <code title="get /v2/eval-types/{eval_type_uuid}">client.eval_types.<a href="./src/aymara_sdk/resources/eval_types.py">retrieve</a>(eval_type_uuid) -> <a href="./src/aymara_sdk/types/eval_type.py">EvalType</a></code>
- <code title="get /v2/eval-types/">client.eval_types.<a href="./src/aymara_sdk/resources/eval_types.py">list</a>() -> <a href="./src/aymara_sdk/types/eval_type_list_response.py">EvalTypeListResponse</a></code>

# EvalRuns

Types:

```python
from aymara_sdk.types import (
    EvalResponse,
    EvalRun,
    EvalRunInput,
    EvalRunGetResponsesResponse,
    EvalRunRunScoreResponse,
)
```

Methods:

- <code title="post /v2/eval-runs/">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">create</a>(\*\*<a href="src/aymara_sdk/types/eval_run_create_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_run.py">EvalRun</a></code>
- <code title="get /v2/eval-runs/{eval_run_uuid}">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">retrieve</a>(eval_run_uuid, \*\*<a href="src/aymara_sdk/types/eval_run_retrieve_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_run.py">EvalRun</a></code>
- <code title="get /v2/eval-runs/">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">list</a>(\*\*<a href="src/aymara_sdk/types/eval_run_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_run.py">SyncOffsetPage[EvalRun]</a></code>
- <code title="delete /v2/eval-runs/{eval_run_uuid}">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">delete</a>(eval_run_uuid, \*\*<a href="src/aymara_sdk/types/eval_run_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/eval-runs/{eval_run_uuid}/responses">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">get_responses</a>(eval_run_uuid, \*\*<a href="src/aymara_sdk/types/eval_run_get_responses_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_run_get_responses_response.py">EvalRunGetResponsesResponse</a></code>
- <code title="post /v2/eval-runs/-/score-responses">client.eval_runs.<a href="./src/aymara_sdk/resources/eval_runs/eval_runs.py">run_score</a>(\*\*<a href="src/aymara_sdk/types/eval_run_run_score_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_run_run_score_response.py">EvalRunRunScoreResponse</a></code>

## Image

Types:

```python
from aymara_sdk.types.eval_runs import ImageGetPresignedURLsResponse
```

Methods:

- <code title="post /v2/eval-runs/image/get-presigned-urls">client.eval_runs.image.<a href="./src/aymara_sdk/resources/eval_runs/image.py">get_presigned_urls</a>(\*\*<a href="src/aymara_sdk/types/eval_runs/image_get_presigned_urls_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_runs/image_get_presigned_urls_response.py">ImageGetPresignedURLsResponse</a></code>

## Summary

Types:

```python
from aymara_sdk.types.eval_runs import EvalRunSuiteSummary
```

Methods:

- <code title="post /v2/eval-runs/summary/">client.eval_runs.summary.<a href="./src/aymara_sdk/resources/eval_runs/summary.py">create</a>(\*\*<a href="src/aymara_sdk/types/eval_runs/summary_create_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_runs/eval_run_suite_summary.py">EvalRunSuiteSummary</a></code>
- <code title="get /v2/eval-runs/summary/{summary_uuid}">client.eval_runs.summary.<a href="./src/aymara_sdk/resources/eval_runs/summary.py">retrieve</a>(summary_uuid, \*\*<a href="src/aymara_sdk/types/eval_runs/summary_retrieve_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_runs/eval_run_suite_summary.py">EvalRunSuiteSummary</a></code>
- <code title="get /v2/eval-runs/summary/">client.eval_runs.summary.<a href="./src/aymara_sdk/resources/eval_runs/summary.py">list</a>(\*\*<a href="src/aymara_sdk/types/eval_runs/summary_list_params.py">params</a>) -> <a href="./src/aymara_sdk/types/eval_runs/eval_run_suite_summary.py">SyncOffsetPage[EvalRunSuiteSummary]</a></code>
- <code title="delete /v2/eval-runs/summary/{summary_uuid}">client.eval_runs.summary.<a href="./src/aymara_sdk/resources/eval_runs/summary.py">delete</a>(summary_uuid, \*\*<a href="src/aymara_sdk/types/eval_runs/summary_delete_params.py">params</a>) -> None</code>

# Files

Types:

```python
from aymara_sdk.types import FileUploadResponse
```

Methods:

- <code title="post /v2/files/">client.files.<a href="./src/aymara_sdk/resources/files.py">upload</a>(\*\*<a href="src/aymara_sdk/types/file_upload_params.py">params</a>) -> <a href="./src/aymara_sdk/types/file_upload_response.py">FileUploadResponse</a></code>
