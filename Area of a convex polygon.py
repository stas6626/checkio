'''
Дан выпуклый многоугольник на координатной плоскости.
Данный многоугольник представлен, как массив координат вершин.
Вершины соединены последовательно друг с другом и последняя в массиве соединена с первой.
Многоугольник имеет N вершин. Вам нужно написать программу для расчета площади многоугольника.
Результат должен быть с точностью до одного знака или ±0.1.
'''
import numpy
def checkio(data):
    data.append(data[0])
    count=0
    for i in range(0,len(data)-1):
        count+=(data[i][0]*data[i+1][1])-(data[i+1][0]*data[i][1])
        
    
    ans=0.5*(abs(round(count,1)))
    return ans