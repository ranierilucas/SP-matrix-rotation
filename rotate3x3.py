# sentido horário, matriz 3x3
# l2 --> c0; c0 --> l0'; l0 --> c2; c2 --> l2'; l1 --> c1 ; c1--> l1';
def imprimir(arrayOfArray):
    for array in arrayOfArray:
        print(array)
    print('\n')


def turn90degree(arrayOfarray):
    result = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(len(result)):
        result[0][i] = arrayOfarray[2-i][0]
        result[1][i] = arrayOfarray[2-i][1]
        result[2][i] = arrayOfarray[2-i][2]
    return result


arrayOfarray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(5):
    imprimir(arrayOfarray)
    arrayOfarray = turn90degree(arrayOfarray)
