#-----LIBRERIAS-----

import board    # Esta libreria sirve para asignar constantes fijas a los pines
                # del tablero, esto hace que usar el módulo de la placa sea
                # más seguro y confiable 
                
import digitalio   # Este módulo sirve utilizar la pantalla LCD con una
                   # retroalimentación de un solo color, en el caso que se
                   # desee una retroalimentación RGB (varios colores) se debe
                   # definir los pines de salida según su ubicación en el board 
                   # y el color 

import adafruit_character_lcd.character_lcd as characterlcd
            # Este módulo permite escribir fácilmente el código de Python que
            # que controla una LCD de caracteres (ya sea con luz de fondo
            # individual o con luz de fondo RGB)


#------ TAMAÑO DE LA PANTALLA LCD --------
            
lcd_columns = 16   # Estas líneas de código definen el tamaño de caracteres de
lcd_rows = 2       # nuestra LCD, en este caso la pnatalla LCD es de 16 columas
                   # y 2 filas, si se tiene una LCD de caracteres de diferente
                   # tamaño se debe modificar estos valores
                   
#---- ASIGNACIÓN DE LOS PINES DE CONFIGURACIÓN DE LA RASPBERRY PI Y LCD --------                  
                   
#Según la ubicación en la placa :           -LCD-   -RASPBERRY PI 3-MODELO B-                
lcd_rs = digitalio.DigitalInOut(board.D22) # pin 4          pin 15    
lcd_en = digitalio.DigitalInOut(board.D17) # pin 6          pin 11                                                                                      
lcd_d4 = digitalio.DigitalInOut(board.D25) # pin 11         pin 22
lcd_d5 = digitalio.DigitalInOut(board.D24) # pin 12         pin 18
lcd_d6 = digitalio.DigitalInOut(board.D23) # pin 13         pin 16
lcd_d7 = digitalio.DigitalInOut(board.D18) # pin 14         pin 12
 
 
# INICIALIZAMOS LA CLASE LCD

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

# Esta línea de código especifica el tipo de retroalimentación de la pantalla
# reconociendo la función de cada pin de la LCD, la retroalimentacion
# es de un solo color, esto queda especificado en el argumento "Mono", para varios
# colores el argumento sería "RGB"

# CUERPO (VOID)

print ('  Mensaje Proyectado \n')  # En esta línea se imprime un mensaje que 
                                   # indique que el texto ya se proyecto en la LCD
                            
lcd.message = "HERRAMIENTAS DE\n SOFTWARE 5035"  # Esta línea sirve para ESCRIBIR
                                                 # el mensaje que se va a proyectar
                                                 # en la pantalla LCD, tomando en cuenta
                                                 # que solo se pueden escribir 16 caracteres
                                                 # por linea de texto, para escribir
                                                 # en la siguiente linea se utiliza
                                                 # el argumento "\n"

print ('Digite 2 para borrar la pantalla LCD') # En esta línea se imprime un mensaje
                                               # que indica al usuario quede digitar el
                                               # numero 2 para borrar la pantalla del LCD
                                                                                              
a= int(input())  # Se guarda en una variable el valor ingresado por el usuario, el valor es
                 # de tipo entero "int" e "input" debido a que es un dato de entrada
                 
if a==2:   # Primera condición a cumplir según el dato que ingrese el usuario
    
    lcd.clear() # Esta línea sirve para BORRAR la pantalla LCD
    
else:   # Contra punto de la primera condición
    
    print ('Opcion incorrecta') # En el caso que se digite un numero distinto a 2 se imprime
                                # el siguiente mensaje
  