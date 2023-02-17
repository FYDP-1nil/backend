import requests
page_id_1 = 101787976183954
facebook_access_token_1 = 'EAAILuM32DZBEBACPImGBo0rlpMXh5qrQxbnZAON4lWh6mrdmmRG6gj2e5f1aoOtJ3DbJZAAMXscvJ4YcxVu3PXeBYST4ZBgT5ZAVmxUidyDOnlybZBdXsx3ZAEZAox7R7cOxPhK3TLqPzTxUH85ZBuCfzoNMVAUeZASWrVE8bdagDtzcIzbOeD9ZCXZAx9ZCCf60lmrt2HSH1dxY44SnHrMzj90oazlp89X4qDarpC2eizKRebgZDZD'
image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
image_location = 'http://image.careers-portal.co.za/f_output.jpg'
img_payload = {
'url': image_location,
'access_token': facebook_access_token_1
}
#Send the POST request
r = requests.post(image_url, data=img_payload)
print(r.text)