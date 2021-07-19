def int_to_rus(num):
    dict = { 0 : 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
          6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять', 10 : 'десять',
          11 : 'одинадцать', 12 : 'двенадцать', 13 : 'тринадцать', 14 : 'четырнадцать',
          15 : 'пятнадцать', 16 : 'шестнадцать', 17 : 'семнадцать', 18 : 'восемнадцать',
          19 : 'девятнадцать', 20 : 'двадцать',
          30 : 'тридцать', 40 : 'сорок', 50 : 'пятьдесят', 60 : 'шестьдесят',
          70 : 'семьдесят', 80 : 'восемьдесят', 90 : 'девяносто', } 
    #Словарь для основных числительных
    
    _list_1 = [21, 31, 41, 51, 61, 71, 81, 91, 
        101, 121,131, 141, 151, 161, 171, 181, 191,
        201, 221, 231, 241, 251, 261, 271, 281, 291,
        301, 321, 331, 341, 351, 361, 371, 381, 391,
        401, 421, 431, 441, 451, 461, 471, 481, 491,
        501, 521, 531, 541, 551, 561, 571, 581, 591,
        601, 621, 631, 641, 651, 661, 671, 681, 691,
        701, 721, 731, 741, 751, 761, 771, 781, 791,
        801, 821, 831, 841, 851, 861, 871, 881, 891,
        901,  921, 931, 941, 951, 961, 971, 981, 991,]
        
    _list_2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54,62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 
         102, 103, 104,122, 122, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154,162, 163, 164, 172, 173, 174, 182, 183, 184, 192, 193, 194,
         202, 203, 204,222, 222, 224, 232, 233, 234, 242, 243, 244, 252, 253, 254,262, 263, 264, 272, 273, 274, 282, 283, 284, 292, 293, 294,
         302, 303, 304,322, 322, 324, 332, 333, 334, 342, 343, 344, 352, 353, 354,362, 363, 364, 372, 373, 374, 382, 383, 384, 392, 393, 394,
         402, 403, 404,422, 422, 424, 432, 433, 434, 442, 443, 444, 452, 453, 454,462, 463, 464, 472, 473, 474, 482, 483, 484, 492, 493,494,
         502, 503, 504,522, 522, 524, 532, 533, 534, 542, 543, 544, 552, 553, 554,562, 563, 564, 572, 573, 574, 582, 583, 584, 592, 593,594,
         602, 603, 604,622, 622, 624, 632, 633, 634, 642, 643, 644, 652, 653, 654,662, 663, 664, 672, 673, 674, 682, 683,684, 692, 693,694,
         702, 703, 704,722, 722, 724, 732, 733, 734, 742, 743, 744, 752, 753, 754,762,763, 764, 772, 773, 774, 782, 783, 784, 792, 793,794,
         802, 803, 804,822, 822, 824, 832, 833, 834, 842, 843, 844, 852, 853, 854,862, 863, 864, 872, 873, 874, 882, 883, 884, 892, 893,894,
         902, 903, 904,922, 922, 924, 932, 933, 934, 942, 943, 944, 952, 953, 954,962, 963, 964, 972, 973, 974, 982, 983, 984, 992, 993,994,]
    
    # Есть несколько вариантов рефакторинга такого списка, но они код при этом становится Гораздо менее понятным
    
    assert(0 <= num)
    
#вывод чисел от 1 до 19"""
    if (num < 20):
        return dict[num]


#вывод чисел от 20 до 99"""
    if (num < 100):
        if num % 10 == 0: return dict[num]
        else: return dict[num // 10 * 10] + ' ' + dict[num % 10]


#условие с кейсами на рекурсию к предыдущим условиям
#конкретно это выводит сотни - от 1 до 9

    if (num < 1000):
        if num == 100: return ' сто' 
        elif 100<num<200: return ' сто ' + int_to_rus(num % 100)
        elif  num == 200:  return  ' двести'
        elif  200<num<300:  return  ' двести ' + int_to_rus(num % 100)
        elif  num == 300:  return  ' триста'
        elif  300<num<400:  return  ' триста ' + int_to_rus(num % 100)
        elif  num == 400:  return  ' четыреста'
        elif  400<num<500:  return  ' четыреста ' + int_to_rus(num % 100)
        else: return dict[num // 100] + 'сот ' + int_to_rus(num % 100)


#условие с кейсами на рекурсию к предыдущим условиям
#конкретно это выводит тысячи - от 1 до 999999
 
    if (num <= 999999):
        
    #вспомагательные переменные для отработки списков в начале модуля
        _x = num%1000
        _y = num//1000
        
        if _x != 0 and _y in _list_1:
           a = int_to_rus(num // 1000) + ' тысяча, ' + int_to_rus(num % 1000)
           a = str(a)
           a = a.replace('один', 'одна')
           return a
        elif _x==0  and  _y in _list_1: return int_to_rus(num // 1000) + ' тысяча'
        elif num == 1000 : return  'одна тысяча'
        elif _y in _list_2 and _x != 0 : return int_to_rus(num // 1000) + ' тысячи, ' + int_to_rus(num % 1000)
        elif _y in _list_2: return int_to_rus(num // 1000) + ' тысячи'
        elif 4<_y<21 and  _x != 0: return int_to_rus(num // 1000) + ' тысяч, '  + int_to_rus(num % 1000)
        elif 4<_y<21 : return int_to_rus(num // 1000) + ' тысяч'
        else: 
            if _x != 0: 
                return int_to_rus(num // 1000) + ' тысяч, ' + int_to_rus(num % 1000)
            else:  return int_to_rus(num // 1000) + ' тысяч'


#тут всё тоже самое для миллионов"""  
    if (num > 999999):
        
        _a = num%1000000
        _b = num//1000000
        
        if _a != 0 and _b in _list_1: return int_to_rus(num // 1000000) + ' миллион, ' + int_to_rus(num % 1000000)
        elif _a==0  and  _b in _list_1: return int_to_rus(num // 1000000) + ' миллион'
        elif num == 1000000 : return int_to_rus(num // 1000000) + ' миллион'
        elif _b in _list_2 and _a != 0 : return int_to_rus(num // 1000000) + ' миллиона, ' + int_to_rus(num % 1000000)
        elif _b in _list_2: return int_to_rus(num // 1000000) + ' миллиона'
        elif 4<_b<21 and  _a != 0: return int_to_rus(num // 1000000) + ' миллионов, '  + int_to_rus(num % 1000000)
        elif 4<_b<21 : return int_to_rus(num // 1000000) + ' миллионов'
        else: 
            if _a != 0: 
                return int_to_rus(num // 1000000) + ' миллионов, ' + int_to_rus(num % 1000000)
            else:  return int_to_rus(num // 1000000) + ' миллионов'
# Числа удобнее оформить ввиде ссылок. Тут сделал для лучшего понимания
# Далее по той же схеме можно продолжить до бесконечности (миллиарды, триллионы и тд.)

    raise AssertionError('num is too large: %s' % str(num))
    

number = int(input('Введите целое число от нуля ДО! миллиарда для преобазования в числительное: '))
print(int_to_rus(number))

# Для проверки достаточно просто запустить
