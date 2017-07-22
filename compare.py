from pypubg import core
import re

# Load our API key here from a file
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

# Retrieve Stats for a player based on their region and gamemode
def retrieve_stats(key, player, mode, region):
    # Setup the api connection
    pubgapi = core.PUBGAPI(key)
    # Get the Raw Stats for the player
    p_stats = pubgapi.player_mode_stats(player, game_mode=mode, game_region=region)
    return p_stats

# Get a specific stat for a specific player from there stats collection
def get_specific_stat(player_stats, name):
    for stats in player_stats:
         for data in stats['Stats']:
              if data['label'] == name:
                  return data['value']


trn_key = api_key_load("api_key")

for player in ("akustic", "denahuen"):
    p_stats = retrieve_stats(trn_key,player,"solo","agg")
    print("{}: ".format(player))
    for stat_label in ("K/D Ratio", "Rating", "Win %"):
        value = get_specific_stat(p_stats, stat_label)
        print("{}: {}".format(stat_label, value))
