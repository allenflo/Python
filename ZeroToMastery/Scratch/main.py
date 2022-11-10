a = 1

def parent():
    a=10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)


