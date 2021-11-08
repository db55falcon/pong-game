import pygame
import time

pygame.init()
WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
main_font = pygame.font.Font("freesansbold.ttf", 20)


class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = 200
        self.width = 20
        self.height = 100
        self.score = 0
        self.speed = 1

    def display(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Ball:
    def __init__(self):
        self.x = 240
        self.y = 240
        self.width = 20
        self.height = 20
        self.speedx = 1
        self.speedy = 0.6

    def display(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speedx
        self.y += self.speedy


def draw(win):
    win.fill((0, 0, 0))
    player.display(win)
    bot.display(win)
    ball.display(win)
    player_score = main_font.render(f"{player.score}", True, (255, 255, 255))
    bot_score = main_font.render(f"{bot.score}", True, (255, 255, 255))
    win.blit(player_score, (75, 20))
    win.blit(bot_score, (400, 20))
    pygame.display.update()


player = Paddle(40)
bot = Paddle(440)
ball = Ball()
start = False
run = True


def reset():
    player.y = 200
    bot.y = 200
    ball.x = 240
    ball.y = 240

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if start:
        ball.move()
        if bot.y + 50 < ball.y + 10 and bot.y + bot.height + bot.speed <= 500:
            bot.y += bot.speed
        if bot.y + 50 > ball.y + 10 and bot.y - bot.speed >= 0:
            bot.y -= bot.speed

        if ball.y <= 0 or ball.y + ball.height >= HEIGHT:
            ball.speedy *= -1
        if ball.x + 20 >= bot.x and ball.x + 20 <= bot.x + 20:
            if ball.y + 20 >= bot.y and ball.y <= bot.y + 100:
                ball.speedx *= -1
        if ball.x <= player.x + 20 and ball.x >= player.x:
            if ball.y + 20 >= player.y and ball.y <= player.y + 100:
                ball.speedx *= -1
        if ball.x <= -40:
            bot.score += 1
            reset()
            start = False
        if ball.x <= -520:
            player.score += 1
            reset()
            start = False
    controls = pygame.key.get_pressed()
    if controls[pygame.K_UP] and player.y - player.speed >= 0:
        player.y -= player.speed
        start = True
    if controls[pygame.K_DOWN] and player.y + player.height + player.speed <= HEIGHT:
        player.y += player.speed
        start = True
    draw(win)





