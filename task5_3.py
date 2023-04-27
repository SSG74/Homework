
numnum = int(input('Введите число: '))
rever_num = 0
def recursive_reverse(num):
    global rever_num

    if num == 0:
        return num
    else:
        digit = num % 10
        rever_num = (rever_num * 10) + digit
        recursive_reverse(num // 10)
    return rever_num

rever_num = recursive_reverse(numnum)
#print(f'"Обратное" число = {rever_num}')

def len_int(num):
    #len_int = 0
    if num == 0:
        return 1
    len_ = 0
    while num:
        num //= 10
        len_ += 1
    return (len_)

a = len_int(numnum)
b = len_int(rever_num)
if a != b:
    print(f'"обратное" число: {rever_num:0{a}}')
else:
    print(f'"Обратное" число = {rever_num}')