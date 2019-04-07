# twitterframe

🥚🔜🐦 twiterframe. A basic command line application used in tandem with Twitter API to create .csv files.

In the future this project will have an interactive shell that will feature creating, connecting and committing to a database.

# Project Currently: **BETA**

Mac saved the project. Shoutout to @macscheffer

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

🔜 ```listener``` will be a group of subcommands that will either start or stop the twitter streamer.

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

❗️ ```crawl``` gets a Twitter error response: status code = 429 due to the application's rate limit on the amount of requests to be served.

❗️ ```listener``` does not do anything. Yeah I know, big issue here.

❗️ Some exceptions are not working apprropriately.

❗️ Honestly there are so many known issues at this point LOL

❗️ ```tweepy``` does not have enough attributes in the class methods to my liking.

❗️ Going to learn some more object oriented programming and classmethod related stuff, so that I can either A) build a new tweepy or B) add more funcitonality to the next version of tweepy.

❗️ Streaming does not work.

❗️ RateLimitError is not being raised even if intentional.

### Contributors with 💚

🏆 @colejhudson

🏆 @macscheffer

### Contact

📬 christopher.a.louie@gmail.com


