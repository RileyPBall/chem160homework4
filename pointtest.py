from point import *
p1=point(3, [1., 2., 3.])
print("point 1=",p1)
p2=point(3, [6., 7., 8.])
print("point 2=",p2)
p1.add(p2)
print("The square magnitude of p1+p2=", p1.sqmag())

