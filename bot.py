# -*- coding: utf-8 -*-


import telebot
import FechaHora
import time
import random

btoken = '794080034:AAFIoR4bNFeFIsyrEe2Oe1FWhzi-TZvx0Fg'
bot = telebot.TeleBot(token=btoken)

comandos = {
	"start": 'Bienvenido a TalkerBot',
	"help" : 'Soy solo un bot conversador, comenzemos a hablar! Podés'+
		'pedirme que guarde una nota, una alerta, pedirme la hora y el día,'+
		'y más, pero mucho más!',
	"commands" : 'listar comandos',		
	"alertas" : 'Guarda alertas y te avisa'
}

saludos = ["hola", "holaa", "holi", "que onda?", "hii"]
dia = ["DIA", "dia", "Dia", "Día", "día"]
hora = ["HORA", "Hora", "hora"]

# ---------------- BIENVENIDO -------------------------
@bot.message_handler(commands=["start"])
def send_welcome(m):
	bot.reply_to(m, comandos["start"] + ", " + str(m.chat.first_name))

@bot.message_handler(commands=["help"])
def command_help(msg):
	bot.reply_to(msg, comandos["help"])

# ---------------- FECHA Y HORA -----------------------
@bot.message_handler(func = lambda msg: msg.text in dia)
def at_answer(msg):
	bot.reply_to(msg, time.strftime("%d/%m"))
	
@bot.message_handler(func = lambda msg: msg.text in hora)
def at_answer(msg):
	bot.reply_to(msg, time.strftime("%H:%M"))


# ------------------ SALUDOS --------------------------

def verificar(msg):
	for i in saludos:
		if i in msg: 
			return True
	
@bot.message_handler(func=lambda msg: verificar(msg.text))
def command_text_hi(msg):
    bot.send_message(msg.chat.id, random.choice(saludos))
    
    
    
bot.polling()
