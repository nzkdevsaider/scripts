import datetime
import time
hora = datetime.datetime.now()
reloj = hora.strftime("%H:%M:%S")

print(reloj)
print("La siguiente hora se mostrará en 2 horas, 10 minutos y 20 segundos")


def timer():
    while True:
        time.sleep(7820)
        print(reloj)
