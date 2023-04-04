# Collecting Data

startingYear = 2023  # First year data will be collected for
finalYear = 2023  # Final year data will be collected for

# Rating Player

# Offensive Statistics
offense = {
    "orbWeight": 1,     # Offensive Rebounds
    "astWeight": 1,     # Assists Per Game
    "ppgWeight": 2.5,   # Points Per Game
    "astpcWeight": .5,  # Assist Percentage
    "owsWeight": 2,     # Offensive Win Share
    "tspcWeight": .5,   # True Shooting Percentage
    "perWeight": 3.5,   # Player Efficiency Rating
    "obpmWeight": 4.5,  # Offensive Box Plus Minus
    "ptsWeight": 2,     # Total Points
    "usgpcWeight": .5   # Usage Percentage
}

# Defensive Statistics
defense = {
    "drbWeight": .75,     # Defensive Rebounds
    "stlWeight": 1,     # Steals Per Game
    "blkWeight": 1,     # Blocks Per Game
    "stlpcWeight": 1.5,  # Steal Percentage
    "blkpcWight": 1.5,   # Block Percentage
    "dwsWeight": 2.5,     # Defensive Win Shares
    "dbpmWeight": 3,  # Defensive Box Plus Minus
}

MAX_RATING = 98         # Rating of the player who had the best season
MIN_RATING = 68         # Rating of the player who had the worst season
