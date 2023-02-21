import sys
import time
import telepot
from telepot.loop import MessageLoop
from instabot import Bot
import os

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'photo':
        print("Text: " + str(msg))

        filename = str(msg['photo'][-1]['file_id'])
        print("Dateiname: " + filename)
        description = msg['caption']
        print("Beschreibung: " + description)
        bot.download_file(msg['photo'][-1]['file_id'], "temp.png")



        instabot.upload_photo("temp.png", caption=description)
        cwd = os.getcwd()
        os.remove(cwd + "/temp.png")


if __name__ == '__main__':
    instabot = Bot()
    instabot.login(username="ENTER INSTA USERNAME", password="ENTER INSTA PASSWORD")
    token = open('token.txt', 'r').read().replace('\n', '')

    bot = telepot.Bot(token)
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')
    while 1:
        time.sleep(10)
