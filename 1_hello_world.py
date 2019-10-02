from prefect import task, Flow

@task
def say_hello():
    print("Hello, world!")


with Flow("My first flow!") as flow:
    say_hello()

state = flow.run()

