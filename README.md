# Bank-Customer-Churn-Analysis
Análisis automatizado de retención de clientes (Churn) utilizando Python. El proyecto procesa datos bancarios, visualiza patrones críticos de fuga (demografía y finanzas) y genera automáticamente un reporte ejecutivo en PDF para la toma de decisiones estratégicas

# Análisis de Fuga de Clientes Bancarios (Churn Analysis)

## Contexto del Proyecto
Este proyecto simula un encargo de consultoría de datos para una entidad financiera que enfrenta una tasa de abandono del 20%. El objetivo fue identificar **quiénes se van y por qué** para proponer estrategias de retención.

## Tecnologías Usadas
* **Python:** Pandas (Limpieza), Matplotlib/Seaborn (Visualización).
* **Reporting:** FPDF (Generación automática de reportes PDF).

## Hallazgos Clave
1.  **Tasa de Fuga:** 20.4% de la cartera de clientes.
2.  **Demografía:** Las mujeres en Alemania presentan el mayor riesgo de abandono.
3.  **Insight Financiero:** Contrario a la intuición, **los clientes con mayor capital son los que más abandonan el banco**, lo que representa un riesgo crítico de liquidez.

## Estructura del Repositorio
* `Analisis_fuga.py`: Script completo de limpieza y generación de gráficas.
* `output/Reporte_Ejecutivo_Fuga.pdf`: Reporte final listo para directivos.
