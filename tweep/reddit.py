import praw
from dotenv import load_dotenv, find_dotenv
import os

from tweepy.models import User

load_dotenv(find_dotenv())

ID = os.getenv("ID")
SECRET = os.getenv("SECRET")
CONSOLE = os.getenv("CONSOLE")
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

agent = praw.Reddit(
    client_id=ID,
    client_secret=SECRET,
    user_agent=CONSOLE,
    username=USERNAME,
    password=PASSWORD
)


class Reddit:
    def __init__(self):
        self.already = []

    def already_done(self, sub):
        if sub in self.already:
            return True

    def get_link(self, sub):
        return sub.url

    def reply(self, sub, comment):
        try:
            sub.reply(comment)
            self.already.append(sub)
        except Exception as e:
            print(e)
