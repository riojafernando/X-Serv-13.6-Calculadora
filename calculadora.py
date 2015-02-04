#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

"""Calculadora sencilla que suma, resta, multiplica y divide"""

def sumar(sumando1, sumando2):
    """Suma dos enteros o floats"""
    return sumando1 + sumando2

def restar(minuendo, sustraendo):
    """Resta dos enteros o floats"""
    return minuendo - sustraendo

def multiplicar(factor1, factor2):
    """Multiplica dos enteros o floats"""
    return factor1 * factor2

def dividir(dividendo, divisor):
    """Divide dos enteros o floats"""
    return dividendo / divisor

if __name__ == "__main__":
	operacion = str(sys.argv[1])

	try:
		numero1 = float(sys.argv[2])
	except ValueError:
		sys.exit("Sorry, I need a number ")

	try:
		numero2 = float(sys.argv[3])
	except ValueError:
		sys.exit("Sorry, I need a number ")

	if operacion == "sum":
		print ("El resultado es: " + str(sumar(numero1, numero2)))
	elif operacion == "rest":
		print ("El resultado es: " + str(restar(numero1, numero2)))

	elif operacion == "div":
		try:
			print ("El resultado es: " + str(dividir(numero1, numero2)))
		except ZeroDivisionError:
			sys.exit("I can't solve this operation ")

	elif operacion == "mult":
		print ("El resultado es: " + str(multiplicar(numero1, numero2)))
	else:
		print ("Your operation is incorrect")

