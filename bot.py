import requests
import json
import os

def sendThisFuckinPhoto():
	#os.remove("_faces.jpg")
	#os.remove("Image_res.jpg")
	#os.remove("img.jpg")
	#os.remove("faces_detected.jpg")
	#requests.post("https://api.vk.com/api.php?oauth=1&method=messages.send&user_id=300397513&message=ky&attachment=&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
	resp = requests.post("https://api.vk.com/api.php?oauth=1&method=photos.getMessagesUploadServer&peer_id=300397513&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
	r = (resp.json())
	"""
	{'response': 
	{'album_id': -64, 
	'upload_url': 'https://pu.vk.com/c858136/upload.php?act=do_add&mid=-152643625&aid=-64&gid=0&peer_id=300397513&rhash=66fd35828faf90f0cebe2d3d4b87d10d&api=1&method=message&mailphoto=1&server=858136&_origin=https%3A%2F%2Fapi.vk.com&_sig=78f1bdecd32cc2df89be7205cf4a1dff', 'user_id': 0, 'group_id': 152643625}}
	"""
	files = {"file": open("blank_with_text.jpg", "rb")}
	#args = {"key": "API_KEY"}
	url = r['response']['upload_url']


	#{'response': [{'id': 457258287, 'album_id': -64, 'owner_id': 300397513, 'photo_75': 'https://sun9-19.userapi.com/c858436/v858436835/148484/VqTX-PiQZqE.jpg', 'photo_130': 'https://sun9-22.userapi.com/c858436/v858436835/148485/v8le5zHBxes.jpg', 'photo_604': 'https://sun9-4.userapi.com/c858436/v858436835/148486/msle1ae6YqE.jpg', 'width': 511, 'height': 511, 'text': '', 'date': 1579385002, 'access_key': 'f3c58221ab1c718e73'}]}
	#print(r['response']['upload_url'])

	data = requests.post(url, files=files)
	data = (data.json())

	files["file"].close()

	resp = requests.post("https://api.vk.com/api.php?oauth=1&method=photos.saveMessagesPhoto&photo="+str(data['photo'])+"&hash="+str(data['hash'])+"&server="+str(data['server'])+"&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
	r = (resp.json())
	print(r['response'][0])

	photo = "photo"+str(r['response'][0]['owner_id'])+"_"+str(r['response'][0]['id'])+"_"+str(r['response'][0]['access_key'])

	requests.post("https://api.vk.com/api.php?oauth=1&method=messages.send&user_id=300397513&attachment="+photo+"&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
	#os.remove("blank_with_text.jpg")