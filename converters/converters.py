from dataclasses import dataclass, field
from typing import Iterable, Generator


@dataclass
class IterableToGenerator:
    def __call__(self, iterable: Iterable) -> Generator:
        generator = (value for value in iterable)
        return generator
