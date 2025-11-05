# Playwright Form Filler

Tired of manually filling out endless forms? Whether you’re testing long multi-page onboarding flows or just want to save time, this tool has you covered.

Simply describe your desired form inputs in a configuration file, and the script will automatically fill them in for you using Playwright, all while keeping you in control. You can pause between steps, inspect the page, and continue when ready.

--- 

## Installation

- Setup dependencies

```bash
make setup
```

- Run script (config file must be at <project root>/config.json)
 
```bash
make run 

```

---

## Configuration

- Example configuration file

```json
{
  "page_url": "http://localhost:3000/form.html",
  "steps": [
    {
      "fields": {
        "#firstName": "Alice",
        "#lastName": "Z"
      }
    },
    {
      "fields": {
        "#firstName": "Alice",
        "#lastName": "Z"
      }
    }
  ]
}
```


- Configuration Parameters

- `page_url`
The URL of the form page to be autofilled.

- `steps`
An array of step objects. After each step, the script pauses to allow manual review or navigation before continuing.

  - `fields`
  A collection of key-value pairs where the key is a CSS selector and the value is the text to input.

