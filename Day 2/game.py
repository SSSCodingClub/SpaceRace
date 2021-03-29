from setup import *

class Asteroid:

	width, height = 8, 8
	speed = 0.3
	min_possible_height = SCREEN_HEIGHT / 5

	color = (255, 255, 255)

	def __init__(self):
		self.is_on_screen = True
		self.velocity = pygame.Vector2(random.choice((-1, 1)) * self.speed, 0)
		self.position = pygame.Vector2(0, random.random() * (SCREEN_HEIGHT - self.min_possible_height))

		if self.velocity.x < 0:
			self.position.x = SCREEN_WIDTH + self.width / 2
		else:
			self.position.x = -self.width / 2

	def update(self, delta_time):
		self.position += self.velocity * delta_time
		if self.position.x > SCREEN_WIDTH + self.width / 2 or self.position.x < -self.width / 2:
			self.is_on_screen = False

	def draw(self, screen):
		r = pygame.Rect(
			self.position.x - self.width/2,
			self.position.y - self.height/2,
			self.width, 
			self.height)
		pygame.draw.rect(screen, self.color, r)

class Player:

	width, height = 64, 64
	speed = 0.3

	texture = pygame.transform.scale(pygame.image.load("ship.png"), (width, height))

	def __init__(self, position_x, position_y):
		self.position = pygame.Vector2(position_x, position_y)

	def move_forward(self, delta_time):
		self.position.y -= self.speed * delta_time

	def move_backward(self, delta_time):
		if self.position.y < SCREEN_HEIGHT - self.height/2:
			self.position.y += self.speed * delta_time

	def update(self, delta_time):
		if self.position.y < -self.height/2:
			self.position.y = SCREEN_HEIGHT + self.height/2

	def draw(self, screen):
		top_left = (self.position.x - self.width/2, self.position.y - self.height/2)
		screen.blit(self.texture, top_left)

class SpaceRace:

	asteroid_population = 15

	def __init__(self):
		self.asteroids = []
		self.player_one = Player(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT - 50)
		self.player_two = Player(SCREEN_WIDTH * 0.75, SCREEN_HEIGHT - 50)
		for _ in range(self.asteroid_population):
			a = Asteroid()
			a.position.x = random.random() * SCREEN_WIDTH
			self.asteroids.append(a)

	def update(self, delta_time):

		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_w]:
			self.player_one.move_forward(delta_time)
		if pressed[pygame.K_s]:
			self.player_one.move_backward(delta_time)
		if pressed[pygame.K_UP]:
			self.player_two.move_forward(delta_time)
		if pressed[pygame.K_DOWN]:
			self.player_two.move_backward(delta_time)

		self.player_one.update(delta_time)
		self.player_two.update(delta_time)

		for asteroid in self.asteroids:
			asteroid.update(delta_time)
			if not asteroid.is_on_screen:
				self.asteroids.remove(asteroid)
				self.asteroids.append(Asteroid())

	def draw(self, screen):
		self.player_one.draw(screen)
		self.player_two.draw(screen)
		for asteroid in self.asteroids:
			asteroid.draw(screen)