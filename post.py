import selenium
import random

print('Generator of links for Yandex.Disk and Pastebin.com')

##def ext(ex, self):
##    ex = str(input('If you want quit is program, then enter Y, otherwise N:'))
##    if ex == 'Y':
##        exit()
##    else:
##        pass
service = str(input('Select service (pastebin | yandex.disk):'+'\n'))
col = 0
if service == 'yandex.disk':
    while col != 100:
        #haven't +-/*!&$#?=w@<>
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        #length = int(input(col +'Length links?'+ '\n'))
        length = 14
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        res = str(f'https://yadi.sk/d/{link}'+'\n'+f'https://yadi.sk/i/{link}'+'\n')
        '''
        Переход по ссылке в переменной res и работа с html
        '''
        
        col = str(col)
        print(col+' '+res)
        col = int(col)
        col = col+1
elif service == 'pastebin':
    while col != 100:
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        length = 8
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        res1 = str(f'https://pastebin.com/{link}'+'\n')
        '''
        Переход по ссылке в переменной res1 и работа с html
        '''
        
        col = str(col)
        print(col+' '+res1)
        col = int(col)
        col = col+1
else:
    print('Service not found')
    col = int(col)
    col = col+1

