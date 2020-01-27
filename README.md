# pyoidc-redis-session-backend

This repository contains source code for a Redis-based session storage backend for the `oic` Python library.

## Installation

**This project hasn't been released to PyPi yet, but you can find the test package in TestPyPi: https://test.pypi.org/project/pyoidc-redis-session-backend-alehuo/.**

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

Run tests with `pytest`.

## Contributions

Contributions to this repository are welcome.

## License

This project is licensed with MIT license.