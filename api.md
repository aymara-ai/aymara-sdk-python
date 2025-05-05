# Shared Types

```python
from aymara_ai.types import ContentType, FileReference, Status
```

# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/aymara_ai/resources/health.py">check</a>() -> None</code>

# Evals

Types:

```python
from aymara_ai.types import Eval, EvalPrompt, EvalResponse, PromptExample
```

Methods:

- <code title="post /v2/evals">client.evals.<a href="./src/aymara_ai/resources/evals/evals.py">create</a>(\*\*<a href="src/aymara_ai/types/eval_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">Eval</a></code>
- <code title="get /v2/evals">client.evals.<a href="./src/aymara_ai/resources/evals/evals.py">list</a>(\*\*<a href="src/aymara_ai/types/eval_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">SyncOffsetPage[Eval]</a></code>
- <code title="delete /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals/evals.py">delete</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/evals/{eval_uuid}">client.evals.<a href="./src/aymara_ai/resources/evals/evals.py">get</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_get_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval.py">Eval</a></code>
- <code title="get /v2/evals/{eval_uuid}/prompts">client.evals.<a href="./src/aymara_ai/resources/evals/evals.py">list_prompts</a>(eval_uuid, \*\*<a href="src/aymara_ai/types/eval_list_prompts_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_prompt.py">SyncOffsetPage[EvalPrompt]</a></code>

## Runs

Types:

```python
from aymara_ai.types.evals import EvalRunExample, EvalRunRequest, EvalRunResult, ScoredResponse
```

Methods:

- <code title="post /v2/eval-runs">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">create</a>(\*\*<a href="src/aymara_ai/types/evals/run_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/evals/eval_run_result.py">EvalRunResult</a></code>
- <code title="get /v2/eval-runs">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">list</a>(\*\*<a href="src/aymara_ai/types/evals/run_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/evals/eval_run_result.py">SyncOffsetPage[EvalRunResult]</a></code>
- <code title="delete /v2/eval-runs/{eval_run_uuid}">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">delete</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/evals/run_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/eval-runs/{eval_run_uuid}">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">get</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/evals/run_get_params.py">params</a>) -> <a href="./src/aymara_ai/types/evals/eval_run_result.py">EvalRunResult</a></code>
- <code title="get /v2/eval-runs/{eval_run_uuid}/responses">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">list_responses</a>(eval_run_uuid, \*\*<a href="src/aymara_ai/types/evals/run_list_responses_params.py">params</a>) -> <a href="./src/aymara_ai/types/evals/scored_response.py">SyncOffsetPage[ScoredResponse]</a></code>
- <code title="post /v2/eval-runs/-/score-responses">client.evals.runs.<a href="./src/aymara_ai/resources/evals/runs.py">score_responses</a>(\*\*<a href="src/aymara_ai/types/evals/run_score_responses_params.py">params</a>) -> <a href="./src/aymara_ai/types/evals/eval_run_result.py">EvalRunResult</a></code>

# EvalTypes

Types:

```python
from aymara_ai.types import AIInstruction, EvalType
```

Methods:

- <code title="get /v2/eval-types">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">list</a>(\*\*<a href="src/aymara_ai/types/eval_type_list_params.py">params</a>) -> <a href="./src/aymara_ai/types/eval_type.py">SyncOffsetPage[EvalType]</a></code>
- <code title="get /v2/eval-types/-/instructions">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">find_instructions</a>(\*\*<a href="src/aymara_ai/types/eval_type_find_instructions_params.py">params</a>) -> <a href="./src/aymara_ai/types/ai_instruction.py">SyncOffsetPage[AIInstruction]</a></code>
- <code title="get /v2/eval-types/{eval_type_uuid}">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">get</a>(eval_type_uuid) -> <a href="./src/aymara_ai/types/eval_type.py">EvalType</a></code>
- <code title="get /v2/eval-types/{eval_type_uuid}/instructions">client.eval_types.<a href="./src/aymara_ai/resources/eval_types.py">list_instructions</a>(eval_type_uuid, \*\*<a href="src/aymara_ai/types/eval_type_list_instructions_params.py">params</a>) -> <a href="./src/aymara_ai/types/ai_instruction.py">SyncOffsetPage[AIInstruction]</a></code>

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
from aymara_ai.types import FileUpload, FileCreateResponse
```

Methods:

- <code title="post /v2/files">client.files.<a href="./src/aymara_ai/resources/files.py">create</a>(\*\*<a href="src/aymara_ai/types/file_create_params.py">params</a>) -> <a href="./src/aymara_ai/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="post /v2/files/-/uploads">client.files.<a href="./src/aymara_ai/resources/files.py">upload</a>(\*\*<a href="src/aymara_ai/types/file_upload_params.py">params</a>) -> <a href="./src/aymara_ai/types/file_upload.py">FileUpload</a></code>
