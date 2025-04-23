import math

# Base class
class Solid:
    def accept_data(self):
        pass

    def surface_area(self):
        pass

    def volume(self):
        pass

# Derived class for Cube
class Cube(Solid):
    def accept_data(self):
        self.side = float(input("Enter the side of the cube: "))

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

# Derived class for Sphere
class Sphere(Solid):
    def accept_data(self):
        self.radius = float(input("Enter the radius of the sphere: "))

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

# Derived class for Cylinder
class Cylinder(Solid):
    def accept_data(self):
        self.radius = float(input("Enter the radius of the cylinder: "))
        self.height = float(input("Enter the height of the cylinder: "))

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

# Example usage
def main():
    print("Choose a solid:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")

    choice = int(input("Enter your choice (1-3): "))
    
    if choice == 1:
        solid = Cube()
    elif choice == 2:
        solid = Sphere()
    elif choice == 3:
        solid = Cylinder()
    else:
        print("Invalid choice.")
        return

    solid.accept_data()
    print("Surface Area:", round(solid.surface_area(), 2))
    print("Volume:", round(solid.volume(), 2))

if __name__ == "__main__":
    main()
