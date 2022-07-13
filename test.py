import requests

oauth = '1086qrtpttkoegzh1y638n8tdxiud2'

headers = {
    'Authorization': 'Bearer ' + oauth
}

client_id = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()['client_id']
id = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()['user_id']
headers = {
    'Authorization': 'Bearer ' + oauth,
    'Client-Id': client_id
}
stream_key = requests.get('https://api.twitch.tv/helix/streams/key',
                   params={'broadcaster_id': id},
                   headers=headers).json()
print(stream_key)