from setuptools import setup, find_packages

setup(
    name="progzee",
    version="0.1.0",
    description="A Python library for simplifying IP proxy usage in HTTP requests, with proxy rotation.",
    author="Aldin Kiselica",
    packages=find_packages(),
    install_requires=["requests", "click"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "progzee=progzee.cli:cli",
        ],
    },
)
