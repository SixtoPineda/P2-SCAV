import subprocess

in_file = input("Introduce el nombre COMPLETO del archivo a transcodificar: ")

#nos devuelve los tipos de codec q tiene el archivo, asi sabemos si tiene canal de audio y video, solo video, o solo audio
codec = subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_type -of default=noprint_wrappers=1 {in_file}", shell=True)

#strings para luego comparar con el sresultado del comando anterior y saber si es video solo o video con audio o solo sea un audio
string_audio_type = str(b'codec_type=audio\n')#solo audio
string_video_type = str(b'codec_type=video\n')#solo video
string_videoAudio_type = str(b'codec_type=video\ncodec_type=audio\n')#video y audio

#Comprobamos si el tipo de archivo con el que trabajar tiene canal de audio y video, solo audio.
videoAudio = (str(codec) == string_videoAudio_type)
audio = (str(codec) == string_audio_type)
video = (str(codec) == string_video_type)

if(videoAudio == True):#tenemos un video con canal de audio y video
    typeTranscode = input("\nTu archivo contiene video y audio, de cual de ellos quiere modificar su codec?\n\tVideo: 1\n\tAudio: 2\n\tAmbos: 3\n\nDiga el número según la opción escogida: ")

    if(int(typeTranscode) == 1):#opción para cambiar el codec del video
        codec_escogido = input("\n\tOpciones de codec: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
        if(int(codec_escogido) == 1):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg1video MPEG1_{in_file}", shell=True)
        elif(int(codec_escogido) == 2):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg2video MPEG2_{in_file}", shell=True)
        elif(int(codec_escogido) == 3):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg4 MPEG4_{in_file}", shell=True)
        elif(int(codec_escogido) == 4):
            subprocess.run(f"ffmpeg -i {in_file} -c:v h264 h264_{in_file}", shell=True)
        print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )

    elif(int(typeTranscode) == 2):#opción para cambiar el codec del audio
        codec_escogido = input("\n\tOpciones de codec para audio: \n\tMP3: 1\n\tAAC: 2\n\t\tNúmero de codec escogido: ")
        if(int(codec_escogido) == 1):
            subprocess.run(f"ffmpeg -i {in_file} -acodec mp3 -vcodec copy MP3_{in_file}", shell=True)
        elif(int(codec_escogido) == 2):
            subprocess.run(f"ffmpeg -i {in_file} -acodec aac -vcodec copy AAC_{in_file}", shell=True)
        print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )

    elif(int(typeTranscode) == 3):#opción para cambiar el codec del video y el audio
        codec_escogido_v = input("\n\tOpciones de codec Video: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
        codec_escogido_a = input("\n\tOpciones de codec para audio: \n\tMP3: 1\n\tAAC: 2\n\t\tNúmero de codec escogido: ")

        if((int(codec_escogido_v) == 1) and (int(codec_escogido_a) == 1)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg1video -c:a mp3 MPEG1_MP3_{in_file}", shell=True)
        elif((int(codec_escogido_v) == 1) and (int(codec_escogido_a) == 2)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg1video -c:a aac MPEG1_AAC_{in_file}", shell=True)

        elif((int(codec_escogido_v) == 2) and (int(codec_escogido_a) == 1)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg2video -c:a mp3 MPEG2_MP3_{in_file}", shell=True)
        elif((int(codec_escogido_v) == 2) and (int(codec_escogido_a) == 2)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg2video -c:a aac MPEG2_AAC_{in_file}", shell=True)

        elif((int(codec_escogido_v) == 3 )and (int(codec_escogido_a) == 1)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg4 -c:a mp3 MPEG4_MP3_{in_file}", shell=True)
        elif((int(codec_escogido_v) == 3) and (int(codec_escogido_a) == 2)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg4 -c:a aac MPEG2_AAC_{in_file}", shell=True)

        elif((int(codec_escogido_v) == 4) and (int(codec_escogido_a) == 1)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v h264 -c:a mp3 h264_MP3_{in_file}", shell=True)
        elif((int(codec_escogido_v) == 4) and (int(codec_escogido_a) == 2)):
            subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg2video -c:a aac MPEG2_AAC_{in_file}", shell=True)
        print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n")

elif(audio == True):#tenemos un audio

    codec_escogido = input("\n\tOpciones de codec para audio: \n\t\tMP3: 1\n\t\tACC: 2\n\tNúmero de codec escogido: ")

    if(int(codec_escogido) == 1):
        subprocess.run(f"ffmpeg -i {in_file} -c:a mp3 output.mp3", shell=True)
    elif(int(codec_escogido) == 2):
        subprocess.run(f"ffmpeg -i {in_file} -c:a aac output.aac", shell=True)
    print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )

elif(video == True):#tenemos un video sin audio

    codec_escogido = input("\n\tOpciones de codec: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")

    if(int(codec_escogido) == 1):
        subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg1video MPEG1_{in_file}", shell=True)
    elif(int(codec_escogido) == 2):
        subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg2video MPEG2_{in_file}", shell=True)
    elif(int(codec_escogido) == 3):
        subprocess.run(f"ffmpeg -i {in_file} -c:v mpeg4 MPEG4_{in_file}", shell=True)
    elif(int(codec_escogido) == 4):
        subprocess.run(f"ffmpeg -i {in_file} -c:v h264 h264_{in_file}", shell=True)
    print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )
else:
    print("\n\n\t\tFORMATO NO CONOCIDO\n\n")
