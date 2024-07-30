from domain.task_run import TaskInput, TaskRun
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RunRequest(BaseModel):
    task_input: TaskInput


@app.post("/run")
def run(request: RunRequest) -> TaskRun: ...
