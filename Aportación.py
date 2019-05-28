from time import sleep
import os
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
 
# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2
 
# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)
 
 
# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)


print ('Digite 1 para proyectar el mensaje ')
a= int(input())
if a!=1:
    print ('opcion incorrecta')
else:
    if a==1:
     lcd.message = "INTERFAZ \n   AMIGABLE"
     print ('Digite 2 para borrar la pantalla')
     b= int(input())
     if b==2:
       lcd.clear()
       print ('pantalla borrada')
     else:
       print ('opcion incorrecta') 
