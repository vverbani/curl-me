# Curl Me

Python script to imitate heavy traffic for API's. Curl Me allows full control over API traffic being pushed towards your API. This was created for the purpose of testing how an API or APIM will handle the heavy traffic.

The total requests made against an API are calculated based off (total requests / worker). More requests would require more async workers to perform all the requests in a timely fashion. More workers however use more resources, so please use this at your own risk.

## Prerequisites

1. Latest [Python](https://www.python.org/downloads/) Version

## Usage

Note that these calls were made when Python3 was the latest available version. When cloning this repo - this may change depending on your version. Please reference the download documentation listed above in the #Prerequisites section.


### Short form arguments

```bash
python3 curl-me.py -u http://localhost:8080/new-api/get -r 11 -p '{"names": ["J.J.", "April"], "years": [25, 29]}' -h '{Authorization: 123asdasd983ikjv76h3h4j4jnaas}
```

### Long form arguments

```bash
python3 curl-me.py -u http://localhost:8080/new-api/get --range 11 --payload '{"names": ["J.J.", "April"], "years": [25, 29]}' --h '{Authorization: 123asdasd983ikjv76h3h4j4jnaas}
```