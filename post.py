from selenium import *
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.common.exceptions import InvalidElementStateException as IESE



print('Generator of links for Yandex.Disk and Pastebin.com')
service = str(input('Select service (pastebin | yandex.disk):'+'\n'))

#driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe')

'''
Для скрытия работы Selenium в браузере и CommandPrompt Selenium
На данный момент скрывает только работу в браузере
'''                                                                              
driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe')
##options = Options()
##options.add_argument("headless")
##options.headless = True
##options.add_argument('--disable-gpu')
##driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe', options=options)

'''
Для возможности непрерывной работы  : Желаете ли Вы продолжить работу или нет?
'''
##def ext(ex, self):
##    ex = str(input('If you want quit is program, then enter Y, otherwise N:'))
##    if ex == 'Y':
##        exit()
##    else:
##        pass


if service == 'yandex.disk':
    loc = 0
    m = int(input('Please, enter quantity of links:'))
    while loc != m:
        #haven't +-/*!&$#?=w@<>
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        #length = int(input(col +'Length links?'+ '\n'))
        length = 14
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        res1 = str(f'https://yadi.sk/d/{link}')
        res2 = str(f'https://yadi.sk/i/{link}')
        '''
        DEBAGGING
        '''
        if (res1 != True) or (res2 != True):
            random.shuffle(chars)
            link = ''.join([random.choice(chars) for x in range(length)])
            res1 = str(f'https://yadi.sk/d/{link}')
            res2 = str(f'https://yadi.sk/i/{link}')
            driver.get(res1, res2)
            try:
                yc0 = driver.find_elements_by_class_name(' ')
                if (yc0 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res1+'\n')
                    print(col+' '+'+'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res1+'\n')
                    print(col+' '+'-'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
            except NoSuchElementException:
                yc1 = driver.find_elements(By.XPATH, ' ')
                if (yc1 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res1+'\n')
                    print(col+' '+'+'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res1+'\n')
                    print(col+' '+'-'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
            except NoSuchElementException:
                yc2 = driver.find_elements_by_class_name(' ')
                if (yc2 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res1+'\n')
                    print(col+' '+'+'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res1+'\n')
                    print(col+' '+'-'+' '+res2+'\n')
                    col = int(col)
                    col = col+1
        else:
            print('Error 01')       
##        '''
##        Переход по ссылке в переменной res и работа с html
##        '''
##        driver.get(res)
##        yc = driver.find_elements_by_xpath(' ')
##        if (yc != None) or (yc == 'Not Found (#404)'):
##            #pass
##            col = str(col)
##            print(col+' '+'-'+' '+res1)
##            col = int(col)
##            col = col+1
##            driver.close()
##        else:
##            col = str(col)
##            print(col+' '+'+'+' '+res1)
##            col = int(col)
##            col = col+1
##            driver.close()
elif service == 'pastebin':
    col = 0
    n = int(input('Please, enter quantity of links:'))
    while col != int(n):
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        length = 8
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        res0 = str(f'https://pastebin.com/{link}')
##      res1 = str(f'https://pastebin.com/u/{link}'+'\n')
##      Generate link on users
        '''Transition on link at value res1 and work with html'''
        if (res0 != True):
            random.shuffle(chars)
            link = ''.join([random.choice(chars) for x in range(length)])
            res0 = str(f'https://pastebin.com/{link}')
            driver.get(res0)
            try:
                pstb0 = driver.find_elements_by_class_name('username')
                if (pstb0 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
            except NoSuchElementException:
                pstb1 = driver.find_elements(By.XPATH, '//div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]')
                if (pstb1 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
            except NoSuchElementException:
                pstb2 = driver.find_elements_by_class_name('info-top')
                if (pstb2 == True):
                    col = str(col)
                    print(col+' '+'+'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
                else:
                    col = str(col)
                    print(col+' '+'-'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
        else:
            pass
            '''
            WRITE SELECTED LINKS IN RESULT
            '''
            '''Eceptions errors'''
            '''
            Сделать возможность работы Selenium в скрытом режиме
            + до тех пор, пока не будет положительного результата
            '''
else:
    print('Service not found')


