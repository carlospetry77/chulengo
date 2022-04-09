#import smbus

#Esta librería sirve para definir todas las funciones a utilizar dentro del programa principal.



def hola(name):
    return print("Hola, ", name)

def read():
    return

def write():
    return

def config():
    return

def write_lcd(msg):
    #Acá se debe enviar el mensaje al lcd.
    return

def release_cap():
    return print("Liberando tapa...")

def fill_cap():
    return print("Cargando tapas...")

def push_bottle(dist):
    return print("Empujando botellas...")

def fill_bottle(size):
    return print("Llenando botellas...")

def close_bottle(size):
    return print("Tapando botellas...")

def conveyor_belt(mode):
    if mode == 'ON':
        return print("Cinta encendida...")
    elif mode == 'OFF':
        return print("Cinta apagada...")

def whaser(seg=0, mode):
    if mode == 'ON'and seg > 0:
        print("Lavando botellas...")
    elif mode == 'ON' and seg <= 0:
        print("Error, el tiempo de lavado debe ser mayor de cero")
    elif mode == 'OFF':
        print("Apagar bomba...")
    else:
        print("Configuración incorrecta")