from SunFounder_Line_Follower import Line_Follower
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar

lf = Line_Follower.Line_Follower()
UA = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)

print("Calibration sensibilité suiveur de ligne")
time.sleep(0.5)
print("Veuillez poser le robot sur du blanc (absence de ligne)")
print("Tourner le potentiomètre jusqu a obtenir tout juste la valeur maximale")

for i in range(1,30):
	print(lf.read_analog())
	print('')
	time.sleep(0.5)

print("Veuillez poser le robot sur du noire")
print("Assurez-vous qu'une valeur presque minimale est affichée, sinon ajusté le potentiomètre")
for i in range(1,30):
	print(lf.read_analog())
	print('')
	time.sleep(0.5)

print("Calibration sensibilité suiveur de ligne terminée")
time.sleep(0.5)
print("Calibration sensibilité détecteur obstacle")
time.sleep(0.5)
print("Veuillez poser le robot devant un obstacle à la distance d arret desiree")
print(""Assurez-vous de retiré tous les autres objets dans son champs de vision")
time.sleep(5)
print(pret)
time.sleep(1)
for i in range(1,4):
	print(printUA.get_distance())
	print('')
	time.sleep(0.5)

print("Noter les valeurs donnees. Ces valeurs devraient etre utilisees comme mesure de detection d obstacle")


