import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo')
    print('client.user.name')
    print(client.user.id)

#Geral

@client.event
async def on_member_join(member):
  canal = client.get_channel("418078186828595200")
  regras = client.get_channel("417825019746320384")
  msg = "Bem vindo {}\n leia as {}".format(member.mention, regras.mention)
  await client.send_message(canal,msg)
  await client.send_message(member,msg)

@client.event
async def on_member_remove(member):
    canal = client.get_channel("418078186828595200")
    msg = "Vamos sentir a tua falta,{}.".format(member.mention)
    await client.send_message(member, msg)
    await client.send_message(canal,msg)

#Diversão

@client.event
async def on_message(message):
    if message.content.lower().startswith('l!ajuda'):
        await client.send_message(message.channel, "```css\n Lista dos Comandos:\n Diversão: l!moeda, \n Musica: l!entrar, l!sair```")


    if message.content.lower().startswith('l!moeda'):
        choice = random.randint(1,2)

    if choice == 1:
       await client.send_message(message.channel, "Você tirou coroa!")

    if choice == 2:
       await client.send_message(message.channel, "Você tirou cara!")
