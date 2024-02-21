<div align='center'>

![GSpy](/docs/img/GSpy256.jpg)

# GSpy

GSpy es una aplicación que permite el resumen y la traducción de los mejores documentos académicos encontrados en Google Scholar.

</div>

## Dependencias

Las dependecians se pueden encontrar en el fichero [Requirements](requirements.txt).

* scholarly: Implementa ScraperAPI en python, para hacer web scrapping en Google Scholar.
* numpy: Funciones de utilidad matemática, como la media o la ordenación de elementos.
* PyPDF2: Extracción del contenido dentro de PDFs.
* nltk: Procesamiento de lenguaje natural, para la tokenización de palabras y frases.
* translate: Implementa Google Translate API en python, para la traducción de texto a multiples idiomas.

## Estructura

* [Data](data): Contiene los datos generados por la aplicación. Estos son los PDFs relacionados a la temática que el usuario pide y JSON con información sobre el resultado de la query o los contenidos resumidos.
* [Docs](docs): Contiene la documentación del código fuente y los recursos usados para esta.
* [Out](out): Contiene todos los resumenes realizados, tanto los originales como los traducidos en ficheros txt.
* [Src](src): Contiene el codigo fuente.
    * [Build](src/build.py): Contiene todo los pasos previos que la aplicación necesita para el despliegue de esta.
    * [Data](src/data.py): Contiene las funciones necesarias para guardar datos generados por la aplicación.
    * [Main](src/main.py): Punto de entrada de la aplicación.
    * [Natural Language](src/natural_language.py): Procesamiento del lenguaje natural de los articulos.
    * [Recommendation](src/recommendation.py): Sistema de recomendación de artículos.
* [Gitignore](.gitignore): Contiene una lista de ficheros que no son interesantes de guardar.
* [README](README.md): Es el documento que estas leyendo.
* [Requirements](requirements): Contiene los paquetes dependencia del proyecto.

## Funcionamiento

1. Se pide al usuario un tema para buscar, debe ser en Inglés (se implementará para otros idiomas en versiones futuras).

2. Sistema de Recomendación: Se realiza el proceso de búsqueda de publicaciones relacionadas, su selección y se descargará el pdf asociado en la carpeta [data](data).

3. Resumen del contenido: Se realiza un resumen mediante técnicas de reducción del contenido y se muestra la ruta del fichero de texto resultante alojada en la carpeta [out](out).

4. Traducción del contenido: Se pide al usuario un idioma válido, se aplica la traducción sobre el contenido resumido y se muestra la ruta del fichero de texto resultante alojada en la carpeta [out](out). Este proceso se repite hasta que el usuario escriba *quit*.

```console
1.- What topic do you whant to search? _ (Insert topic)

2.- Searching for publications...
Picking the best publication...
Best article found is: {Name}
Link: {Link}
Fetching data...
Parsing data...

3.- Summarizing its contents...
Saved summary at {file location}

4.- Available languages: {languages}
Type "quit" to exit translation process.
Repeats:
    Select a valid language: _ (Insert language | quit)
    Translating document to {language}...
    Saved translation at: {new file location}

Thanks for using GSpy!
```

## Ejemplo

<div align='center'>

[![Ejemplo](/docs/img/GSpy512Play.jpg)](docs/video/example.mkv)

</div>

## Documentación

* [Despliegue.](docs/src/build.md)
* [Data.](docs/src/data.md)
* [Main.](docs/src/main.md)
* [Natural Language.](docs/src/natural_language.md)
* [Recommendation.](docs/src/recommendation.md)
