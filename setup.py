from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="progzee",
    version="0.1.3",
    description="A Python tool for making HTTP requests with proxy rotation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aldin Kiselica",
    url="https://github.com/kiselitza/progzee",
    packages=find_packages(),
    install_requires=["requests", "click"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "progzee=progzee.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
