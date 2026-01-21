from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linkfy",
    version="1.0.0",
    author="Matheus Campos",
    author_email="mclealpvp10@gmail.com",
    description="A simple CLI tool to shorten URLs with local SQLite history",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusc457/linkfy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "pyperclip>=1.8.0",
    ],
    entry_points={
        "console_scripts": [
            "linkfy=linkfy.main:main",
        ],
    },
)
