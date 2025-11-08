# TaskManager 📝

Un gestor de tareas inteligente desarrollado en Python que permite crear, gestionar y completar tareas de forma eficiente. Incluye integración con IA para descomponer tareas complejas en subtareas más simples y accionables.

## 📁 Estructura del proyecto
```
TaskManager/
├── main.py               # Punto de entrada con interfaz de menú y gestión de opciones
├── task_manager.py       # Lógica principal y operaciones de archivos
├── ai_service.py         # Integración con OpenAI
├── test_task_manager.py  # Suite de pruebas unitarias
├── .env                  # Variables de entorno (no en git)
├── requirements.txt      # Dependencias del proyecto
├── tasks.json           # Archivo de datos personal (no en git)
├── example_tasks.json   # Plantilla de ejemplo
├── .gitignore          # Configuración de git
└── README.md            # Documentación del proyecto
```

### Archivos ignorados
Los siguientes archivos están excluidos del control de versiones:
- `tasks.json`: Archivo de datos local
- `.venv/`: Entorno virtual de Python
- `__pycache__/`: Archivos compilados de Python
- `.env`: Variables de entorno

## 💾 Almacenamiento de datos

Las tareas se almacenan localmente en `tasks.json`. Este archivo:
- Se crea automáticamente en la primera ejecución
- Contiene tu lista personal de tareas
- No se incluye en el control de versiones
- Utiliza esta estructura:

```json
[
    {
        "id": 1,
        "description": "Create tasks.json",
        "completed": true
    }
]
```

## 🚀 Características principales

- **Gestión de tareas**: Crear, listar, completar y eliminar tareas
- **Persistencia**: Almacenamiento automático en JSON con mecanismo de reintentos
- **Manejo de errores**: Operaciones de archivo robustas con reintentos
- **Interfaz de línea de comandos**: Menú interactivo con validación de entrada
- **Integración con IA**: Descomposición de tareas usando OpenAI (cuando está configurado)
- **Sugerencias de tipo**: Mejor claridad y mantenibilidad del código

## 🛡️ Manejo de errores

La aplicación incluye:
- Mecanismo de reintentos para operaciones de archivo (máximo 3 intentos)
- Validación de entrada en el menú
- Gestión segura de IDs de tareas
- Manejo de salida controlada

## 🛠️ Tecnologías utilizadas

- **Python 3.13+**: Lenguaje principal
- **OpenAI API**: Para la funcionalidad de IA
- **JSON**: Almacenamiento de datos
- **unittest**: Framework de testing
- **python-dotenv**: Gestión de variables de entorno

## 🎮 Uso del programa

### Ejecutar la aplicación

```bash
python main.py
```

### Menú principal

El programa presenta un menú interactivo con las siguientes opciones:

1. **Añadir tarea**: Crear una nueva tarea simple
2. **Añadir tarea compleja (con IA)**: Usar IA para descomponer una tarea compleja
3. **Listar tareas**: Mostrar todas las tareas con su estado
4. **Completar tarea**: Marcar una tarea como completada
5. **Eliminar tarea**: Eliminar una tarea del sistema
6. **Salir**: Cerrar la aplicación

### Ejemplos de uso

#### Añadir una tarea simple
```
Elige una opción: 1
Descripción de la tarea: Comprar leche
Tarea añadida: Comprar leche
```

#### Añadir una tarea compleja con IA
```
Elige una opción: 2
Descripción de la tarea compleja: Organizar una fiesta de cumpleaños
```
La IA descompondrá esta tarea en subtareas como:
- Hacer lista de invitados
- Reservar lugar para la celebración
- Planificar el menú y comprar comida
- Decorar el espacio
- Coordinar actividades y entretenimiento

## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas unitarias que cubren toda la funcionalidad principal.

### Ejecutar las pruebas

```bash
python -m unittest test_task_manager.py -v
```

### Cobertura de pruebas

Las pruebas cubren:
- ✅ Añadir tareas
- ✅ Eliminar tareas existentes
- ✅ Manejo de tareas inexistentes
- ✅ Listar tareas
- ✅ Completar tareas

## 🤖 Funcionalidad de IA

La integración con OpenAI permite:

- **Descomposición inteligente**: Convierte tareas complejas en 3-5 subtareas accionables
- **Manejo de errores**: Gestión robusta de fallos en la API
- **Configuración flexible**: Funciona sin IA si no se configura la API key

### Ejemplo de descomposición de IA

**Entrada**: "Aprender Python"

**Salida**:
- Instalar Python y configurar el entorno de desarrollo
- Estudiar los conceptos básicos (variables, tipos de datos, estructuras de control)
- Practicar con ejercicios de programación básica
- Crear un proyecto pequeño para aplicar lo aprendido
- Revisar y refactorizar el código creado

## 🔒 Seguridad

- Las API keys se gestionan a través de variables de entorno
- No se almacenan credenciales en el código fuente
- Manejo seguro de errores en las llamadas a la API

## 🚧 Limitaciones conocidas

- La funcionalidad de IA requiere conexión a internet
- Las tareas se almacenan en texto plano (sin encriptación)
- No hay funcionalidad de backup automático

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## 📋 Roadmap

### Próximas características

- [ ] Interfaz gráfica de usuario (GUI)
- [ ] Categorías de tareas
- [ ] Fechas de vencimiento
- [ ] Recordatorios
- [ ] Exportar/importar tareas
- [ ] Búsqueda y filtrado avanzado
- [ ] Estadísticas de productividad

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Base desaroollada por [MoureDev](https://github.com/mouredev)
Mejoras añaadidas por [Pablo](https://github.com/PabloBartolomeMolina)
---

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

- Abre un [issue](https://github.com/PabloBartolomeMolina/python-task-manager/issues)
- Contacta al desarrollador a través de [Linkedin](https://www.linkedin.com/in/pablo-bartolome-molina/)

---

*Proyecto desarrollado con 💙 en Python*