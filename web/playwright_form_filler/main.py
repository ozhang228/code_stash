from playwright.sync_api import sync_playwright

from config import config


def main():
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
