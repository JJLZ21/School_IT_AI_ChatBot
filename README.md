# IT-ChatBot

Simple overview of use/purpose.

## Description

An in-depth paragraph about your project and overview of use.

## Requirement

### Rasa Version

- Rasa 3.0

### Virtual Envirement

Create and active the virtual envirement

```
cd IT-ChatBot
python -m venv ./venv
.\venv\Scripts\activate
```

### Major Dependencies

- requests
- pysqlite3
- gspread
- rasa
- rasa-sdk
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

#### First update pip to 22.0.4

```
python -m pip install --upgrade pip
pip install -r ./requirement
```

## Story Flows

1. "I need help" -> either click the buttons or type "wifi issue" (similar for printer/login issues)

```
I need help
either click the buttons or type "wifi issue"
```

2. "plx come to" -> follow the response instruction -> 101

```
plx come to
follow the response instruction
101
```

3. "I want to borrow macbook" -> follow the response instruction -> 2 digits input (1-99)

```
I want to borrow macbook
follow the response instruction
2 digits input (1-99)
```

4.  "I want to borrow 10 headphones" -> either callback or success response

```
I want to borrow 10 headphones
either callback or success response
```

5. "I want to borrow iphone" -> follow the response instruction -> "headphone"/"macbook"/"ipad"

```
I want to borrow iphone
follow the response instruction
headphone
```

## Running

### Testing on Termial

1. First termial run rasa shell

```
rasa shell
```

2. Second termial cd to the actions Dictionary and run rasa run actions

```
cd actions
rasa run actions
```

### Running in other place

Find more in [here](https://rasa.com/docs/rasa/connectors/your-own-website)

## Issue

- Google gmail API token.json will expire and need additional authentication
- Slack Timeout Issue

## Authors

[Jack Zhu](https://www.linkedin.com/in/jack-jiali-zhu/)

## Acknowledgments

- [Google](https://developers.google.com/docs/api) API Documentation
- [Rasa](https://rasa.com/docs/rasa/) Documentation
