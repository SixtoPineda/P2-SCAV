# ***SCAV: P2-Python & Video***

## **EJERCICIOS**

### EJERCICIO-1
#### ***Python: Data from the container***

<p align="justify">Con el fin de recortar el video 10 segundos procedí a ejecutar un comando desde el terminal usando <em>ffmpeg</em>. Este comando lo encontré en la página de <em>VIDAGNU</em>:</p><p align="center"><em>ffmpeg -ss 00:<strong>07:05.0</strong> -i BBB.mp4 -c copy -t 00:00:<strong>10.0</strong> BBB_10s.mp4</em></p><p align="justify">Donde asignamos que en el minuto 7 y segundo 5 empezamos a reproducir el video durante 10 segundos. El resultado de dicho video de diez segundos lo guardamos en el video-output (BBB_10s.mp4). De esta forma obtenemos un corte de 10 segundos del video original justo a partir del minuto 00:07:05.</p><p align="justify">Fuente:<br>https://www.vidagnu.com/como-recortar-o-tomar-una-porcion-de-un-video-con-ffmpeg-en-linux/</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-1/BBB_10s.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video (Mi Youtube): https://youtu.be/WndicksBocw</p>

<p align="justify">En el video final podemos ver que dura 10 segundos y que hace referencia al minuto 00:07:05 del video original. </p>

### EJERCICIO-2
#### ***Python: Rename the 5 quality outputs***

<p align="justify">Nuevamente mediante un comando usando <em>ffmpeg</em> procedemos a realizar el histograma YUV y plotearlo sobre la misma imagen o video. Para ello utilicé el comando dado por la misma página de <em>FFmpeg</em>:</p><p align="center"><em>ffmpeg -i BBB_10s.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" histo_BBB.mp4</em></p><p align="justify">Fuente:<br>https://trac.ffmpeg.org/wiki/Histogram</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-2/histo_BBB.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video (Mi Youtube): https://youtu.be/-1ttAqNjws4</p>

<p align="justify">En el resultado vemos el histograma de las tres componentes de YUV (Y, Cb y Cr). Donde Y nos informa sobre la luminancia, es decir información en blanco y negro, por esa razón la barra de color debajo del histograma que representa la Y está en escala de grises. Vemos también el histograma de las componentes Cb y Cr, que hacen referencia a la crominancia, es decir, la información sobre el color. </p>

### EJERCICIO-3
#### ***Python: Resize of any input given***

<p align="justify">Igual que en la práctica 1, cuando realizamos la reducción de calidad de las imágenes con una reducción de escala, para el caso del video, usaremos el mismo comando, pero en vez de pasar una imagen al comando, le pasamos un video. </p><p align="center"><em>ffmpeg -i BBB_10s.mp4 -vf scale=<strong>1280:720</strong> 1280x720.mp4</em></p><p align="justify">Fuente:<br>https://trac.ffmpeg.org/wiki/Scaling</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-3/1280x720.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video 1280X720 (Mi Youtube): https://youtu.be/-zjsgdHLAMk</p>
<p align="center"> Link resultado del video 640X480 (Mi Youtube): https://youtu.be/qdyaH8BuRuA</p>
<p align="center"> Link resultado del video 360X240 (Mi Youtube): https://youtu.be/oTOrATpGNek</p>
<p align="center"> Link resultado del video 160X120 (Mi Youtube): https://youtu.be/qquzqcsQgkA</p>

<p align="justify">Como podemos ver en los distintos videos, a medida que reducimos la resolución de éstos, la calidad también lo hace.</p>

### EJERCICIO-4
#### ***Python: Transcode input into an output with another codec***

<p align="justify">Para realizar este ejercicio, nuevamente ejecutaremos dos comandos usando <em>ffmpeg</em> para cambiar el tipo de canal de audio a mono y posteriormente cambiar el tipo de codificación del audio original. Para ello, tal y como vemos a continuación en las capturas de pantalla, el audio del video original es de tipo multicanal, en este caso 5.1 Surround lo cual significa que usa 6 canales de audio. De igual forma también podemos ver que se usa <em>acc</em> como codec del audio. Para pasar el audio del video a mono, realicé el siguiente comando encontrado en la propia página de <em>FFmpeg</em>:</p><p align="center"><em>ffmpeg -i BBB_10s.mp4 -ac <strong>1</strong> monoBBB10s.mp4</em></p><p align="justify">Del mismo modo, una vez hecho esto procedí a realizar el cambio de codec del audio, para ello usé el comando encontrado en una conversación en la página <em>StackExchange</em>:</p><p align="center"><em>ffmpeg -i monoBBB10s.mp4 -acodec <strong>mp3</strong> -vcodec copy mono_mp3_BBB10s.mp4</em></p>


<p align="justify">Fuentes:<br>Pasar a mono: https://trac.ffmpeg.org/wiki/AudioChannelManipulation<br>Cambiar audio codec: https://superuser.com/questions/215430/would-like-to-change-audio-codec-but-keep-video-settings-with-ffmpeg</p>


##### **Antes y después de cambiar tipo de canal y codificación del audio**
###### **Antes**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/propiedades_original.png" width="500" high="700"/>
</p>

###### **Después**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/propiedades_mono_mp3_final.png" width="500" high="700"/>
</p>

##### **Comandos**

###### **Pasamos a mono**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/pasarAMono.png" width="800"/>
</p>

###### **Cambiamos audio codec a mp3**   
   
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/pasarA-MP3.png" width="800"/>
</p>


##### **Resultados**

<p align="center"> Video con audio original (Mi Youtube): https://youtu.be/WndicksBocw</p>
<p align="center"> Link resultado del video con canal audio mono (Mi Youtube): https://youtu.be/WYFJUyrX-4A</p>
<p align="center"> Link resultado del video con canal audio mono y diferente audio codec (MP3) (Mi Youtube): https://youtu.be/wAuYziIrgJw</p>

<p align="justify">Como podemos escuchar, si comparamos el video original con el que tiene un único canal, se aprecia claramente con auriculares como se pierde esa sensación espacial que nos da el audio multicanal 5.1 Surround que tenía el video original, como hemos podido ver en la captura de las propiedades el video.<br>En cambiar también el tipo de codificación del audio, las diferencias apenas son notorias.</p>


### EJERCICIO-5
#### ***Python: Integrate previous exercises into one script***

<p align="justify">Con el fin de poder realizar todos los ejercicios anteriores, procedí a buscar la forma de ejecutar desde el fichero python un comando como si fuera el terminal y poder usar <em>ffmpeg</em>. Para ello me ayudé de la conversación de la página <em>StackOverflow</em>:</p><p align="center"><em><strong>subprocess.run</strong>(f"<strong>Comando FFmpeg</strong>", shell=True)</em></p><p align="justify">Donde si nosotros colocamos dentro de ese espacio marcado el comando que anteriormente poníamos desde el terminal, se realizará el mismo proceso y obtendremos los resultados para cada uno de los ejercicios. Cabe decir que lo que nos permite ejecutar estos comandos es la función <em>run</em> de la libreria <em>subprocess</em>. </p><p align="justify">Fuente:<br>https://stackoverflow.com/questions/59279463/how-to-cut-video-properly-with-this-ffmpeg-python-script</p>

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
