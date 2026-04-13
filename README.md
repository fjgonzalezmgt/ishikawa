# ð Generador de Ishikawa + 5 PorquÃ©s con IA

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat&logo=openai&logoColor=white)](https://openai.com/)
[![Conda](https://img.shields.io/badge/Conda-Environment-44A833?style=flat&logo=anaconda&logoColor=white)](https://docs.conda.io/)

AplicaciÃ³n web para generar anÃ¡lisis de causa raÃ­z automÃ¡ticamente utilizando la metodologÃ­a de **Diagrama de Ishikawa (Espina de Pescado)** combinada con **5 PorquÃ©s**, potenciado por la API de OpenAI.

> **ð¡ IMPORTANTE - Consideraciones de Uso**
> 
> Esta herramienta genera anÃ¡lisis de causa raÃ­z automatizados que deben considerarse como **punto de partida** para el anÃ¡lisis formal. El anÃ¡lisis definitivo y las acciones correctivas son responsabilidad del **equipo de mejora continua**.
> 
> Se recomienda:
> - Revisar y validar todas las causas identificadas con el equipo
> - Complementar con datos histÃ³ricos y experiencia del proceso
> - Verificar las causas raÃ­z con evidencia antes de implementar acciones
> - Utilizar como herramienta de facilitaciÃ³n en sesiones de anÃ¡lisis de problemas

---

## ð Tabla de Contenido

- [ð CaracterÃ­sticas Principales](#-caracterÃ­sticas-principales)
- [ð Requisitos Previos](#-requisitos-previos)
- [ð InstalaciÃ³n](#-instalaciÃ³n)
- [â¶ï¸ Uso](#ï¸-uso)
- [ð MetodologÃ­a](#-metodologÃ­a)
- [ð InterpretaciÃ³n de Resultados](#-interpretaciÃ³n-de-resultados)
- [ð¾ Formatos de ExportaciÃ³n](#-formatos-de-exportaciÃ³n)
- [ð¯ CaracterÃ­sticas Avanzadas](#-caracterÃ­sticas-avanzadas)
- [ð¡ Consejos de Uso](#-consejos-de-uso)
- [ð ï¸ Estructura del Proyecto](#ï¸-estructura-del-proyecto)
- [ð SoluciÃ³n de Problemas](#-soluciÃ³n-de-problemas)
- [ð Referencias](#-referencias)
- [ð Licencia](#-licencia)

---

[cc-by]: https://creativecommons.org/licenses/by/4.0/deed.es
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## ð CaracterÃ­sticas Principales

### ð AnÃ¡lisis de Causa RaÃ­z con IA

- **Diagrama de Ishikawa (6M)**: AnÃ¡lisis estructurado en 6 categorÃ­as principales
  - ð **Mano de Obra**: Personal, habilidades, capacitaciÃ³n, motivaciÃ³n
  - ð **MÃ©todos**: Procesos, procedimientos, estÃ¡ndares operativos
  - âï¸ **MÃ¡quinas**: Equipos, herramientas, mantenimiento, tecnologÃ­a
  - ð¦ **Materiales**: Materias primas, insumos, calidad, proveedores
  - ð **MediciÃ³n**: Sistemas de control, instrumentos, indicadores
  - ð **Medio Ambiente**: Condiciones fÃ­sicas, organizaciÃ³n, layout

- **TÃ©cnica de 5 PorquÃ©s**: ProfundizaciÃ³n sistemÃ¡tica hasta la causa raÃ­z
  - AnÃ¡lisis de 5 niveles de profundidad por cada causa
  - IdentificaciÃ³n clara de causas raÃ­z accionables
  - Acciones correctivas recomendadas especÃ­ficas

- **GeneraciÃ³n con IA**: Utiliza GPT-4o para anÃ¡lisis inteligente y contextualizado

### 📎 Análisis Multimodal

- **Soporte de imágenes**: Sube fotos de defectos, diagramas de proceso, layouts de planta
  - 📷 Formatos: JPG, JPEG, PNG, WEBP
  - 🔍 El modelo analiza visualmente las imágenes junto con el contexto textual
  
- **Soporte de documentos**: Incluye reportes, especificaciones, procedimientos
  - 📄 PDFs: El modelo procesa directamente archivos PDF sin extracción
  - 📝 Word: Documentos DOCX se analizan nativamente
  - 📋 Texto plano: Archivos TXT se incorporan al contexto
  
- **Contexto enriquecido**: Las imágenes y documentos proporcionan información visual y documental que complementa el análisis de causa raíz### ð VisualizaciÃ³n y AnÃ¡lisis

- **Interfaz interactiva**: NavegaciÃ³n por pestaÃ±as intuitiva
- **Vista por categorÃ­as**: OrganizaciÃ³n clara de causas por cada M
- **5 PorquÃ©s expandibles**: Tabs para explorar cada causa en detalle
- **Resumen ejecutivo**: VisiÃ³n general del anÃ¡lisis generado

### ð¾ ExportaciÃ³n MÃºltiple

1. **Excel Estructurado**:
   - Hoja "Resumen": InformaciÃ³n general del problema
   - Hoja "Diagrama Ishikawa": Tabla con todas las causas por categorÃ­a
   - Hoja "5 PorquÃ©s": AnÃ¡lisis completo con los 5 niveles de profundidad
   - Formato profesional con colores y estilos
   - Filtros automÃ¡ticos habilitados

2. **Drawing.io (Diagrama Visual)**:
   - Diagrama de espina de pescado completo
   - VisualizaciÃ³n grÃ¡fica de todas las categorÃ­as y causas
   - Editable en [Draw.io](https://app.diagrams.net)
   - Formato XML estÃ¡ndar

3. **JSON**:
   - Estructura de datos completa
   - Ideal para integraciÃ³n con otros sistemas

### ð ConfiguraciÃ³n Flexible

- **Multiidioma**: Interfaz y anÃ¡lisis en EspaÃ±ol o InglÃ©s
- **Modelos de IA configurables**: GPT-4o, GPT-4o-mini, GPT-4-turbo
- **Causas ajustables**: De 1 a 5 causas por categorÃ­a segÃºn complejidad
- **Prompts personalizables**: Plantillas editables en archivos markdown

---

## ð Requisitos Previos

### 1. Cuenta de OpenAI
- Cuenta activa en [OpenAI](https://platform.openai.com/)
- API Key con acceso a modelos GPT-4
- CrÃ©ditos o suscripciÃ³n activa

### 2. Software Instalado
- **Python 3.11+** (recomendado 3.11)
- **Conda** o **Miniconda** (para gestiÃ³n de entornos)
- Editor de texto para configuraciÃ³n (VS Code, Notepad++, etc.)

### 3. Conocimientos BÃ¡sicos
- Conceptos de anÃ¡lisis de causa raÃ­z
- Uso bÃ¡sico de terminal/lÃ­nea de comandos
- Familiaridad con metodologÃ­as de mejora continua (deseable)

---

## ð InstalaciÃ³n

### OpciÃ³n 1: InstalaciÃ³n con Conda (Recomendado)

```bash
# 1. Clonar o descargar el repositorio
cd ruta/al/proyecto/ishikawa

# 2. Crear el entorno conda desde el archivo YAML
conda env create -f environment.yml

# 3. Activar el entorno
conda activate ishikawa

# 4. Verificar instalaciÃ³n
python --version
streamlit --version
```

### OpciÃ³n 2: InstalaciÃ³n con pip

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

### ConfiguraciÃ³n de API Key

1. Crear archivo `.env` en la raÃ­z del proyecto:
```bash
copy .env.example .env    # Windows
cp .env.example .env      # Linux/Mac
```

2. Editar `.env` y agregar tu API Key:
```env
OPENAI_API_KEY=sk-tu-api-key-aqui
```

3. **IMPORTANTE**: Nunca subas el archivo `.env` a repositorios pÃºblicos

---

## â¶ï¸ Uso

### Inicio RÃ¡pido

```bash
# Con conda
conda activate ishikawa
streamlit run app.py

# Con pip/venv
# (activar entorno virtual primero)
streamlit run app.py
```

La aplicaciÃ³n se abrirÃ¡ automÃ¡ticamente en tu navegador en `http://localhost:8501`

### Flujo de Trabajo

1. **Definir Problema** (Tab 1):
   - Describe claramente el problema a analizar
   - Agrega contexto adicional si es relevante
   - **Sube archivos de referencia** (opcional):
     - 📷 Imágenes: Fotos de defectos, diagramas de flujo, layouts
     - 📄 PDFs: Reportes de calidad, especificaciones técnicas
     - 📝 Documentos: Procedimientos, instructivos de trabajo
   - Haz clic en "Generar AnÃ¡lisis de Causa RaÃ­z"

2. **Revisar AnÃ¡lisis** (Tab 2):
   - Explora las 6 categorÃ­as de Ishikawa
   - Revisa las causas identificadas en cada categorÃ­a
   - Analiza los 5 PorquÃ©s de cada causa
   - Identifica las causas raÃ­z

3. **Exportar Resultados**:
   - Descarga anÃ¡lisis en Excel (recomendado para documentaciÃ³n)
   - Descarga diagrama en Drawing.io (para presentaciones)
   - Copia JSON si necesitas integraciÃ³n

### Ejemplo de Uso

**Problema**: "Alta tasa de defectos en productos terminados"

**Contexto**: "Línea de ensamblaje electrónico con 50 operadores, turnos rotativos, proceso semi-automatizado"

**Archivos adjuntos** (opcional): 
- 📷 Foto del producto defectuoso (defecto.jpg)
- 📄 PDF con especificaciones técnicas (specs.pdf)
- 📊 Diagrama de proceso actual (proceso.png)

La IA generará:
- 3 causas por cada una de las 6 categorÃ­as (18 causas totales)
- 5 niveles de "por quÃ©" para cada causa (90 preguntas totales)
- 18 causas raÃ­z identificadas
- Acciones recomendadas especÃ­ficas

---

## ð MetodologÃ­a

### Diagrama de Ishikawa (6M)

```
                    Mano de Obra          MÃ©todos
                          |                  |
                          |                  |
        âââââââââââââââââââ´âââââââââââââââââââ´ââââââââââ> PROBLEMA
                          |                  |
                          |                  |
                    MÃ¡quinas           Materiales
                          
                    MediciÃ³n       Medio Ambiente
```

Cada categorÃ­a analiza aspectos especÃ­ficos:

| CategorÃ­a | Enfoque de AnÃ¡lisis |
|-----------|-------------------|
| ð Mano de Obra | Habilidades, entrenamiento, fatiga, motivaciÃ³n, comunicaciÃ³n |
| ð MÃ©todos | Procedimientos, estÃ¡ndares, instrucciones, polÃ­ticas |
| âï¸ MÃ¡quinas | Equipos, herramientas, mantenimiento, capacidad, tecnologÃ­a |
| ð¦ Materiales | Calidad, especificaciones, proveedores, almacenamiento |
| ð MediciÃ³n | Instrumentos, calibraciÃ³n, sistemas de control, datos |
| ð Medio Ambiente | Temperatura, espacio, iluminaciÃ³n, organizaciÃ³n, layout |

### TÃ©cnica de 5 PorquÃ©s

Ejemplo real de anÃ¡lisis:

```
CAUSA PRINCIPAL: Operadores no siguen el procedimiento estÃ¡ndar

Â¿Por quÃ© 1? â No conocen el procedimiento actualizado
Â¿Por quÃ© 2? â No recibieron capacitaciÃ³n sobre cambios recientes
Â¿Por quÃ© 3? â No existe un sistema para notificar cambios en procedimientos
Â¿Por quÃ© 4? â No hay una plataforma de gestiÃ³n de documentos
Â¿Por quÃ© 5? â No se ha asignado presupuesto para sistemas de gestiÃ³n documental

CAUSA RAÃZ: Falta de inversiÃ³n en sistemas de gestiÃ³n documental

ACCIÃN RECOMENDADA: Implementar un sistema digital de gestiÃ³n de procedimientos 
con notificaciones automÃ¡ticas y tracking de capacitaciones
```

---

## ð InterpretaciÃ³n de Resultados

### Estructura del AnÃ¡lisis

```json
{
  "problema": "DescripciÃ³n del problema",
  "resumen": "Resumen ejecutivo del anÃ¡lisis",
  "categorias": [
    {
      "categoria": "Mano de Obra",
      "causas": [
        {
          "causa_principal": "DescripciÃ³n breve",
          "descripcion": "Detalle de cÃ³mo contribuye al problema",
          "cinco_porques": ["Por quÃ© 1", "Por quÃ© 2", ..., "Por quÃ© 5"],
          "causa_raiz": "Causa raÃ­z identificada",
          "acciones_recomendadas": "Acciones especÃ­ficas"
        }
      ]
    }
  ]
}
```

### PriorizaciÃ³n de Acciones

1. **Causas RaÃ­z Comunes**: Si mÃºltiples causas convergen en la misma raÃ­z, priorizarla
2. **Impacto vs Esfuerzo**: Evaluar quÃ© acciones tienen mayor impacto con menor esfuerzo
3. **Factibilidad**: Considerar recursos disponibles y restricciones organizacionales
4. **Medibilidad**: Preferir acciones cuyos resultados sean medibles

---

## ð¾ Formatos de ExportaciÃ³n

### 1. Excel (.xlsx)

**Estructura de archivo:**
- **Hoja "Resumen"**: Problema, metodologÃ­a, fecha
- **Hoja "Diagrama Ishikawa"**: Tabla con categorÃ­a, causa, descripciÃ³n
- **Hoja "5 PorquÃ©s"**: AnÃ¡lisis completo con 5 niveles + causa raÃ­z + acciones

**CaracterÃ­sticas:**
- â Formato profesional con colores corporativos
- â Filtros automÃ¡ticos habilitados
- â Columnas autoajustadas
- â Wrap text en celdas con mucho contenido
- â Causa raÃ­z resaltada en verde

### 2. Drawing.io (.drawio)

**Contenido:**
- Diagrama de espina de pescado visualEstructura XML editable
- Cabeza (problema) en la derecha
- 6 categorÃ­as distribuidas arriba y abajo
- Causas conectadas a cada categorÃ­a

**CÃ³mo usar:**
1. Descargar el archivo `.drawio`
2. Abrir en [app.diagrams.net](https://app.diagrams.net)
3. Editar, personalizar colores, mover elementos
4. Exportar como PNG, PDF, SVG para presentaciones

### 3. JSON

**Uso recomendado:**
- IntegraciÃ³n con otros sistemas
- AnÃ¡lisis programÃ¡tico
- Almacenamiento en bases de datos
- APIs y pipelines de datos

---

## ð¯ CaracterÃ­sticas Avanzadas
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
- **PDF**: Reportes, especificaciones, manuales (procesados directamente por GPT-4o)
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
### PersonalizaciÃ³n de Prompts

Los prompts estÃ¡n en archivos markdown editables:

```
prompts/
âââ ishikawa_prompt_es.md   # EspaÃ±ol
âââ ishikawa_prompt_en.md   # InglÃ©s
```

Puedes:
- âï¸ Modificar las instrucciones para la IA
- ð¨ Ajustar el tono y estilo del anÃ¡lisis
- ð Agregar nuevos idiomas creando archivos `ishikawa_prompt_{idioma}.md`
- ð Cambiar la estructura del JSON de salida

### SelecciÃ³n de Modelos

| Modelo | Velocidad | Calidad | Costo | Recomendado para |
|--------|-----------|---------|-------|------------------|
| GPT-4o | RÃ¡pido | Excelente | Medio | Uso general (recomendado) |
| GPT-4o-mini | Muy RÃ¡pido | Buena | Bajo | Problemas simples, pruebas |
| GPT-4-turbo | Medio | Excelente | Alto | AnÃ¡lisis complejos crÃ­ticos |

### NÃºmero de Causas

- **1-2 causas**: Problemas muy especÃ­ficos o anÃ¡lisis rÃ¡pido
- **3 causas** (recomendado): Balance entre profundidad y practicidad
- **4-5 causas**: Problemas complejos que requieren anÃ¡lisis exhaustivo

---

## ð¡ Consejos de Uso

### â Mejores PrÃ¡cticas

1. **Define problemas especÃ­ficos**: 
   - â "Hay problemas de calidad"
   - â "15% de productos tienen defectos de soldadura en placa PCB"

2. **Proporciona contexto relevante**:
   - Tipo de industria/proceso
   - Volumen de producciÃ³n
   - Datos cuantitativos disponibles
   - Cambios recientes en el proceso
   - **Archivos de soporte**: Imágenes, PDFs, documentos que ilustren el problema

3. **Valida con el equipo**:
   - Usa el anÃ¡lisis como punto de partida
   - Sesiones de revisiÃ³n con expertos del proceso
   - Complementa con datos histÃ³ricos

4. **Documenta seguimiento**:
   - Guarda anÃ¡lisis con fecha
   - Registra acciones implementadas
   - Mide resultados de mejoras

### â ï¸ Limitaciones

- La IA genera anÃ¡lisis basados en patrones generales, no conoce tu proceso especÃ­fico
- Revisa y valida todas las causas con evidencia real
- Los 5 PorquÃ©s pueden variar segÃºn el contexto real
- Las acciones recomendadas son genÃ©ricas, debes adaptarlas- **Archivos**: PDFs muy largos (>20 páginas) pueden procesarse parcialmente
- **Rendimiento**: Múltiples archivos grandes pueden aumentar el tiempo de análisis
---

## ð ï¸ Estructura del Proyecto

```
ishikawa/
â
âââ app.py                      # AplicaciÃ³n Streamlit principal
âââ ishikawa_generator.py       # Clase generadora de anÃ¡lisis
âââ environment.yml             # Archivo de entorno Conda
âââ requirements.txt            # Dependencias Python
âââ .env                        # ConfiguraciÃ³n (NO SUBIR A GIT)
âââ .env.example               # Plantilla de configuraciÃ³n
âââ .gitignore                 # Archivos ignorados por Git
âââ README.md                  # Esta documentaciÃ³n
âââ LICENSE                    # Licencia CC BY 4.0
â
âââ prompts/                   # Plantillas de prompts
â   âââ ishikawa_prompt_es.md
â   âââ ishikawa_prompt_en.md
â
âââ run_app.bat               # Script para Windows (opcional)
```

### Archivos Clave

- **`app.py`**: Interfaz web Streamlit, maneja UI y flujo de usuario
- **`ishikawa_generator.py`**: LÃ³gica de generaciÃ³n, llamadas a OpenAI API, exportaciones
- **`prompts/*.md`**: Plantillas de instrucciones para la IA

---

## ð SoluciÃ³n de Problemas

### Error: "API Key no configurada"

**Causa**: Archivo `.env` no existe o estÃ¡ vacÃ­o

**SoluciÃ³n**:
```bash
# Crear archivo .env
echo OPENAI_API_KEY=sk-tu-api-key > .env
```

### Error: "Error al generar anÃ¡lisis"

**Posibles causas**:
1. **Sin crÃ©ditos en OpenAI**: Verifica tu cuenta en [platform.openai.com](https://platform.openai.com)
2. **API Key invÃ¡lida**: Verifica que copiaste correctamente la key
3. **Problema de conexiÃ³n**: Verifica tu conexiÃ³n a internet
4. **Rate limit**: Espera unos minutos e intenta nuevamente

### AplicaciÃ³n no inicia

```bash
# Verificar que el entorno estÃ¡ activado
conda activate ishikawa

# Reinstalar dependencias
pip install --force-reinstall -r requirements.txt

# Verificar versiÃ³n de Python
python --version  # Debe ser 3.11+
```

### ExportaciÃ³n falla

**Excel**: AsegÃºrate de tener permisos de escritura en la carpeta
**Drawing.io**: El archivo se descarga pero debes abrirlo en app.diagrams.net

---

## ð Referencias

### MetodologÃ­as

- **Ishikawa (Espina de Pescado)**: Desarrollado por Kaoru Ishikawa en los 1960s
- **5 PorquÃ©s**: TÃ©cnica creada por Taiichi Ohno (Toyota Production System)
- **6M**: ClasificaciÃ³n estÃ¡ndar en manufactura (Mano, MÃ©todo, MÃ¡quina, Material, MediciÃ³n, Medio)

### Recursos Adicionales

- [ASQ - Ishikawa Diagram](https://asq.org/quality-resources/fishbone)
- [Lean Enterprise Institute - 5 Whys](https://www.lean.org/lexicon-terms/5-whys/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## ð Licencia

Este proyecto estÃ¡ licenciado bajo **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

**Esto significa que puedes:**
- â Compartir - copiar y redistribuir el material
- â Adaptar - remix, transformar y construir sobre el material
- â Uso comercial permitido

**Bajo las siguientes condiciones:**
- ð **AtribuciÃ³n**: Debes dar crÃ©dito apropiado, proporcionar un enlace a la licencia e indicar si se hicieron cambios

Ver [LICENSE](LICENSE) o [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/deed.es) para mÃ¡s detalles.

---

## ð¤ Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## ð§ Soporte

Para preguntas, problemas o sugerencias:
- Abre un issue en el repositorio
- Consulta la [documentaciÃ³n de OpenAI](https://platform.openai.com/docs)
- Revisa el cÃ³digo fuente (estÃ¡ documentado)

---

## ð Agradecimientos

- **OpenAI** por proporcionar la API de GPT-4
- **Streamlit** por el framework de interfaces web
- **Kaoru Ishikawa** y **Taiichi Ohno** por estas metodologÃ­as atemporales
- Comunidad de Lean/Six Sigma por mantener vivas estas prÃ¡cticas

---

**Generado con â¤ï¸ para profesionales de mejora continua y calidad**
- **Escalas detalladas**: GuÃ­a completa de interpretaciÃ³n de S, O, D y RPN
- **Ejemplo de Excel**: Formato recomendado con explicaciÃ³n de columnas
- **Consejos de uso**: Mejores prÃ¡cticas para obtener resultados Ã³ptimos
- **Enlaces a recursos**: Referencias a estÃ¡ndares AIAG, ISO y documentaciÃ³n de OpenAI

## ð Requisitos Previos

- Python 3.8 o superior
- Cuenta de OpenAI con API Key ([Obtener aquÃ­](https://platform.openai.com/api-keys))

## ð InstalaciÃ³n

1. **Clonar o descargar este repositorio**

2. **Crear un ambiente conda** (recomendado)
   ```bash
   conda create -n fmea python=3.11 -y
   ```

3. **Instalar dependencias**
   ```bash
   # Instalar paquetes desde conda
   conda install -n fmea pandas openpyxl python-dotenv streamlit -y
   
   # Instalar OpenAI con pip (no disponible en conda)
   conda run -n fmea pip install openai
   ```
   
   **Alternativa**: Si prefieres usar pip para todo:
   ```bash
   conda activate fmea
   pip install -r requirements.txt
   ```

4. **Configurar la API Key de OpenAI** (Obligatorio)
   
   Crea un archivo `.env` en el directorio del proyecto:
   ```bash
   copy .env.example .env
   ```
   
   Edita el archivo `.env` y agrega tu API key de OpenAI:
   ```
   OPENAI_API_KEY=sk-tu-api-key-aqui
   ```
   
   > **Importante**: La aplicaciÃ³n solo funcionarÃ¡ si la API key estÃ¡ configurada en el archivo `.env`

## â¶ï¸ Uso

### ð¬ Inicio RÃ¡pido

1. **Iniciar la aplicaciÃ³n**
   ```bash
   conda run -n fmea streamlit run app.py
   ```
   
   O si prefieres activar el ambiente primero:
   ```bash
   conda activate fmea
   streamlit run app.py
   ```

2. **Acceder a la interfaz web**
   - La aplicaciÃ³n se abrirÃ¡ automÃ¡ticamente en `http://localhost:8501`
   - Si no se abre, accede manualmente a esa URL

### ð Flujo de Trabajo Completo

#### 1ï¸â£ **ConfiguraciÃ³n** (Barra Lateral)
- â **API Key**: Verifica que estÃ© configurada correctamente (se carga desde `.env`)
- ð **Idioma**: Selecciona EspaÃ±ol o English para el anÃ¡lisis
- ð **Modos de fallo**: Ajusta cuÃ¡ntos escenarios generar por paso (1-5, recomendado: 2-3)

#### 2ï¸â£ **Carga de Proceso** (Tab: ð¤ Cargar Proceso)
- Haz clic en "Browse files" o arrastra tu archivo Excel
- Visualiza el preview de tus datos cargados
- La app valida automÃ¡ticamente el formato
- Si todo estÃ¡ correcto, aparece el botÃ³n "ð Generar AnÃ¡lisis FMEA"

#### 3ï¸â£ **GeneraciÃ³n de FMEA**
- Haz clic en "ð Generar AnÃ¡lisis FMEA"
- Observa la barra de progreso mientras la IA trabaja:
  - â³ Enviando solicitud a OpenAI...
  - ð Procesando respuesta...
  - â Â¡FMEA generado exitosamente!
- Â¡CelebraciÃ³n con confetti! ð

#### 4ï¸â£ **AnÃ¡lisis y EdiciÃ³n** (Tab: ð AnÃ¡lisis FMEA)
- **Revisa las mÃ©tricas principales**:
  - Total de items generados
  - RPN promedio del proceso
  - Cantidad de riesgos altos
  - RPN mÃ¡ximo encontrado

- **Explora los datos**:
  - Tabla interactiva con todos los campos del FMEA
  - Edita valores directamente en las celdas
  - Agrega o elimina filas segÃºn necesites
  - Observa el recÃ¡lculo automÃ¡tico del RPN

- **Analiza la distribuciÃ³n de riesgos**:
  - GrÃ¡fica de cantidad por categorÃ­a (Bajo/Medio/Alto)
  - Top 5 riesgos mÃ¡s crÃ­ticos

#### 5ï¸â£ **ExportaciÃ³n** (Tab: ð AnÃ¡lisis FMEA)
- Define el nombre de tu archivo de salida
- Haz clic en "ð¥ Descargar Excel"
- ObtÃ©n un archivo Excel profesional con:
  - â Formato condicional por colores segÃºn RPN
  - â Filtros automÃ¡ticos en todas las columnas
  - â Encabezados formateados
  - â Columnas ajustadas al contenido

#### 6ï¸â£ **Consulta la Ayuda** (Tab: ð Ayuda)
- Definiciones completas de FMEA
- Escalas de Severidad, Ocurrencia y DetecciÃ³n
- InterpretaciÃ³n del RPN
- Formato recomendado de Excel
- Mejores prÃ¡cticas y consejos

### â¡ Inicio RÃ¡pido con Script

Para Windows, simplemente ejecuta:
```bash
run_app.bat
```

Este script automÃ¡ticamente activa el ambiente conda y lanza la aplicaciÃ³n.

## ð Formato de Excel de Entrada

Tu archivo Excel debe contener los pasos de tu proceso. Se recomienda la siguiente estructura:

| NÃºmero | DescripciÃ³n | Responsable | Entradas | Salidas |
|--------|-------------|-------------|----------|---------|
| 1 | RecepciÃ³n de materia prima | AlmacÃ©n | Orden de compra, Material | Material verificado |
| 2 | InspecciÃ³n de calidad | Control de Calidad | Material | Reporte de inspecciÃ³n |
| 3 | Almacenamiento temporal | AlmacÃ©n | Material aprobado | Material almacenado |

**Columnas requeridas**:
- Al menos una columna con la descripciÃ³n del paso (puede llamarse: DescripciÃ³n, Description, Paso, Actividad, etc.)

**Columnas opcionales** (mejoran el anÃ¡lisis):
- NÃºmero de paso
- Responsable
- Entradas
- Salidas
- Recursos
- Procedimiento

> **Nota**: Puedes usar el archivo `template_proceso.xlsx` como referencia.

## ð InterpretaciÃ³n de Resultados

### Escalas de EvaluaciÃ³n

#### Severidad (S): 1-10
Gravedad del efecto del fallo:
- **10**: Peligroso sin advertencia
- **7-9**: Muy alta a peligrosa con advertencia
- **4-6**: Moderada a baja
- **1-3**: MÃ­nima o sin efecto

#### Ocurrencia (O): 1-10
Probabilidad de que ocurra la causa:
- **10**: Casi inevitable (â¥1 en 2)
- **7-9**: Alta frecuencia
- **4-6**: Moderada
- **1-3**: Remota a casi imposible

#### DetecciÃ³n (D): 1-10
Capacidad de detectar el fallo:
- **10**: Imposible de detectar
- **7-9**: Muy difÃ­cil de detectar
- **4-6**: Moderadamente detectable
- **1-3**: Muy fÃ¡cil de detectar

### RPN (Risk Priority Number)

**RPN = Severidad Ã Ocurrencia Ã DetecciÃ³n**

- **RPN > 100**: â ï¸ **Riesgo Alto** - Requiere acciÃ³n inmediata
- **50 â¤ RPN â¤ 100**: â¡ **Riesgo Medio** - Requiere atenciÃ³n
- **RPN < 50**: â **Riesgo Bajo** - Monitorear

## ð¯ CaracterÃ­sticas Avanzadas

### Modelo de IA

La aplicaciÃ³n utiliza **GPT-5.4**, el modelo frontera de OpenAI, que proporciona:
- AnÃ¡lisis de alta calidad y precisiÃ³n
- ComprensiÃ³n contextual profunda de procesos
- Evaluaciones realistas de Severidad, Ocurrencia y DetecciÃ³n
- Sugerencias de acciones correctivas especÃ­ficas y Ãºtiles

### Configuraciones Personalizables

- **API Key**: Se configura Ãºnicamente desde archivo `.env` (mayor seguridad)
- **Modos de fallo por paso**: Controla cuÃ¡ntos escenarios de fallo generar (1-5)
- **Idioma**: Genera el anÃ¡lisis en EspaÃ±ol o InglÃ©s
- **EdiciÃ³n en vivo**: Modifica cualquier valor y el RPN se recalcula automÃ¡ticamente

### Formato de ExportaciÃ³n

El Excel exportado incluye:
- â Encabezados formateados con color
- â Formato condicional por RPN:
  - ð¢ Verde: RPN < 50
  - ð¡ Amarillo: 50 â¤ RPN â¤ 100
  - ð´ Rojo: RPN > 100
- â Filtros automÃ¡ticos en todas las columnas
- â Ancho de columnas ajustado automÃ¡ticamente

## ð Seguridad y Privacidad

- â ï¸ **ProtecciÃ³n de API Keys**: 
  - Nunca subas archivos `.env` a repositorios pÃºblicos
  - El archivo `.env` estÃ¡ incluido en `.gitignore` por seguridad
  - La API key solo se carga desde el archivo `.env` (no se permite ingreso manual)
- ð **Datos del proceso**: Los datos se envÃ­an a OpenAI para el anÃ¡lisis. Revisa los tÃ©rminos de servicio de OpenAI
- ð¾ **Datos locales**: La aplicaciÃ³n no almacena tus datos. Todo se procesa en memoria

## ð¡ Consejos de Uso

1. **â ï¸ Herramienta de apoyo**: Esta aplicaciÃ³n genera un **borrador inicial** de FMEA. El anÃ¡lisis final debe ser validado y completado por el responsable del proceso y su equipo de trabajo, quienes conocen mejor los detalles operativos
2. **API Key**: AsegÃºrate de configurar el archivo `.env` con tu `OPENAI_API_KEY` antes de iniciar
3. **Procesos simples**: Usa 2 modos de fallo por paso para anÃ¡lisis rÃ¡pidos y enfocados
4. **Procesos complejos**: Aumenta a 3-4 modos de fallo para anÃ¡lisis exhaustivos
5. **EdiciÃ³n**: Siempre revisa y ajusta los valores segÃºn tu experiencia del proceso
6. **PriorizaciÃ³n**: EnfÃ³cate primero en items con RPN > 100
7. **Reinicio**: Si cambias la API key en `.env`, reinicia la aplicaciÃ³n para que tome efecto

## ð ï¸ Estructura del Proyecto

```
fmea/
âââ app.py                  # AplicaciÃ³n Streamlit principal
âââ fmea_generator.py       # LÃ³gica de generaciÃ³n FMEA con OpenAI
âââ requirements.txt        # Dependencias del proyecto
âââ .env.example           # Plantilla de configuraciÃ³n
âââ .gitignore             # Archivos a ignorar en Git
âââ LICENSE                # Licencia Creative Commons BY 4.0
âââ README.md              # Este archivo
âââ template_proceso.xlsx  # Ejemplo de archivo de entrada
âââ run_app.bat            # Script de inicio para Windows
âââ prompts/               # Plantillas de prompts para la IA
    âââ fmea_prompt_es.md  # Prompt en espaÃ±ol (personalizable)
    âââ fmea_prompt_en.md  # Prompt en inglÃ©s (personalizable)
```

### ð PersonalizaciÃ³n de Prompts

Los prompts utilizados para generar el anÃ¡lisis FMEA estÃ¡n almacenados en archivos markdown en la carpeta `prompts/`. Esto te permite:

- âï¸ **Personalizar las instrucciones** para la IA segÃºn tus necesidades especÃ­ficas
- ð **Agregar nuevos idiomas** creando archivos `fmea_prompt_XX.md` (donde XX es el cÃ³digo del idioma)
- ð¯ **Ajustar las escalas** de Severidad, Ocurrencia y DetecciÃ³n segÃºn estÃ¡ndares corporativos
- ð **Modificar el formato de salida** para incluir campos adicionales
- ð **Versionar los prompts** independientemente del cÃ³digo Python

Los prompts utilizan placeholders que se reemplazan automÃ¡ticamente:
- `{num_failures}`: NÃºmero de modos de fallo por paso
- `{process_steps}`: Lista enumerada de los pasos del proceso

> **Nota**: DespuÃ©s de modificar los prompts, simplemente recarga la pÃ¡gina en Streamlit para que los cambios tomen efecto.

## ð SoluciÃ³n de Problemas

### Error: "Invalid API Key" o "API Key no configurada"
- Verifica que el archivo `.env` exista en el directorio del proyecto
- Abre el archivo `.env` y confirma que la API key estÃ© correctamente escrita (empieza con `sk-`)
- AsegÃºrate de tener crÃ©ditos disponibles en tu cuenta de OpenAI
- Reinicia la aplicaciÃ³n despuÃ©s de modificar el archivo `.env`
- No incluyas espacios ni comillas extras: `OPENAI_API_KEY=sk-tu-key-aqui`

### Error: "No se encontrÃ³ columna de descripciÃ³n"
- Verifica que tu Excel tenga una columna con la descripciÃ³n de los pasos
- Los nombres vÃ¡lidos incluyen: DescripciÃ³n, Description, Paso, Actividad, etc.

### La aplicaciÃ³n no inicia
- Verifica que todas las dependencias estÃ©n instaladas
- Verifica que el ambiente conda estÃ© activo o uses `conda run -n fmea`
- Lista los paquetes instalados: `conda list -n fmea`

### El anÃ¡lisis tarda mucho
- Es normal para procesos grandes (el modelo GPT-5.4 analiza en profundidad)
- Para procesos muy grandes (>20 pasos), considera dividirlos en secciones
- El tiempo depende de la carga de OpenAI y tu conexiÃ³n a internet

## ð Referencias

- [AIAG FMEA Handbook](https://www.aiag.org/)
- [ISO 31010:2019 - Risk Assessment Techniques](https://www.iso.org/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## ð Licencia

Este proyecto estÃ¡ licenciado bajo la [Licencia Creative Commons Attribution 4.0 Internacional (CC BY 4.0)](LICENSE).

Eres libre de:
- â **Compartir** â copiar y redistribuir el material en cualquier medio o formato
- â **Adaptar** â remezclar, transformar y construir a partir del material para cualquier propÃ³sito, incluso comercialmente

Bajo el siguiente tÃ©rmino:
- ð **AtribuciÃ³n** â Debes dar crÃ©dito adecuado a Quality Analytics, proporcionar un enlace a la licencia e indicar si se realizaron cambios.

Para mÃ¡s detalles, consulta el archivo [LICENSE](LICENSE) o visita [creativecommons.org/licenses/by/4.0/deed.es](https://creativecommons.org/licenses/by/4.0/deed.es)

## ð¤ Contribuciones

Sugerencias y mejoras son bienvenidas. Por favor, reporta cualquier problema o sugerencia.

## ð§ Soporte

Para preguntas o soporte, contacta al equipo de Quality Analytics.

---

**Desarrollado usando Streamlit y OpenAI | Â© 2026 Quality Analytics**
