def gerador_num_naturais():
    i = 0
    while True:
        yield i
        i += 1


naturais = gerador_num_naturais()


for i in naturais:
    print(i)
