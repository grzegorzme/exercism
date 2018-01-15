import time
import datetime

if __name__ == '__main__':
    print('Starting heartbeat...')
    while True:
        print('[{}] I\'m alive!'.format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S.%f')))
        time.sleep(10)
