import subprocess

#Pedimos al susuario que nos introduzca el nombre del video original, final para cada una de las resoluciones aplicadas al video original.
name_video = input("Introduzca el nombre del video con el que trabajar (sin extensión): ")
name_1280x720 = input("\nIntroduzca el nombre para video resolución 1280x720: ")
name_640x480 = input("\nIntroduzca el nombre para video resolución 640x480: ")
name_360x240 = input("\nIntroduzca el nombre para video resolución 360x240: ")
name_160x120 = input("\nIntroduzca el nombre para video resolución 160x120: ")

scaleValue = ["1280:720","640:480","360:240","160:120"]#array con las distintas resoluciones
nameVideo = [name_1280x720,name_640x480,name_360x240,name_160x120]#array con cada nombre para cada resolucion
for i in range(len(scaleValue)):

    subprocess.run(f"ffmpeg -i {name_video}.mp4 -vf scale={scaleValue[i]} {nameVideo[i]}.mp4 ", shell=True)
