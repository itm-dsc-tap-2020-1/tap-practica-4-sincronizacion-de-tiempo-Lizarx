import datetime
from time import ctime
import ntplib
import os

servidor_de_tiempo = "time-e-g.nist.gov"
cliente_ntp = ntplib.NTPClient()
t1 = datetime.datetime.now()
print("Hora de inicio de la peticion: "+str(t1))
respuesta = cliente_ntp.request(servidor_de_tiempo)
t2 = datetime.datetime.now()
print("Hora de llegada de la peticion: "+str(t2))
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("Hora que se recibió del servidor: "+str(hora_actual))
print("Ajuste: "+str((t2-t1)/2))
Reloj=hora_actual+((t2-t1)/2)
print("Hora cambiada: "+str(Reloj))
os.system(f"date --set '{Reloj}'")