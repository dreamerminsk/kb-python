from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    title: str
    original: str
    page: str


@dataclass
class Person:
    id: int
    name: str


@dataclass
class Year:
    pass


@dataclass
class Weekend:
    pass


@dataclass
class Thursday:
    pass
