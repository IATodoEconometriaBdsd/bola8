# Spooky Bola-8

Una aplicación web interactiva de la clásica Bola 8 Mágica con un tema terrorífico. Pregunta al "fantasma del tornillo" y recibe respuestas místicas.

## Descripción

Esta es una aplicación web desarrollada con Flask que simula una Bola 8 Mágica con un tema de terror. Los usuarios pueden hacer preguntas y recibir respuestas aleatorias del "fantasma del tornillo". La interfaz cuenta con un diseño espeluznante con imágenes de arañas y un fondo temático.

## Características

- Interfaz web interactiva con temática de terror
- Respuestas aleatorias a tus preguntas
- Diseño responsive con CSS personalizado
- Imágenes decorativas de arañas
- Comunicación asíncrona con el servidor usando JavaScript

## Tecnologías utilizadas

- **Python 3.x**
- **Flask**: Framework web para Python
- **HTML/CSS**: Para la interfaz de usuario
- **JavaScript**: Para la interacción asíncrona

## Estructura del proyecto

```
bola-8/
│
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── .gitignore            # Archivos ignorados por Git
│
├── templates/
│   └── index.html        # Página principal
│
└── static/
    ├── ccs/
    │   └── style.css     # Estilos CSS (actualmente no utilizado)
    └── images/
        ├── fondo.jpg     # Imagen de fondo
        ├── spider1.png   # Imagen decorativa
        ├── spider2.png   # Imagen decorativa
        └── spider3.png   # Imagen decorativa
```

## Instalación y configuración

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos para clonar y ejecutar el proyecto

1. **Clonar el repositorio**

```bash
git clone https://github.com/TU_USUARIO/spooky-bola8.git
cd spooky-bola8
```

2. **Crear un entorno virtual**

En Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar las dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**

```bash
python app.py
```

5. **Abrir en el navegador**

Abre tu navegador y visita: `http://127.0.0.1:5000`

## Uso

1. Abre la aplicación en tu navegador
2. Haz clic en el botón "Pregunta al fantasma del tornillo!"
3. Recibe una respuesta mística del más allá
4. Repite las veces que quieras

## Respuestas posibles

El fantasma puede responder con:
- "Sí"
- "No"
- "Tal vez"
- "Definitivamente"
- "Pregunta de nuevo más tarde"

## Contribuir

Si deseas contribuir a este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añade nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Desarrollado como proyecto educativo de programación orientada a objetos en Python.

## Notas

- El modo debug está activado en `app.py` para facilitar el desarrollo. **Desactívalo en producción**.
- Las imágenes en la carpeta `static/images/` son parte del diseño temático.
- Puedes personalizar las respuestas modificando la lista en la función `adivinar()` en `app.py`.
