from __future__ import unicode_literals
import time
import telepot
import requests
import os, sys
import youtube_dl
from pydl import MyLogger, my_hook, ydl_opts
import re
from pprint import pprint

TOKEN = "5390174010:AAFiL6mRSpYhbrzkUe78JKd1Hz8W0TkKUhI"


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    input_text = msg['text']
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)
    path = '/app'
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', input_text)
    url = str(url)
    url = url.replace('[', '')
    url = url.replace("'", '')
    url = url.replace(']', '')
    print(url)
    try:
        msg = bot.sendMessage(chat_id, "Downloading the file...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            # bot.getUpdates
            files = os.listdir(path)
            for file in files:
                if ".mp3" in file:
                    url = "https://api.telegram.org/bot%s/sendAudio" % (TOKEN)
                    files = {'audio': open(file, 'rb')}
                    data = {'chat_id': chat_id}
                    r = requests.post(url, files=files, data=data)
                    # print(r.status_code, r.reason, r.content)
                    pprint(r.content)
                    bot.deleteMessage(telepot.message_identifier(msg))
                    os.remove(file)

    except:
        bot.sendMessage(chat_id, 'Operation failed, please try again later or talk to my creator.')


bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening ...')

while 1:
    time.sleep(10)


