import math

# Base class
class RegularShape:
    def accept_data(self):
        pass

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass

# Derived class for Circle
class Circle(RegularShape):
    def accept_data(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Derived class for Square
class Square(RegularShape):
    def accept_data(self):
        self.side = float(input("Enter the side of the square: "))

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

# Derived class for Equilateral Triangle
class EquilateralTriangle(RegularShape):
    def accept_data(self):
        self.side = float(input("Enter the side of the equilateral triangle: "))

    def calculate_perimeter(self):
        return 3 * self.side

    def calculate_area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

# Derived class for Regular Polygon (generic)
class RegularPolygon(RegularShape):
    def accept_data(self):
        self.num_sides = int(input("Enter number of sides: "))
        self.side_length = float(input("Enter the length of each side: "))

    def calculate_perimeter(self):
        return self.num_sides * self.side_length

    def calculate_area(self):
        apothem = self.side_length / (2 * math.tan(math.pi / self.num_sides))
        return 0.5 * self.calculate_perimeter() * apothem

# Example usage:
def main():
    print("Select a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Equilateral Triangle")
    print("4. Regular Polygon")

    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        shape = Circle()
    elif choice == 2:
        shape = Square()
    elif choice == 3:
        shape = EquilateralTriangle()
    elif choice == 4:
        shape = RegularPolygon()
    else:
        print("Invalid choice")
        return

    shape.accept_data()
    print("Perimeter / Circumference:", round(shape.calculate_perimeter(), 2))
    print("Area:", round(shape.calculate_area(), 2))

if __name__ == "__main__":
    main()
