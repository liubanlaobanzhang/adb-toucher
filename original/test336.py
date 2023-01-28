import requests

api = 'https://api.github.com/repos/liubanlaobanzhang/adb-toucher'
all_info = requests.get(api).json()
cur_update = all_info['pushed_at']
print('cur_update')
if cur_update != 1:
    exit()