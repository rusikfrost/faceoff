import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import seed
from random import randint

from app import *
from bot import *

import requests
import time
import json
import sys
import os

def write_msg(user_id, message):
	vk.method('messages.send', {'user_id': user_id, 'random_id':randint(0, 999999), 'message': message})

# API-ключ созданный ранее
token = "e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, mode=2)

# Основной цикл
for event in longpoll.listen():
	# Если пришло новое сообщение
	if event.type == VkEventType.MESSAGE_NEW:
		#print(event.type)
		# Если оно имеет метку для меня( то есть бота)
		if event.to_me:
		
			# Сообщение от пользователя
			request = event.text
			
			# Каменная логика ответа
			if request == "привет":
				write_msg(event.user_id, "Хай")
			elif request == "пока":
				write_msg(event.user_id, "Пока((")
			elif request == "нах":
				break
				exit()
			elif request == "":
				print("--------------------------------------------------------------------------------------------------")
				attach1 = (event.message_id)
				#test_ph = ("https://vk.com/im?sel=-152643625&z=photo"+attach1+"%2Fmail1840505")
				print(attach1)
				resp = requests.post("https://api.vk.com/api.php?oauth=1&method=messages.getById&message_ids="+str(attach1)+"&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
				r = resp.json()
				print(r)
				#print(type(event))
				print("--------------------------------------------------------------------------------------------------")
				#time.sleep(3) 

				#https://sun9-56.userapi.com/c855432/v855432044/1d405a/ecIWzXBWuIs.jpg
				# 300397513_457258451
				#https://vk.com/im?sel=-152643625&z=photo300397513_457258451%2Fmail1840505
				
				
				# здесь скорее всего берется первый элемент или отрабатывает раньше, чем загрузится фото
				#resp = ""
				#r = ""
				#resp = requests.post("https://api.vk.com/api.php?oauth=1&method=messages.getHistoryAttachments&start_from=0&peer_id=300397513&preserve_order=1&media_type=photo&count=1&v=5.67&access_token=e18295dcb57646dce3ab05d11d9766507573ddbc2e6cdce7c99d5de3956aafe83cea3b4f349f297610091")
				#r = resp.json()
				#print(r['response']['items'][0]['attachment']['photo']['photo_807'])
				img = requests.get(r['response']['items'][0]['attachments'][0]['photo']['photo_807'])
				img_file = open('img.jpg', 'wb')
				img_file.write(img.content)
				img_file.close() 
				#os.system("app.py")
				#print(r)
				fuckThePhoto('img.jpg')
				write_msg(event.user_id, "yop")
			else:
				print(event.message)
				write_msg(event.user_id, "Не поняла вашего ответа...")


"""
img = r.get("img_url")
img_file = file('path_to_image', 'w')
img_file.write(img.content)
img_file.close() 
"""