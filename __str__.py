#Create class
class Point:
    def __init__(self,x=0 ,y=0):
        self.x = x
        self.y = y

    # Method to print points in coordinate format
    def __str__(self):
        return f"(x={self.x}, y={self.y})"

#Create object
p1 = Point(2,3)
print(p1)
