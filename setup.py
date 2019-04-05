"""
twitterframe
- a command line application to create dataframes from Twitter data.
- Must have Twitter developer keys to use.
"""

import setuptools

REQUIRED = [
    "tweepy",
    "pandas",
    "click"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(

    name="twitterframe",
    version="1.0.0",
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    entry_points='''
        [console_scripts]
        twitterframe=twitterframe.main:cli
    ''',

    )
