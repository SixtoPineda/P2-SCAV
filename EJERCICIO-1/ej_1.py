import subprocess

archivo = input("\n\nIntroduzca el nombre COMPLETO o path del archivo con el que trabajar: ")

#mostramos el bit_rate, la "duration" del viedo, y el codec tanto del audio como del video.
subprocess.run(f"ffprobe -v error -show_entries format=bit_rate:format=duration:stream=codec_long_name -of default=noprint_wrappers=1 {archivo}", shell=True)
