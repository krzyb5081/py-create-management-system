import pickle
import dataclasses
from datetime import datetime

@dataclass
class Specialty:
    name: str
    number: int

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]

def write_groups_informatioms(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = 0
    for group in groups:
        if len(group.students) < max_students:
            max_students = len(group.students)
    return max_students
