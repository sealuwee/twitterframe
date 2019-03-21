"""
twitterframe
- a command line application to create dataframes from Twitter data.
- must have Twitter developer keys.
"""

import setuptools

REQUIRED = [
    "twitter",
    "tweepy",
    "pandas",
    "click"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(

    name="twitterframe",
    version="0.0.1",
    author="Ruwai",
    description="A basic command line application used in tandem with Twitter API to frame anything from Twitter into a Pandas DataFrame, or exported as a CSV.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Ruwai/twitterframe",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[

        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    entry_points='''
        [console_scripts]
        twitterframe=twitterframe.scripts.cli:cli
    ''',

    )
