from setuptools import setup, find_packages

setup(
    name="starwars-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]==0.9.0",
        "rich==13.7.0",
        "httpx==0.25.2",
    ],
    entry_points={
        "console_scripts": [
            "starwars=cli:app",
        ],
    },
)