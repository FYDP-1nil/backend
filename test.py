import requests
# page_id_1 = 101787976183954
# facebook_access_token_1 = 'EAAILuM32DZBEBAEzXmfQKvjHyBcsYum2kiWOn7yAxcTxtSHKvJHfreIVGThZByL03p7Qw2IBG3ZCcZA6LIoXdgLaHRf41XMB5J0UCQfZCMwWDm8lJs9YBalq5HnsWZBLIHRfLtALZCmeBJDVU6DUSZAQnY4633H247bTrTidwyS1ORZCWBwzepnJoFYtrKFMcTET9NoZC7cvjwaKVp8BMRMk7PPeYIylZBogyc3rIyaazOjEAZDZD'
# # image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
# post_url = 'https://graph.facebook.com/{}/feed/'.format(page_id_1)
# # print(post_url)
# # image_location = 'http://image.careers-portal.co.za/f_output.jpg'
# payload = {
# 'message': "Hi I am scheduler of 1 nil, i m cute",
# 'access_token': facebook_access_token_1
# }
# #Send the POST request
# r = requests.post(post_url, payload)
# print((r.status_code == 200))

page_id_1 = 101787976183954
facebook_access_token_1 = 'EAAILuM32DZBEBANiH9IUe3hRNeNupYikcYJbq2qZBXx1I1ZBx3bweC2imZAy79Y3t8bNwjWCKuTMafZAeTO22mRP7vaFJxNaItPlTWEsZBqw0QEb2CNdISEO42i1xWa6YedJpHF8c8Pf37RqvGAUZB6c7f3kZA3uKeQixQ0GN7p7f208uDNzZAsQfSZBsA9ENIGNT6ftYuk3hp5gZDZD'
post_url = 'https://graph.facebook.com/{}/feed/'.format(page_id_1)
payload = {
    'message': "For 40 yards....KICK IS GOOD!!!\n\nEagles [3] - Giants 0",
    'access_token': facebook_access_token_1
}
r = requests.post(post_url, payload)
print((r.status_code == 200))
# page_id_1 = 101787976183954
# facebook_access_token_1 = 'EAAILuM32DZBEBAEzXmfQKvjHyBcsYum2kiWOn7yAxcTxtSHKvJHfreIVGThZByL03p7Qw2IBG3ZCcZA6LIoXdgLaHRf41XMB5J0UCQfZCMwWDm8lJs9YBalq5HnsWZBLIHRfLtALZCmeBJDVU6DUSZAQnY4633H247bTrTidwyS1ORZCWBwzepnJoFYtrKFMcTET9NoZC7cvjwaKVp8BMRMk7PPeYIylZBogyc3rIyaazOjEAZDZD'
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