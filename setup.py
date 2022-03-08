from setuptools import setup

setup(
    name="z^2",
    version="0.1.4",
    description="The z^2 Programming Language",
    url="https://github.com/kokonut27/zsq",
    author="kokonut27",
    license="Apache 2.0",
    packages=["zsq"],
    install_requires=["click"],
    scripts=["scripts/zsq", "tests/tests.py"],
)