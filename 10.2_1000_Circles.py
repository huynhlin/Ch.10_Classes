'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''
import arcade
import random
arcade.open_window(500, 300, "1000 Circles")
arcade.start_render()


class Circle:
    def __init__(self):
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 300)
        self.radius = 10
        self.color = [0, 0, 0]
        for y in range(0, 3):
            self.color[y] = random.randint(1, 255)

    def draw_circle(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


for x in range(1, 10000):
    canvas = Circle()
    canvas.draw_circle()

arcade.finish_render()
arcade.run()
