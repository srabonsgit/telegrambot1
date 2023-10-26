import telebot
from telegram import Update

from telegram.ext import Application, CommandHandler, MessageHandler, filters, _contexttypes

#commands

async def start_command(update:Update, context):
        await update.message.reply_text('Hey Buddy Iam a simple bot working for Deadpool. please contact him directly')
async def help(update:Update, context):
    await update.message.reply_text('Iam a robo working under, and iam in under constraction. Please contract the developer directly')
# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('6734265868:AAGIkfyFwVm1uxEU8Xyfg-16pc_MxrDvjzY')

@bot.message_handler(func=lambda message: message.text.lower() == '-alive')
def reply_canva_pro(message):
    bot.reply_to(message, 'Yes Iam alive go sleep')

@bot.message_handler(func=lambda message: message.text.lower() == 'bye')
def reply_canva_pro(message):
    bot.reply_to(message, 'Okay bye')

@bot.message_handler(func=lambda message: message.text.lower() == '@srabondm8')
def reply_canva_pro(message):
    bot.reply_to(message, 'Iam busy now')

@bot.message_handler(func=lambda message: message.text.lower() == 'canva lgbe nh')
def reply_canva_pro(message):
    bot.reply_to(message, 'latti dimu')

@bot.message_handler(func=lambda message: message.text.lower() == '@srabondm8 achen')
def reply_canva_pro(message):
    bot.reply_to(message, 'nahi')

@bot.message_handler(func=lambda message: message.text.lower() == '-speed-test')
def reply_canva_pro(message):
    bot.reply_to(message, 'Downlod speed 10 mbps upload speed 12mbps. Test complete in 2s ')
@bot.message_handler(func=lambda message: message.text.lower() == '-bam-a')
def reply_canva_pro(message):
    bot.reply_to(message, '@aurum443 valo hoye jan naile khobor ache')

@bot.message_handler(func=lambda message: message.text.lower() == '-bam-b')
def reply_canva_pro(message):
 bot.reply_to(message, '@black2o12  valo hoye jan naile khobor ache')

@bot.message_handler(func=lambda message: message.text.lower() == '-gal-i')
def reply_canva_pro(message):
 bot.reply_to(message, '২। কুত্তার বাচ্ছা  ৩। হারামির বাচ্চা ৪। হারামি ৫। হারামজাদা ৬। হারামখোর ৭। খাঙ্কিরপোলা ৮। খান্কি মাগির পোলা ৯চোদনা ১০। চুদির ভাই ১১। চুতমারানি ১২। চুদির পোলা ১৩। তর মায়রে চুদি ১৪। তর মায়রে বাপ ')

@bot.message_handler(func=lambda message: message.text.lower() == 'canva')
def reply_canva_pro(message):
 bot.reply_to(message, 'Yes avilable dm srabonsm8')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'Hey Buddy I am a simple bot working for Deadpool. Please contact him directly')


# Start the bot
bot.polling()
Expose 3306
