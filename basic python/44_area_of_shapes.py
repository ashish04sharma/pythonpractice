# Calculate the area of common shapes

PI = 3.14159


def circle_area(radius):
    return PI * radius ** 2


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


print("Circle with radius 7:", round(circle_area(7), 2))
print("Rectangle 4 x 6:", rectangle_area(4, 6))
print("Triangle base 10 height 5:", triangle_area(10, 5))
