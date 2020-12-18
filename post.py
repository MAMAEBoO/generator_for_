##!C:\Users\User\AppData\Local\Programs\Python\Python38.exe 
# Python 3.8.6
##!\usr\bin\env

from selenium import *
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidElementStateException as IESE
from setuptools import *

Author = 'SlayerLeon'

print('Generator of links for Yandex.Disk and Pastebin.com')

'''
Для скрытия работы Selenium в браузере и CommandPrompt Selenium
На данный момент скрывает только работу в браузере
'''
##driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe')
options = Options()
options.add_argument("headless")
options.headless = True
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe', options=options)

'''
Для возможности непрерывной работы  : Желаете ли Вы продолжить работу или нет?
'''
##
##if (query == 'N') or (query == 'not') or (query == 'n') or (query == 'Not') or (query == 'no') or (query == 'No') or (query == 'Нет') or (query == 'нет') or (query == 'не') or (query == 'Не') or (query == 'Да') or (query == 'да') or (query == 'Y') or (query == 'y') or (query == 'Yes') or (query == 'yes'):
##    while (query == 'N') or (query == 'not') or (query == 'n') or (query == 'Not') or (query == 'no') or (query == 'No') or (query == 'Нет') or (query == 'нет') or (query == 'не') or (query == 'Не'):
global query
def main0():
    query = input(str('If you want close is program, then enter Y/y, otherwise N/n? \n'))
    service = str(input('Select service (pastebin | yandex.disk):'+'\n'))
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
            if (res1 != True) or (res2 != True):
                random.shuffle(chars)
                link = ''.join([random.choice(chars) for x in range(length)])
                res1 = str(f'https://yadi.sk/d/{link}')
                res2 = str(f'https://yadi.sk/i/{link}')
                def yc_pluse():
                    global loc
                    loc = str(loc)
                    print(loc+' '+'+'+' '+res1+'\n')
                    print(loc+' '+'+'+' '+res2+'\n')
                    loc = int(loc)
                    loc = loc+1

                def yc_minus():
                    global loc
                    loc = str(loc)
                    print(loc+' '+'-'+' '+res1+'\n')
                    print(loc+' '+'-'+' '+res2+'\n')
                    loc = int(loc)
                    loc = loc+1

                driver.get(res1)
                driver.get(res2)
                try:
                    yc0 = driver.find_elements_by_class_name('content__centered')
                    if (yc0 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc1 = driver.find_elements(By.XPATH, '//div/div/div/div/div[2]/div[2]')
                    if (yc1 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc2 = driver.find_elements_by_xpath('//div/div/div/div/div[2]/div[2]')
                    if (yc2 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc3 = driver.find_elements(By.CLASS_NAME, 'content__centered')
                    if (yc3 == True):
                        yc_pluse()
                    else:
                        yc_minus()
            else:
                print('ERROR : 00/0_NoSuchElement')

    elif service == 'pastebin':
        col = 0
        n = int(input('Please, enter quantity of links:'))
        while col != int(n):
            chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
            length = 8
            random.shuffle(chars)
            link = ''.join([random.choice(chars) for x in range(length)])
            res0 = str(f'https://pastebin.com/{link}')

##          res1 = str(f'https://pastebin.com/u/{link}'+'\n')
##          Generate link on users
            '''Transition on link at value res1 and work with html'''
            if (res0 != True):
                random.shuffle(chars)
                link = ''.join([random.choice(chars) for x in range(length)])
                res0 = str(f'https://pastebin.com/{link}')
                def pstb_pluse():
                    global col
                    col = str(col)
                    print(col+' '+'+'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
                def pstb_minus():
                    global col
                    col = str(col)
                    print(col+' '+'-'+' '+res0+'\n')
                    col = int(col)
                    col = col+1

                driver.get(res0)
                try:
                    pstb0 = driver.find_elements_by_class_name('username')
                    if (pstb0 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                except NoSuchElementException:
                    pstb1 = driver.find_elements(By.XPATH, '//div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]')
                    if (pstb1 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                except NoSuchElementException:
                    pstb2 = driver.find_elements_by_class_name('info-top')
                    if (pstb2 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                else:
                    print('ERROR : 00/1_NoSuchElement')
                finally:
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
        print('ERROR : 01_ServiceNotFound')
    
global query
while query != (Y or y or n or N):
    print('ERROR : 02_UnknownValue')
    query = input(str('If you want close is program, then enter Y/y, otherwise N/n? \n'))
else:
    if query == (N or n):
        main0()
    elif query == (Y or y):
        exit()
    else:
        print('ERROR : 03_UnknownErrorPleaseResetProgramm')
# else:
    # print('ERROR : 02_UnknownValue')
    # exit()

##        query = input(str('If you want close is program, then enter Y, otherwise N? \n'))
##
##        print('Please, enter other value')
##        query = input(str('If you want close is program, then enter Y, otherwise N? \n'))
##    else:
##        exit()
