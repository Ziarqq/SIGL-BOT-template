# SIGL-BOT 2021

## Pre-requisites
* Have discord installed on your laptop or access it through a web browser

## Useful References
- Discord API Documentation : https://discord.com/developers/docs/intro
- Discord.py Library Documentation : https://discordpy.readthedocs.io/en/stable/index.html
- Python Package Manager Documentation : https://pypi.org/project/pip/


## Setup 

* Create a new discord server, this will be your test sandbox for testing your bot 
* Go to https://discord.com/developers/applications and create a new application. Give it the name you want and add a cool profile picture for it 
* Under the 'bot' tab, click on 'Add a bot', give it a username as well 
* Reveal your bot private token and paste it in `main.py` 
* Activate developpers feature :
    * Go to discord settings > App settings > Advanced
    * Activate developper mode
* Right click on your nickname in the right-side bar of your server and click on ' Copy ID'. Paste it in the `author_id` variable ìn `main.py`
* Add the bot to your server by clicking on the OAuth2 tab 
    * Select the `bot` scope and `Admministrator` permissions
    * A URL will then be generated. By clicking on it, you will have the opportunity to add your bot to one of the server you already joined

## Advices
- **Code quality** and **lisibility** as well as documentation on how you solved problems will be greatly appreciated/rewarded
- Cheating is allowed, but **getting catched isn't**
- Your bot ability to produce **well-formatted answers** on the server is as important as solving the problem
- You are allowed to invite members to your server for test purposes
- Creation of new files is recommended. Clean architectures will be rewarded
- Extra-miles are challenges to go further with a particular usecase. Focus on the Todo-list then the extra miles items

## TODO LIST

### Warm-up 

[X] When typing `!name` the bot should write back the name of the user typing the command

[X] When typing `!count` the bot should write back for each possible status (Online, Offline, Idle, Do not disturb) the number of members (including yourself) in the server with that status
- Example : "3 members are online, 2 are idle and 4 are off"
- Extra mile : Instead of counting the members, list them sorted by status

### Administration
[X] When typing `!admin <A member nickname>`, your bot should create an Admin role (if it doesn't exists) on your server, allowing them to manage channels, kick and ban members, and give it to the member in parameter

[-] When typing `!mute <A member nickname>`, your bot should create a Ghost role (if it doesn't exists), disabling all textual channels permissions for that member. When typing that command towards an already muted member, the action should be reverted

[X] When typing `!ban <A member nickname>`, your bot should ban that member from the server (**Test with caution**)

### It's all fun and games
[X] When typing `!xkcd`, your post should post a random comic from https://xkcd.com

[ ] When typing `!poll <question> <choice1?> <choice2?>, ... <choice n?> `, your bot should post a @here mention followed by your question. If none of the choice arguments are filled, your bot should by default react with one :thumbsup: emoji and one :thumbsdown: emoji in order to allow people to vote. If at least two choices arguments are filled, the bot should react with the appropriate emojis. Any other call should result in an error
- Example : `!poll "Should we get burgers or salad tonight ?" :hamburger: :salad:`
- Extra-mile : Define a time-limit for the poll. When the limit has been reached, bot will bot a message with the final result and delete the original poll message

[ ] When typing `!tictactoe <player1> <player2>` the bot should launch a game of textual tictactoe between the two players, allowing them to play turn after turn until one player wins or draw game

### Bonus

If you reached this point, congratulations, you have a basic bot for your discord server. Check for the extra-mile content if you didn't already. Otherwise, try to think of some fun or useful features to add to your bot among which :

 - Setting reminders for events 
 - Rewarding the most active members of your server
 - Advanced role management (Directing new members to a #rules channel and giving them basic permissions after they agree, )


