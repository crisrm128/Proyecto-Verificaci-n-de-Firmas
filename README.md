# Proyecto-Verificacion-de-Firmas

**********   MÉTODO SIN REDES NEURONALES: ********** 
Para probar todas las imágenes de la carpeta pruebas, se tiene que descomentar
el for que va de 0 a 9, además de igualar al variable pruebasIndex = j+1. Se
debe también comentar el plot de las líneas 71 y 72 y descomentar la línea 74
del comando input, para que cada vez que muestre los resultados de una carpeta, 
el programa espere a que se pulse intro para mostrar las siguientes.

**********   MÉTODO CON REDES NEURONALES: ********** 
Descargar archivo "Signature_Verification.zip" de este enlace:
https://drive.google.com/file/d/1_xDfUsaft8TKOSEcDjhn3eBSFTV5jAM4/view?usp=sharing

Para poder utilizar y probar la red neuronal, se debe subir la carpeta "Signature_Verification"
al Drive personal. 
El archivo .ipynb se debe cargar como cuaderno en Google Colaboratory (o utilizar 
el .py en su defecto), y se deben subir los ficheros "data_processing.py" y "BHSig260.zip" 
al entorno de ejecución para mayor rapidez.

**********   DEMO:  ********** 
Descargar archivo "Demo_web" de este enlace:
https://drive.google.com/file/d/18qBrPhF_D2P0InQdQXxSwANx37uEWJrE/view?usp=sharing

Para probar la página web, se debe comprobar en la carpeta correspondiente que
se tienen instalados los requisitos de requirements.txt . En caso contrario, se
puede realizar directamente: pip install -r requirements.txt. A continuación, se
ejecutan los siguientes comandos:
python DownloadData.py
cd frontend
npm install
npm run build
cd ..
python main.py

En la terminal aparecerá una dirección, por lo que se debe copiar y abrir en una
pestaña del navegador.
