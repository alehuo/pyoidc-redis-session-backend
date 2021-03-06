import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyoidc-redis-session-backend",
    version="1.0.3",
    author="alehuo",
    author_email="aleksi.huotala@helsinki.fi",
    description="Redis-based session storage for oic library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alehuo/pyoidc-redis-session-backend",
    packages=['pyoidc_redis_session_backend'],
    py_modules=['pyoidc_redis_session_backend.RedisSessionBackend'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    install_requires=['oic', 'jsonpickle', 'redis', 'pycryptodome', 'pycryptodomex'],
    python_requires='>=3.6',
)