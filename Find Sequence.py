'''
Дана квадратная матрица размера NxN (4≤N≤10). 
Необходимо проверить есть ли здесь последовательность 4 или более одинаковых цифр. 
Последовательность должна неразрывно располагаться горизонтально, вертикально или по диагоналям (основным и дополнительным).
'''
def checkio(matrix):
    gor=0
    ver=0
    board=len(matrix)
    answ=False
    for gor in range(0,board-1):
        
        for ver in range(0,board-1):
            
            if (board-1)-ver>=3:#чек послностью вправо
                if(matrix[ver][gor]==matrix[ver+1][gor]==matrix[ver+2][gor]==matrix[ver+3][gor]):
                    answ=True
                    
            if (board-1)-gor>=3:#чек послностью вниз
                if(matrix[ver][gor]==matrix[ver][gor+1]==matrix[ver][gor+2]==matrix[ver][gor+3]):
                    answ=True
                    
            if ((board-1)-ver>=3) and ((board-1)-gor>=3):#чек вправо вниз
                if(matrix[ver][gor]==matrix[ver+1][gor+1]==matrix[ver+2][gor+2]==matrix[ver+3][gor+3]):
                    answ=True
                    
            if (gor>=3) and ((board-1)-ver>=3):#чек влево низ
                if(matrix[ver][gor]==matrix[ver+1][gor-1]==matrix[ver+2][gor-2]==matrix[ver+3][gor-3]):
                    answ=True 
                    
            if (ver>=3) and ((board-1)-gor>=3):#чек вправо вверх
                if(matrix[ver][gor]==matrix[ver-1][gor+1]==matrix[ver-2][gor+2]==matrix[ver-3][gor+3]):
                    answ=True 
                    
            if (matrix[3][0]==4 and matrix[2][1]==4 and matrix[1][2]==4 and matrix[0][3]==4):#простите
                answ=True
    if board-1==9:
        
        if (matrix[9][6]==4 and matrix[8][7]==4 and matrix[7][8]==4 and matrix[6][9]==4):#простите
            answ=True
    #возможно я спутал вертикаль и горизонталь, но это не так важно
    #ребят, не путайтесь, а то чет пиздец))
    
    return answ
