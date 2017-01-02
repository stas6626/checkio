'''
В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.
'''

def checkio(data):
    solu=str()
    if (data//1000>0):
        solu='M'*(data//1000)
        data=data%1000
        
    if (data>899):
        solu=solu+"CM"
        data=data-900
        
    if (data//500>0):
        solu=solu+"D"
        data=data-500
        
    if (data>399):
        solu=solu+"CD"
        data=data-400
        
    if (data//100>0):
        solu=solu+'C'*(data//100)
        data=data-(data//100)*100
    
    if (data>89):
        solu=solu+"XC"
        data=data-90
        
    if (data//50>0):
        solu=solu+'L'
        data=data-50
    
    if (data>39):
        solu=solu+"XL"
        data=data-40
        
    if (data//10>0):
        solu=solu+"X"*(data//10)
        data=data%10
        
    if (data==9):
        solu=solu+"IX"
        data=data-9
        
    if (data>4):
        solu=solu+"V"
        data=data-5
        
    if (data==4):
        solu=solu+"IV"
        data=data-4
        
    if (data>0):
        solu=solu+"I"*data
        data=0
    
    
    return solu
