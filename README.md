# 🎯 Generador de Ishikawa + 5 Porqués con IA

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com/)
[![Conda](https://img.shields.io/badge/Conda-Environment-44A833?style=flat&logo=anaconda&logoColor=white)](https://docs.conda.io/)

Aplicación web para generar análisis de causa raíz automáticamente utilizando la metodología de **Diagrama de Ishikawa (Espina de Pescado)** combinada con **5 Porqués**, potenciado por la API de OpenAI.

> **💡 IMPORTANTE - Consideraciones de Uso**
> 
> Esta herramienta genera análisis de causa raíz automatizados que deben considerarse como **punto de partida** para el análisis formal. El análisis definitivo y las acciones correctivas son responsabilidad del **equipo de mejora continua**.
> 
> Se recomienda:
> - Revisar y validar todas las causas identificadas con el equipo
> - Complementar con datos históricos y experiencia del proceso
> - Verificar las causas raíz con evidencia antes de implementar acciones
> - Utilizar como herramienta de facilitación en sesiones de análisis de problemas

---

## 📑 Tabla de Contenido

- [✨ Características Principales](#-características-principales)
- [📋 Requisitos Previos](#-requisitos-previos)
- [🚀 Instalación](#-instalación)
- [▶️ Uso](#️-uso)
- [📊 Metodología](#-metodología)
- [📈 Interpretación de Resultados](#-interpretación-de-resultados)
- [💾 Formatos de Exportación](#-formatos-de-exportación)
- [🎯 Características Avanzadas](#-características-avanzadas)
- [💡 Consejos de Uso](#-consejos-de-uso)
- [🛠️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [🔧 Solución de Problemas](#-solución-de-problemas)
- [📚 Referencias](#-referencias)
- [📄 Licencia](#-licencia)

---

[cc-by]: https://creativecommons.org/licenses/by/4.0/deed.es
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## ✨ Características Principales

### 🔍 Análisis de Causa Raíz con IA

- **Diagrama de Ishikawa (6M)**: Análisis estructurado en 6 categorías principales
  - 👥 **Mano de Obra**: Personal, habilidades, capacitación, motivación
  - 📝 **Métodos**: Procesos, procedimientos, estándares operativos
  - ⚙️ **Máquinas**: Equipos, herramientas, mantenimiento, tecnología
  - 📦 **Materiales**: Materias primas, insumos, calidad, proveedores
  - 📏 **Medición**: Sistemas de control, instrumentos, indicadores
  - 🌍 **Medio Ambiente**: Condiciones físicas, organización, layout

- **Técnica de 5 Porqués**: Profundización sistemática hasta la causa raíz
  - Análisis de 5 niveles de profundidad por cada causa
  - Identificación clara de causas raíz accionables
  - Acciones correctivas recomendadas específicas

- **Generación con IA**: Utiliza GPT-5.4 para análisis inteligente y contextualizado

### 📎 Análisis Multimodal

- **Soporte de imágenes**: Sube fotos de defectos, diagramas de proceso, layouts de planta
  - 📷 Formatos: JPG, JPEG, PNG, WEBP
  - 🔍 El modelo analiza visualmente las imágenes junto con el contexto textual
  
- **Soporte de documentos**: Incluye reportes, especificaciones, procedimientos
  - 📄 PDFs: El modelo GPT-5.4 procesa directamente archivos PDF sin extracción
  - 📝 Word: Documentos DOCX se analizan nativamente
  - 📋 Texto plano: Archivos TXT se incorporan al contexto
  
- **Contexto enriquecido**: Las imágenes y documentos proporcionan información visual y documental que complementa el análisis de causa raíz

### 🎨 Visualización y Análisis

- **Interfaz interactiva**: Navegación por pestañas intuitiva
- **Vista por categorías**: Organización clara de causas por cada M
- **5 Porqués expandibles**: Tabs para explorar cada causa en detalle
- **Resumen ejecutivo**: Visión general del análisis generado

### 💾 Exportación Múltiple

1. **Excel Estructurado**:
   - Hoja "Resumen": Información general del problema
   - Hoja "Diagrama Ishikawa": Tabla con todas las causas por categoría
   - Hoja "5 Porqués": Análisis completo con los 5 niveles de profundidad
   - Formato profesional con colores y estilos
   - Filtros automáticos habilitados

2. **Drawing.io (Diagrama Visual)**:
   - Diagrama de espina de pescado completo
   - Visualización gráfica de todas las categorías y causas
   - Editable en [Draw.io](https://app.diagrams.net)
   - Formato XML estándar

3. **JSON**:
   - Estructura de datos completa
   - Ideal para integración con otros sistemas

### 🎛️ Configuración Flexible

- **Multiidioma**: Interfaz y análisis en Español o Inglés
- **Modelo de IA**: GPT-5.4 (modelo frontera de OpenAI)
- **Causas ajustables**: De 1 a 5 causas por categoría según complejidad
- **Prompts personalizables**: Plantillas editables en archivos markdown

---

## 📋 Requisitos Previos

### 1. Cuenta de OpenAI
- Cuenta activa en [OpenAI](https://platform.openai.com/)
- API Key con acceso a GPT-5.4
- Créditos o suscripción activa

### 2. Software Instalado
- **Python 3.11+** (recomendado 3.11)
- **Conda** o **Miniconda** (para gestión de entornos)
- Editor de texto para configuración (VS Code, Notepad++, etc.)

### 3. Conocimientos Básicos
- Conceptos de análisis de causa raíz
- Uso básico de terminal/línea de comandos
- Familiaridad con metodologías de mejora continua (deseable)

---

## 🚀 Instalación

### Opción 1: Instalación con Conda (Recomendado)

```bash
# 1. Clonar o descargar el repositorio
cd ruta/al/proyecto/ishikawa

# 2. Crear el entorno conda desde el archivo YAML
conda env create -f environment.yml

# 3. Activar el entorno
conda activate ishikawa

# 4. Verificar instalación
python --version
streamlit --version
```

### Opción 2: Instalación con pip

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Configuración de API Key

1. Crear archivo `.env` en la raíz del proyecto:
```bash
copy .env.example .env    # Windows
cp .env.example .env      # Linux/Mac
```

2. Editar `.env` y agregar tu API Key:
```env
OPENAI_API_KEY=sk-tu-api-key-aqui
```

3. **IMPORTANTE**: Nunca subas el archivo `.env` a repositorios públicos

---

## ▶️ Uso

### Inicio Rápido

```bash
# Con conda
conda activate ishikawa
streamlit run app.py

# Con pip/venv
# (activar entorno virtual primero)
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Flujo de Trabajo

1. **Definir Problema** (Tab 1):
   - Describe claramente el problema a analizar
   - Agrega contexto adicional si es relevante
   - **Sube archivos de referencia** (opcional):
     - 📷 Imágenes: Fotos de defectos, diagramas de flujo, layouts
     - 📄 PDFs: Reportes de calidad, especificaciones técnicas
     - 📝 Documentos: Procedimientos, instructivos de trabajo
   - Haz clic en "Generar Análisis de Causa Raíz"

2. **Revisar Análisis** (Tab 2):
   - Explora las 6 categorías de Ishikawa
   - Revisa las causas identificadas en cada categoría
   - Analiza los 5 Porqués de cada causa
   - Identifica las causas raíz

3. **Exportar Resultados**:
   - Descarga análisis en Excel (recomendado para documentación)
   - Descarga diagrama en Drawing.io (para presentaciones)
   - Copia JSON si necesitas integración

### Ejemplo de Uso

**Problema**: "Alta tasa de defectos en productos terminados"

**Contexto**: "Línea de ensamblaje electrónico con 50 operadores, turnos rotativos, proceso semi-automatizado"

**Archivos adjuntos** (opcional): 
- 📷 Foto del producto defectuoso (defecto.jpg)
- 📄 PDF con especificaciones técnicas (specs.pdf)
- 📊 Diagrama de proceso actual (proceso.png)

La IA generará:
- 3 causas por cada una de las 6 categorías (18 causas totales)
- 5 niveles de "por qué" para cada causa (90 preguntas totales)
- 18 causas raíz identificadas
- Acciones recomendadas específicas

---

## 📊 Metodología

### Diagrama de Ishikawa (6M)

```
                    Mano de Obra          Métodos
                          |                  |
                          |                  |
        ─────────────────┴──────────────────┴──────────> PROBLEMA
                          |                  |
                          |                  |
                    Máquinas           Materiales
                          
                    Medición       Medio Ambiente
```

Cada categoría analiza aspectos específicos:

| Categoría | Enfoque de Análisis |
|-----------|-------------------|
| 👥 Mano de Obra | Habilidades, entrenamiento, fatiga, motivación, comunicación |
| 📝 Métodos | Procedimientos, estándares, instrucciones, políticas |
| ⚙️ Máquinas | Equipos, herramientas, mantenimiento, capacidad, tecnología |
| 📦 Materiales | Calidad, especificaciones, proveedores, almacenamiento |
| 📏 Medición | Instrumentos, calibración, sistemas de control, datos |
| 🌍 Medio Ambiente | Temperatura, espacio, iluminación, organización, layout |

### Técnica de 5 Porqués

Ejemplo real de análisis:

```
CAUSA PRINCIPAL: Operadores no siguen el procedimiento estándar

¿Por qué 1? → No conocen el procedimiento actualizado
¿Por qué 2? → No recibieron capacitación sobre cambios recientes
¿Por qué 3? → No existe un sistema para notificar cambios en procedimientos
¿Por qué 4? → No hay una plataforma de gestión de documentos
¿Por qué 5? → No se ha asignado presupuesto para sistemas de gestión documental

CAUSA RAÍZ: Falta de inversión en sistemas de gestión documental

ACCIÓN RECOMENDADA: Implementar un sistema digital de gestión de procedimientos 
con notificaciones automáticas y tracking de capacitaciones
```

---

## 📈 Interpretación de Resultados

### Estructura del Análisis

```json
{
  "problema": "Descripción del problema",
  "resumen": "Resumen ejecutivo del análisis",
  "categorias": [
    {
      "categoria": "Mano de Obra",
      "causas": [
        {
          "causa_principal": "Descripción breve",
          "descripcion": "Detalle de cómo contribuye al problema",
          "cinco_porques": ["Por qué 1", "Por qué 2", ..., "Por qué 5"],
          "causa_raiz": "Causa raíz identificada",
          "acciones_recomendadas": "Acciones específicas"
        }
      ]
    }
  ]
}
```

### Priorización de Acciones

1. **Causas Raíz Comunes**: Si múltiples causas convergen en la misma raíz, priorizarla
2. **Impacto vs Esfuerzo**: Evaluar qué acciones tienen mayor impacto con menor esfuerzo
3. **Factibilidad**: Considerar recursos disponibles y restricciones organizacionales
4. **Medibilidad**: Preferir acciones cuyos resultados sean medibles

---

## 💾 Formatos de Exportación

### 1. Excel (.xlsx)

**Estructura de archivo:**
- **Hoja "Resumen"**: Problema, metodología, fecha
- **Hoja "Diagrama Ishikawa"**: Tabla con categoría, causa, descripción
- **Hoja "5 Porqués"**: Análisis completo con 5 niveles + causa raíz + acciones

**Características:**
- ✅ Formato profesional con colores corporativos
- ✅ Filtros automáticos habilitados
- ✅ Columnas autoajustadas
- ✅ Wrap text en celdas con mucho contenido
- ✅ Causa raíz resaltada en verde

### 2. Drawing.io (.drawio)

**Contenido:**
- Diagrama de espina de pescado visual
- Estructura XML editable
- Cabeza (problema) en la derecha
- 6 categorías distribuidas arriba y abajo
- Causas conectadas a cada categoría

**Cómo usar:**
1. Descargar el archivo `.drawio`
2. Abrir en [app.diagrams.net](https://app.diagrams.net)
3. Editar, personalizar colores, mover elementos
4. Exportar como PNG, PDF, SVG para presentaciones

### 3. JSON

**Uso recomendado:**
- Integración con otros sistemas
- Análisis programático
- Almacenamiento en bases de datos
- APIs y pipelines de datos

---

## 🎯 Características Avanzadas

### 📎 Tipos de Archivos Soportados

#### 📷 Imágenes (Análisis Visual)
- **JPG/JPEG**: Fotos de defectos, productos, equipos
- **PNG**: Diagramas, capturas de pantalla, gráficos
- **WEBP**: Imágenes optimizadas

**Casos de uso:**
- 📸 Fotos de defectos o fallas en productos
- 📐 Diagramas de flujo de proceso
- 🏭 Layouts de planta o distribución de equipos
- 📈 Gráficos de control o tendencias
- 🔧 Imágenes de equipos o herramientas

#### 📄 Documentos (Análisis Textual)
- **PDF**: Reportes, especificaciones, manuales (procesados directamente por GPT-5.4)
- **DOCX**: Procedimientos, instructivos, análisis previos
- **TXT**: Logs, notas, datos de producción

**Casos de uso:**
- 📋 Reportes de calidad o auditorías
- 📘 Especificaciones técnicas del producto
- 📝 Procedimientos operativos estándar (SOPs)
- 📊 Datos históricos o logs de producción
- 🔬 Reportes de laboratorio o análisis previos

**Límites recomendados:**
- Hasta 5-10 archivos por análisis
- Imágenes: preferiblemente < 5MB cada una
- PDFs: < 10 páginas para mejor rendimiento
- Total combinado: mantener contexto manejable

### Personalización de Prompts

Los prompts están en archivos markdown editables:

```
prompts/
├── ishikawa_prompt_es.md   # Español
└── ishikawa_prompt_en.md   # Inglés
```

Puedes:
- ✏️ Modificar las instrucciones para la IA
- 🎨 Ajustar el tono y estilo del análisis
- 🌐 Agregar nuevos idiomas creando archivos `ishikawa_prompt_{idioma}.md`
- 📐 Cambiar la estructura del JSON de salida

### Modelo de IA

La aplicación utiliza **GPT-5.4**, el modelo frontera de OpenAI, que proporciona:
- Análisis de alta calidad y precisión excepcional
- Comprensión contextual profunda de procesos industriales
- Evaluaciones realistas basadas en mejores prácticas
- Sugerencias de acciones correctivas específicas y útiles
- Procesamiento nativo de imágenes y documentos PDF

### Número de Causas

- **1-2 causas**: Problemas muy específicos o análisis rápido
- **3 causas** (recomendado): Balance entre profundidad y practicidad
- **4-5 causas**: Problemas complejos que requieren análisis exhaustivo

---

## 💡 Consejos de Uso

### ✅ Mejores Prácticas

1. **Define problemas específicos**: 
   - ❌ "Hay problemas de calidad"
   - ✅ "15% de productos tienen defectos de soldadura en placa PCB"

2. **Proporciona contexto relevante**:
   - Tipo de industria/proceso
   - Volumen de producción
   - Datos cuantitativos disponibles
   - Cambios recientes en el proceso
   - **Archivos de soporte**: Imágenes, PDFs, documentos que ilustren el problema

3. **Valida con el equipo**:
   - Usa el análisis como punto de partida
   - Sesiones de revisión con expertos del proceso
   - Complementa con datos históricos

4. **Documenta seguimiento**:
   - Guarda análisis con fecha
   - Registra acciones implementadas
   - Mide resultados de mejoras

### ⚠️ Limitaciones

- La IA genera análisis basados en patrones generales, no conoce tu proceso específico
- Revisa y valida todas las causas con evidencia real
- Los 5 Porqués pueden variar según el contexto real
- Las acciones recomendadas son genéricas, debes adaptarlas
- **Archivos**: PDFs muy largos (>20 páginas) pueden procesarse parcialmente
- **Rendimiento**: Múltiples archivos grandes pueden aumentar el tiempo de análisis

---

## 🛠️ Estructura del Proyecto

```
ishikawa/
│
├── app.py                      # Aplicación Streamlit principal
├── ishikawa_generator.py       # Clase generadora de análisis
├── environment.yml             # Archivo de entorno Conda
├── requirements.txt            # Dependencias Python
├── .env                        # Configuración (NO SUBIR A GIT)
├── .env.example               # Plantilla de configuración
├── .gitignore                 # Archivos ignorados por Git
├── README.md                  # Esta documentación
├── LICENSE                    # Licencia CC BY 4.0
│
├── prompts/                   # Plantillas de prompts
│   ├── ishikawa_prompt_es.md
│   └── ishikawa_prompt_en.md
│
└── run_app.bat               # Script para Windows (opcional)
```

### Archivos Clave

- **`app.py`**: Interfaz web Streamlit, maneja UI y flujo de usuario
- **`ishikawa_generator.py`**: Lógica de generación, llamadas a OpenAI API, exportaciones
- **`prompts/*.md`**: Plantillas de instrucciones para la IA

---

## 🔧 Solución de Problemas

### Error: "API Key no configurada"

**Causa**: Archivo `.env` no existe o está vacío

**Solución**:
```bash
# Crear archivo .env
echo OPENAI_API_KEY=sk-tu-api-key > .env
```

### Error: "Error al generar análisis"

**Posibles causas**:
1. **Sin créditos en OpenAI**: Verifica tu cuenta en [platform.openai.com](https://platform.openai.com)
2. **API Key inválida**: Verifica que copiaste correctamente la key
3. **Problema de conexión**: Verifica tu conexión a internet
4. **Rate limit**: Espera unos minutos e intenta nuevamente

### Aplicación no inicia

```bash
# Verificar que el entorno está activado
conda activate ishikawa

# Reinstalar dependencias
pip install --force-reinstall -r requirements.txt

# Verificar versión de Python
python --version  # Debe ser 3.11+
```

### Exportación falla

**Excel**: Asegúrate de tener permisos de escritura en la carpeta
**Drawing.io**: El archivo se descarga pero debes abrirlo en app.diagrams.net

---

## 📚 Referencias

### Metodologías

- **Ishikawa (Espina de Pescado)**: Desarrollado por Kaoru Ishikawa en los 1960s
- **5 Porqués**: Técnica creada por Taiichi Ohno (Toyota Production System)
- **6M**: Clasificación estándar en manufactura (Mano, Método, Máquina, Material, Medición, Medio)

### Recursos Adicionales

- [ASQ - Ishikawa Diagram](https://asq.org/quality-resources/fishbone)
- [Lean Enterprise Institute - 5 Whys](https://www.lean.org/lexicon-terms/5-whys/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## 📄 Licencia

Este proyecto está licenciado bajo **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

**Esto significa que puedes:**
- ✅ Compartir - copiar y redistribuir el material
- ✅ Adaptar - remix, transformar y construir sobre el material
- ✅ Uso comercial permitido

**Bajo las siguientes condiciones:**
- 📝 **Atribución**: Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se hicieron cambios

Ver [LICENSE](LICENSE) o [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/deed.es) para más detalles.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📧 Soporte

Para preguntas, problemas o sugerencias:
- Abre un issue en el repositorio
- Consulta la [documentación de OpenAI](https://platform.openai.com/docs)
- Revisa el código fuente (está documentado)

---

## 🙏 Agradecimientos

- **OpenAI** por proporcionar la API de GPT-5.4
- **Streamlit** por el framework de interfaces web
- **Kaoru Ishikawa** y **Taiichi Ohno** por estas metodologías atemporales
- Comunidad de Lean/Six Sigma por mantener vivas estas prácticas

---

**Generado para profesionales de mejora continua y calidad**
