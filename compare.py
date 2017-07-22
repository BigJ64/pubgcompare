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

def build_stat_dict(key, player):
    player_dict = {}
    p_stats = retrieve_stats(key,player,"solo","agg")
    for stat_label in ("K/D Ratio", "Rating", "Win %"):
        player_dict[stat_label] = float(get_specific_stat(p_stats, stat_label))
    return player_dict

# load the api key from the file named api_key
trn_key = api_key_load("api_key")

# Define the empty player list
player_list = []

# Get 2 players and add them to the player list. Don't except empty inputs.
print("Enter the 2 players you would like to compare:" )
while True:
    new_player = input("> ")
    if new_player is not "":
        player_list.append(new_player)
    else:
        print("You didn't enter a player")
    if len(player_list) == 2:
        break

# Get the stats we want for the players on the player list
for player in player_list:
    p_stats = retrieve_stats(trn_key,player,"solo","agg")
    print("{}: ".format(player))
    for stat_label in ("K/D Ratio", "Rating", "Win %"):
        value = get_specific_stat(p_stats, stat_label)
        print("{}: {}".format(stat_label, value))
