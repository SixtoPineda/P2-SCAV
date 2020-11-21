import subprocess

#Pedimos al usuario que nos de al nombre del archivo completo, es decir, con el .mp4, .jpg, .png, etc.
#Y le pedimos que nos diga que resolución quiere ponerle a dicho documento.
in_file = input("Introduzca el nombre COMPLETO del archivo al que aplicar el cambio de resolución: ")
print("\nA continuación introduzca la resolución deseada:\n")
width= input("Width: ")
height = input("height: ")
print("\n")

subprocess.run(f"ffmpeg -i {in_file} -vf scale={width}:{height} {width}x{height}-{in_file} ", shell=True)

print("\n\n\n\tARCHIVO GENERADO CORRECTAMENTE CON EL NOMBRE: ",width,"x",height,"-",in_file,"\n\n\n" )
