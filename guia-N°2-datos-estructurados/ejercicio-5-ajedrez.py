#simulador de ajedrez
tablero = {}

#Colocar piezas blancas y negras
piezasB = ['TB','CB','AB','QB','KB','AB','CB','TB']
piezasN = ['TN','CN','AN','QN','KN','AN','CN','TN']
cols = list("abcdefgh")

#Blancas
for i in range(8):
    tablero[cols[i] + '1'] = piezasB[i]
    tablero[cols[i] + '2'] = 'PB'
#lineas vacias 3–6
for fila in ['3','4','5','6']:
    for c in cols:
        tablero[c + fila] = None
#Negras
for i in range(8):
    tablero[cols[i] + '7'] = 'PN'
    tablero[cols[i] + '8'] = piezasN[i]

#Mapear símbolos
sim = {'TB':'R','CB':'N','AB':'B','QB':'Q','KB':'K','PB':'P',
       'TN':'r','CN':'n','AN':'b','QN':'q','KN':'k','PN':'p'}

#Lista para capturas
capt = []

while True:
    #Dibujar tablero
    print("  " + " ".join(cols))
    for f in map(str, range(8,0,-1)):
        linea = []
        for c in cols:
            p = tablero[c+f]
            linea.append(sim[p] if p else '.')
        print(f + " " + " ".join(linea))
    print()
    if capt:
        print("Capturadas:", " ".join(sim[p] for p in capt))
    break