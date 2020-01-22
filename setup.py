import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyoidc-redis-session-backend-alehuo",  # Replace with your own username
    version="1.0.0",
    author="Aleksi Huotala",
    author_email="aleksi.huotala@helsinki.fi",
    description="Redis-based session storage for pyoidc library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alehuo/pyoidc-redis-session-backend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['oic', 'jsonpickle', 'redis', 'pycryptodome'],
    python_requires='>=3.6',
)