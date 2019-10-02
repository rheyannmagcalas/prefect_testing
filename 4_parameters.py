from prefect import task, Parameter, Flow

@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))

with Flow("Say hi!") as flow:
    name = Parameter("name")
    say_hello(name)

flow.run(name="Ran")
