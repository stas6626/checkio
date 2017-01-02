'''
Даны две анаграммы, как слова разделенные дефисом. 
Ваша задача переставить буквы первого слово во второе.
Для этого у вас есть два стека и однобуквенный буфер.
Первый стек - это где изначально размещено первое слово, второй - куда разместить его анаграмму.
Слово размещается в стеке буква за буквой. 
Первая буква слова размещена на "дне" стека и далее "поверх" до последней буквы.
Вам нужно найти кратчайшую последовательность действий для того чтобы переместить и переставить первое слово в анаграмму.
Первый стек помечен, как 1, второй - 2 и буфер - 0.
Действие описывается, как строка с двумя цифрами - откуда и куда.
Для примера: "12" означает переместить букву с вершины первого стека во второй.
Результат должен быть представлен, строка где действия разделены запятыми.
'''

def checkio(data):
    first=[]#Наше первое слово
    second=[]#Пустой массив куда будем скидывать
    buffer=[]#Тот самый один элемент
    result=[]#Что мы должны получить
    actions=''#что мы делали
    
    for i in range(0,len(data)//2-1):#Бьем на два массива
        first.append(data[i])
        
    for i in range(len(data)//2+1,len(data)):
        result.append(data[i])

           
    for i in range(0,len(data)//2-1):
        while (len(buffer)==0):#Ищем первую букву которая нам интересна, дабы перекинуть ее в стек
            if first[-1]==result[i]:# все что нам не подходит в секонд
                buffer.append(first.pop())
                actions+='10,'
            else:
                second.append(first.pop())
                actions+='12,'
        while ((len(second)!=i)):# как нашли, нужно очистить секонд перекинув обратно в исходный
            if len(second)==0:
                break
            first.append(second.pop())
            actions+='21,'
#        while (second[i]!=result[i]):
#            first.append(second.pop())
#            actions+='21 '
            
        second.append(buffer.pop())
        actions+='02,'
    
    ans=''
    for i in range(0,len(actions)-1):
        ans+=actions[i]    
    return ans

    '''
    for i in result:# А теперь обман века
        smeg=len(first)-first.index(i)-1 #сколько раз выкидывать а потом закидывать
        del first[first.index(i)]
        actions+=smeg*'12,'
        actions+='10,'
        actions+=smeg*'21,'
        actions+='02,'
        
    ans=''
    for i in range(0,len(actions)-1):
        ans+=actions[i]    
    return ans
    '''
    
