from prefect import Task, Flow

class AddTask(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int=None) -> int:
        if y is None:
            y = self.default
        return x + y

# initialize the task instance
add = AddTask(default=1)


with Flow("My third flow!") as flow:
    first_result = add(1, y=2)
    second_result = add(x=first_result, y=100)

state = flow.run()
