from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

botName = 'Your friend:'

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)

for file in os.listdir('C:/Users/rados/repos/ChatBot\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    print(file)
    data = open('C:/Users/rados/repos\ChatBot\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'+file, 'r').readlines()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print(botName,reply)
    else:
        print(botName, 'Bye! :(')
        break