#1
class Vector() :
    def __init__(self, s):
        self.x, self.y, self.z = map(float, s.split(" , "))
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __plus__(self, other):
        if isinstance(other , Vector):
            return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
        elif isinstance(other , int) or isinstance(other , float):
            return Vector(self.x + other , self.y + other , self.z + other)
    def __minus__(self, other):
        if isinstance(other , Vector):
            return Vector(self.x - other.x , self.y - other.y , self.z - other.z)
        elif isinstance(other , int) or isinstance(other , float):
            return Vector(self.x - other , self.y - other , self.z - other)

    def __scpr__(self, other):
        if isinstance(other , Vector):
            return Vector(self.x * other.x , self.y * other.y , self.z * other.z)
        elif isinstance(other , int) or isinstance(other , float):
            return Vector(self.x * other , self.y * other , self.z * other)
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
#1.1
n = int(input())
V = []
m = 0
for i in range(n):
    V = V + [vector(input(),input(),input())]

for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            a = ((V[i1].x - V[i2].x)**2 + (V[i1].y - V[i2].y)**2 + (V[i1].z - V[i2].z)**2)**0.5
            b = ((V[i1].x - V[i3].x)**2 + (V[i1].y - V[i3].y)**2 + (V[i1].z - V[i3].z)**2)**0.5
            c = ((V[i3].x - V[i2].x)**2 + (V[i3].y - V[i2].y)**2 + (V[i3].z - V[i2].z)**2)**0.5
            p = 0.5*(a + b + c)
            S = (p*(p-a)*(p-b)*(p-c))**0.5
            if S > m: m = S

print(m)
#1.2
    def area(a, b, c):
    ab = abs(b - a)
    bc = abs(c - b)
    ca = abs(a - c)
    p = (ab + bc + ca) / 2
    return (p * (p - ab) * (p - bc) * (p - ca))**0.5

points = [
    Vector("1, 2, 3"),
    Vector("4, 5, 6"),
    Vector("7, 8, 9"),
    Vector("10, 11, 12"),
    Vector("13, 14, 15")
]

center = Vector("0, 0, 0")
for point in points:
    center += point
center *= 1 / len(points)
print(f"Координаты центра масс: {center}")

max_area = 0
max_triangle = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        for k in range(j + 1, len(points)):
            a = area(points[i], points[j], points[k])
            if a > max_area:
                max_area = a
                max_triangle = (points[i], points[j], points[k])
print(f"Три точки, образующие треугольник с наибольшей площадью: {max_triangle[0]}, {max_triangle[1]}, {max_triangle[2]}")
print(f"Площадь этого треугольника: {max_area}")
