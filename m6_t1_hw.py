"""
import random

# Каждый раз один и тот же набор
random.seed(5)

Используя функцию random.randint(1, 1000), 
сформировать список из 20 элементов и сохранить в файл.
После этого, считать числа из файла и посчитать сумму чисел > 99.
"""
import random

# Каждый раз один и тот же набор
random.seed(555)
sum = 0
file = open('C:\\Users\\Ilya_\\Desktop\\example_1.txt', 'w', encoding='utf-8')
for _ in range(20):
    file.write(str(random.randint(1, 1000)) + '\n')
file.close()

with open('C:\\Users\\Ilya_\\Desktop\\example_1.txt', encoding='utf-8') as file_2: # with as только для чтения?
    for _ in file_2:
        if int(_) > 99:
            sum += int(_) 
print(sum)    
        
        
        
        
        
        
        
        
        
        