from point import Point
__author__ = 'pzqa'


l1 = list(map(lambda i: Point(i, i*i), range(-5, 6)))

l2 = list(filter(lambda el: el.x % 2 == 0, l1))

print(l1)
print(l2)
