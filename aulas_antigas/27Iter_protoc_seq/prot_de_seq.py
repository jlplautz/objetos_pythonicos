class Trem:

    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, item):
        indice = item if item >= 0 else self.num_vagoes + item
        if 0 <= indice < self.num_vagoes:
            # indice 2 -> vagão #3
            return 'vagao #%s' % (indice + 1)
        raise IndexError('vagão inexistente %s' % item)


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)

    print('\n')

    for vagao in reversed(Trem(4)):
        print(vagao)
