from setuptools import setup, find_packages

setup(
    name="gpytranslate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.27.2,<0.28.0", "ujson"
    ],
    author="JonesRoot",
    description="[FORK] Google Translate unofficial API.",
)
