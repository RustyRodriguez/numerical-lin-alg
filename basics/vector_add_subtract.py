
def add(x, y):
    assert len(x) == len(y)

    return [item1 + item2 for item1, item2 in zip(x, y)]

def subtract(x, y):
    assert len(x) == len(y)

    return [item1 - item2 for item1, item2 in zip(x, y)]

if __name__ == '__main__':
    a = [5, 3, 7]
    b = [1, 2, 4]

    print(add(a, b))
    print(subtract(a, b))