#  Ответ:
#  Алгоритм Timsort, используемый в функции sorted() и методе .sort,
#  встроенных в python. Алгоритм имеет линейно-лагарифмическую временную
#  сложность O(n log n) в лучших, худших и средних случаях, так как его
#  его работа основана на сортировке слиянием, но частично использует
#  сортировку вставками, что позволяет ему работать быстрее на коротких
#  и частично отсортированных массивах и иногда достигать скорости O(n)
#  в лучших случаях.
#  Также, в случае с sorted() .sort, имеет хорошую оптимизацию.
#  _____________________________________________________________________________
#  В коде ниже представлены:
#  - функции marge_sort() и marge(), реализующие алгоритм рекурсивной
#  сортировки слиянием;
#  - функция random_array(), генерирующая список случайных не уникальных
#  целых чисел с устанавливаемым объемом;
#  - функция sort_time_test() реализует проверку времени быстродействия
#  получаемых алгоритмов сортировки на списках случайных целых чисел
#  объемом 1000, 10000 и 100000 элементов. Использована для сравнения
#  скорости работы встроенной функции sorted() и merge_sort

import time
import random


def merge_sort(array):
    len_array = len(array)
    if len_array <= 1:
        return array
    left_list = merge_sort(array[0: len_array // 2])
    right_list = merge_sort(array[len_array // 2: len_array])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result = []
    ind_l, ind_r = 0, 0
    len_left, len_right = len(left_list), len(right_list)
    while ind_l < len_left and ind_r < len_right:
        if left_list[ind_l] <= right_list[ind_r]:
            result.append(left_list[ind_l])
            ind_l += 1
        else:
            result.append(right_list[ind_r])
            ind_r += 1
    return result + left_list[ind_l:] + right_list[ind_r:]


def random_array(count):
    return [random.randint(-100, 100) for _ in range(count)]


def sort_time_test(sort, name='sorting algorithm'):

    start_time = time.perf_counter()
    small_arr = random_array(1000)
    sort(small_arr)
    small_arr_time = time.perf_counter() - start_time

    start_time = time.time()
    medium_arr = random_array(10000)
    sort(medium_arr)
    medium_arr_time = time.time() - start_time

    start_time = time.time()
    big_arr = random_array(100000)
    sort(big_arr)
    big_arr_time = time.time() - start_time

    print(f'{name}:\n'
          f'time-test: 1000 elements - {small_arr_time}\n'
          f'time-test: 10000 elements - {medium_arr_time}\n'
          f'time-test: 100000 elements - {big_arr_time}')


sort_time_test(sorted, 'Timsort')
sort_time_test(merge_sort, 'Margesort')
