from typing import Any

from pydantic import BaseModel

TaskInput = dict[str, Any]
TaskOutput = dict[str, Any]


class TaskRun(BaseModel):
    task_input: TaskInput
    task_output: TaskOutput
