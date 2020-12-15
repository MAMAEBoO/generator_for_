from selenium import *
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *


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
    while col != 100:
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        length = 8
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        res0 = str(f'https://pastebin.com/{link}'+'\n')
        '''
        Переход on link at value res1 and work with html
        '''
        driver.get(res0)
        pstb = driver.find_elements_by_xpath(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]')
        '''
        Eceptions errors
        '''
        try:
            if (pstb != None) or (pstb == 'Not Found (#404)'):
                col = str(col)
                print(col+' '+'-'+' '+res0)
                col = int(col)
                col = col+1
                driver.close()
            else:
                col = str(col)
                print(col+' '+'+'+' '+res0)
                col = int(col)
                col = col+1
                driver.close()
        except NoSuchElementException or StaleElementReferenceException or InvalidSessionIdException:
            if (pstb != None) or (pstb == 'Not Found (#404)'):
                col = str(col)
                print(col+' '+'-'+' '+res0)
                col = int(col)
                col = col+1
                driver.close()
            else:
                col = str(col)
                print(col+' '+'+'+' '+res0)
                col = int(col)
                col = col+1
                driver.close()


        '''
        Сделать возможность работы Selenium в скрытом режиме
        + до тех пор, пока не будет положительного результата
        '''
            
##        /html/body/div[1]/div[2]/div[1]/div[2]/div[1] Not found 404 on Pastebin
##        col = str(col)
##        print(col+' '+res1)
##        col = int(col)
##        col = col+1
else:
    print('Service not found')
    col = int(col)
    col = col+1

