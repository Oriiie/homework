testlist_bubblesort = [40,723, 781, 610, 440, 819, 728,
                        280, 998, 744, 40, 303, 708, 279, 910]

testlist_decision = [560, 769, 349, 97, 881, 108, 827,
                     131, 301, 952, 255, 787, 625, 549, 5]

testlist_insertion = [984, 738, 859, 281, 548, 399, 894,
                      53,145,260,787,140, 472, 566, 752]



def bubbles_sort(list):
    for i in range(0, len(list)-1, 1):
        for j in range(0, len(list)-1, 1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def decisions_sort(list):
    for i in range(0, len(list)-1,1):
        minimal_number = i
        for j in range(i,len(list)-1,1):
            if list[j] < list[minimal_number]:
                minimal_number = j
        list[i], list[minimal_number] = list[minimal_number], list[i]
    return list

def insertions_sort(list):
    for i in range(0, len(list)-1,1):
        if list[i]>list[i+1]:
            catchvariable = list.pop(i+1)
            for j in range (0, len(list)-2,1):
                if list[j] > catchvariable:
                    list.insert(j,catchvariable)
                    break
    return list
    
print('Первый массив до сортировки: \n', testlist_bubblesort)
print('Первый массив после сортировки: \n', bubbles_sort(testlist_bubblesort))
print('Второй массив до сортировки: \n',testlist_decision)
print('Второй массив после сортировки: \n', decisions_sort(testlist_decision))
print('Третий массив до сортировки: \n', testlist_insertion)
print('Третий массив после сортировки: \n', insertions_sort(testlist_insertion))