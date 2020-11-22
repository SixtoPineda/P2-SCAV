# ***SCAV: P2-Python & Video***

## **EJERCICIOS**
<p align="justify">Mediante la fuente:</p><p align="center">"https://www.askpython.com/python/examples/python-user-input#:~:text=Python%20user%20input%20from%20the,value%20entered%20by%20the%20user"</p><p align="justify">Sabemos como usar la función <em>input()</em> para pedir al usuario que introduzca una cierta información y guardar ésta en una variable:</p><p align="center"> <em>valueInfo = input("Introduzca la info: ")</em></p>

### EJERCICIO-1
#### ***Python: Data from the container***

<p align="justify">Con el fin de mostrar tres de los datos más importantes que contiene el container procedí a ejecutar un comando desde el terminal usando <em>ffmpeg</em>. Este comando lo encontré en la própia página de <em>FFmpeg</em>:</p><p align="center"><em>ffprobe -v error -show_entries <strong>format=bit_rate:format=duration:stream=codec_long_name</strong> -of default=noprint_wrappers=1 {archivo}</em></p><p align="justify">Donde podemos ver que mostramos la información del bitrate del video, su duración, y el tipo de codec, donde se mostrará el codec del video y del audio que contiene éste. </p><p align="justify">Fuente:<br>https://trac.ffmpeg.org/wiki/FFprobeTips</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-1/result_ej_1.png" width="600"/>
</p>

<p align="justify">Como podemos ver en la captura, se nos muestra el tipo de codec del video: h.264, el codec del audio: AAC, la duración: 10.6s, y el bitRate: 6737785 bps. </p>

### EJERCICIO-2
#### ***Python: Rename the 5 quality outputs***

<p align="justify">Para este ejercicio reciclé código del <em>Seminario 2</em>:</p><p align="center"><em>ffmpeg -i {name_video}.mp4 -vf scale={scaleValue[i]} {nameVideo[i]}.mp4 </em></p><p align="justify">Donde <em>name_video</em> hace referencia al nombre del video con el que quiere trabajar el usuario y <em>nameVideo[i]</em> representa la array contenedora de todos los nombres dados por el usuario para cada uno de los videos con distinta resolución.</p><p align="justify">Fuente: <em>Seminario 2</em></p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-2/result_ej_2.png" width="600"/>
</p>

<p align="justify">Como podemos ver en la captura se nos guardan cada uno de los videos reducidos en calidad con su respectivo nombre según haya sido asignado por el usuario. </p>

### EJERCICIO-3
#### ***Python: Resize of any input given***

<p align="justify">Igual que en la práctica 1 y el seminario 2 escalando el input (video o imagen) podemos cambiar la resolución de éstos. Por ello, con el siguiente comando podemos redimensionar cualquier archivo de entrada: </p><p align="center"><em>ffmpeg -i {in_file} -vf <strong>scale={width}:{height}</strong> {width}x{height}-{in_file}</em></p><p align="justify">Observamos que <em>in_file</em> hace referencia al archivo de entrada del usuario y, <em>width y height</em> son la nueva resolución del archivo <em>WIDTHxHEIGHT</em>. </p><p align="justify">Fuente: <em>Práctica 1 y Seminario 2</em></p>

##### **Resultados**

###### **IMAGEN**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-3/result_img_ej_3.png" width="400"/>
</p>

###### **VIDEO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-3/result_video_ej_3.png" width="400"/>
</p>




<p align="justify">Como podemos ver en ambas captura, según los datos dados por el usuario, obtenemos la salida reescalada correspondiente.</p>

### EJERCICIO-4
#### ***Python: Transcode input into an output with another codec***

<p align="justify">Con el fin de dar la posibilidad de cambiar el tipo de codec del archivo del usuario, daremos la posibilidad de que éste introduzca un video con audio, un audio o un video sin audio. A partir de aquí, crearemos condicionales según el tipo de archivo introducido. Con el fin de poder saber que tipo de archivo ha sido introducido, usaremos una función de <em>subprocess</em> llamada <em>check_output</em>, que nos devuelve la salida del comando realizado. Por esta razón ejecutaremos el comando:<br><em>ffprobe -v error -show_entries stream=codec_type -of default=noprint_wrappers=1 {in_file}</em><br> y de esta forma saber de que tipo de codec se trata. Si la salida de este archivo es que tenemos un codec de tipo audio solo, el archivo es un audio, si se trata de video solo, se tratará de un video sin audio, pero si nos devuelve dos tipos de codec, audio y video, significará que se nos pasó un video con canal de audio también.<br>A partir de aquí ya sabemos con que tipo de archivo nos encontramos, por lo tanto, podemos empezar a mostrar las opciones para cada caso:</p>

<p align="justify">&nbsp;- Video (video y audio): en este caso daremos la posibilidad de cambiar el codec del video únicamente, el audio o de ambos.<br>&nbsp;&nbsp;&nbsp;·Codec video: Damos la opción de cambiar entre MPEG-1, MPEG-2, MPEG4 y h.264. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>new_codec</strong> MPEG1_{in_file}</p>

<p align="justify">&nbsp;&nbsp;&nbsp;·Codec audio:  Damos la opción de cambiar entre MP3 y AAC. Realicaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -acodec <strong>new_codec</strong> -vcodec copy MP3_{in_file}</p>

<p align="justify">&nbsp;&nbsp;&nbsp;·Codec video y audio:  Damos la opción de cambiar entre todas las posibilidades anteriores. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>video_codec</strong> -c:a <strong>audio_codec</strong> MPEG1_MP3_{in_file}</p>

<p align="justify">&nbsp;- Audio: en este caso daremos la posibilidad de cambiar el codec del audio únicamente. <br>&nbsp;&nbsp;&nbsp;·Codec audio: Damos la opción de cambiar entre MP3 y AAC. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:a <strong>new_codec</strong> output.mp3</p>

<p align="justify">&nbsp;- Video sin audio: en este caso daremos la posibilidad de cambiar el codec del video únicamente. <br>&nbsp;&nbsp;&nbsp;·Codec video: Damos la opción de cambiar entre MPEG-1, MPEG-2, MPEG4 y h.264. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>new_codec</strong> MPEG1_{in_file}</p>


##### **Resultados**

###### **VIDEO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_video_ej_4.png" width="400"/>
</p>

###### **AUDIO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_audio_ej_4.png" width="400"/>
</p>

###### **VIDEO SIN AUDIO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_videosinAudio_ej_4.png" width="400"/>
</p>

<p align="justify">Como podemos ver en las capturas, el archivo final corresponde con la solicitud de cambio de codec por parte del usuario. </p>


### EJERCICIO-5
#### ***Python: Integrate previous exercises into one script***

<p align="justify">Con el fin de poder realizar todos los ejercicios anteriores, procedí a buscar la forma de ejecutar desde el fichero python un comando como si fuera el terminal y poder usar <em>ffmpeg</em>. Para ello me ayudé de la conversación de la página <em>StackOverflow</em>:</p><p align="center"><em><strong>subprocess.run</strong>(f"<strong>Comando FFmpeg</strong>", shell=True)</em></p><p align="justify">Donde si nosotros colocamos dentro de ese espacio marcado el comando que anteriormente poníamos desde el terminal, se realizará el mismo proceso y obtendremos los resultados para cada uno de los ejercicios. Cabe decir que lo que nos permite ejecutar estos comandos es la función <em>run</em> de la libreria <em>subprocess</em>. </p><p align="justify">Fuente:<br>https://stackoverflow.com/questions/59279463/how-to-cut-video-properly-with-this-ffmpeg-python-script</p>

<p align="justify"></p>

<p align="justify">Importamos la librería <em>subprocess</em> y creamos una variable con el nombre del video original a partir del cual realizar todos los ejercicios. Cabe decir que el primer ejercicio se realizará a partir del original propuesto, pero el segundo, tercero y cuarto se realizarán a partir del video de 10 segundos resultante del ejericio 1. </p>

```python
imports
```
<p align="justify">Para el primer ejercicio </p>

```python
####################### EJERCICIO-1 ################################

```
<p align="justify">En el segundo ejercicio, </p>

```python

####################### EJERCICIO-2 ################################

```
<p align="justify">Para el ejercicio 3, </p>

```python

####################### EJERCICIO-3 ################################



```
<p align="justify">Para el ejercicio 4,</p>

```python

####################### EJERCICIO-4 ################################


```


##### **Script**
```python
CÓDIGO ENTERO
```

<p align="justify">Si ejecutamos este código en un fichero python veremos que al momento empiezan a aparecer los resultados de cada uno de los procesos en la carpeta donde se ha ejecutado el script.</p>
