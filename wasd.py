import pygame 
import time
from random import randint

pygame.init() 
window_width = 1200
window_hight = 700
win = pygame.display.set_mode((window_width, window_hight)) 
pygame.display.set_caption("Moving rectangle") 


class Rectangle:
	density = 0.01
	window_width = 1200
	window_hight = 700
	loss = 0.002
	def __init__(self, x, y, width, height, speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed
		self.weight = width * height * self.density

	def top(self):
		return self.y + self.height
	
	def bottom(self):
		return self.y

	def right(self):
		return self.x + self.width

	def left(self):
		return self.x

	def drow_rect(self):
		return (self.left(), self.y - self.height, self.width, self.height)

	def check_borders(self):
		if self.x + self.width >= self.window_width and self.speed > 0:
			self.speed *= -1
			self.speed -= self.speed * self.loss
		elif self.x <= 0 and self.speed < 0:
			self.speed *= -1
			self.speed -= self.speed * self.loss
	

def check_collision(a, b):
	if a.x < b.x:
		if a.right() >= b.x:
			return True
		else:
			return False
	else:
		if b.right() >= a.x:
			return True
		else:
			return False

run = True
loss = 0.002

rect1 = Rectangle(60, 200, 50, 50, randint(-5, 5))
rect2 = Rectangle(60, 200, 55, 55, randint(-5, 5))
rect3 = Rectangle(60, 200, 50, 50, randint(-5, 5))
rect4 = Rectangle(60, 200, 50, 50, randint(-5, 5))
rect5 = Rectangle(60, 200, 50, 50, randint(-5, 5))
rect6 = Rectangle(60, 200, 100, 100, randint(-5, 5))

# выстраивам их в порядке возрастания координат
# если они будут меняться местами, то менять их местами в данном массиве
rectangles = [rect1, rect2, rect3, rect4, rect5, rect6]

while run: 
	pygame.time.delay(5) 

	for event in pygame.event.get(): 

		if event.type == pygame.QUIT: 
			run = False
	keys = pygame.key.get_pressed() 

	for i in range(len(rectangles) - 1):
		if check_collision(rectangles[i], rectangles[i + 1]):
			speed_1_new = (2 * rectangles[i + 1].weight * rectangles[i + 1].speed + \
				(rectangles[i].weight - rectangles[i + 1].weight) * rectangles[i].speed) / (rectangles[i].weight + rectangles[i + 1].weight)
			speed_2_new = (2 * rectangles[i].weight * rectangles[i].speed + \
				(rectangles[i + 1].weight - rectangles[i].weight) * rectangles[i + 1].speed) / (rectangles[i].weight + rectangles[i + 1].weight)
			rectangles[i].speed = speed_1_new * (1 - loss)
			rectangles[i + 1].speed = speed_2_new * (1 - loss)
			rectangles[i + 1].x += 1
			rectangles[i].x -= 1
	for rectan in rectangles:
		rectan.x += rectan.speed

	for rectan in rectangles:
		rectan.check_borders()

	win.fill((0, 0, 0)) 
	for rectan in rectangles:
		pygame.draw.rect(win, (255, 0, 0), rectan.drow_rect())

	pygame.display.update() 

pygame.quit() 
