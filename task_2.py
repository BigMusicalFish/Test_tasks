#  Ответ:
#  Класс listFIFO реализует буфер FIFO на основе списка (list).
#  Плюсы:
#  - так как список в python реализован как динамический массив,поиск элемента
#  по индексу и удаление элемента из конца списка осуществляются за константное
#  время О(1);
#  Минусы:
#  - удаление алементов из начала списка осуществляется за линейное время О(n),
#  так как все последующие элементы должны быть сдвинуты;
#  _____________________________________________________________________________
#  Класс DequeFIFO реализует буфер FIFO на основе дека collections.deque.
#  Плюсы:
#  - так как дек реализован как двухсторонняя очередь, исзвлечение и добавление
#  элементов осуществляяется за линейное время О(1);
#  Минусы:
#  - поиск элементов по индексу осуществляется за линейное время О(n), так как
#  необходим перебор элементов;
#  _____________________________________________________________________________
#  В обоих классах реализована фиксация емкости буфера и логика обработки
#  переполнения для возможности управления памятью
#  _____________________________________________________________________________
#  Функции methods_time() и test_fifo() реализуют проверку быстродействия
#  методов append(), pop() и get_by_index() классов listFIFO и DequeFIFO
#  _____________________________________________________________________________

import time
import random
from collections import deque


class listFIFO:
    '''Буфер FIFO с фиксировнной емкостью на основе списка'''

    def __init__(self, size):
        self.size = size  # максимальная емкость буфера
        self.buffer = []  # пустой буфер на основе списка

    def append(self, item):
        '''Добавляет элемент в конец буфера'''
        if len(self.buffer) >= self.size:  # проверяет на переполнение буфера
            raise OverflowError('Full buffer')  # исключение, если буфер полный
        self.buffer.append(item)  # добавляет элемента в конец буфера

    def pop(self):
        '''Извлекает элемент из начала буфера'''
        if not self.buffer:  # проверяет буфер на наличие элементов
            raise IndexError('Empty buffer')  # исключение, если буфер пуст
        return self.buffer.pop(0)  # извлекает элемент из начала буфера

    def get_by_index(self, index):
        '''Возвращает элемент из буфера по индексу'''
        if index < 0 or index >= len(self.buffer):  # валидность индекса
            raise IndexError('Index out of range')  # исключение, если индекс не валиден
        return self.buffer[index]  # возвращаем элемент по индексу

    def len_size(self):
        '''Возвращает текущее количество элементов в буфере'''
        return len(self.buffer)


class DequeFIFO(listFIFO):
    '''Буфер FIFO с фиксировнной емкостью на основе дека'''

    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)  # пустой буфер на основе дека

    def pop(self):
        '''Извлекает элемент из начала буфера'''
        if not self.buffer:
            raise IndexError("Empty buffer")
        return self.buffer.popleft()


def methods_time(buffer, size, name='buffer FIFO'):

    # время добавления элементов в конец буфера
    start_time = time.time()
    for i in range(size):
        buffer.append(i)
    append_time = time.time() - start_time

    # время удаления элементов из начала буфера
    start_time = time.time()
    for _ in range(size):
        buffer.pop()
    pop_time = time.time() - start_time

    # время поиска элемента буфера по случайному индексу
    start_time = time.perf_counter()
    for i in range(size):
        buffer.append(i)
    for _ in range(size):
        index = random.randint(0, size - 1)
        buffer.get_by_index(index)
    get_index = time.perf_counter() - start_time

    print(f'{name}:\n'
          f'append time, s - {append_time}\n'
          f'pop time, s - {pop_time}\n'
          f'get by index time, s - {get_index}')


# запуск тестовой функции
def test_fifo(size):
    list_fifo = listFIFO(size)
    deque_fifo = DequeFIFO(size)

    methods_time(list_fifo, size, 'listFIFO')
    methods_time(deque_fifo, size, 'DequeFIFO')


size = 100000
test_fifo(size)
