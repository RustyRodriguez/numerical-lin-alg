import math


def two_norm(x):
    return math.sqrt(sum(item * item for item in x))

if __name__ == '__main__':
    print(two_norm([3, 4]))