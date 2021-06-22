import discord
from discord import Spotify
from discord.ext import commands
import io
import subprocess
import aiohttp
import requests
import praw
import random
import ffmpeg
import asyncio
from datetime import datetime, timedelta
import time
import r6stats
import weather
import sysinfo
import sys
import ctx
from discord.voice_client import VoiceClient
import youtube_dl
import coinflip
import blackjack
import json
import ast
#sys.path.insert(1, 'chatbot/')
#import main
import logging
import os
import threading
from twisted.internet import task
from twisted.internet import reactor
import minecraft_heads
import minecraft_skins
from io import BytesIO
from PIL import Image


timeout = 10.0

logger = logging.getLogger('mylogger')

handler = logging.FileHandler('discordbot.log')
logger.addHandler(handler)

client = discord.Client()

reddit = praw.Reddit(client_id="praw client-id",
                     client_secret="praw client-secret",
                     user_agent="praw user-agent")

subreddits_darkmemes = ["lmGoingToHellForThis", "darkmemers", "dark_edgy_memes", "DarkMemesForDarkHumou"]   #list of subreddits the bot chooses from
subreddits_hentai = ["hentai", "ecchi", "hentaisource", "animemilfs"]

#darkemes is under quarantine!

subreddit = reddit.subreddit("darkmemers")
alrsend_img = []
dm_img = []
hn_img = []
ff_img = []
mp3_qu = []
users = {}
timedout = False
@client.event
async def on_ready():
    global startup_time
    startup_time = datetime.now()
    #startup_time = startup_time.strftime("%X")
    print('logged in as {0.user}'.format(client))
    #print('---------------------------')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def endSong(guild, path):
    os.remove(path)

class afkwaiter(object):
    def __init__(self):
        pass
    def waiter(self):
        while True:
            channel = client.get_channel(id="afk-channel-id")
            vc = channel.connect()
            if vc.members:
                vc = channel.connect()
            if not vc.members:
                vc.disconnect()
            #await channel.connect()
    
                    


class blackjack(object):
    def __init__(self):
        pass
    def wait(self):
        timedout = False
        time.sleep(60)
        timedout = True


class listManager(object):
    def __init__(self):
        print("thread1 started")
        #with open('user_messages_backup.txt', 'r') as f:
        #    #s = f.read()
        #    startup_dict = f.read()
        #    print("startup_dict: " + startup_dict)
        #    users = startup_dict
        #    print("users: " + users)

        #with open('user_messages_backup.txt', 'w') as file:
        #    file.write(json.dumps(startup_dict))
        #    file.close()

    def rem(self):
        while True:
            if len(alrsend_img) >= 1:
                try:
                    print("removed:", alrsend_img[0], "from _sub")
                    del alrsend_img[0]
                except:
                    print("nothing in list _sub")
            if len(dm_img) >= 1:
                try:
                    print("removed: ", dm_img[0], " from _darkmeme")
                    del dm_img[0]
                except:
                    print("nothing in list _darkmeme")
            if len(hn_img) >= 1:
                try:
                    print("removed: ", hn_img[0], " from _hentai")
                    del hn_img[0]
                except:
                    print("nothing in list _hentai")
            if len(ff_img) >= 1:
                try:
                    print("removed: ", ff_img[0], " from _5050")
                    del ff_img[0]
                except:
                    print("nothing in list _5050")
            if len(mp3_qu) >= 1:
                try:
                    print("removed: ", mp3_qu[0])
                    logger.warning(str(datetime.now().strftime("%d.%m.%Y %X")) +": " + "removed: "+ mp3_qu[0])
                    os.remove(mp3_qu[0])
                except:
                    print("nothing there")

            #with open('user_messages_backup.txt', 'w') as file:
            #    file.write(json.dumps(users))
            #    print("saved")
            #    file.close()
            time.sleep(1800) # 1800

def start():
    r = listManager()
    r1 = afkwaiter()
    t1 = threading.Thread(target=r.rem)
    t2 = threading.Thread(target=r1.waiter)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    #t2.start()
def start_blackjack_waiter():
    r = blackjack()
    t1 = threading.Thread(target=r.wait)
    t1.setDaemon(True)
    t1.start()

start()



@client.event
async def on_voice_state_update(member, before, after):
    id = "afk-channel-id"
    if not member.id == "id from bot":
        try:
            if after.channel.id == id:
                try:
                    voice_client = await client.get_channel(id=id).connect()
                    await voice_client.guild.get_member("id from bot").edit(mute=False)     #enmute self in afk channel

                    for vc in client.voice_clients:
                        vc.play(discord.FFmpegPCMAudio(source='music/afk_wait.mp3'))
                        
                except Exception as e:
                    pass
                
        except AttributeError as e:
            for voice_client in client.voice_clients:
                await voice_client.disconnect()




@client.event
async def on_message(message):
    client = discord.Client()
    if message.author == client.user:
        return

    msg = message.content
    if message.content.startswith('_'):
        print("---------------------------------------")
        print(message.author,": ", msg)
        #logger.warning(str(datetime.now().strftime("%d.%m.%Y %X")) +": " + str(message.author) + ": " + str(msg))


    #message counter
    #message_author = str(message.author)
    #if message_author in users:
    #    print("User in dictionary!")
    #    users[str(message.author)] += 1
    #else:
    #    users[str(message.author)] = 1

    #if message.content.startswith('_messages'):
    #    temp = message.content
    #    user_name = temp.split(" ")[1]
    #    await message.channel.send(str(user_name) + ": " + str(users[user_name]))



    #if message.content.startswith('_read_test'):
    #    with open('user_messages_backup.txt', 'r') as f:
    #        s = f.read()
    #        test_dict = ast.literal_eval(s)
    #    print(test_dict)


#help
    if message.content.startswith('_help'):
        await message.channel.send("```Commands: \n"
                                   "_sys \n"
                                   "_pic \n"
                                   "_size \n"
                                   "_darkmeme \n"
                                   "_hentai \n"
                                   "_uptime \n"
                                   "_wetter berlin/weimar \n"
                                   "_sub <subreddit> <number of pictures the bot should send> \n"
                                   "_flip <kopf/zahl> \n"
                                   "_r6 <username> for r6s stats \n"
                                   "_spam <username> <1-10 number of messages> (if no number is provided it will be set to 1) \n"
                                   #"_head <name> searches for minecraft head commands \n"
                                   "_skin <username> download skin from user ```")
                                   #"_chat to chat with me(alpha) \n"

#send pic
#    if message.content.startswith('_pic'):
#        localFile=open("filename.jpg","wb")
#        try:
#            conn.retrieveFile("img_share","filename.jpg",localFile) 
#        except Exception as e:
#            print(e)
#            connect_smb()
#            conn.retrieveFile("img_share","filename.jpg",localFile) 
#        pic = open("filename.jpg", "rb")
#        channel = message.channel
#        await channel.send(file=discord.File(pic, 'pic.jpg'))

#coinflip
    if message.content.startswith('_flip'):
        temp = message.content
        side = temp.split(" ")[1]
        player = message.author.mention
        res = coinflip.flip()
        if side == "kopf":
            kopf = 1
            zahl = 0
        if side == "zahl":
            kopf = 0
            zahl = 1

        if res == kopf:
            await message.channel.send(f"{player} hat Gewonnen!")
        else:
            if side == "kopf":
                await message.channel.send(f"{player} leider Zahl :(")
            if side == "zahl":
                await message.channel.send(f"{player} leider Kopf :(")



#join vc
#    if message.content.startswith('_join'):
#        author = message.author
#        channel = author.voice.channel
#        vc = await channel.connect()
#        #await channel.connect()
#    elif message.content.startswith('_disconnect'):
#        for vc in client.voice_clients:
#            if vc.guild == message.guild:
#                await vc.disconnect()
#play
#    if message.content.startswith('_play'):
#        temp = message.content
#        url = temp.split(" ")[1]
#        for vc in client.voice_clients:
#        #    vc.play(discord.FFmpegPCMAudio('test.mp3'))
#            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                file = ydl.extract_info(url, download=True)
#
#                path = str(file['title']) + "-" + str(file['id'] + ".mp3")
#                mp3_qu.append(path)
#                print(mp3_qu)
#
#            vc.play(discord.FFmpegPCMAudio(path))
#            vc.source = discord.PCMVolumeTransformer(vc.source, 1)
#
#            await message.channel.send(f"Playing... {url}")

#    elif message.content.startswith('_stop'):
#        pass





#systeminfo
    if message.content.startswith('_sys'):
        await message.channel.send(f"CPU: {sysinfo.cpu()}%")
        await message.channel.send(f"RAM: {sysinfo.ram()}G")

#spam user _spam <id> <number of msg> <msg>
    if message.content.startswith('_spam'):
        index = 0
        temp = message.content
        user = temp.split(" ")[1]
        try:
            num = temp.split(" ")[2]
        except IndexError as e:
            num = 1
        if int(num) > 10:
            num = 10
        msg = temp.split(" ")[3:]
        msg2 = ' '.join(msg)
        while int(index) < int(num):
            await message.channel.send(f"{user} {msg2}")
            index += 1


#ping (MUSS IN EINEM NEUEN THREAD GESTARTED WERDEN SONST WARTET DER BOT AUF EINE ANTWORT VOM SERVER -> BOT STOPT FÜR X SEKUNDEN)
#    if message.content.startswith('_ping'):
#        temp = message.content
#        ip_to_ping = temp.split(" ",1)[1]
#        server_response = os.system('ping -c 1 ' + ip_to_ping)
#        if server_response == 0:
#            await message.channel.send("Server " + ip_to_ping + " is up!")
#        else:
#            await message.channel.send("Server " + ip_to_ping +  " is down!")

#chatbot
#    if message.content.startswith('_chat'):
#        temp = message.content
#        msg = temp.split(" ",1)[1]
#        main.inp = msg
#        main.chat(main.inp)
#        await message.channel.send(main.out)

    '''
#minecraft heads
    if message.content.startswith('_head'):
        #await search_for_mc_heads()
        temp = message.content
        minecraft_heads.sterm = temp.split(" ")[1]
        c_results = temp.split(" ")[2]
        minecraft_heads.result = c_results
        minecraft_heads.search(minecraft_heads.sterm, minecraft_heads.result)
        channel = message.channel
        a = 0
        for i in minecraft_heads.data:
            print(a)
            await message.channel.send(minecraft_heads.cmd[a])
            data = i #bytes(''.join(minecraft_heads.data[i]))
            stream = BytesIO(data)
            await channel.send(file=discord.File(stream, 'img.png'))
            a += 1
    '''
    #    temp = message.content
    #    minecraft_heads.sterm = temp.split(" ")[1]
    #    c_results = temp.split(" ")[2]
    #    minecraft_heads.result = c_results
    #    minecraft_heads.search(minecraft_heads.sterm, minecraft_heads.result)
    #    channel = message.channel
    #    a = 0
    #    for i in minecraft_heads.data:
    #        print(a)
    #        await message.channel.send(minecraft_heads.cmd[a])
    #        data = i #bytes(''.join(minecraft_heads.data[i]))
    #        stream = BytesIO(data)
    #        await channel.send(file=discord.File(stream, 'img.png'))
    #        a += 1

#minecraft skin download
    if message.content.startswith('_skin'):
        temp = message.content
        mc_user = temp.split(" ",1)[1]
        minecraft_skins.player_name = mc_user
        minecraft_skins.search(minecraft_skins.player_name)
        channel = message.channel
        msg = "User: " + mc_user
        await message.channel.send(msg)
        stream = BytesIO(minecraft_skins.data)
        await channel.send(file=discord.File(stream, 'skin.png'))

#r6stats
    if message.content.startswith('_r6'):
        temp = message.content
        r6stats.username = temp.split(" ",1)[1]
        r6stats.search(r6stats.username)
        await message.channel.send(r6stats.ges)

#uptime/user uptime
    if message.content.startswith('_uptime'):
        now = datetime.now()
        uptime = now - startup_time
        uptime = str(uptime).split(".", 1)[0]
        await message.channel.send(f"Uptime: {uptime} (Bot)")

#weather
    if message.content.startswith('_wetter'):
        temp = message.content
        city = temp.split(" ",1)[1]

        weather.get_weather(city)

        if city == "weimar":
            await message.channel.send(f"```Weimar: \n - Temperatur: {weather.we_temp_c} °C \n - Gefühlt wie: {weather.we_feels_c} °C \n - Luftfeuchtigkeit: {weather.we_hum} %```")
        if city == "berlin":
            await message.channel.send(f"```Berlin: \n - Temperatur: {weather.be_temp_c} °C \n - Gefühlt wie: {weather.be_feels_c} °C \n - Luftfeuchtigkeit: {weather.be_hum} %```")
        if city == "graz":
            await message.channel.send(f"```Graz: \n - Temperatur: {weather.ga_temp_c} °C \n - Gefühlt wie: {weather.ga_feels_c} °C \n - Luftfeuchtigkeit: {weather.ga_hum} %```")

#darkmemes
    if message.content.startswith('_darkmeme'): # and str(message.channel) == "channelname": to restrict to specific channel
        for submission in reddit.subreddit(random.choice(subreddits_darkmemes)).random_rising(limit=1):
            print(submission.title)
            print(submission.url)
            while submission.url in dm_img:
                for submission in reddit.subreddit(random.choice(subreddits_darkmemes)).random_rising(limit=1):
                    print("new ", submission.title)
                    print("new ", submission.url)

        if submission.url.endswith(".png") or submission.url.endswith(".jpg") or submission.url.endswith(".jpeg"):
            async with aiohttp.ClientSession() as session:
                async with session.get(submission.url) as resp:
                    if resp.status != 200:
                        return await channel.send('Could not download file...')
                        await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    channel = message.channel
                    await message.channel.send(submission.title)
                    dm_img.append(submission.url)
                    await channel.send(file=discord.File(data, 'meme.png'))
        else:
            await message.channel.send("Error: File is not an image")

#hentai
    if message.content.startswith('_hentai'): #and str(message.channel) == "channelname": to restrict to specific channel
        for submission in reddit.subreddit(random.choice(subreddits_hentai)).random_rising(limit=1):
            print(submission.title)
            print(submission.url)
            while submission.url in hn_img:
                for submission in reddit.subreddit(random.choice(subreddits_hentai)).random_rising(limit=1):
                    print("new ", submission.title)
                    print("new ", submission.url)

        if submission.url.endswith(".png") or submission.url.endswith(".jpg") or submission.url.endswith(".jpeg"):
            async with aiohttp.ClientSession() as session:
                async with session.get(submission.url) as resp:
                    if resp.status != 200:
                        return await channel.send('Could not download file...')
                        await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    channel = message.channel #restrict to specific channel :client.get_channel("<channelid for hentai>")
                    await message.channel.send(submission.title)
                    hn_img.append(submission.url)
                    await channel.send(file=discord.File(data, 'hentai.png'))
        else:
            await message.channel.send("Error: File is not an image")

#50/50
    if message.content.startswith('_5050') and str(message.channel) == "fiftyfifty":
        for submission in reddit.subreddit("FiftyFifty").random_rising(limit=1):
            print(submission.title)
            print(submission.url)
            while submission.url in ff_img or "v.redd.it" in submission.url:
                for submission in reddit.subreddit("FiftyFifty").random_rising(limit=1):
                    print("new ", submission.title)
                    print("new ", submission.url)
            extension_url = submission.url.split(".")
            extension_url = extension_url[-1]
            print("extension : " + extension_url)
            if extension_url == "jpg" or extension_url == "png" or extension_url == "jpeg":
                is_video = False
                extension = "." + extension_url
            else:
                is_video = True


        if submission.url.endswith(".png") or submission.url.endswith(".jpg") or submission.url.endswith(".jpeg"):
            async with aiohttp.ClientSession() as session:
                async with session.get(submission.url) as resp:
                    channel = message.channel #restrict to specific channel :client.get_channel("<channelid for 50/50 channel>")
                    if resp.status != 200:
                        return await channel.send('Could not download file...')
                        await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())

                    await message.channel.send(submission.title)
                    ff_img.append(submission.url)
                    if is_video == False:
                        print("isnt video")
                        f5_name = "some" + extension
                    else:
                        await channel.send("Downloading video...")
                        f5_name = "some.mp4"
                    print("f5_name : " + f5_name)
                    await channel.send(file=discord.File(data, f5_name, spoiler=True))
        else:
            await message.channel.send("Error: File is not an image")

#own subreddit:
    try:    #try except only bc of invalid subreddits (404)
        if message.content.startswith('_sub'):
            temp = message.content
            subredd = temp.split(" ")[1]
            try:
                user_limit = temp.split(" ")[2]
                user_limit = int(user_limit)
                print(user_limit)
            except:
                print("error no comment given")
                user_limit = 1

            for number in range(user_limit):
                print("number: " + str(number))

                for submission in reddit.subreddit(subredd).random_rising(limit=1):
                    print(submission.title)
                    print(submission.url)
                    while submission.url in alrsend_img:
                        for submission in reddit.subreddit(subredd).random_rising(limit=1):
                            print("new ", submission.title)
                            print("new ", submission.url)
                    extension_url = submission.url.split(".")
                    extension_url = extension_url[-1]
                    print("extension : " + extension_url)

                    if extension_url == "jpg":
                        is_video = False
                        extension = "." + extension_url
                    if extension_url == "png":
                        is_video = False
                        extension = "." + extension_url
                    if extension_url == "jpeg":
                        is_video = False
                        extension = "." + extension_url
                    else:
                        is_video = False
                        #submission.url = submission.url + "/DASH_720.mp4"
                        print("mp4: " + submission.url)
                        extension = "." + extension_url

                #if submission.url.endswith(".png") or submission.url.endswith(".jpg") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif"):
                async with aiohttp.ClientSession() as session:
                    async with session.get(submission.url) as resp:
                        if resp.status != 200:
                            return await channel.send('Could not download file...')
                            await message.channel.send('Could not download file...')
                        data = io.BytesIO(await resp.read())
                        channel = message.channel
                        await message.channel.send(submission.title)
                        alrsend_img.append(submission.url)
                        if is_video == False:
                            f_name = "some" + extension
                        else:
                            await channel.send("Downloading video...")
                            f_name = "some.mp4"
                        print("f_name : " + f_name)
                        await channel.send(file=discord.File(data, f_name))
        #else:
            #await message.channel.send("Error: File is not an image")
    except Exception as e:
            print("error occurred! " + str(e))
            logger.error(str(datetime.now().strftime("%d.%m.%Y %X")) +": ! " + str(e) + " on section #own subreddit")
            await message.channel.send("Error(file is to large or does not exist)")

    if message.content.startswith('_clear_sub') and str(message.author) == "admin#0001":
        print(alrsend_img)
        print("clearing alrsend_img...")
        alrsend_img.clear()
        print(alrsend_img)
    if message.content.startswith('_clear_ff') and str(message.author) == "admin#0001":
        print(ff_img)
        print("clearing ff_img...")
        ff_img.clear()
        print(ff_img)
    if message.content.startswith('_clear_hn') and str(message.author) == "admin#0001":
        print(hn_img)
        print("clearing hn_img...")
        hn_img.clear()
        print(hn_img)
    if message.content.startswith('_clear_dm') and str(message.author) == "admin#0001":
        print(dm_img)
        print("clearing dm_img...")
        dm_img.clear()
        print(dm_img)

#bot size
    if message.content.startswith('_size'):
        file1_len = len(open('discord_bot.py').readlines())
        file4_len = len(open('sysinfo.py').readlines())
        file5_len = len(open('weather.py').readlines())
        #file6_len = len(open('chatbot/main.py').readlines())
        file7_len = len(open('coinflip.py').readlines())
        file8_len = len(open('minecraft_heads.py').readlines())
        file9_len = len(open('minecraft_skins.py').readlines())
        file10_len = len(open('r6stats.py').readlines())
        len_all = int(file1_len)+int(file2_len)+int(file3_len)+int(file4_len)+int(file5_len)+int(file7_len)+int(file8_len)+int(file9_len)+int(file10_len)
        await message.channel.send(f"Bot size: {len_all} lines (9 Files)")


async def search_for_mc_heads():
    temp = message.content
    minecraft_heads.sterm = temp.split(" ")[1]
    c_results = temp.split(" ")[2]
    minecraft_heads.result = c_results
    minecraft_heads.search(minecraft_heads.sterm, minecraft_heads.result)
    channel = message.channel
    a = 0
    for i in minecraft_heads.data:
        print(a)
        await message.channel.send(minecraft_heads.cmd[a])
        data = i #bytes(''.join(minecraft_heads.data[i]))
        stream = BytesIO(data)
        await channel.send(file=discord.File(stream, 'img.png'))
        a += 1



client.run('Bot-token')
