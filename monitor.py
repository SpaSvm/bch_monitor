import requests
import time
from time_counter import readable_time

time_to_hf = int(input('Enter the HardFork date here: '))

""" Мониторинг происходит пока не наступит заданное время для развилки """
while time_to_hf > time.time():
    time.sleep(2)
    """ Запрашиваем данные с сервиса блокчейн """
    r = requests.get('https://api.blockchain.info/stats')
    r2 = requests.get('https://api.blockchain.info/pools?timespan=5days')
    r3 = requests.get('https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json')

    """ Выводим полученные данные и время до развилки """
    print(
        'Response 1: {}'.format(r.json()['timestamp']),
        'Response 2: {}'.format(r2.json()),
        'Response 3: {}'.format(r3.json()['status']),
        '----------------------',
        'Real time: {}'.format(time.time()),
        readable_time(time_to_hf),
        sep='\n'
    )

print('\nHardFork time has come')
