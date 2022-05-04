from dotenv import load_dotenv
from instabot import Bot
import os

igbot = Bot()

load_dotenv()
user = os.environ.get('username')
pawd = os.environ.get('password')
igbot.login(username=user, password=pawd)

recipients = ["taindp98"]

text = "Hello, I'm on Instagram as ngochung.ly. Follow my photos and videos with this link: https://www.instagram.com/ngochung.ly/"

igbot.send_messages(text, recipients)