def hashearcodigo(codigo):
    def stringtonat(c):
        nat_num = 0
        length = len(c)
        base = 2

        for i in range(length):
            nat_num += ord(c[i]) * (base ** (length - 1 - i))
        return nat_num

    return stringtonat(codigo)

print(hashearcodigo('AN1235465'))