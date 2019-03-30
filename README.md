# twitterframe

🥚🔜🐦 twiterframe. A basic command line application used in tandem with Twitter API to frame content from Twitter as a CSV.

In the future, I want to add more flexibility with the preferred output. (i.e. JSON, SQL databases, etc.)

# Progress so far...

✅ Users are able to create .json files to store their API keys.

✅ Added click functionality.

✅ Functional Command Line Application by invoking ```twitterframe```

✅ Added a command that removes your Twitter API credentials file from your home directory.

✅ ```scrape``` command is now functioning as it should be.

✅ Opened up project on pypi.org so it can be 'pip-install-able' [here](https://pypi.org/project/twitterframe/)

🔜 Make some basic documentation on installation/usage.

🔜 ```crawl``` command will require a mandatory argument for how many tweets to get per request, and the rate limit for the TwitterAPI is reached, an exception is passed.

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

### Contributors with 💚

🏆 @colejhudson

### Contact

📬 christopher.a.louie@gmail.com


