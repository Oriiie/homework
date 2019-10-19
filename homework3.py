'''tree = [['-', 1, '-', '-', '-', '-'],
        [1, '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-','-'],
        ['-', '-', '-', '-', '-', '-']]'''

def tree_check():
    if (tree == [['-','-','-','-','-','-'],
               ['-','-','-','-','-','-'],
               ['-','-','-','-','-','-'],
               ['-','-','-','-','-','-'],
               ['-','-','-','-','-','-'],
               ['-','-','-','-','-','-']]):
        return 0

tree = [['-', 5, '-', '-', 2, '-'],
     [5, '-', 10, 8, 9, '-'],
     ['-', 10, '-', '-', '-', '-'],
     ['-', 8, '-', '-', 6, 4],
     [2, 9, '-', 6, '-',3],
     ['-', '-', '-', 4, 3, '-']]

min_amount_const = 0

min_amount = 0
i_keeper = 0
j_keeper = 0

shortest_tree = 0

allowed_subarrays = [0]

allowed_columns = []

for i in range(len(tree)):    
    allowed_columns.append(i)

pathes_indexes = []

minimal_weights = []


for i in range(len(tree)):                     #задаем максимально возможное 
    for j in range(len(tree)):                 #число для корректной сортировки -
        if (type(tree[i][j]) is int):          #сумма значений ребер этого графа,
            min_amount_const += tree[i][j]     #очевидно, будeт больше, чем
            min_amount += tree[i][j]           #какое-либо из них по отдельности
                                            

for k in range(len(tree)):
    for i in range(len(tree)):
        
        if(len(allowed_subarrays) == (len(tree))):#проверяет, все ли строки были
                break                           #зайдествованы хотя бы 1 раз
        if (tree_check() == 0):   #нужно для работы с графами, где <6 элементов
            break
        if i in allowed_subarrays:         #проверяет присутствие элементов
            for j in range(len(tree)):
                if j in allowed_columns:
                    if (type(tree[i][j]) is int):
                        
                        if (tree[i][j]<min_amount): #выбирает наименьший
                            min_amount = tree[i][j] #из доступных
                            i_keeper = i
                            j_keeper = j
                            
            allowed_subarrays.append(j_keeper)#добавляет строку в список доступа
            allowed_columns.remove(j_keeper) #убирает столбец из списка доступа

            #этот блок делает запись о том, какое ребро принимало участие,
            #считает сумму минимального дерева и меняет сам граф:
            #хотя граф и не выводится программой отдельно, если вывести его
            #через цикл for после всех итераций,
            #можно заметить, что он весь состоит из '-'
            pathes_indexes.append(str(i_keeper+1)+'-'+str(j_keeper+1))
            shortest_tree += min_amount
            minimal_weights.append(str(min_amount))
            min_amount = min_amount_const
            tree[j_keeper][i_keeper] = '-'
            tree[i_keeper][j_keeper] = '-'
            for i in range(len(tree)):
                tree[i][j_keeper] = '-'
                
print('Итого: для постройки минимального остовного дерева, \n' +
      'нам необходимы следующие рёбра: ')
for i in range (len(pathes_indexes)):
    print(pathes_indexes[i] + ' с весом ' +  minimal_weights[i])
print('А итоговая длина всего остовного дерева = '+ str(shortest_tree))

