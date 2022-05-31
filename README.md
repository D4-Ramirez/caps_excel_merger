# 📄 Combinador de archivos Excel

Este es un programa realizado para el Centro de Asesoria Psicológica y Salud (CAPS) de la Pontificia Universidad Javeriana, el cual tiene como objetivo combinar archivos de Excel con una estructura en específico.

## ⚙ Requerimientos

* Tener Google Chrome instalado

## 🛠 Herramientas utilizadas

* [Python](https://www.python.org/) - Lenguaje de programación
* [Pandas](https://pandas.pydata.org/) - Libreria para manejo de archivos de Excel
* [Eel](https://github.com/ChrisKnott/Eel) - Libreria que permite crear un frontend a partir de HTML, CSS y JS

## 💻 Instalación

En caso que hayas tomado la desición de realizar tu práctica social dentro del CAPS, este apartado es para ti.
Para comenzar es importante que dentro de tu máquina este instalado ___Python 3.9.7 o superior___, en caso que no lo tengas instalado, puedes instalarlo con el siguiente [enlace](https://www.python.org/downloads/).

Ya teniendo instalado Python ya puedes instalar las librerías requeridas para ejecutar el programa. En primer lugar tienes que instalar el paquete ___Pandas___, el cual permite leer y modificar los archivos de Excel que se solicitan. Para instalar el paquete utiliza el comando:

```
pip install pandas
```

También debes instalar el paquete ___Eel___, el cual permite ejecutar el frontend de la aplicación, para instalarlo debes utiliar el siguiente comando:

```
pip install eel
```

En caso que ya el programa este finalizado y desees generar un archivo .EXE, debes instalar la libreria __PyInstaller__, para instalarla utiliza el comando:
```
pip install eel
```
Y para empaquetar el programa dentro de un archivo .EXE, utiliza el comando:
```
python -m eel main.py web --onefile --noconsole
```

## ✅ Cosas por hacer

- [ ] Manejar excepciones
- [ ] Crear mensajes de error en el frontend
- [ ] Permitir guardar archivos en ubicaciones especificadas por el usuario
- [ ] Permitir cambiar los archivos seleccionados por el usuario
- [ ] Mostrar estado de la combinación de varios archivos
- [ ] Mostrar el nombre o dirección del archivo que el usuario a seleccionado
- [ ] Migrar frontend de Eel a Tkinter
