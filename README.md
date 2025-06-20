Pagina Web Messi
Esta es una aplicación web básica desarrollada con Flask en Python, diseñada para permitir a los usuarios dejar comentarios y ver los comentarios guardados.

Características
Guardar Comentarios: Permite a los usuarios enviar comentarios a través de una API REST (/guardar_comentario) que se guardan en un archivo de texto (comentarios.txt).

Ver Comentarios: Permite recuperar y mostrar todos los comentarios guardados a través de una API REST (/ver_comentarios).

Estructura del proyecto

Para que la aplicación funcione correctamente, tu directorio de proyecto (por ejemplo, PaginaWebMessi) debe contener todos los archivos principales. Si esta carpeta está anidada dentro de otra, la estructura sería similar a esta:

directorio_padre/
└── PaginaWebMessi/      # Esta es tu carpeta de proyecto principal
    ├── app.py              # El script principal de la aplicación Flask
    ├── Messi.html          # La página web principal sobre Messi
    ├── comentarios.txt     # Archivo donde se guardan los comentarios (se crea automáticamente)
    ├── tu_imagen.jpg       # Ejemplo de una imagen (si usas alguna en Messi.html)
    └── tu_estilo.css       # Ejemplo de un archivo CSS (si usas alguno en Messi.html)

ESTA ES LA FORMA QUE LO TENGO YO, PARA QUE ME FUNCIONE LOS COMENTARIOS;
O PUEDE CALAR SIN USAR SUBCARPETA Y TODO EN UNA MISMA CARPETA.

Requisitos
Asegúrate de tener Python instalado en tu sistema.

Instalación
Clona este repositorio (si lo tienes en GitHub) o descarga los archivos directamente.

PASOS:

Navega al directorio del proyecto en tu terminal:

cd /ruta/a/tu_proyecto

Instala Flask si aún no lo tienes:

pip install Flask

Ejecución de la Aplicación
Desde el directorio raíz de tu proyecto en la terminal, ejecuta el siguiente comando:

python app.py

Esto iniciará el servidor de desarrollo de Flask. Verás un mensaje similar a este:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debug mode: on

Uso
Accede a la página web: Abre tu navegador web y ve a http://127.0.0.1:5000/.

Dejar un comentario: En la página Messi.html

Ver comentarios: Puedes acceder a los comentarios guardados en el archivo comentarios.txt

NOTA: ESTO ES PARA QUE PUEDAS PROBAR LA PAGINA WEB CON TODAS LAS IMAGENES CARGADAS, Y PUEDAS ENVIAR LOS COMENTARIOS

2DA OPCION: PUEDES HACER LOS MISMOS PASOS, PERO SOLO CARGA LA PRIMERA PAGINA, PERO TAMPOCO CARGA LAS IMAGENES, PERO SI FUNCIONA LA FUNCION DE LOS COMENTARIOS

ASI QUE PREFIERO MEJOR LO HAGA COMO LA PRIMERA OPCION 

RECOMENDACIONES: 

LA CARPETA PRINCIPAL ESTAN LOS ARCHIVOS PARA QUE SE MUESTRE LA PAGINA DE MANERA FUNCIONAL SIN COMENTARIOS, PARA QUE SE VEA EL DISEÑO Y LA INFORMACION DE MI PAGINA, DE MANERA CORRECTA 

MEJOR OPCION: 
LA SUBCARPETA DONDE ESTA EN (MessiComentarios) LO TENGO AHI POR QUE ES PARA EL EJEMPLO PARA LOS COMENTARIOS, YA QUE AHI SI FUNCIONA Y SE GUARDAN LOS COMENTARIOS, AHI FUNCIONA LOS CCOMENTARIOS Y SE VE MAS COMPLETO LA PAGINA, CON EL DISEÑO, INFORMACION Y FUNCIONAL EN LOS COMENTARIOS.
