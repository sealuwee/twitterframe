# twitterframe

🥚🔜🐦 twiterframe. A basic command line application used in tandem with Twitter API to frame content from Twitter into your preferred format.

In the future, I want to add more flexibility with the preferred output. (i.e. JSON, SQL databases, etc.)

# Project Currently: **ON HOLD**

[Tweepy](https://github.com/tweepy/tweepy/blob/e6616fed65e75bbb93633290eadd5940c41772e7/tweepy/models.py#L73) does not currently have the values from Twitter's API that I would like to use for the purpose of this project.

For example, if you click on the link for tweepy, it should bring you to Line 73 of the ```tweepy/models.py``` script, where the ```class Status(Model):```  and ```@classmethod``` is located. The ```Status``` object (which is just a ```Tweet``` object) from Twitter's API should give you a set of attributes like the following from the [Twitter Developer documentation](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object).

Unforunately, if we refer back to [tweepy](https://github.com/tweepy/tweepy/blob/e6616fed65e75bbb93633290eadd5940c41772e7/tweepy/models.py#L73), inside of the parse function, we can see that the ```key,value``` pairings do not provide as many ```Tweet``` object attributes as one may like to have. (That one being me.) And so what I am going to be working on in the mean time is a pull request to @tweepy, and add the attributes I want to see from Twitter's API.

Hopefully all goes well and i'll be able to use tweepy once again, and finish up this command-line-application, but in the mean time, please use my pre-alpha version from the **Installation**.

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

### Contact

📬 christopher.a.louie@gmail.com


