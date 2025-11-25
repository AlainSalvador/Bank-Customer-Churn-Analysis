import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from fpdf import FPDF

sns.set(style="whitegrid")

#Cargar el dataset
df = pd.read_csv("Churn_Modelling.csv")

#Mostrar las primeras 5 filas del dataset
#print(df.head())

#Información técnica (tipos de datos, valores nulos, etc. )
#print(df.info())

#Resumen estadístico de las variables numéricas
#print(df.describe()) 

#Eliminar columnas irrelevantes
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

#Verificacion de duplicados y nulos
duplicados = df.duplicated().sum()
nulos = df.isnull().sum()
#print("Duplicados:", duplicados)
#print("Nulos:", nulos)  

#Dataset final
#print(df.shape)

#Tasa general de fuga
conteo_fuga = df['Exited'].value_counts()
print(conteo_fuga) #0 se queda, 1 se va

#Gráfico
plt.figure(figsize=(6,6))
plt.pie(conteo_fuga,
        labels=['Clientes Retenidos (0)', 'Clientes Perdidos (1)'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['lightblue', 'red'])
plt.title('Porcentaje global de fuga de clientes')
plt.show()

#Análisis demográfico
fig, ax = plt.subplots(1, 2, figsize=(14,5))
#Genero
sns.countplot(x='Gender', hue='Exited', data=df, ax=ax[0], palette="viridis")
ax[0].set_title('Fuga de Clientes por género')
ax[0].set_ylabel('Cantidad de personas')
#Pais
sns.countplot(x='Geography', hue='Exited', data=df, ax=ax[1], palette="viridis")
ax[1].set_title('Fuga de Clientes por pais')
ax[1].set_ylabel('Cantidad de personas')

plt.tight_layout()
plt.show()

#Impacto Financiero (Balance)

plt.figure(figsize=(10, 6))

# Boxplot: Relación entre Fuga y Dinero en cuenta
sns.boxplot(x='Exited', y='Balance', data=df, palette='viridis')

plt.title('Distribución de Balance Bancario: Retenidos vs Fugados')
plt.xlabel('Estado (0=Se queda, 1=Se va)')
plt.ylabel('Balance en Cuenta ($)')
plt.show()


print("--- GENERANDO REPORTE PDF, POR FAVOR ESPERA... ---")

# --- PASO 1: RE-GENERAR Y GUARDAR LOS GRÁFICOS COMO IMÁGENES ---
# Gráfico 1: Pastel (Churn Rate)
plt.figure(figsize=(6, 4))
plt.pie(df['Exited'].value_counts(), labels=['Retenidos', 'Perdidos'], autopct='%1.1f%%', colors=['#66b3ff','#ff9999'], startangle=90)
plt.title('Tasa Global de Fuga')
plt.savefig('grafico_pastel.png', bbox_inches='tight', dpi=100)
plt.close()

# Gráfico 2: Barras (País)
plt.figure(figsize=(6, 4))
sns.countplot(x='Geography', hue='Exited', data=df, palette='viridis')
plt.title('Fuga por País')
plt.savefig('grafico_pais.png', bbox_inches='tight', dpi=100)
plt.close()

# Gráfico 3: Boxplot (Dinero)
plt.figure(figsize=(6, 4))
sns.boxplot(x='Exited', y='Balance', data=df, palette='viridis')
plt.title('Impacto del Dinero en la Fuga')
plt.savefig('grafico_dinero.png', bbox_inches='tight', dpi=100)
plt.close()

# --- PASO 2: CREAR EL PDF ---

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Reporte de Riesgo de Fuga - Global FinBank', 0, 1, 'C')
        self.ln(5)

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Introducción
pdf.cell(0, 10, txt="Estimados Directores,", ln=1)
pdf.multi_cell(0, 10, txt="Tras analizar la base de datos de 10,000 clientes, hemos detectado patrones alarmantes que explican la fuga de capital. A continuacion los 3 hallazgos clave:")
pdf.ln(5)

# Hallazgo 1
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="1. Situacion Actual: 1 de cada 5 clientes se va.", ln=1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 10, txt="Nuestra tasa de churn ha alcanzado el 20.4%. Esto supera el margen saludable del sector.")
pdf.image('grafico_pastel.png', x=60, w=90) # Insertar imagen
pdf.ln(5)

# Hallazgo 2
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="2. Foco Rojo: Alemania y Publico Femenino", ln=1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 10, txt="Alemania presenta la mayor tasa de abandono proporcional. Ademas, las mujeres tienden a cerrar sus cuentas con mayor frecuencia que los hombres.")
pdf.image('grafico_pais.png', x=60, w=90)
pdf.ln(5)

# Hallazgo 3 (El más importante)
pdf.add_page() # Nueva página para que no se amontone
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="3. CRITICO: Fuga de Capitales Altos", ln=1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 10, txt="Contrario a la intuicion, los clientes que se van TIENEN MAYOR SALDO PROMEDIO que los que se quedan. Estamos perdiendo cuentas de alto valor, mientras que las cuentas con saldo $0 permanecen.")
pdf.image('grafico_dinero.png', x=50, w=100)
pdf.ln(10)

# Conclusión
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="RECOMENDACION FINAL:", ln=1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 10, txt="Se sugiere implementar urgentemente un programa de fidelizacion VIP enfocado en Alemania y revisar la experiencia de usuario para el segmento femenino.")

# Guardar PDF
pdf.output("Reporte_Ejecutivo_Fuga.pdf")

print(f"¡ÉXITO! El reporte 'Reporte_Ejecutivo_Fuga.pdf' ha sido creado.")