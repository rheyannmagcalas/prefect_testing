from prefect import task, Flow

@task
def add(x, y=1):
    return x + y

@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))

with Flow("My second flow!") as flow:
    add(1, 2)
    say_hello("ran")

state = flow.run()


