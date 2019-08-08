# twitterframe

🥚🔜🐦 twiterframe. A basic command line application used in tandem with Twitter API to create .csv files.

In the future this project will have an interactive shell that will feature creating, connecting and committing to a database.

# Project Currently: **ON HOLD**

- somewhat functional, use at your own expense or make a pull request to improve on it if you wish!

# Installation and Usage:

- **Coming soon**.

# Progress so far...

✅ Users are able to create .json files to store their API keys.

✅ Added click functionality.

✅ Functional Command Line Application by invoking ```twitterframe```

✅ Added a command that removes your Twitter API credentials file from your home directory.

✅ ```scrape``` command is now functioning as it should be.

✅ Opened up project on pypi.org so it can be 'pip-install-able' [here](https://pypi.org/project/twitterframe/)

🔜 Make some basic documentation on installation/usage.

🔜 ```crawl``` command will require a mandatory argument for how many tweets to get per request, and the rate limit for the TwitterAPI is reached, an exception is passed.

✅ ```listener``` will be a group of subcommands that will either start or stop the twitter streamer.

🔜 **Shell environment**. Instead of it just being a command-line-application where we invoke twitterframe, I would like to just invoke twitterframe to build out a shell environment to do all of these cool twitter things.

🔜 In the true working version of this project, I definitely want to have the shell environment up and running.

🔜 The goal is to honestly make it into a really comfortable shell environment for commands and managing databases.

🔜 This is starting to get less simple... lol

🔜 Add functionality for a StreamListener class that will listen for live tweets and bin based on sentiment.

🔜 Decorate the command line application with more colors


# Ideas on new features and commands

💡 Command that dumps tweets into a SQL database.

💡 Add more emojis.

💡 Add click.progress_bar(s) on commands like ```scrape``` and ```crawl``` to show progress.

💡 Remove some of the comments because the code looks kinda ugly.

💡 A way to parse images in tweets/replies/retweets. Dump into a JSON or CSV.

💡 Add options/configurations to determine the output for exporting tweets from ```scrape```,
```crawl```, etc.

💡 Create options for the output for each given command. (i.e. ```scrape``` would have the option to dump the tweets from user: @twitteruser, to either a CSV, an SQL database, etc.) (etc. is used quite liberally in my explanations of things in this README.)


# Known issues

❗️ ```crawl``` command is not pulling tweets by the specified times.


### Contributors with 💚

🏆 @colejhudson

🏆 @macscheffer

### Contact

📬 christopher.a.louie@gmail.com


