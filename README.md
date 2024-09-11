# 🤖 OscarBot: Chatbot IA para el Área de Tecnología del Banco de Occidente

## 📝 Descripción
Este proyecto implementa OscarBot, un chatbot de Inteligencia Artificial personalizado para el área de tecnología del Banco de Occidente. OscarBot está diseñado para proporcionar asistencia en procesos internos, responder preguntas sobre el banco y facilitar el acceso a la información para el equipo de tecnología.

## ✨ Características
- 🧠 OscarBot está basado en la biblioteca ChatterBot con personalización adicional
- 🏦 Integración de conocimientos específicos del Banco de Occidente
- 🔤 Procesamiento de lenguaje natural utilizando spaCy
- 💾 Persistencia del modelo entrenado entre sesiones
- 💻 Interfaz de línea de comandos para interacción fácil con OscarBot

## 🛠️ Requisitos
- Python 3.7+
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clone este repositorio:
   ```
   git clone https://github.com/BancoOccidente/oscarbot.git
   cd oscarbot
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Descargue el modelo de lenguaje de spaCy:
   ```
   python -m spacy download en_core_web_sm
   ```

## 🖥️ Uso

1. Para iniciar OscarBot, ejecute:
   ```
   python main.py
   ```

2. Interactúe con OscarBot a través de la interfaz de línea de comandos.

3. Para salir, presione Ctrl+C o escriba "salir".

## 📚 Entrenamiento

OscarBot viene pre-entrenado con información general y específica del Banco de Occidente. Para actualizar o añadir nueva información al modelo:

1. Añada nuevos datos de entrenamiento al archivo `training_data.csv`.
2. Ejecute el script de entrenamiento:
   ```
   python train.py
   ```

## 📁 Estructura del Proyecto
```
oscarbot/
├── main.py            # Script principal para ejecutar OscarBot
├── train.py           # Script para entrenar el modelo de OscarBot
├── utils.py           # Funciones de utilidad
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Este archivo
```

## 🤝 Contribución
Para contribuir al desarrollo de OscarBot:
1. Haga un fork del repositorio
2. Cree una nueva rama (`git checkout -b feature/NuevaCaracteristica`)
3. Haga commit de sus cambios (`git commit -m 'Añadir nueva característica a OscarBot'`)
4. Haga push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abra un Pull Request
   

## 📜 Licencia
OscarBot es propiedad del Banco de Occidente y su uso está restringido a empleados y contratistas autorizados.
