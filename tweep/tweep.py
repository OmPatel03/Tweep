from reddit import *
from twitter import *
from reply import *
import time
from keep_alive import keep_alive
rbot = Reddit()
tbot = Twitter()
replier = Reply()


def reply_generator(sub):
    link = rbot.get_link(sub)
    name, mentions, text, favorites, retweets, media, hashtags = tbot.get_data(
        link)
    reply = replier.reply(name, mentions, text, favorites,
                          retweets, media, hashtags)
    return reply


def main():
    while True:
        times = 0
        for sub in agent.domain("twitter.com").new():
            if times >= 30:
                break
            if rbot.already_done(sub):
                continue
            reply = reply_generator(sub)
            rbot.reply(sub, reply)
            time.sleep(60)
            times += 1


keep_alive()
while True:
    main()
