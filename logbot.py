import discord
import asyncio
import threading
import re
import requests
import json
import os
import cgi
import urllib.parse
from random import randint
from time import gmtime, strftime

messages = 0
client = discord.Client()

token = os.environ.get('token')
apikey = os.environ.get('api_key')


@client.event
async def on_ready():
	print("-----------------------------------------")
	print("Logged in as: ", client.user.name + "")
	print("UID:",client.user.id) 
	print("Discord version:",discord.__version__)
	print("----------")
    
@client.event
async def on_message_delete(message):
    mystring = message.content
    isascii = lambda s: len(s) == len(s.encode())
    if isascii(mystring) == True:
        print("Name: " + str(message.author.name + "#" + message.author.discriminator))
        #print("URL " + str(message.author.avatar))
        print("Message: " + str(message.content))
        print("Channel: " + str(message.channel.name))
        lol = message.content
        lol = lol.replace("'", "")
        lol = lol.replace("<<", "")
        lol = lol.replace("<", "< ")
        #lol = lol.replace("<", "(arrow left)")
        #lol = lol.replace("+", "%2B");
        lol = urllib.parse.quote(lol)
            
        print("Message After Encoding/Edits: " + str(lol))
            
        if message.attachments:
            x = str(message.attachments[0])
                
            l = x.replace("'", '"')
                
            y = json.loads(l)
            
            #print(y["proxy_url"])
            
        #print("Type " + str(message.channel.type))
        print("[BETA] Sending request.....")
            
        if (message.author.bot == False):
            if message.author.avatar_url == client.user.default_avatar_url:
                avatar = str("https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png")
            else:
                avatar = str(message.author.avatar_url)
            if not message.content.startswith("```") and len(lol) > 3 and "wheel" not in lol:
                if not message.attachments:
                    if str(message.channel.type) == "private":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + str(lol) + "&type=Private&is_image=0")
                    if str(message.channel.type) == "text":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + str(lol) + "&type=Server" + "&type_name=" + str(message.server.name) + "&channel_name=" + str(message.channel.name) + "&is_image=0")
                    if str(message.channel.type) == "group":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + str(lol) + "&type=Group" + "&type_name=" + str(message.channel) + "&channel_name=" + str(message.channel.name) + "&is_image=0")
                else:
                    if str(message.channel.type) == "private":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + y["proxy_url"] + "&type=Private" + "&is_image=1")
                    if str(message.channel.type) == "text":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + y["proxy_url"] + "&type=Server" + "&type_name=" + str(message.server.name) + "&channel_name=" + str(message.channel.name) + "&is_image=1")
                    if str(message.channel.type) == "group":
                        response = requests.get("http://removed.ga/apirequest?api_key=" + apikey + "&name=" + message.author.name + "@" + message.author.discriminator +  "&avatar_url=" + avatar + "&message=" + y["proxy_url"] + "&type=Group" + "&type_name=" + str(message.channel) + "&channel_name=" + str(message.channel.name) + "&is_image=1")

client.run(token, bot=False, reconnect=True)