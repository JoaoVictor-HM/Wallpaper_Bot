# Wallpaper_Bot
This is a discord bot made in python. Its role is to bring good wallpapers to the users of the servers. The wallpapers are taken from a subreddit, 
through the praw api, used to get data from reddit. This api requires the creation of a script on reddit's platform, which is accessed through credentials 
contained in the .env. The env file contained in the repository is an example with the template that should be followed for possible adaptations of the code.
Once the script was created on reddit, the next step was to create the bot itself. This was done in python using the discord.py library. This library makes it 
possible to implement commands using asynchronous functions. This was the main use for the library. 

