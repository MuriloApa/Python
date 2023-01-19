x, y, z = map(float, input().split())
if ( x + y > z and x + z > y and y + z > x):
    print("Perimetro = {:.1f}".format(x +y + z))
else:
    print("Area = {:.1f}".format((x+y)*z/2))
