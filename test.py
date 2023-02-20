# import requests
# page_id_1 = 101787976183954
# facebook_access_token_1 = 'EAAILuM32DZBEBANgvn1cD5swm8MgdBEUJ3nZBpxql6Ta6d2eD3wmuWsBKC30A7Fb1GTCIbfX0bZBh1ZCMeaVKbKZAQEzwi01d29yc7mmb7XWL7uMkyqaZCrMEgIYt8nqxi514ZCh7rQqzqPvEyicqAK5WWZBPGpwzYgUChWaHMMXNKl1ZBuohuheSC7dlP1E96WlpULr2UDP92xCeaU2itzIX'
# image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
# image_location = 'http://image.careers-portal.co.za/f_output.jpg'
# img_payload = {
# 'url': image_location,
# 'access_token': facebook_access_token_1
# }
# #Send the POST request
# r = requests.post(image_url, data=img_payload)
# print(r.text)
# oauth = 'hwlx7ujsduz9x75i75v8malkhzhrc2'

# headers = {
#     'Authorization': 'Bearer ' + oauth
# }

# response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers).json()
# client_id = response['client_id']
# print(client_id)
# broadcaster_id = response['user_id']
# headers = {
#     'Authorization': 'Bearer ' + oauth,
#     'Client-Id': client_id
# }
# stream_key = requests.get('https://api.twitch.tv/helix/streams/key',
#                             params={'broadcaster_id': broadcaster_id},
#                             headers=headers).json()
# print(stream_key)