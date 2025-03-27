# [General]

## Type user names that should not be allowed to input commands
## Useful for banning bots or trolls from inputting commands, either by accident or on purpose
BannedUsers = ["namehere"]

# DICTIONARY OF WORDS FOR THE SPELLING GAME
full_dictionary = ["test"]

# Disable same user playing twice in a row, recommended to prevent users from cheating
disableSameUser = False

# Print the current word progress to the console
printProgress = False

# Announce the completion of a word in chat
announceWin = True

# [ Connection Settings ]

# TWITCH CONNECTION SETTINGS

# Your Twitch username
TWITCH_CHANNEL = ""

# Are you streaming on Twitch? 
# Set this to True if you are, False if you're streaming on Youtube
STREAMING_ON_TWITCH = True

# YOUTUBE CONNECTION SETTINGS

# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = ""

# Your Youtube Stream URL. 
# Replace NONE with your stream URL if you're streaming on Youtube
YOUTUBE_STREAM_URL = None


# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch. 
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.6
# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages. 
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 
