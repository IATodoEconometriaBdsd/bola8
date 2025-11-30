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
- PyCharm Community o Professional (recomendado) o cualquier editor de código
- Git instalado en tu sistema

## Opción 1: Clonar y configurar en PyCharm (Recomendado para estudiantes)

### Paso 1: Clonar el repositorio desde PyCharm

1. **Abrir PyCharm**
2. En la pantalla de bienvenida, selecciona **"Get from VCS"** (Version Control System)
   - Si ya tienes un proyecto abierto: Ve a `File` → `New` → `Project from Version Control`
3. En la ventana que aparece:
   - **URL**: Pega `https://github.com/IATodoEconometriaBdsd/bola8.git`
   - **Directory**: Elige dónde quieres guardar el proyecto en tu computadora
   - Haz clic en **"Clone"**
4. PyCharm descargará el proyecto automáticamente

### Paso 2: Configurar el entorno virtual en PyCharm

1. Una vez clonado el proyecto, PyCharm puede detectar automáticamente que necesitas crear un entorno virtual
   - Si aparece una notificación en la esquina inferior derecha, haz clic en **"Configure Python Interpreter"**
2. Si no aparece la notificación:
   - Ve a `File` → `Settings` (en Windows/Linux) o `PyCharm` → `Preferences` (en Mac)
   - Navega a `Project: bola8` → `Python Interpreter`
   - Haz clic en el ícono de engranaje ⚙️ → **"Add Interpreter"** → **"Add Local Interpreter"**
3. En la ventana de configuración:
   - Selecciona **"Virtualenv Environment"**
   - Marca **"New"**
   - **Base interpreter**: Selecciona tu instalación de Python 3.x
   - **Location**: Déjalo como está (usualmente será `.venv` dentro del proyecto)
   - Marca la opción **"Inherit global site-packages"** si quieres (opcional)
   - Haz clic en **"OK"**

### Paso 3: Instalar las dependencias

PyCharm debería detectar automáticamente el archivo `requirements.txt`:
1. Busca una notificación en la parte superior del editor que dice **"Package requirements file"**
2. Haz clic en **"Install requirements"**
3. En la ventana que aparece, haz clic en **"Install"**

**Alternativa manual:**
1. Abre la terminal integrada de PyCharm: `View` → `Tool Windows` → `Terminal`
2. Ejecuta:
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la aplicación

**Método 1: Usando el botón Run de PyCharm**
1. Abre el archivo `app.py`
2. Haz clic derecho en cualquier parte del código
3. Selecciona **"Run 'app'"** (o presiona `Shift + F10`)
4. PyCharm ejecutará la aplicación y verás la salida en la consola

**Método 2: Desde la terminal de PyCharm**
1. Abre la terminal: `View` → `Tool Windows` → `Terminal`
2. Ejecuta:
```bash
python app.py
```

### Paso 5: Abrir en el navegador

1. Una vez que la aplicación esté corriendo, verás en la consola:
   ```
   * Running on http://127.0.0.1:5000
   ```
2. **Haz Ctrl + Click** sobre la URL en PyCharm (se abrirá automáticamente en tu navegador)
   - O copia y pega `http://127.0.0.1:5000` en tu navegador

---

## Opción 2: Clonar desde línea de comandos

Si prefieres usar la terminal o Git Bash:

### 1. Clonar el repositorio

```bash
git clone https://github.com/IATodoEconometriaBdsd/bola8.git
cd bola8
```

### 2. Crear un entorno virtual

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

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

### 5. Abrir en el navegador

Abre tu navegador y visita: `http://127.0.0.1:5000`

---

## Solución de problemas comunes

### Error: "python no se reconoce como comando"
- Asegúrate de tener Python instalado
- Verifica que Python esté en las variables de entorno PATH
- Intenta usar `py` en lugar de `python`

### Error: "No module named 'flask'"
- Asegúrate de tener el entorno virtual activado
- Ejecuta: `pip install -r requirements.txt`

### El navegador muestra "This site can't be reached"
- Verifica que la aplicación esté corriendo en la terminal
- Asegúrate de usar la URL correcta: `http://127.0.0.1:5000` o `http://localhost:5000`

### PyCharm no detecta el intérprete de Python
- Ve a `File` → `Settings` → `Project` → `Python Interpreter`
- Selecciona manualmente el intérprete de Python del entorno virtual (`.venv/Scripts/python.exe` en Windows o `.venv/bin/python` en Linux/Mac)

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
