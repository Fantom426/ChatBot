
import aiml
import telebot
import constants
import os
import random


kernel = aiml.Kernel()
bot = telebot.TeleBot(constants.token)

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std_startup.xml", commands = "LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")


@bot.message_handler(commands=["start"])
def handle_text(message):
    bot.send_message(message.chat.id, "Welcome")


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id,
                     ("I can help you"))


@bot.message_handler(commands=['stop'])
def handle_text(message):
    bot.send_message(message.chat.id, "..")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "PHOTO":
        directory = "C:/ChatBot/Photo"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
    else:
        bot_responce = kernel.respond(message.text, message.chat.id)
        bot.send_message(message.chat.id, bot_responce)




bot.polling(none_stop=True, interval=0)