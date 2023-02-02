#AUTORA: ANAID JIMENEZ MOREANO
#ALGORITMO DE YUVAL


import pandas as pd
import hashlib
import numpy as np

#compara 2 documentos de hash y localiza las colisiones
def compara(hash1,hash2):
    df1 = pd.read_csv(hash1,  dtype="string", names=['hash'], engine='python')
    df2 = pd.read_csv(hash2,  dtype="string", names=['hash'], engine='python')
    print(df1)
    print(df2)
    dfc = []

    #b=np.where(df1['hash'] == df2['hash'])
    dfc.append(pd.merge(df1, df2, how='inner', left_on='hash', right_on='hash'))
    #print(dfc)

    print("Colisiones:\n")

    for h in range(len(dfc)):
        print(dfc[h])
        with open('documento2.txt', 'a') as f:
            f.writelines(dfc[h])



#transformacion binaria
def bina(decimal, n):
    binario = ""
    if decimal <= 0:
        for j in range(n):
            binario = "0" + binario
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario

    if len(list(binario)) < n:
        t = n - len(list(binario))
        for k in range(t):
            binario = "0" + binario
    return binario

#combina los bloques segun la secuencia binaria y genera un documento con el texto para hashear
#YUBAL
def combina(df1,df2):

    a=pow(2,len(df1))
    print("combinaciones: "+str(a))
    combinaciones=[]
    for i in range(a):
        t=bina(i,len(df2))
        combinaciones.append(t)
        #print(t)
    #print(combinaciones)

    #se declara 2 dtfrms
    arr=[]
    arr2=[]

    #print(list(combinacioes[2]))
    #para cada combinacion se debe realizar el procedimiento
    for y in range(len(combinaciones)):
        mensajex =''
        arr.append(list(combinaciones[y]))
        #print(arr)

        for u in range(len(df1)):
            #print(arr[y])
            if (arr[y][u] =='0'):
                #print(arr[y][u])
                mensajex=mensajex+" "+str(df1.loc[u,'frase'])
                #print(mensajex)
            else:
                #print(arr[y][u])
                mensajex=mensajex+" "+str(df2.loc[u, 'frase'])
                #print(mensajex)

        arr2.append(mensajex)
        #print(arr2)
        #AQUI SE PUEDE HALLAR LA FUNCION INVERSA IMPRIMIENDO LA ITERACION Y SABER QUE MENSAJE COMPARO
    return arr2



#hashea y escribe el hash de 20 bits en el documento
def hash(df,documento):
    ''' separar dataframe por espacio y generar su hash'''

    #print(df)
    texto = []

    for i in range(len(df)):
        #frasee=str(df.loc[i,'frase'])
        texto.append(hashlib.md5(df[i].encode()).hexdigest())
        #print(texto[i][0:5])

        with open(documento, 'a') as f:
            f.writelines(texto[i][0:5]+"\n")


if __name__ == '__main__':


    print("uso: Borrar el contenido de documento2,\nhashes1 y hashes2 antes de correr el programa\n "
          "esto trabaja a 20 bits con n lineas \nque se le asige a los"
          " mensajes en los archivos de texto de nombre mensajex")

    mensaje='mensaje.txt'
    mensaje2='mensaje2.txt'

    mensaje3='mensaje3.txt'
    mensaje4='mensaje4.txt'

    hash1='hashes1.txt'
    hash2='hashes2.txt'

    documento2='documento2.txt'

    df1 = pd.read_csv(mensaje, sep="/n", dtype="string", names=['frase'], engine ='python')
    df2 = pd.read_csv(mensaje2, sep="/n", dtype="string", names=['frase'], engine ='python')

    df3 = pd.read_csv(mensaje3, sep="/n", dtype="string", names=['frase'], engine='python')
    df4 = pd.read_csv(mensaje4, sep="/n", dtype="string", names=['frase'], engine='python')

    n=len(df1)

    #MEZCLA TEXTO Y
    com=combina(df1,df2)
    com2 = combina(df3, df4)

    #SACA LOS HASHES
    hash(com,hash1)
    hash(com2, hash2)



    #COMPARA LOS HASHES Y HALLA COLISIONES
    compara(hash1,hash2)





