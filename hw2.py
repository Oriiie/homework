from random import randrange
import time
from datetime import datetime
import random

my_list = [7,8,1,3,8,6,8,8,0,9,9,0,5,5,1]
print('Изначальный список = ', my_list)

def merger_method(some_list):
    fixmas = []
    size_of_slice = 2
    for k in range (len(some_list)):
        
        for i in range (0,len(some_list),size_of_slice):
            
            sliceN = some_list[i:i+size_of_slice]
            
            for l in range (len(sliceN)):
                for o in range (len(sliceN)-1):
                    if sliceN[o]>sliceN[o+1]:
                        sliceN[o],sliceN[o+1]=sliceN[o+1],sliceN[o]
                        
            fixmas = fixmas + sliceN
            
        size_of_slice = size_of_slice * 2
        my_list = fixmas
        fixmas = []
        if (size_of_slice>len(some_list)+1):
            break
    print('Отсортированный с помощью метода слияния список :' ,
          '\n' , my_list)

def heaphelp(some_list, heap_size, index_of_root):
    largest = index_of_root
    left_child = (2 * index_of_root) + 1
    right_child = (2 * index_of_root) + 2
    if left_child < heap_size and some_list[left_child] > some_list[largest]:
        largest = left_child
    if right_child < heap_size and some_list[right_child] > some_list[largest]:
        largest = right_child
    if largest != index_of_root:
        some_list[index_of_root], some_list[largest] = some_list[largest], some_list[index_of_root]
        heaphelp(some_list, heap_size, largest)


def heap_sort(some_list):
    n = len(some_list)
    for i in range(n, -1, -1):
        heaphelp(some_list, n, i)
    for i in range(n - 1, 0, -1):
        some_list[i], some_list[0] = some_list[0], some_list[i]
        heaphelp(some_list, i, 0)
    return some_list


def quick_sort(some_list):
    
   if len(some_list) <= 1:
       return some_list
   else:
       middlepos = random.choice(some_list)
       
   lesser_list = [n for n in some_list if n < middlepos]
 
   e_list = [middlepos] * some_list.count(middlepos)
   
   bigger_list = [n for n in some_list if n > middlepos]
   
   return quick_sort(lesser_list) + e_list + quick_sort(bigger_list)

#сортировка слиянием и время сортировки
start_time = datetime.now()

merger_method(my_list)

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

#сортировка методом кучи/пирамидальным и время сортировки

start_time = datetime.now()

print('Отсортированный с помощью сортировки кучей список: \n', heap_sort(my_list))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

#сортировка быстрым методом и время сортировки

start_time = datetime.now()

print("Отсортированный с помощью быстрой сортировки спиок: ",
      '\n', quick_sort(my_list))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))


