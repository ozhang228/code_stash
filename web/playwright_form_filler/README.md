# Playwright Form Filler

Tired of filling out forms all day? Have a really long multi-page form that takes ages to fill out and test (looking at you kyc.cumberland.io/onboard-entity)?

Lucky for you, now you can write down your form declaratively at `config.json` and have it autofill.

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

