from model.Model import Model

class Task(Model):
    title: str

class TaskList(Model):
    task_list: list[Task] = []