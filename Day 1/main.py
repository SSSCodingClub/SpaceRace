from setup import *
from game import SpaceRace

is_running = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

previous_time = current_time = pygame.time.get_ticks()

game = SpaceRace()

while is_running:

	current_time = pygame.time.get_ticks()
	delta_time = current_time - previous_time
	previous_time = current_time

	screen.fill((0, 0, 0))

	game.update(delta_time)
	game.draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.update()

pygame.quit()