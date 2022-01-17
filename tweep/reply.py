
class Reply:

    def cleanse_markdown(self, text):
        final = text.replace("#", "\\#").replace(
            "_", "\\_").replace("[", "\\[").replace("`", "\\`")
        return final

    def gen_name(self, names):
        screen = names[0]
        handle = names[1]
        final = "*Name* : **{}** (@{})".format(screen, handle)
        return final

    def gen_mentions(self, mentions):
        screens = mentions[0]
        names = mentions[0]
        final = """  
                \n\n*Mentions* : """
        if len(screens) == 0:
            return "\n\nMentions: None"
        for i in range(len(screens)):
            final += "**{}** (@{}), ".format(screens[i], names[i])
        final = final[:-2]
        return final

    def gen_text(self, text):
        text = self.cleanse_markdown(text)
        final = """  
                \n\n*Content* : \n\n> {}""".format(text)
        return final

    def gen_favorites(self, favorites):
        final = """  
             \n\n*Likes* : {}""".format(favorites)
        return final

    def gen_retweets(self, retweets):
        final = """  
             \n\n*Retweets* : {}""".format(retweets)
        return final

    def gen_media(self, media):
        if len(media) == 0:
            return """  
                 \n\n*Media* : None"""
        final = """  
                \n\n"""
        for i in range(len(media)):
            final += "[Attachment]({}) ".format(media[i])
        return final

    def gen_hashtags(self, hashtags):
        if len(hashtags) == 0:
            return """  
            \n\n*Hashtags* : None"""
        final = """  
        \n\n*Hashtags* : """
        for hashtag in hashtags:
            final += "\#{} ".format(hashtag)
        return final

    def reply(self, name, mentions, text, favorites, retweets, media, hashtags):
        rname, rmentions, rtext, rfavorites, rretweets, rmedia, rhashtags = self.gen_name(name), self.gen_mentions(mentions), self.gen_text(
            text), self.gen_favorites(favorites), self.gen_retweets(retweets), self.gen_media(media), self.gen_hashtags(hashtags)
        final = rname + rmentions + rtext + rfavorites + rretweets + rmedia + rhashtags
        # final.join((rname, rmentions, rtext, rfavorites,
        #           rretweets, rmedia, rhashtags))
        return final
