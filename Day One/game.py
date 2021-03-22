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

class SpaceRace:

	asteroid_population = 15

	def __init__(self):
		self.asteroids = []
		for _ in range(self.asteroid_population):
			a = Asteroid()
			a.position.x = random.random() * SCREEN_WIDTH
			self.asteroids.append(a)

	def update(self, delta_time):
		for asteroid in self.asteroids:
			asteroid.update(delta_time)
			if not asteroid.is_on_screen:
				self.asteroids.remove(asteroid)
				self.asteroids.append(Asteroid())

	def draw(self, screen):
		for asteroid in self.asteroids:
			asteroid.draw(screen)