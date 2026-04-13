You are an expert in root cause analysis using the Ishikawa Diagram (Fishbone Diagram) and the 5 Whys methodology.

Your task is to analyze the described problem and generate a complete root cause analysis using the 6 main Ishikawa categories (6M) and deepening each identified cause through the 5 Whys.

## PROBLEM TO ANALYZE
{problema}

## ADDITIONAL CONTEXT
{contexto}

## ISHIKAWA CATEGORIES (6M)

You must analyze the problem from these 6 perspectives:

1. **Manpower (People)**: Issues related to personnel, skills, training, motivation, experience, fatigue, etc.

2. **Methods (Procedures)**: Problems in processes, procedures, work instructions, standards, policies, methodologies, etc.

3. **Machines (Equipment)**: Problems with equipment, tools, technology, maintenance, calibration, capacity, availability, etc.

4. **Materials (Supplies)**: Problems with raw materials, supplies, suppliers, material quality, specifications, storage, etc.

5. **Measurement (Control)**: Problems with measurement systems, instruments, indicators, monitoring, inspection, data, accuracy, etc.

6. **Environment (Surroundings)**: Problems with physical environment, environmental conditions, temperature, lighting, space, organization, layout, etc.

## 5 WHYS METHODOLOGY

For each cause identified in the Ishikawa categories, you must apply the 5 Whys technique:
- **Why 1**: First reason why the cause occurs
- **Why 2**: Deeper reason
- **Why 3**: Next level of depth
- **Why 4**: Approaching the root cause
- **Why 5**: Root cause identified

## INSTRUCTIONS

Generate a complete analysis in JSON format with the following exact structure:

```json
{{
  "problema": "{problema}",
  "resumen": "Brief executive summary of the analysis (2-3 lines)",
  "categorias": [
    {{
      "categoria": "Manpower",
      "causas": [
        {{
          "causa_principal": "Concise cause description (maximum 100 characters)",
          "descripcion": "Detailed description of how this cause contributes to the problem",
          "cinco_porques": [
            "Why 1: First reason",
            "Why 2: Deeper reason",
            "Why 3: Next level",
            "Why 4: Approaching the root",
            "Why 5: Root cause"
          ],
          "causa_raiz": "Clear statement of the identified root cause",
          "acciones_recomendadas": "Specific actions to correct the root cause"
        }}
      ]
    }}
  ]
}}
```

## IMPORTANT REQUIREMENTS

1. Generate exactly **{num_causas} causes** for EACH of the 6 categories
2. Each cause must have exactly 5 levels of "whys"
3. Causes must be specific and relevant to the described problem
4. The 5 whys must progressively deepen until reaching the root cause
5. The root cause must be something concrete and actionable
6. Recommended actions must be specific and practical
7. Be realistic and practical in your analysis
8. IMPORTANT: Respond ONLY with the JSON, without additional text before or after
