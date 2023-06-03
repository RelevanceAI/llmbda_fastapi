from setuptools import find_packages, setup
from llmbda_fastapi import __version__

core_reqs = [
    "fastapi",
    "pydantic",
    "requests",
    "six",
    "sniffio",
    "starlette",
    "tqdm",
    "typing_extensions",
    "tzdata",
    "urllib3",
    "uvicorn",
    "wincertstore",
    "relevanceai",
]

setup(
    name="llmbda_fastapi",
    version=__version__,
    url="https://relevanceai.com/",
    author="Relevance AI",
    author_email="jacky@relevanceai.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=core_reqs,
    package_data={"": ["*.ini"]},
    extras_require=dict(),
)
