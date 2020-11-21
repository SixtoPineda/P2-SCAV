import subprocess

print("\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Introducir archivo (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0

    archivo = input("\n\nIntroduzca el nombre COMPLETO del archivo con el que trabajar (video, audio, imagen): ")

    #comprobamos si se trata de un video, o un audio
    arch_type = subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_type -of default=noprint_wrappers=1 {archivo}", shell=True)
    #mismo código que en ej_4 para comprobar ante que tipo de archivo nos encontramos
    string_audio_type = str(b'codec_type=audio\n')
    string_video_type = str(b'codec_type=video\n')
    string_videoAudio_type = str(b'codec_type=video\ncodec_type=audio\n')
    string_img_type = str(b'bit_rate=N/A\n')#Extra: para saber si nos encontramos antes una imagen dado que el "codec_type" es "video" tanto para video como imagen


    if (True == (str(arch_type) == string_videoAudio_type)): #true si se trata de un video con audio

        #Mostramos la informacion sobre el archivo necesaria según las opciones de modificación que se muestrarán a continuación
        resolucion = subprocess.check_output(f"ffprobe -v error -select_streams v:0 -show_entries stream=height,width -of csv=s=x:p=0 {archivo}", shell=True)#resolución del video
        codec_video = subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {archivo}", shell=True)#codec del video y del audio
        print("\nInfo del archivo: \n\t- Video con resolución: ", resolucion, "\n\t- Codec video y audio: ", codec_video)

        #mostramos las opciones de los parámetros que se pueden modificar
        print("\nOpciones a modificar: \n\t- Resolución: 1\n\t- Codec: 2")
        relOrCodec = input("\nIndique el número de opción escogido: ")

        #PRIMERA OPCIÓN - RESOLUCIÓN
        if(int(relOrCodec) == 1): #cambiamos la resolucion del video con audio
            print("\nA continuación introduzca la nueva resolución:\n")
            width= input("\tWidth: ")
            height = input("\theight: ")
            name_arch = input("\nNombre del archivo final (sin extensión):  ")
            subprocess.run(f"ffmpeg -i {archivo} -vf scale={width}:{height} {name_arch}.mp4 ", shell=True)

        #SEGUNDA OPCIÓN - CODEC
        elif(int(relOrCodec) == 2): #cambiamos el codec del video con audio
            typeTranscode = input("\nTu archivo contiene video y audio, de cual de ellos quiere modificar su codec?\n\tVideo: 1\n\tAudio: 2\n\tAmbos: 3\n\nDiga el número según la opción escogida: ")

            if(int(typeTranscode) == 1):#cambiamos solo codec del audio
                codec_escogido = input("\n\tOpciones de codec: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")

                if(int(codec_escogido) == 1):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg1video {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 2):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 3):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg4 {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 4):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v h264 {name_arch}.mp4", shell=True)
                print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )

            elif(int(typeTranscode) == 2):#cambiamos codec solo del audio del video
                codec_escogido = input("\n\tOpciones de codec para audio: \n\tMP3: 1\n\tAAC: 2\n\t\tNúmero de codec escogido: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")

                if(int(codec_escogido) == 1):
                    subprocess.run(f"ffmpeg -i {archivo} -acodec mp3 -vcodec copy {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 2):
                    subprocess.run(f"ffmpeg -i {archivo} -acodec aac -vcodec copy {name_arch}.mp4", shell=True)
                print("\n\n\n\tARCHIVO TRANSCODIFICADO CORRECTAMENTE\n\n\n" )

            elif(int(typeTranscode) == 3):#cambiamos codec tanto de audio como de video
                codec_escogido_v = input("\n\tOpciones de codec Video: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
                codec_escogido_a = input("\n\tOpciones de codec para audio: \n\tMP3: 1\n\tAAC: 2\n\t\tNúmero de codec escogido: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")

                if((int(codec_escogido_v) == 1) and (int(codec_escogido_a) == 1)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg1video -c:a mp3 {name_arch}.mp4", shell=True)
                elif((int(codec_escogido_v) == 1) and (int(codec_escogido_a) == 2)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg1video -c:a aac {name_arch}.mp4", shell=True)

                elif((int(codec_escogido_v) == 2) and (int(codec_escogido_a) == 1)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video -c:a mp3 {name_arch}.mp4", shell=True)
                elif((int(codec_escogido_v) == 2) and (int(codec_escogido_a) == 2)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video -c:a aac {name_arch}.mp4", shell=True)

                elif((int(codec_escogido_v) == 3 )and (int(codec_escogido_a) == 1)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg4 -c:a mp3 {name_arch}.mp4", shell=True)
                elif((int(codec_escogido_v) == 3) and (int(codec_escogido_a) == 2)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg4 -c:a aac {name_arch}.mp4", shell=True)

                elif((int(codec_escogido_v) == 4) and (int(codec_escogido_a) == 1)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v h264 -c:a mp3 {name_arch}.mp4", shell=True)
                elif((int(codec_escogido_v) == 4) and (int(codec_escogido_a) == 2)):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video -c:a aac {name_arch}.mp4", shell=True)


    elif(True == (str(arch_type) == string_video_type)):#true si se trata de un video sin audio o una posible imagen

        #comprobamos si se trata de un video sin audio o de una imagen
        videoOrImg = subprocess.check_output(f"ffprobe -v error -show_entries stream=bit_rate -of default=noprint_wrappers=1 {archivo}", shell=True)

        if(True == (str(videoOrImg) == string_img_type)):#true si se trata de una imagen

            #mostramos la información sobre la resolución de la imagen
            resolucion = subprocess.check_output(f"ffprobe -v error -select_streams v:0 -show_entries stream=height,width -of csv=s=x:p=0 {archivo}", shell=True)
            print("\nInfo del archivo: \n\t- Imagen con resolución: ", resolucion)

            #damos la posibilidad de cambiar la resolución de la imagen
            cambiar_res = input("\nQuiere cambiar la resolución?\n\t(Sí[1], No[0]):  ")
            if(int(cambiar_res) == 1):
                print("\nA continuación introduzca la nueva resolución:\n")
                width= input("\tWidth: ")
                height = input("\theight: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")
                subprocess.run(f"ffmpeg -i {archivo} -vf scale={width}:{height} {name_arch}.jpg ", shell=True)


        elif(False == (str(videoOrImg) == string_img_type)):#se trata de un video sin audio

            #mostramos la informacion sobre la resolución y tipo de codec del video
            resolucion = subprocess.check_output(f"ffprobe -v error -select_streams v:0 -show_entries stream=height,width -of csv=s=x:p=0 {archivo}", shell=True)
            codec_video = subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {archivo}", shell=True)
            print("\nInfo del archivo: \n\t- Imagen con resolución: ", resolucion, "\n\t- Codec video: ", codec_video)

            #damos la opción de cambiar el codec, la resolución o ambos del video
            orden = input("\nTu archivo contiene un video sin audio, quire modificar su codec, su resolución o ambos?\n\tCodec: 1\n\tResolución: 2\n\tAmbos: 3\n\nDiga el número según la opción escogida: ")

            if(int(orden) == 1):#cambiar codec del video sin audio
                codec_escogido = input("\n\tOpciones de codec: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")

                if(int(codec_escogido) == 1):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg1video {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 2):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 3):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg4 {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 4):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v h264 {name_arch}.mp4", shell=True)

            elif(int(orden) == 2):#cambiar resolucion del video sin audio
                print("\nA continuación introduzca la nueva resolución:\n")
                width= input("\tWidth: ")
                height = input("\theight: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")
                subprocess.run(f"ffmpeg -i {archivo} -vf scale={width}:{height} {name_arch}.mp4 ", shell=True)

            elif(int(orden) == 3):#cambiar codec y resolucon del video sin audio
                codec_escogido = input("\n\tOpciones de codec: \n\tMPEG-1: 1\n\tMPEG-2: 2\n\tMPEG4: 3\n\th.264: 4\n\t\tNúmero de codec escogido: ")
                print("\nA continuación introduzca la nueva resolución:\n")
                width= input("\tWidth: ")
                height = input("\theight: ")
                name_arch = input("\nNombre del archivo final (sin extensión):  ")

                if(int(codec_escogido) == 1):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg1video -vf scale={width}:{height} {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 2):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg2video -vf scale={width}:{height} {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 3):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v mpeg4 -vf scale={width}:{height} {name_arch}.mp4", shell=True)
                elif(int(codec_escogido) == 4):
                    subprocess.run(f"ffmpeg -i {archivo} -c:v h264 -vf scale={width}:{height} {name_arch}.mp4", shell=True)


    elif(True == (str(arch_type) == string_audio_type)):#true si se trata de un audio

        #mostramos la información sobre el tipo de codec que tiene el audio
        codec_audio = subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {archivo}", shell=True)
        print("\nInfo del archivo: \n\t- Audio con codec: ", codec_audio)

        #damos la posibilida de cambiar el codec del audio
        cambiar_res = input("\nQuiere cambiar el codec?\n\t(Sí[1], No[0]):  ")
        
        if(int(cambiar_res) == 1):
            codec_escogido = input("\n\tOpciones de codec para audio: \n\tMP3: 1\n\tACC: 2\n\tNúmero de codec escogido: ")
            name_arch = input("\nNombre del archivo final (sin extensión):  ")

            if(int(codec_escogido) == 1):
                subprocess.run(f"ffmpeg -i {archivo} -c:a mp3 {name_arch}.mp3", shell=True)
            elif(int(codec_escogido) == 2):
                subprocess.run(f"ffmpeg -i {archivo} -c:a aac {name_arch}.aac", shell=True)


    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\n\n\t- Introducir archivo (1)")
    print("\n\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
