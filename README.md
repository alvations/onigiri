# Onigiri

Unofficial Python SDK for [RIT Translate](https://rapidapi.com/dev-rit-singapore/api/rit-translate)


Install
====


```
pip install onigiri
```

Usage
====

First, subscribe to the [RIT Translate API on RapidAPI](https://rapidapi.com/dev-rit-singapore/api/rit-translate)
to get the `X-RapidAPI-Key` value.

Then in Python:

```python
from onigiri import Client

# Initialize the client.
# Fill in the '...' with the appropriate key from `X-RapidAPI-Key` header key.
oni = Client(rapidapi_key="...")

# Translate a single sentence.
oni.translate('I am pregnant.', target_language='fr', source_language='en')
```
