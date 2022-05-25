import os
import discord
import secrets
import string
import random
import requests
import json
import datetime
import time

passlength = 16
specialcharacters = "!@#$'%^\"&*()[]{}-_"

token = os.environ['TOKEN']


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  print(response)
  json_data = json.loads(response.text)
  print (json_data)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def get_ip():
  r = requests.get("https://api.ipify.org/?format=json")
  return r.json()['ip']
  
def get_bored():
  r = requests.get("https://www.boredapi.com/api/activity")
  return r.json()['activity']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower().startswith('!commands'):
    await message.channel.send('Hello my Friend!!!! How r u???? Try to type:\n!hello: to say hello\t\n!ciao: to say ciao\t\n!fluffy: for Fluffy\'s bio\t\n!time or !date: for UTC time\t\n!randompwd: to generate random password\t\n!randomuser: to generate random username\t\n!inspire: Daily Inspirational Quotes\t\n!yt: Youtube Link\t !twitch: Twitch Link')

  if message.content.lower().startswith('!hello'):
    await message.channel.send('Hello!')

  if message.content.lower().startswith('!ciao'):
    await message.channel.send('Ciao!')

  if message.content.lower().startswith('!fluffy'):
    await message.channel.send('Hey dude! My name is Fluffy and I am here to help you')

  if message.content.lower().startswith('!randompwd'):
      source = string.ascii_letters + string.digits + specialcharacters
      password = ''.join(secrets.choice(source) for i in range(passlength))
      await message.channel.send(password)

  if message.content.lower().startswith('!randomuser'):
    with open('nouns.txt', 'r') as infile:
      nouns = infile.read().strip(' \n').split('\n')
    with open('adjectives.txt', 'r') as infile:
      adjectives = infile.read().strip(' \n').split('\n')
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    word1 = word1.title()
    word2 = word2.title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))
    await message.channel.send(username)

  if message.content.lower().startswith('!inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.content.lower().startswith('!time') or message.content.lower().startswith('!date'):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    await message.channel.send("UTC time is: %s " %(st))

  if message.content.lower().startswith('!yt'):
    link="https://www.youtube.com"
    await message.channel.send(link)

  if message.content.lower().startswith('!twitch'):
    link="https://www.twitch.tv"
    await message.channel.send(link)

  if message.content.lower().startswith('!ip'):
    ip = get_ip()
    await message.channel.send(ip)

  if message.content.lower().startswith('!bored'):
    bored = get_bored()
    await message.channel.send("If u are bored, u can %s"%(bored))


client.run(token)