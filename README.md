# Onigiri

Unofficial Python SDK for RIT Translate


Install
====


```
pip install onigiri
```

Usage
====

```python
from onigiri import Client

# Initialize the client.
oni = Client(rapidapi_key="...") # Fill in the '...' with the approp$

# Translate a single sentence.
oni.translate('I am pregnant.', target_language='fr', source_language='en')
```
