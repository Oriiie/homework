def primas_sort():

    tree = [['-', 10, '-', 7, 5, '-','-','-'],
            [10, '-', 6, '-', '-', 9,'-','-'],
            ['-', 6, '-', '-', '-', 4,'-',1],
            [7, '-', '-', '-', 8, '-',9,'-'],
            [5, '-', '-', 8, '-', '-',3,1],
            ['-', 9, 4, '-', '-', '-','-',4],
            ['-', '-', '-', 9, 3, '-','-',2],
            ['-', '-', 1, '-', 1, 4,2,'-']]
    
    i_keeper = 0
    j_keeper = 0

    sum_of_tree = 1111
    const_sum_of_tree = 1111

    x_axes_array = [0]

    y_axes_array = [0,1,2,3,4,5,6,7]

    pathes = []

    one_rib_weight = []

    minimal_weight = 0

    for k in range (len(tree)-1):
        for i in range (len(tree)):
            if i in x_axes_array:
                for j in range(len(tree)):
                    if j in y_axes_array:
                        if type(tree[i][j]) == int:
                            if(tree[i][j]<sum_of_tree):
                                sum_of_tree = tree[i][j]
                                i_keeper = i
                                j_keeper = j
        x_axes_array.append(j_keeper)
        y_axes_array.remove(j_keeper)
        minimal_weight = minimal_weight + sum_of_tree
        one_rib_weight.append(sum_of_tree)
        tree[j_keeper][i_keeper] = '-'
        sum_of_tree = const_sum_of_tree
        pathes.append(str(i_keeper+1)+'-'+str(j_keeper+1))
    

    print("Итого, имеем:")
    for i in range (len(pathes)):
        print("             ребро ",pathes[i], " с весом ", one_rib_weight[i])
    print("Общий вес минимального остовного дерева = ", minimal_weight)



def crascalls_sort():
    allowed_ribs = [['1-2',10], ['1-4',7], ['1-5',5],  ['2-3',6],
                ['2-6',9], ['3-6',4], ['3-8',1], ['4-5',8],
                ['4-7',9], ['5-7',3], ['5-8',1], ['6-8',4], ['7-8',2]]



    def sortsort():
        for k in range(len(check_second)):
            for j in range (0,len(allowed_ribs),1):
                if (check_second[k]==allowed_ribs[j][0]):
                    clear_array.append(j)
                

    final_ribs = []

    check_first = []

    check_second = []

    clear_array = []

    tree_weigth = []

    min_weigth = 0
    
    for i in range (len(allowed_ribs)):
        for j in range (len(allowed_ribs)-1):
            if allowed_ribs[j][1] > allowed_ribs[j+1][1]:
                allowed_ribs[j], allowed_ribs[j+1] = \
                                    allowed_ribs[j+1],allowed_ribs[j]

    for i in range (len(allowed_ribs)):
        i = 0
        if (allowed_ribs == []):
            break
        if(len(final_ribs)==7):
                break
        if (int(allowed_ribs[i][0][0]) not in check_first):
            check_first.append(int(allowed_ribs[i][0][0]))
        if (int(allowed_ribs[i][0][2]) not in check_first):
            check_first.append(int(allowed_ribs[i][0][2]))
        final_ribs.append(allowed_ribs.pop(i))
        check_first.sort()
        for j in range (len(check_first)):
            for k in range (len(check_first)):
                if(str(check_first[j])+'-'+str(check_first[k]) \
                   not in check_second):
                    check_second.append(str(check_first[j])+\
                                        '-'+str(check_first[k]))
        sortsort()
        for k in range (len(clear_array)):
            if(len(final_ribs)==7):
                break
            allowed_ribs.pop(clear_array[k])
            if (allowed_ribs == []):
                break
        clear_array.clear()
        
    print("Итого, имеем: ")
    for i in range (len(final_ribs)):
        print("             pебро ", final_ribs[i][0], \
              " с весом ", final_ribs[i][1])
    for i in range (len(final_ribs)):
        min_weigth = min_weigth + final_ribs[i][1]
    print("Общий вес минимального остовного дерева = ", min_weigth)
    
            
print("Поиск остовного дерева методом Прима: ")
primas_sort()
print("\n\nПоиск остовного дерева методом Краскалла: ")
crascalls_sort()


