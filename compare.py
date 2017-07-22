from pypubg import core

# Define our API key here
trn_key = ""

# Setup the api connection
pubgapi = core.PUBGAPI(trn_key)

# Print out the Raw Stats for one player
print(pubgapi.player_mode_stats("akustic", game_mode="solo", game_region='agg'))

# Print Player Skill
print(pubgapi.player_skill("akustic", game_mode="solo"))
