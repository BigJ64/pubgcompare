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
    api = core.PUBGAPI(key)
    # Get the Raw Stats for the player
    p_stats = api.player_mode_stats(player, game_mode=mode, game_region=region)
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

# Define the empty player list
pl_list = []

# Get 2 players and add them to the player list. Don't except empty inputs.
print("Enter the 2 players you would like to compare:" )
while True:
    new_player = input("> ")
    if new_player is not "":
        pl_list.append(new_player)
    else:
        print("You didn't enter a player")
    if len(pl_list) == 2:
        break

# Get stats dictonary for each player
player_0 = build_stat_dict(api_key_load("api_key"), pl_list[0])
player_1 = build_stat_dict(api_key_load("api_key"), pl_list[1])

print('')
# Display K/D Ratio Comparison
print("{} has a K/D Ratio of {}.".format(pl_list[0],player_0['K/D Ratio']))
print("{} has a K/D Ratio of {}.".format(pl_list[1],player_1['K/D Ratio']))
if player_0['K/D Ratio'] > player_1['K/D Ratio']:
    print("{} has the better K/D Ratio.".format(pl_list[0]))
elif player_0['K/D Ratio'] < player_1['K/D Ratio']:
    print("{} has the better K/D Ratio.".format(pl_list[1]))
else:
    print("{} and {} have an equal K/D Ratio.".format(pl_list[0],pl_list[1]))
print('')
# Display Win % Comparison
print("{} has a Win % of {}% ".format(pl_list[0],player_0['Win %']))
print("{} has a Win % of {}%.".format(pl_list[1],player_1['Win %']))
if player_0['Win %'] > player_1['Win %']:
    print("{} has the better Win %.".format(pl_list[0]))
elif player_0['Win %'] < player_1['Win %']:
    print("{} has the better Win %.".format(pl_list[1]))
else:
    print("{} and {} have an equal Win %.".format(pl_list[0],pl_list[1]))
print('')
# Display Skill Rating Comparison
print("{} has a Skill Rating of {}.".format(pl_list[0],player_0['Rating']))
print("{} has a Skill Rating of {}.".format(pl_list[1],player_1['Rating']))
if player_0['Rating'] > player_1['Rating']:
    print("{} has the better Skill Rating.".format(pl_list[0]))
elif player_0['Rating'] < player_1['Rating']:
    print("{} has the better Skill Rating.".format(pl_list[1]))
else:
    print("{} and {} have an equal Skill Rating.".format(pl_list[0],pl_list[1]))
