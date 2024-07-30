from domain.task_run import TaskRun


def test_hello():
    run = TaskRun(task_input={}, task_output={})
    assert run.model_dump_json() == '{"task_input":{},"task_output":{}}'
