# Depliegue

Se recomienda tener instalada una versión de python entre 3.8.10 y 3.12.0.

1. Dirijase al directorio donde quiere instalar la aplicación.
2. Descomprime el proyecto o clona con git el repositorio.

```shell
git clone https://github.com/SammyHM/RRT.git
```
3. Monta la aplicación en el directorio.

## Automático

Ejecuta el script [build.py](src/build.py) que creará el entorno de la applicación e instalará sus dependencias. 

```shell
python src/build.py
```

## Manual

Puedes realizar los siguientes pasos manualmente ajustando a tus necesidades para tener un mayor control sobre la installación.

#### Shell

```shell
python venv .venv
pip install requirements.txt
python nltk.downloader stopwords
python nltk.downloader punkt
```

#### Visual Studio

> 1. Instala la extensión *Python*.
> 2. Pulsa *Ctrl+Shift+p* y selecciona *Python: Create Environment...*
> 3. Selecciona el tipo de entorno
> 4. Añade el fichero requirements.txt como dependencia.

<div align='center'>

![Entorno](/docs/img/Environment.png)
![Requerimientos](/docs/img/Requirements.png)

</div>

```shell
.venv/Scripts/python.exe nltk.downloader stopwords
.venv/Scripts/python.exe nltk.downloader punkt
```

4. Espera a que termine la instalación
5. Ejecuta el script [main.py](src/main.py).