import requests
import time
from time_counter import readable_time


def monitoring_bch(time_to_hf=1600000000):
    """ Мониторинг происходит пока не наступит заданное время для hardfork """
    while time_to_hf > time.time():
        time.sleep(2)
        """ Запрос данных с сервиса блокчейн """
        r = requests.get('https://api.blockchain.info/stats')
        r2 = requests.get('https://api.blockchain.info/pools?timespan=5days')
        r3 = requests.get('https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json')

        """ Вывод полученных данных и времени до hardfork """
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

""" Код сработает при запуске файла напрямую """
if __name__ == '__main__':
    try:
        time_to_hf = int(input('Enter the HardFork date here: '))
    except ValueError:
        time_to_hf = 1600000000
    monitoring_bch(time_to_hf)
