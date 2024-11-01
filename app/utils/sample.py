from dataclasses import dataclass


@dataclass
class User:
    age: int
    name: str


def foo(new: User):
    print(f"hai, {new.name} you're {new.age} year old")

parm = User(age=19, name="Adnan")
foo(parm)


