from pypubg import core
import re

# Define our API key here from a file

def api_key_load(file_name):
    try:
        file = open(file_name)
    except IOError:
        print("Error: {} file does not appear to exist.".format(file_name))
        raise
    else:
        for line in file:
            # Strip out any whitespace
            li = line.strip()
            # Set our matching pattern to try and verify the key before using it
            pattern = re.compile("^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$")
            # Match our api key and set it as the key to use
            if not li.startswith("#") and pattern.match(li):
                key = li.rstrip()
                return key
                file.close()

trn_key = api_key_load("api_key")

# Setup the api connection
pubgapi = core.PUBGAPI(trn_key)

# Print out the Raw Stats for one player
print(pubgapi.player_mode_stats("akustic", game_mode="solo", game_region='agg'))

# Print Player Skill
print(pubgapi.player_skill("akustic", game_mode="solo"))
