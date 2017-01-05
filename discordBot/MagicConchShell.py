from random import randint

class MagicConchShell():

    magicConchSpeech = ["Maybe someday", "Nothing", "Neither", "Follow the seahorse", "I don't think so", "No", "Yes","Try asking again"]
    def __init__(self):
         return

    def responseToCall(self):
         response = self.magicConchSpeech[randint(0, len(self.magicConchSpeech) - 1)]
         return response



