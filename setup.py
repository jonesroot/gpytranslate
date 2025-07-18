from setuptools import find_packages, setup

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "I'm From Indonesian, and I'm still learning."

setup(
    name="gpytranslate",
    version="0.1.1",
    author="LuciferHex",
    author_email="ikyodeos01@gmail.com",
    description="I'm From Indonesian, and I'm still learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["aiofiles~=23.2.1", "httpx[http2]>=0.27.2,<0.28.0"],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="Gtrans",
    python_requires=">=3.9",
)
