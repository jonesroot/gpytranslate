from setuptools import setup, find_packages

setup(
    name="gpytranslate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx", "ujson"
    ],
    author="JonesRoot",
    description="Google Translate unofficial API",
)
