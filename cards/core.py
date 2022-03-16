# -*- coding: utf-8 -*-
from dataclasses import asdict, dataclass


@dataclass
class Card:
    id: int
    summary: str = ""
    owner: str = "Default"
    state: str = "todo"

    @classmethod
    def from_dict(cls, card_dict: dict):
        return Card(**card_dict)

    def to_dict(self):
        return asdict(self)
