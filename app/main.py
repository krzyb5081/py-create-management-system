import dataclasses
from datetime import datetime

@dataclass
class Speciality:
    name: str
    number: int

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str

@dataclass
class Group:
    speciality: Speciality
    course: int
    students: list[Student]

