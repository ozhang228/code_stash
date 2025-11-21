from typing import Protocol

from pydantic import BaseModel, computed_field

FieldSelector = str
FieldValue = str


class Field(BaseModel, frozen=True):
    @property
    def selector(self) -> FieldSelector:
        raise NotImplementedError

    value: FieldValue


class RadioField(Field, frozen=True):
    name: str
    value: FieldValue

    @computed_field
    @property
    def selector(self) -> FieldSelector:
        return f"input[name='{self.name}'][value='{self.value}']"


class TextField(Field, frozen=True):
    id: str
    value: FieldValue

    @computed_field
    @property
    def selector(self) -> FieldSelector:
        return f"#{self.id}"


class Step(BaseModel):
    fields: list[Field]


class Config(BaseModel):
    page_url: str
    steps: list[Step]


PAGE_URL = "https://kyc.cumberland.io/onboard-entity"

STEPS = [
    Step(fields=[TextField(id="accepted_minimum_trade>input", value="hi")]),
    Step(fields=[RadioField(name="entity_ecp_criteria", value="Yes")]),
]

config = Config(page_url=PAGE_URL, steps=STEPS)
