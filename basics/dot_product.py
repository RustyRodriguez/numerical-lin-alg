
def dot_product(x, y):
    assert len(x) == len(y)

    return sum(item1 * item2 for item1, item2 in zip(x, y))

if __name__ == '__main__':
    a = [1, 2, 4]
    b = [3, 6, 8]

    print(dot_product(a, b))