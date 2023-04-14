import pygame
import time
import random

pygame.init()

#Variables
window_x = 500
window_y = 500
score = 0
global level
level = 1
snake_speed = 10

#Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

#Setting up game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

#Setting up FPS
fps = pygame.time.Clock()

#Defining snake default position and direction
snake_position = [105, 45]
snake_body = [[105, 45],[90, 45],[75, 45],[60, 45]]
direction = 'RIGHT'
change_to = direction

#Fruit position
fruit_position = [random.randrange(1, (window_x//15)) * 15,random.randrange(1, (window_y//15)) * 15]
fruit_spawn = True

#Displaying Score function
def show_score(choice, color, font, size):
	#Creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	level_font = pygame.font.SysFont(font, size)
	
	#Create the display surface object
	score_surface = score_font.render('Score : ' + str(score), True, color)
	level_surface = level_font.render('Level : ' + str(level), True, color )
	
	#Create a rectangular object for the text
	score_rect = score_surface.get_rect()
	level_rect = level_surface.get_rect()
	
	#Displaying text
	game_window.blit(score_surface, score_rect)
	game_window.blit(level_surface, (level_rect[0], level_rect[1] + 20))

#Game over function
def game_over():
	#Creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	#Creating a text surface on which text will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score) , True, red)
	game_over_surface2 = my_font.render('Your level is : ' + str(level), True, red )
	
	#Create a rectangular object for the text
	game_over_rect1 = game_over_surface.get_rect()
	game_over_rect2 = game_over_surface2.get_rect()
	
	#Setting position of the text
	game_over_rect1.midtop = (window_x/2, window_y/3.5)
	game_over_rect2.midtop = (window_x/2, window_y/4.7)
	
	
	#Blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect1)
	game_window.blit(game_over_surface2, game_over_rect2)
	pygame.display.flip()
	
	#Quiting the program
	time.sleep(2)
	pygame.quit()
	quit()

def level_up(score, speed):
	if ( score % 50 == 0):
		global level
		level += 1
		speed += 20


#Game loop
while True:
	fps.tick(snake_speed)
	#Handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	#Condition when we want to change direction on the oposite
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	#How we move our snake
	if direction == 'UP':
		snake_position[1] -= 15
	if direction == 'DOWN':
		snake_position[1] += 15
	if direction == 'LEFT':
		snake_position[0] -= 15
	if direction == 'RIGHT':
		snake_position[0] += 15

	#Snake body growing mechanism
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		level_up(score, snake_speed)
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//15)) * 15,random.randrange(1, (window_y//15)) * 15]
	for block in snake_body[1:]:
		if fruit_position[0] == block[0] and fruit_position[1] == block[1]:
			fruit_position = [random.randrange(1, (window_x//15)) * 15,random.randrange(1, (window_y//15)) * 15]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,pygame.Rect(pos[0], pos[1], 15, 15))
	pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 15, 15))

	#Game over condition
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	# displaying score countinuously
	show_score(1, white, 'times new roman', 20)

	pygame.display.update()