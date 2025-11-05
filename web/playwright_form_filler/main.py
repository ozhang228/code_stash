import argparse
import json

from playwright.sync_api import sync_playwright
from pydantic import BaseModel


class Arguments(BaseModel):
    config_path: str


def parse_arguments() -> Arguments:
    parser = argparse.ArgumentParser(
        description="CLI Tool to simulate filling out a form based on an inputted config file"
    )
    parser.add_argument(
        "-c",
        "--config-file",
        type=str,
        help="The path to the configuration file",
        required=True,
    )

    namespace = parser.parse_args()

    return Arguments(config_path=namespace.config_file)


FieldSelector = str
FieldValue = str


class Step(BaseModel):
    fields: dict[FieldSelector, FieldValue]


class Config(BaseModel):
    page_url: str
    steps: list[Step]


def main():
    args = parse_arguments()

    with open(args.config_path, "r") as f:
        config = Config.model_validate(json.load(f))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(config.page_url)

        # getting to the first page of the form
        page.pause()

        for step in config.steps:
            for selector, value in step.fields.items():
                element = page.query_selector(selector)

                if not element:
                    print(f"Could not find element with selector {selector}")
                    continue

                element_type = element.evaluate("el => el.type")
                match element_type:
                    case "select":
                        element.select_option(value)
                    case "radio":
                        element.check()
                    case "checkbox":
                        element.check()
                    case "text":
                        page.fill(selector, value)
                    case "textarea":
                        page.fill(selector, value)
                    case _:
                        assert False, f"Unsupported element type {element.type}"

            page.pause()


if __name__ == "__main__":
    main()
