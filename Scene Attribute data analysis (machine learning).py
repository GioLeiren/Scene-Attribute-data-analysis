from math import sqrt, ceil, floor, trunc
T, N = input().split()
T, N = [int(T), int(N)]
listaT1atributos = []
listaT1 = []
lista = ['black-bison', 'elephant', 'white-horse', 'brown-horse', 'scarlet-ibis', 'black-ibis', 'white-ibis',
'blue-sky', 'overcast-sky', 'cloudy-sky', 'dusthaze-sky', 'rocky-mountain', 'snowy-mountain', 'birdseye-building',
'perspective-building', 'front-building',  'red-flower', 'purple-flower', 'pink-flower', 'sand', 'tree', 'green-field',
'snowy-field', 'yellow-field', 'road', 'tower', 'blue-ocean', 'green-cliff', 'black-cliff', 'waterfall']
listaT2 = []
listaT4 = []
listaT4atributos = []
listaT5 = []
listaT5atributos = []
listaT5resultado = []

def impressao_csv(n):
    cont1 = 0
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2),int(a3),int(a4)]
        listaT1atributos.append(n1)
        listaT1atributos.append(n2)
        listaT1atributos.append(a1)
        listaT1atributos.append(a2)
        listaT1atributos.append(a3)
        listaT1atributos.append(a4)
        listaT1.append(listaT1atributos[:])
        listaT1atributos.clear()
    for l in listaT1:
        for c in l:
            if cont1 < 5:
                print(f'{l[cont1]},', end='')
            else:
                print(l[5])
            cont1 += 1
        cont1 = 0



def percentual_atributos_objetos(n):
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        listaT2.append(n2)
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]
    for e in lista:
        if e in listaT2:
            porcentagem = (listaT2.count(e) * 100) / N
            print(f'{e}: {porcentagem:.1f}')
        else:
            print(f'{e}: 0.0')

def media_coordenadas_tamanhos(n):
    cont3x = cont3y = larg = alt = 0
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]
        cont3x = cont3x + (a1 + a3)
        cont3y = cont3y + (a2 + a4)
        larg = larg + (a3 - a1)
        alt = alt + (a4 - a2)
    if cont3x / (2*N) - 0.5 >= trunc(cont3x / (2*N)):
        print(f'{ceil(cont3x / (2 * N))}', end=' ')
    elif cont3x / (2*N) - 0.5 < trunc(cont3x / (2*N)):
        print(f'{floor(cont3x / (2 * N))}', end=' ')

    if cont3y / (2*N) - 0.5 >= trunc(cont3y / (2*N)):
        print(f'{ceil(cont3y / (2 * N))}', end=' ')
    elif cont3y / (2*N) - 0.5 < trunc(cont3y / (2*N)):
        print(f'{floor(cont3y / (2 * N))}', end=' ')

    if larg / N - 0.5 >= trunc(larg / N):
        print(f'{ceil(larg / N)}', end=' ')
    elif larg / N - 0.5 < trunc(larg / N):
        print(f'{floor(larg / N)}', end=' ')

    if alt / N - 0.5 >= trunc(alt / N):
        print(f'{ceil(alt / N)}')
    elif alt / N - 0.5 < trunc(alt / N):
        print(f'{floor(alt / N)}')

def maiores_menores_posicoes(n):
    cont3x = cont3y = cont3xy = larg = alt = area = maior = menor = 0
    maior_area = menor_area = p = esquerdamaior = esquerdamenor = maiscentral = 0
    for i in range(0, N):
        cont3x = cont3y = cont3xy = larg = alt = area = 0
        u = input()
        n1 = str(input())
        listaT4atributos.append(n1)
        n2 = str(input())
        listaT4atributos.append(n2)
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]

        cont3x = (a1 + a3) / 2
        deslocado = cont3x - 128

        cont3y = (a2 + a4) / 2
        central = sqrt((cont3x - 128)**2 + (cont3y - 128)**2)

        cont3xy = (cont3x + cont3y) / 2
        listaT4atributos.append(cont3y)

        larg = (a3 - a1)
        alt = (a4 - a2)
        area = larg * alt

        listaT4atributos.append(area)
        listaT4atributos.append(central)
        listaT4atributos.append(deslocado)
        listaT4.append(listaT4atributos[:])
        listaT4atributos.clear()
    while True:
        if p == 0:
            maior = listaT4[p][2]
            menor = listaT4[p][2]
            maior_area = listaT4[p][3]
            menor_area = listaT4[p][3]
            maiscentral = listaT4[p][4]
            esquerdamaior = listaT4[p][5]
            esquerdamenor = listaT4[p][5]
        else:
            if listaT4[p][2] > maior:
                maior = listaT4[p][2]
            if listaT4[p][2] < menor:
                menor = listaT4[p][2]
            if listaT4[p][3] > maior_area:
                maior_area = listaT4[p][3]
            if listaT4[p][3] < menor_area:
                menor_area = listaT4[p][3]
            if listaT4[p][4] < maiscentral:
                maiscentral = listaT4[p][4]
            if listaT4[p][5] < esquerdamaior:
                esquerdamaior = listaT4[p][5]
            if listaT4[p][5] > esquerdamenor:
                esquerdamenor = listaT4[p][5]
        p += 1
        if p == len(listaT4):
            break

    print(f'mais central:', end='')
    for a in listaT4:
        if a[4] == maiscentral:
            print(f' {a[1]},{a[0]}')
    print(f'mais a esquerda:', end='')
    for a in listaT4:
        if a[5] == esquerdamaior:
            print(f' {a[1]},{a[0]}')
    print(f'mais a direita:', end='')
    for a in listaT4:
        if a[5] == esquerdamenor:
            print(f' {a[1]},{a[0]}')
    print(f'mais acima:', end='')
    for a in listaT4:
        if a[2] == menor:
            print(f' {a[1]},{a[0]}')
    print(f'mais abaixo:', end='')
    for a in listaT4:
        if a[2] == maior:
            print(f' {a[1]},{a[0]}')
    print(f'maior area:', end='')
    for a in listaT4:
        if a[3] == maior_area:
            print(f' {a[1]},{a[0]}')
    print(f'menor area:', end='')
    for a in listaT4:
        if a[3] == menor_area:
            print(f' {a[1]},{a[0]}')

def busca_booleana_imagens(n):
    contT5 = -1
    contT5v2 = 0
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        if n1 not in listaT5atributos:
            if contT5 >= 0:
                if n1 != listaT5atributos[0]:
                    listaT5.append(listaT5atributos[:])
                    listaT5atributos.clear()
                    listaT5atributos.append(n1)
                    contT5 += 1
            else:
                listaT5atributos.append(n1)
                contT5 += 1

        listaT5atributos.append(n2)
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2),int(a3),int(a4)]
    listaT5.append(listaT5atributos)
    for e in listaT5:
        for i in e:
            if e.count('tree') > 0:
                if e.count('green-field') == 0 and e.count('snowy-field') == 0 and e.count('yellow-field') == 0:
                    if e[0] not in listaT5resultado:
                        listaT5resultado.append(e[0])
                    contT5v2 += 1
    if contT5v2 == 0:
        print('nada')
    else:
        for c in listaT5resultado:
            print(c)



if T == 1:
    impressao_csv(N)

elif T == 2:
    percentual_atributos_objetos(N)

elif T == 3:
    media_coordenadas_tamanhos(N)

elif T == 4:
    maiores_menores_posicoes(N)

elif T == 5:
    busca_booleana_imagens(N)
