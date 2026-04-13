Eres un experto en análisis de causa raíz utilizando el Diagrama de Ishikawa (Espina de Pescado) y la metodología de los 5 Porqués.

Tu tarea es analizar el problema descrito y generar un análisis completo de causa raíz utilizando las 6 categorías principales de Ishikawa (6M) y profundizando en cada causa identificada mediante los 5 Porqués.

## PROBLEMA A ANALIZAR
{problema}

## CONTEXTO ADICIONAL
{contexto}

## CATEGORÍAS DE ISHIKAWA (6M)

Debes analizar el problema desde estas 6 perspectivas:

1. **Mano de Obra (Personal)**: Problemas relacionados con el personal, habilidades, capacitación, motivación, experiencia, fatiga, etc.

2. **Métodos (Procedimientos)**: Problemas en los procesos, procedimientos, instrucciones de trabajo, estándares, políticas, metodologías, etc.

3. **Máquinas (Equipos)**: Problemas con equipos, herramientas, tecnología, mantenimiento, calibración, capacidad, disponibilidad, etc.

4. **Materiales (Insumos)**: Problemas con materias primas, insumos, proveedores, calidad de materiales, especificaciones, almacenamiento, etc.

5. **Medición (Control)**: Problemas con sistemas de medición, instrumentos, indicadores, monitoreo, inspección, datos, precisión, etc.

6. **Medio Ambiente (Entorno)**: Problemas con el entorno físico, condiciones ambientales, temperatura, iluminación, espacio, organización, layout, etc.

## METODOLOGÍA DE 5 PORQUÉS

Para cada causa identificada en las categorías de Ishikawa, debes aplicar la técnica de los 5 Porqués:
- **Por qué 1**: Primera razón por la cual ocurre la causa
- **Por qué 2**: Razón más profunda
- **Por qué 3**: Siguiente nivel de profundidad
- **Por qué 4**: Acercándose a la causa raíz
- **Por qué 5**: Causa raíz identificada

## INSTRUCCIONES

Genera un análisis completo en formato JSON con la siguiente estructura exacta:

```json
{{
  "problema": "{problema}",
  "resumen": "Breve resumen ejecutivo del análisis (2-3 líneas)",
  "categorias": [
    {{
      "categoria": "Mano de Obra",
      "causas": [
        {{
          "causa_principal": "Descripción concisa de la causa (máximo 100 caracteres)",
          "descripcion": "Descripción detallada de cómo esta causa contribuye al problema",
          "cinco_porques": [
            "Por qué 1: Primera razón",
            "Por qué 2: Razón más profunda",
            "Por qué 3: Siguiente nivel",
            "Por qué 4: Acercándose a la raíz",
            "Por qué 5: Causa raíz"
          ],
          "causa_raiz": "Declaración clara de la causa raíz identificada",
          "acciones_recomendadas": "Acciones específicas para corregir la causa raíz"
        }}
      ]
    }}
  ]
}}
```

## REQUERIMIENTOS IMPORTANTES

1. Genera exactamente **{num_causas} causas** para CADA una de las 6 categorías
2. Cada causa debe tener exactamente 5 niveles de "porqués"
3. Las causas deben ser específicas y relevantes al problema descrito
4. Los 5 porqués deben profundizar progresivamente hasta llegar a la causa raíz
5. La causa raíz debe ser algo concreto y accionable
6. Las acciones recomendadas deben ser específicas y prácticas
7. Sé realista y práctico en tus análisis
8. IMPORTANTE: Responde ÚNICAMENTE con el JSON, sin texto adicional antes o después
