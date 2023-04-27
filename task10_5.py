# Задание 5.
#
# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.
#
# Подсказки:
# --- используйте модуль chardet, иначе задание не засчитается!!!


import subprocess
import chardet

site_one = 'yandex.ru'
site_two = 'youtube.com'

for site in site_one, site_two:
    ARGS = ['ping', site]
    SITE_PING = subprocess.Popen(ARGS, stdout = subprocess.PIPE)
    print(SITE_PING.stdout)
    for line in SITE_PING.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding = res['encoding']))
