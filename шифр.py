def password(number):
    pass_ = ''

    for i in range(1 , number):
        for j in (i + 1 , number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)

    return pass_

print('Введите пароль :')
print(password(int(input())))
