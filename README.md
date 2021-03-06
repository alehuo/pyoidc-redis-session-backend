# pyoidc-redis-session-backend

[![PyPI version](https://badge.fury.io/py/pyoidc-redis-session-backend.svg)](https://badge.fury.io/py/pyoidc-redis-session-backend) [![PyPI license](https://img.shields.io/pypi/l/pyoidc-redis-session-backend.svg)](https://pypi.python.org/pypi/pyoidc-redis-session-backend/) [![GitHub issues](https://img.shields.io/github/issues/alehuo/pyoidc-redis-session-backend.svg)](https://GitHub.com/alehuo/pyoidc-redis-session-backend/issues/) [![GitHub pull-requests](https://img.shields.io/github/issues-pr/alehuo/pyoidc-redis-session-backend.svg)](https://GitHub.com/alehuo/pyoidc-redis-session-backend/pulls/)

This repository contains source code for a Redis-based session storage backend for the `oic` Python library.

## Installation

`pip install pyoidc-redis-session-backend`

## Usage

A ready-to-run project is located at https://github.com/alehuo/pyoidc-redis-session-backend-example

Below is an example piece of code that initializes a Redis client which is then used to create an instance of RedisSessionBackend. After that, a Consumer is created which is then configured to use the Redis session backend as its backend.

```python
import redis
from pyoidc_redis_session_backend import RedisSessionBackend
from oic.oic.consumer import Consumer
from oic.utils.authn.client import ClientSecretBasic, ClientSecretPost

redis_client = redis.Redis("localhost", "6379")
# Pass the redis client into the Redis session backend
backend = RedisSessionBackend(redis_client)
# Create an example consumer with example config
consumer = Consumer(backend, {
    "authz_page": "/auth/callback", # Callback URL of your app
    "response_type": "code",
},
    client_config={
    "client_id": "your_client_id", # Client ID
    "client_authn_method": {
        'client_secret_post': ClientSecretPost,
        'client_secret_basic': ClientSecretBasic
    }
})
consumer.provider_config("oidc_server_url") # OIDC server URL
consumer.set_client_secret("your_client_secret") # Client secret
```

## Development

To initialize the development environment, run:

1. Run `python3 -m venv env`
2. Run `source env/bin/activate`
3. Run `pip install -r requirements.txt`

## Running tests

Run tests with `python -m pytest tests/`.

## Contributions

Contributions to this repository are welcome.

## License

This project is licensed with MIT license.
