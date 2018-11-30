# -*- coding: utf-8 -*-
import time

MINIMO_LETRAS = 3

DIA = ["DIA", "dia", "Dia", "Día"]
HORA = ["HORA", "Hora", "hora"]

def verificar(mensaje):
	if mensaje.length > MINIMO_LETRAS:
		return mensaje in HORA
	return mensaje in DIA

def obtener_fecha():
	return time.strftime("%d/%m")
	
def obtener_hora():
	return time.strftime("%H:%M")
		
	
	
	
