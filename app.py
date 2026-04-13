# -*- coding: utf-8 -*-
"""
Aplicación web para generación automática de Diagramas de Ishikawa + 5 Porqués usando IA.

Esta aplicación web construida con Streamlit permite a los usuarios analizar problemas
utilizando la metodología de Ishikawa (espina de pescado) combinada con los 5 Porqués
para identificar causas raíz de manera profunda y sistemática.

Funcionalidades principales
---------------------------
- Análisis de problemas con metodología Ishikawa (6M)
- Profundización con técnica de 5 Porqués
- Generación automática con GPT-4o
- Visualización interactiva de resultados
- Exportación a Excel estructurado con múltiples hojas
- Exportación a Drawing.io para diagramas visuales
- Soporte multiidioma (Español/Inglés)

Categorías de Análisis (6M)
----------------------------
1. Mano de Obra (Personal)
2. Métodos (Procedimientos)
3. Máquinas (Equipos)
4. Materiales (Insumos)
5. Medición (Control)
6. Medio Ambiente (Entorno)

Configuración
-------------
Requiere archivo .env con:
    OPENAI_API_KEY=sk-your-api-key-here

Uso
---
Ejecutar con:
    streamlit run app.py

Notas
-----
La aplicación utiliza plantillas de prompts configurables almacenadas
en archivos markdown para mayor flexibilidad en la generación de análisis.
"""
import streamlit as st
import os
from dotenv import load_dotenv
from ishikawa_generator import IshikawaGenerator
import json
import base64
from io import BytesIO

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Generador Ishikawa + 5 Porqués",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .categoria-header {
        background-color: #4472C4;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .causa-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
        border-left: 4px solid #4472C4;
    }
    .porque-list {
        background-color: #fff2cc;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .causa-raiz {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        border-left: 4px solid #28a745;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-header">🐟 Análisis de Causa Raíz</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Diagrama de Ishikawa (6M) + 5 Porqués con IA</p>', unsafe_allow_html=True)

# Sidebar - Configuración
st.sidebar.header("⚙️ Configuración")

# API Key - Solo desde archivo .env
api_key = os.getenv("OPENAI_API_KEY", "")
if api_key:
    st.sidebar.success("✅ API Key configurada correctamente")
else:
    st.sidebar.error("⚠️ API Key no configurada")
    st.sidebar.warning("Configura tu API Key en el archivo `.env`")
    st.sidebar.info("""
    **Pasos para configurar:**
    1. Crea un archivo `.env` en la carpeta del proyecto
    2. Agrega la línea: OPENAI_API_KEY=sk-tu-api-key
    3. Reinicia la aplicación
    """)

# Modelo fijo
model = "gpt-5.4"
st.sidebar.info("🤖 **Modelo:** GPT-5.4 (fijo)")

# Idioma
language = st.sidebar.selectbox(
    "🌐 Idioma",
    options=[("Español", "es"), ("English", "en")],
    format_func=lambda x: x[0],
    index=0,
    key="language_selector"
)

# Número de causas por categoría
num_causas = st.sidebar.slider(
    "📊 Causas por categoría",
    min_value=1,
    max_value=5,
    value=3,
    help="Número de causas a identificar para cada una de las 6 categorías de Ishikawa"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 Metodología

**Ishikawa (6M):**
- 🙋 Mano de Obra
- 📋 Métodos
- ⚙️ Máquinas
- 📦 Materiales
- 📏 Medición
- 🌐 Medio Ambiente

**5 Porqués:**
Profundiza en cada causa preguntando "¿Por qué?" cinco veces para llegar a la causa raíz.
""")

# Inicializar session state
if 'analysis' not in st.session_state:
    st.session_state.analysis = None
if 'problema' not in st.session_state:
    st.session_state.problema = ""

# Tabs principales  
tab1, tab2, tab3 = st.tabs(["📝 Definir Problema", "🔍 Análisis", "📚 Ayuda"])

with tab1:
    st.header("📝 Define el Problema a Analizar")
    
    st.markdown("""
    Define claramente el problema que deseas analizar. Sé específico y conciso.
    
    **Ejemplos de problemas:**
    - *"Defectos de calidad en productos terminados"*
    - *"Retrasos constantes en entregas a clientes"*
    - *"Alta rotación de personal en el departamento de producción"*
    - *"Exceso de desperdicio en el proceso de manufactura"*
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        problema = st.text_area(
            "🎯 Describe el problema:",
            height=100,
            placeholder="Ejemplo: Altos índices de defectos en el producto final",
            help="Sé claro y específico sobre el problema que deseas analizar"
        )
        
        contexto = st.text_area(
            "📋 Contexto adicional (opcional):",
            height=150,
            placeholder="Proporciona información relevante sobre el proceso, industria, o situación actual que ayude a contextualizar el problema...",
            help="Incluye información útil como: tipo de industria, volumen de producción, procesos involucrados, etc."
        )
        
        st.markdown("##### 📎 Documentos de referencia (opcional)")
        uploaded_files = st.file_uploader(
            "Sube imágenes, PDFs u otros documentos que ayuden a contextualizar el problema",
            type=['png', 'jpg', 'jpeg', 'webp', 'pdf', 'txt', 'docx'],
            accept_multiple_files=True,
            help="Puedes subir imágenes, PDFs, archivos de texto o documentos de Word para proporcionar contexto visual o documental al análisis"
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} archivo(s) cargado(s)")
            for file in uploaded_files:
                file_size = len(file.getvalue()) / 1024  # KB
                st.caption(f"📄 {file.name} ({file_size:.1f} KB)")
    
    with col2:
        st.info("""
        **Tips para definir el problema:**
        
        ✅ Sé específico y medible
        
        ✅ Enfócate en el "qué", no en el "por qué"
        
        ✅ Usa datos cuando sea posible
        
        ❌ Evita incluir soluciones
        
        ❌ No uses lenguaje vago
        """)
    
    st.markdown("---")
    
    if problema.strip():
        st.session_state.problema = problema
        
        if st.button("🚀 Generar Análisis de Causa Raíz", type="primary", use_container_width=True):
            if not api_key:
                st.error("❌ Debes configurar tu API Key de OpenAI en el archivo .env")
            else:
                with st.spinner("Generando análisis de causa raíz... Esto puede tomar unos momentos."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    def update_progress(value, message):
                        progress_bar.progress(value)
                        status_text.text(message)
                    
                    try:
                        generator = IshikawaGenerator(api_key, model=model, language=language[1])
                        
                        # Preparar archivos subidos
                        files_data = []
                        if uploaded_files:
                            for uploaded_file in uploaded_files:
                                file_data = {
                                    'name': uploaded_file.name,
                                    'type': uploaded_file.type,
                                    'content': uploaded_file.getvalue()
                                }
                                files_data.append(file_data)
                        
                        analysis = generator.generate_ishikawa(
                            problema=problema,
                            contexto=contexto,
                            num_causas_por_categoria=num_causas,
                            uploaded_files=files_data if files_data else None,
                            progress_callback=update_progress
                        )
                        
                        st.session_state.analysis = analysis
                        
                        progress_bar.empty()
                        status_text.empty()
                        
                        st.success("✅ Análisis completado exitosamente!")
                        st.balloons()
                        st.info("👉 Ve a la pestaña **Análisis** para ver los resultados")
                        
                    except Exception as e:
                        st.error(f"❌ Error al generar análisis: {str(e)}")
                        progress_bar.empty()
                        status_text.empty()
    else:
        st.warning("⚠️ Por favor describe el problema para continuar")

with tab2:
    st.header("🔍 Análisis de Causa Raíz")
    
    if st.session_state.analysis:
        analysis = st.session_state.analysis
        
        # Resumen ejecutivo
        st.subheader("📊 Resumen Ejecutivo")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Problema:** {analysis.get('problema', '')}")
            st.markdown(f"**Análisis:** {analysis.get('resumen', '')}")
        with col2:
            st.metric("Total de Causas Identificadas", 
                     len(analysis.get('categorias', [])) * len(analysis.get('categorias', [{}])[0].get('causas', [])) if analysis.get('categorias') else 0)
        
        st.markdown("---")
        
        # Mostrar análisis por categoría
        categorias = analysis.get('categorias', [])
        
        for cat_idx, categoria_data in enumerate(categorias):
            categoria_nombre = categoria_data.get('categoria', '')
            
            # Header de categoría
            st.markdown(f'<div class="categoria-header">🔹 {categoria_nombre}</div>', unsafe_allow_html=True)
            
            causas = categoria_data.get('causas', [])
            
            # Tabs para cada causa dentro de la categoría
            if causas:
                causa_tabs = st.tabs([f"Causa {i+1}" for i in range(len(causas))])
                
                for causa_idx, (causa_tab, causa) in enumerate(zip(causa_tabs, causas)):
                    with causa_tab:
                        col1, col2 = st.columns([1, 1])
                        
                        with col1:
                            st.markdown("**Causa Principal:**")
                            st.info(causa.get('causa_principal', ''))
                            
                            st.markdown("**Descripción:**")
                            st.write(causa.get('descripcion', ''))
                            
                            st.markdown("**Acciones Recomendadas:**")
                            st.success(causa.get('acciones_recomendadas', ''))
                        
                        with col2:
                            st.markdown("**🔍 5 Porqués:**")
                            porques = causa.get('cinco_porques', [])
                            for i, porque in enumerate(porques, 1):
                                st.markdown(f"**{i}.** {porque}")
                            
                            st.markdown("**🎯 Causa Raíz Identificada:**")
                            st.markdown(f'<div class="causa-raiz">{causa.get("causa_raiz", "")}</div>', 
                                      unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Botones de exportación
        st.subheader("💾 Exportar Resultados")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Descargar Excel", use_container_width=True):
                try:
                    generator = IshikawaGenerator(api_key, model=model, language=language[1])
                    
                    # Generar archivo temporal
                    import tempfile
                    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
                    tmp_file.close()  # Cerrar el archivo antes de usarlo
                    
                    output_path = generator.export_to_excel(analysis, tmp_file.name)
                    
                    # Leer archivo para download
                    with open(output_path, 'rb') as f:
                        excel_data = f.read()
                    
                    st.download_button(
                        label="⬇️ Descargar Análisis (Excel)",
                        data=excel_data,
                        file_name="analisis_ishikawa.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                    
                    # Limpiar archivo temporal
                    try:
                        os.unlink(output_path)
                    except:
                        pass  # Ignorar si el archivo ya fue eliminado
                        
                except Exception as e:
                    st.error(f"Error al generar Excel: {str(e)}")
        
        with col2:
            if st.button("📥 Descargar Drawing.io", use_container_width=True):
                try:
                    generator = IshikawaGenerator(api_key, model=model, language=language[1])
                    
                    # Generar archivo temporal
                    import tempfile
                    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.drawio')
                    tmp_file.close()  # Cerrar el archivo antes de usarlo
                    
                    output_path = generator.export_to_drawio(analysis, tmp_file.name)
                    
                    # Leer archivo para download
                    with open(output_path, 'r', encoding='utf-8') as f:
                        drawio_data = f.read()
                    
                    st.download_button(
                        label="⬇️ Descargar Diagrama (Drawing.io)",
                        data=drawio_data,
                        file_name="diagrama_ishikawa.drawio",
                        mime="application/xml",
                        use_container_width=True
                    )
                    
                    # Limpiar archivo temporal
                    try:
                        os.unlink(output_path)
                    except:
                        pass  # Ignorar si el archivo ya fue eliminado
                        
                except Exception as e:
                    st.error(f"Error al generar Drawing.io: {str(e)}")
        
        with col3:
            if st.button("📋 Copiar JSON", use_container_width=True):
                json_str = json.dumps(analysis, indent=2, ensure_ascii=False)
                st.code(json_str, language='json')
                st.info("JSON copiado en el cuadro de arriba")
        
    else:
        st.info("👈 Ve a la pestaña **Definir Problema** y genera un análisis primero")

with tab3:
    st.header("📚 Ayuda y Guía de Uso")
    
    st.markdown("""
    ## 🎯 ¿Qué es el Diagrama de Ishikawa?
    
    El Diagrama de Ishikawa, también conocido como **diagrama de espina de pescado** o **diagrama de causa-efecto**, 
    es una herramienta de análisis que ayuda a identificar las causas potenciales de un problema.
    
    ### Las 6M (Categorías de Análisis)
    
    1. **🙋 Mano de Obra (Personal)**: Factores humanos como habilidades, capacitación, motivación, fatiga
    2. **📋 Métodos (Procedimientos)**: Procesos, procedimientos, instrucciones de trabajo, estándares
    3. **⚙️ Máquinas (Equipos)**: Equipos, herramientas, tecnología, mantenimiento, calibración
    4. **📦 Materiales (Insumos)**: Materias primas, calidad de materiales, proveedores, almacenamiento
    5. **📏 Medición (Control)**: Sistemas de medición, instrumentos, indicadores, datos, precisión
    6. **🌐 Medio Ambiente (Entorno)**: Condiciones ambientales, temperatura, espacio, organización
    
    ## 🔍 ¿Qué son los 5 Porqués?
    
    Los **5 Porqués** es una técnica de análisis que consiste en preguntar "¿Por qué?" repetidamente 
    (típicamente cinco veces) para profundizar en las causas de un problema hasta llegar a la **causa raíz**.
    
    ### Ejemplo de 5 Porqués:
    
    **Problema:** La máquina se detuvo
    
    1. **¿Por qué?** Se sobrecargó y se fundió el fusible
    2. **¿Por qué?** No había suficiente lubricación en los rodamientos
    3. **¿Por qué?** La bomba de lubricación no circulaba suficiente aceite
    4. **¿Por qué?** La entrada de la bomba estaba obstruida con virutas de metal
    5. **¿Por qué?** No hay filtro en la bomba
    
    **Causa Raíz:** Falta de filtro en la bomba de lubricación
    
    ## 🚀 Cómo usar esta aplicación
    
    1. **Configurar API Key**: Asegúrate de tener tu API Key de OpenAI configurada en el archivo `.env`
    
    2. **Definir el Problema**: 
       - Ve a la pestaña "Definir Problema"
       - Describe claramente el problema
       - Opcionalmente, agrega contexto adicional
    
    3. **Generar Análisis**:
       - Haz clic en "Generar Análisis de Causa Raíz"
       - Espera mientras la IA analiza (puede tomar 1-2 minutos)
    
    4. **Revisar Resultados**:
       - Ve a la pestaña "Análisis"
       - Explora las causas por categoría
       - Revisa los 5 porqués de cada causa
       - Identifica las causas raíz
    
    5. **Exportar**:
       - Descarga el análisis en Excel (con múltiples hojas estructuradas)
       - Descarga el diagrama visual en formato Drawing.io
       - Copia el JSON si necesitas los datos en otro formato
    
    ## 💡 Consejos para mejores resultados
    
    - ✅ Define el problema de manera específica y medible
    - ✅ Proporciona contexto relevante sobre tu industria/proceso
    - ✅ Revisa y ajusta el número de causas por categoría según necesites
    - ✅ Usa el análisis como punto de partida para investigación más profunda
    - ✅ Involucra a tu equipo en validar las causas identificadas
    
    ## ⚙️ Configuración Avanzada
    
    - **Modelo de IA**: Puedes elegir entre diferentes modelos de OpenAI
      - `gpt-4o`: Más potente y preciso (recomendado)
      - `gpt-4o-mini`: Más rápido y económico
      - `gpt-4-turbo`: Balance entre velocidad y calidad
    
    - **Idioma**: Los análisis se pueden generar en español o inglés
    
    - **Causas por Categoría**: Ajusta según la complejidad de tu problema (1-5)
    
    ## 📞 Soporte
    
    Para problemas técnicos o preguntas, consulta la documentación de OpenAI o contacta al administrador del sistema.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🐟 Análisis de Causa Raíz con Ishikawa + 5 Porqués</p>
    <p>Powered by OpenAI GPT-5.4</p>
</div>
""", unsafe_allow_html=True)
