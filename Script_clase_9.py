#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:53:41 2023

@author: usuario
"""

###########################################################
#                TALLER DE PROGRAMACIÓN                   #
#        Especialización en Métodos Cuantitativos         #
#  para la Gestión y Análisis de Datos en Organizaciones  #
#         FACULTAD DE CIENCIAS ECONÓMICAS                 #
#            UNIVERSIDAD DE BUENOS AIRES                  #
###########################################################

## Asignatura: TALLER DE PROGRAMACIÓN  
## Año Lectivo: 2023
## Docente: Rita Beatriz Morrone


#Para poder manipular estructuras de directorios, se debe importar
#el "modulo os" que nos permite acceder a funcionalidades dependientes
#del sistema operativo e interactuar con el mismo.

import os

# Consultar Directorio actual (Current Working Directory)
cwd = os.getcwd()

# Imprimir el directorio actual de trabajo
print("Current working directory: {0}".format(cwd))

#Para el manejo y análisis de estructuras de datos,
#utilizaremos entre otras: la librería "Pandas"
#Nos permitirá trabajar con diferentes estructuras de datos:
#Series: una dimensión.
#DataFrame: tablas de dos dimensiones.
#Panel: Cubos de tres dimensiones.
#Para la creación de gráficos utilizaremos el módulo "pyplot" 
#de la librería "matplotlib" y la librería seaborn
#También utilizaremos "numpy" especializada en cálculo númerico y análisis de datos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

#En primer lugar traemos un conjunto de datos xls desde la web
site_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls'

#Abrimos el archivo como un DataFrame, y le asignamos un nombre
archivo = pd.read_excel(site_url, header = 1) 
#Diferentes formas de leer datos en Pandas:
#pd.read_csv()
#pd.read_excel()
#pd.read_html()
#pd.read_json()
#pd.read_sql()
#pd.read_sas()
#pd.read_pickle()

#Atributos de un DataFrame
#Podemos ver diferentes atributos con las siguientes funciones:

archivo.info()
#devuelve: número de filas, número y tipo de columnas,índices, memoria usada.
archivo.shape
#devuelve dimensionalidad
archivo.size
#devuelve el número de elementos.
archivo.columns
#devuelve una lista con los nombres de las columnas.
archivo.index
#devuelve una lista con los nombres de las filas
archivo.dtypes
#devuelve los tipos de datos de las columnas
archivo.tail(3)
#devuelve las últimas n filas
archivo.head(5)
#devuelve las primeras n filas

#Función "DataFrame.describe()" en Pandas:
#Devuelve los datos estadísticos de un archivo DataFrame

estadistica_archivo=archivo.describe()
#devuelve: cantidad de elementos por columna, media, desvío estandar,
#percentiles 25,50,75, valores máximos y mínimos
#En el caso de requerir datos de una columna en particular

edades = archivo["AGE"]

edades.describe()

#también podemos obtener la información por separado:
    
edades.count()
#devuelve el número de elementos
edades.sum()
#devuelve la suma de los datos
edades.cumsum()
#devuelve la suma acumulada de los datos
edades.min()
#devuelve el dato mínimo
edades.max()
#devuelve el dato máximo
edades.mean()
#devuelve la media de los datos
edades.var()
#devuelve la varianza
edades.std()
#devuelve el desvío estandar

#Se puede guardar el resumen de estadísticas en un csv
estadistica_archivo.to_csv('estadistica.csv', sep = ";")

#corroboramos que los datos se gaurdaron correctamente leyendo el archivo
resumen_archivo = pd.read_csv('estadistica.csv', sep=";")
resumen_archivo

#Gráficos

#Gráficos de barras a partir del archivo en estudio

#Paso 1- seleccionamos los datos a graficar
#(si queremos graficar la cantidad de casos por categoría)
#armamos la serie a graficar
genero = archivo.groupby('SEX').count()['ID']

#Paso 2- realizamos un gráfico de barras
#vertical:
genero.plot(kind='bar', title="Cantidad de casos por género", color="tab:blue")
#horizontal:
genero.plot(kind='barh', title="Cantidad de casos por género", color="tab:orange")

#otro ejemplo:
#Graficamos la cantidad de casos según nivel de educación:
    
educacion = archivo.groupby('EDUCATION').count()['ID']
#vertical
educacion.plot(kind = 'bar', title="Cantidad de casos por nivel de educación", color="tab:green")
#horizontal
educacion.plot(kind = 'barh', title="Cantidad de casos por nivel de educación", color="tab:purple")

#usando Seaborn
sb.countplot(x='EDUCATION', data=archivo)


#En el caso de combinar 2 o más variables:
    
#cantidad de casos según género y educación:
genero_educacion= archivo.groupby(["SEX","EDUCATION"])["ID"].count().unstack()
genero_educacion.plot(kind="barh",stacked=True, title="Cantidad de casos por género y educación")

genero_educacion2= archivo.groupby(["EDUCATION","SEX"])["ID"].count().unstack()
genero_educacion2.plot(kind="bar",stacked=True, title="Cantidad de casos por género y educación")

#Gráfico de torta

#grafica un diagrama de sectores con las frecuencias de la variable seleccionada
archivo['EDUCATION'].value_counts().plot.pie(startangle=45,autopct='%.1f %%')

archivo["default payment next month"].value_counts().plot.pie(startangle=45,autopct='%.1f %%')

#Histogramas

archivo.hist("AGE")
archivo.hist("EDUCATION")
archivo.hist('LIMIT_BAL')
archivo.hist("LIMIT_BAL", "SEX")
archivo.hist("EDUCATION", "SEX")


#Boxplot

archivo.boxplot('LIMIT_BAL')
archivo.boxplot("AGE")
archivo.boxplot('LIMIT_BAL', 'SEX', figsize=(5, 5), grid=False)
archivo.boxplot('LIMIT_BAL', 'SEX', figsize=(5, 5), grid=True)

#usando Seaborn:
sb.boxplot(data=archivo['LIMIT_BAL'])
plt.ticklabel_format(style='plain', axis='y')


#Diagrama de dispersión
archivo.plot(kind = 'scatter', x='AGE', y='LIMIT_BAL')
plt.ticklabel_format(style='plain', axis='y')

#usando Seaborn:
sb.lmplot(x='AGE', y='LIMIT_BAL', data=archivo,fit_reg=False)
plt.ticklabel_format(style='plain', axis='y')


# densidad de una variable
sb.displot(archivo['LIMIT_BAL'])

#Matriz de correlación
corr = archivo.corr()
sb.heatmap(corr)

## Otro ejemplo

url = "https://raw.githubusercontent.com/sanchezgaviermatias/Curso_Python-/master/2%20-%20Pandas/Pokemon.csv"
archivo_2 = pd.read_csv(url)

#Miramos algunos atributos:
archivo_2.info()
archivo_2.shape
type(archivo_2)
archivo_2.columns
archivo_2.dtypes
type(archivo_2["Type 1"])
archivo_2.index


#Vemos sus estadísticas:
estadistica_archivo_2=archivo_2.describe()

#Podemos localizar datos que tengan condiciones

#generamos condiciones
condicion = (archivo_2["Type 1"] == "Grass") & -(archivo_2["HP"]>=80)
#generamos un nuevo DataFrame con los datos seleccionados
#la función .loc busca en términos de valores
datos_seleccionados=archivo_2.loc[condicion, :]

#cambiamos la condición
condicion =  (archivo_2["Type 1"].isin(["Grass", "Fire"]))
datos_seleccionados_2=archivo_2.loc[ condicion, : ]


#localizamos datos por su posición
#usamos la función .iloc

#seleccionamos las primeras 10 filas y todas las columnas
archivo_2.iloc[0:10, :]
#seleccionamos las primeras 10 (0 a 9)filas y columnas 2,3 y 4
archivo_2.iloc[0:10,1:4]

#seleccionamos distintas columnas y les cambiamos el nombre

archivo_3=archivo_2[["Name","Speed","Generation"]]
archivo_3.columns=["Nombre","Velocidad","Generación"]


# le indicamos una columna para transformarla en el Ìndice
# Para que los cambios sean permanentes:
#usamos inplace=True

archivo_2.set_index("Name", inplace=True)

#Buscamos un dato a través del índice con la función loc .
archivo_2.loc["Bulbasaur", : ]

archivo_2.loc[["Bulbasaur","Munna"], :]


#Datos faltantes
#Métodos de resolución de NaN

# Hay 3 opciones:

# Eliminar Filas con NaN
# Eliminar Columna con NaN
# Reemplazar NaN con Otros Valores

#Paso 1- vemos donde hay datos faltantes
archivo_2.info()
#otra forma de verlo:
archivo_2.isnull().sum()
#muestra que campo tiene datos faltantes y los cuantifica

# Ordenamos de mayor a menor el detalle anterior
archivo_2.isna().sum().sort_values(ascending=False)

#Paso 2- resolver los datos faltantes

#Método 1 =eliminar columna, (no recomendado)
archivo_2.drop("Type 2",axis=1).head()

#Método 1 =eliminar Filas, mejor que lo anterior (no recomendado)
y = archivo_2.dropna()
#notar que se pierden muchos datos:
print(y.shape, archivo_2.shape)

#Método 3= Reemplazar los datos faltantes 
#se recomienda este!!!!

archivo_2["Type 2"]=archivo_2["Type 2"].fillna("Ninguno")

#otra forma si fuera variables numéricas:
#archivo_2["Type 2"].fillna((archivo_2["Type 2"].mode()), inplace=True)

#Paso 3- chequeamos resultados
archivo_2.isnull().sum()


## Operaciones a realizar sobre el conjunto de datos:

#sumar los valores de un campo determinado
archivo_2["HP"].sum()

#ordenar en referencia a un campo determinado
archivo_4=archivo_2.sort_values(by='Name')

#ver la media de los valores de un campo determinado
archivo_2["HP"].mean()

#ver el desvío estandar de los valores de un campo determinado
archivo_2["HP"].std()


## Operaciones entre Columnas

archivo_2["Poder de Ataque"] = archivo_2["HP"]*(1/3) + archivo_2["Attack"]*(1/3)+archivo_2["Sp. Atk"]*(1/3)
archivo_2["Poder de Ataque"] = round(archivo_2["Poder de Ataque"])

archivo_2["Poder de Defenza"] = archivo_2["HP"]*(1/3) + archivo_2["Defense"]*(1/3)+archivo_2["Sp. Def"]*(1/3)
archivo_2["Poder de Defenza"] = round(archivo_2["Poder de Defenza"])


#Averiguamos el valor Z 
archivo_2["Z_HP"] =  (archivo_2["HP"] - archivo_2["HP"].mean()) / archivo_2["HP"].std()
archivo_2.head()


#Vemos los valores únicos
archivo_2["Type 1"].unique()

#los contamos
archivo_2['Type 1'].nunique()

#Vemos la frecuencia Absoluta de cada uno
archivo_2['Type 1'].value_counts()

#Realizamos un gráfico de torta y vemos la frecuencia relativa
archivo_2['Type 1'].value_counts().plot.pie(startangle=45,autopct='%.1f %%')


# Columnas Condicionales

#creamos una nueva variable a partir de otras
#generamos una columna que clasifique el tiempo de reacción en lenta,mediana,veloz,muy veloz

archivo_2["Speed"].unique()

archivo_2.loc[archivo_2["Speed"] <=50 , 'Reacción'] = "Lenta"

archivo_2.loc[(51<=archivo_2["Speed"]) & (archivo_2["Speed"] <=100) , 'Reacción'] = "Mediana"

archivo_2.loc[(101<=archivo_2["Speed"]) & (archivo_2["Speed"] <=150) , 'Reacción'] = "Veloz"

archivo_2.loc[archivo_2["Speed"]>=151 , 'Reacción'] = "Muy Veloz"


# Podemos aplicar funciones a las columnas

def pokemon_poder(poder):
    """Imprime los pokemon con un determinado poder seleccionado"""
    poder =  (archivo_2["Type 1"].isin([poder]))
    datos_selec=archivo_2.loc[ poder, : ]
         
    return print(datos_selec)


pokemon_poder("Fire")

pokemon_poder("Grass")

# Otras operaciones son:



print(archivo_2["Speed"].min()) # Minimo
print(archivo_2["Speed"].max()) # Maximo
print(archivo_2["Speed"].count()) # Cantidad
print(archivo_2["Speed"].idxmax()) # El Ìndice del valor máximo
print(archivo_2["Speed"].idxmin()) # El Ìndice del valor mínimo
print(archivo_2["Speed"].quantile([.25,.5,.75])) # Los quantiles
print(archivo_2["Speed"].skew()) # Asimetria
print(archivo_2["Speed"].kurtosis()) # Kurtosis

## Concadenar Dataframes

data_1 = pd.DataFrame({1: ['A11', 'A21', 'A31', 'A41'],
                        2: ['A12', 'A22', 'A32', 'A42'],
                        3: ['A13', 'A23', 'A33', 'A43'],
                        4: ['A14', 'A24', 'A34', 'A44']},
                        index=[1, 2, 3, 4])

data_2 = pd.DataFrame({1: ['A51', 'A61', 'A71', 'A81'],
                        2: ['A52', 'A62', 'A72', 'A82'],
                        3: ['A53', 'A63', 'A73', 'A83'],
                        4: ['A54', 'A64', 'A74', 'A84']},
                         index=[5, 6, 7, 8]) 

pd.concat([data_1,data_2]) # concatenamos los DataFrame

pd.concat([data_1,data_2], axis=1) #Por Default axis=0

# ejemplo función y concatenado 

def obtener_Z(df, columna):
    """Obtiene el valor Z de cada elemento de una columna determinada
    de un archivo seleccionado"""
    df2 = pd.DataFrame([])
    df2[f"Z_{columna}"] =  (df[columna] - df[columna].mean()) / df[columna].std()
    return df2

obtener_Z(archivo_2, "Attack")
obtener_Z(archivo_3, "Velocidad")

# Sacamos los valores Z para Attack 

Z_attack = obtener_Z(archivo_2, "Attack")
Z_velocidad=obtener_Z(archivo_2, "Speed")
archivo_6=pd.concat([Z_attack, Z_velocidad ], axis=1)

# Intervalos de Clase

#Para transformar las variables continuas en discretas,
#las ponemos en contenedores.


# Con Cut le indicamos cuanto contenedores queremos
archivo_5=pd.cut(archivo_3["Velocidad"], bins=15)

# qcut se Basa en quantiles 
archivo_3["Velocidad_IC"] = pd.qcut(archivo_3["Velocidad"],[0,0.25,0.5,0.75,1])
archivo_3["Velocidad_IC"]

## Dummy Variables

pd.get_dummies(data = archivo_2, columns=["Legendary"], prefix="Leg_Dummy", drop_first=True )

pd.get_dummies(data = archivo_2, columns=["HP"], drop_first=True )

pd.get_dummies(data = archivo_2, columns=["Type 1"], drop_first=True)

# Otras funciones relacionadas al Texto

archivo_2.reset_index() #Volver al Ìndice Orinigal

# Cambiar los nombres de Columna

archivo_2.rename(columns = {'Type 1':'Poder 1', "Type 2": "Poder 2", "HP": "Salud"}, inplace=True)


archivo_2.columns

archivo_2.columns = [x.lower() for x in archivo_2.columns]
archivo_3.columns=[x.upper()for x in archivo_3.columns]

archivo_2.columns.values[0] ="Poder tipo 1"
archivo_2.columns.values[1] ="Poder tipo 2"


# Exportar Archivos obtenidos:

#Exportando a CSV
archivo_2.to_csv('Pokemon.csv',index=False)
#Exportando a Excel
archivo_2.to_excel("Pokemon.xlsx", index=True)



# Armado de gráficos con Matplotlib

# Grafico de barras verticales

import matplotlib.pyplot as plt
 
## Declaramos valores para el eje x
eje_x = ['Matemática', 'Biología', 'Economía', 'Ingeniería']
 
## Declaramos valores para el eje y
eje_y = [75,83,108,120]
 
## Creamos Gráfica
plt.bar(eje_x, eje_y)
 
## Leyenda en el eje y
plt.ylabel('Cantidad de estudiantes')
 
## Leyenda en el eje x
plt.xlabel('Carreras')
 
## TÌtulo 
plt.title('Inscriptos a carreras')
 
## Mostramos el gráfico
plt.show()


## Grafica de barras horizontales

## Declaramos valores para el eje y, en este caso son categorias
eje_x = ['Programacion', 'Física', 'Matematicas', 'Química']
 
## Declaramos valores para el eje x, ahora son los valores
eje_y = [76,31,45,57]
 
## Creamos Gráfica 
plt.barh(eje_x, eje_y, color="green")
plt.ylabel('Cursos')
plt.xlabel('Cantidad de Aprobados')
plt.title('Estudiantes aprobados por curso')
plt.show()

## Gráfico de barras agrupadas

serie_1 = [1089, 1287, 842, 957, 1485]
serie_2 = [1126, 1453, 735, 1078, 1512]
 
 
numero_de_grupos = len(serie_1)
indice_barras = np.arange(numero_de_grupos)
ancho_barras =0.40
 
plt.bar(indice_barras, serie_1, width=ancho_barras, label='Hombres')
plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Mujeres')
plt.legend(loc='best')
## Se colocan los indicadores en el eje x
plt.xticks(indice_barras + ancho_barras, ('Norte', 'Este', 'Sur', 'Oeste','Centro'))
 
plt.ylabel('Numero de nacimientos')
plt.xlabel('Zona')
plt.title('Nacimientos por genero y Región')
 
plt.show()

## Grafica de Barras apiladas

grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4']
Medicamento_A = [286,450,304,808]
Medicamento_B= [325,732,370,200]
 
indice = np.arange(len(grupos))
 
## Se crean las primeras barras
plt.bar(indice, Medicamento_A, label='Medicamento A')
 
## Se crean las segundas barras y se apilan sobre las primeras
plt.bar(indice, Medicamento_B, label='Medicamento B',  bottom=Medicamento_A)
 
plt.xticks(indice, grupos)
plt.ylabel("Número de pacientes")
plt.xlabel("Grupos")
plt.title('Pacientes según tratamiento recibido')
plt.legend()
 
plt.show()

#Herramientas para Simulaciones

#Se puede generar y trabajar con distribuciones de probabilidad. 

## Distribución Normal

mu = 0 #definimos la media
sigma = 1 #definimos el desvío
#ahora,generamos 1000 números con media 0 y desvío 1
dist_norm = np.random.normal(mu, sigma, 1000)

#graficamos una normal 0,1 con 10000 valores simulados
sb.displot(np.random.normal(mu, sigma, 10000), kind = 'kde')
plt.show()


#iteramos para una lista de n cantidad de variables
n_muestras = [10, 1000, 10000]
mu = 0
sigma = 1

for n in n_muestras:
    
    norm_dist = np.random.normal(mu, sigma, n)
    print("Para un n de: {} Media: {} Varianza: {}".format(n, norm_dist.mean(), norm_dist.std()))
    
    sb.distplot(norm_dist, hist = False, kde = True,
                 kde_kws = {'linewidth': 2}, label = n)
    
plt.legend(prop={'size': 8}, title = 'Cantidad de muestras')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()

#Tomamos una lista con diferentes valores de mu y sigma
parametros = [(1,2.4),(4,1.5),(5,5)]
for mu, sigma in parametros:
    sb.distplot(np.random.normal(mu, sigma, 1000), hist = False, kde = True,
                 kde_kws = {'linewidth': 2}, label = (mu,sigma))
 

plt.legend(prop={'size': 8}, title = 'Par·metros')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()



## Distribución Chi Cuadrado
#Simulamos 1000 valores de una chi cuadrado para diferentes grados de libertad

for gl in [1,2,5,10]:
    sb.distplot(np.random.chisquare(gl,1000), hist = False, kde = True,
                 kde_kws = {'linewidth': 2}, label = gl)
    
plt.legend(prop={'size': 8}, title = 'Grados de libertad')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()

## Distribución Exponencial
#Simulamos una distribución exponencial para diferentes valores de beta

for beta in [1.5,2,5,10]:
    sb.distplot(np.random.exponential(beta,200), hist = False, kde = True,
                 kde_kws = {'linewidth': 2}, label = beta)
    
plt.legend(prop={'size': 8}, title = 'Beta')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()

# Análisis de Distribuciones 
# Tests de Media y Varianza

#Paso 1- Simulamos 2 poblaciones de 100000 valores cada una
poblacion_1 = np.random.normal(1.09, 2, 100000).tolist()
poblacion_2 = np.random.normal(1, 2, 100000).tolist()

#Paso 2- Importamos las librerías a utilizar
from scipy import stats
from random import sample

#Paso-3 generamos una submuestra de cada población aleatoria de 5000 valores cada una
submuestra_1 = sample(poblacion_1, 5000)
submuestra_2 = sample(poblacion_2, 5000)

#Paso-4 evaluamos las medias (H0=las medias son iguales;H1=las medias son distintas)
t = stats.ttest_ind(poblacion_1, poblacion_2, equal_var = False, nan_policy = 'omit', alternative = 'two-sided')

tt_stat, pvalue = t[0], t[1]

pvalue
#esto es sensible al tamaño de la muestra, por eso usamos las muestras grandes
#si pvalue<=alfa---rechazo H0;si pvalue>alfa No rechazo H0


#Armamos una función que evalua el test de medias

def test_medias(submuestra_1, submuestra_2, alpha, regla_2t, equal_var):
    
    tt = stats.ttest_ind(submuestra_1, submuestra_2, equal_var = equal_var, nan_policy='omit', alternative='two-sided')
    tt_stat, pvalue = tt[0], tt[1]
    
    if regla_2t:
        if tt_stat > 2:
            print("Las muestras no provienen de la misma distribución; RECHAZO H0")
        else:
            print("Las muestras provienen de la misma distribución, NO RECHAZO H0")

    else:
        if pvalue < alpha:
            print("Las muestras no provienen de la misma distribución")
        else:
            print("Las muestras provienen de la misma distribución")

test_medias(submuestra_1, submuestra_2, alpha=0.05, regla_2t=True, equal_var =True)

#iterando:

pob_1 = np.random.normal(1.09, 2, 100000).tolist()
pob_2 = np.random.normal(1, 2, 100000).tolist()

aux = [test_medias(sample(pob_1, n_muestras), sample(pob_2, n_muestras), alpha=0.05, regla_2t=True, equal_var =True) for n_muestras in range(100, len(pob_1)+1,10000)]

alpha = 0.05
n_muestras = 0
iters = 0

print('Iter | # samples')
print('----------------')

while True:
    n_muestras += 500
    iters += 1
    print(iters,'   |  ',n_muestras*10)
    
    sub_1 = sample(pob_1, n_muestras*10)
    sub_2 = sample(pob_2, n_muestras*10)
    
    tt = stats.ttest_ind(sub_1, sub_2, equal_var = True, nan_policy='omit', alternative='two-sided')
    tt_stat, pvalue = tt[0], tt[1]

    if pvalue < alpha:
        break

print(f'Se necesitaron {n_muestras*10} (iteraciones: {iters}) muestras para poder determinar con un alpha de 0.05 \
que las muestras NO provienen de las misma población.')