import requests

def get_champion_name(champion_id):
    # Get latest game version
    response = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    latest_version = response.json()[0]

    # Fetch all champions' data
    champ_data_url = f"http://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
    response = requests.get(champ_data_url)
    champ_data = response.json()['data']

    # Fetch the data for this champion
    for champ_name, champ_info in champ_data.items():
        if champ_info['key'] == str(champion_id):
            return champ_name

    return "No champion found with the given id."


#print(get_champion_name(266))  # This will print "Annie"
