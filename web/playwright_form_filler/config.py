from pydantic import BaseModel

FieldSelector = str
FieldValue = str


class Step(BaseModel):
    fields: dict[FieldSelector, FieldValue]


class Config(BaseModel):
    page_url: str
    steps: list[Step]


PAGE_URL = "https://kyc.cumberland.io/onboard-entity"
STEPS = [
    Step(
        fields={
            "#accepted_minimum_trade>input": "",
            "#accepted_terms_conditions>input": "",
        }
    ),
    Step(
        fields={
            "input[name='entity_ecp_criteria'][value='Yes']": "",
        }
    ),
]

config = Config(page_url=PAGE_URL, steps=[])
