import pygame
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.display.set_caption("Snake")
GRID_BLOCK_SIZE = 25
snake = [(random.randint(0, WINDOW_WIDTH // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE)]
FONT_SIZE = 25
pygame.init()
pygame.font.init()
font = pygame.font.Font('arial.ttf', FONT_SIZE)
score = 0
SNAKE_START_LENGTH = 3
dirrections = [0, 0]

# initialize snake
for i in range(SNAKE_START_LENGTH - 1):
    valid = []
    if snake[-1][0] < WINDOW_WIDTH - GRID_BLOCK_SIZE and not (snake[-1][0] + GRID_BLOCK_SIZE, snake[-1][1]) in snake:
        valid.append((snake[-1][0] + GRID_BLOCK_SIZE, snake[-1][1]))
    if snake[-1][0] > 0 and not (snake[-1][0] - GRID_BLOCK_SIZE, snake[-1][1]) in snake:
        valid.append((snake[-1][0] - GRID_BLOCK_SIZE, snake[-1][1]))
    if snake[-1][1] > 0 and not (snake[-1][0], snake[-1][1] - GRID_BLOCK_SIZE) in snake:
        valid.append((snake[-1][0], snake[-1][1] - GRID_BLOCK_SIZE))
    if snake[-1][1] < WINDOW_HEIGHT - GRID_BLOCK_SIZE and not (snake[-1][0], snake[-1][1] + GRID_BLOCK_SIZE) in snake:
        valid.append((snake[-1][0], snake[-1][1] + GRID_BLOCK_SIZE))
    chosen = random.randint(0, len(valid) - 1)
    snake.append(valid[chosen])


def main():
    global food
    food = [random.randint(0, WINDOW_WIDTH // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE]
    global dirrection
    global score
    dirrection = ""
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    end = False
    
    while True:
        CLOCK.tick(15)
        if not end:
            drawScreen()

        updateScore()
        if dirrection:
            nextSnake(dirrection)

        if snake[0][0] == food[0] and snake[0][1] == food[1]:
            score += 1
            food = getFood()
            # add xsign
            xsign = snake[-1][0] - snake[-2][0]
            # add ysign
            ysign = xsign = snake[-2][1] - snake[-1][1]
            snake.append((snake[-1][0] + xsign, snake[-1][1] + ysign))

        if snake[0] in snake[1:]:
            end = True
        
        if snake[0][0] < 0 or snake[0][0] > WINDOW_WIDTH or snake[0][1] > WINDOW_HEIGHT or snake[0][1] < 0:
            end = True

        if end:
            SCREEN.fill(BLACK)
            t = pygame.font.Font('arial.ttf', 50)
            text = t.render("GAME OVER", True, (255,0,0))
            text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            SCREEN.blit(text, text_rect)
            text = t.render(f"SCORE: {score}", True, (255,0,0))
            text_rect = text.get_rect(center=(WINDOW_WIDTH/2, int(WINDOW_HEIGHT/1.2)))
            SCREEN.blit(text, text_rect)
            
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if dirrections[-1] != "down":
                        dirrection = "up"
                        dirrections.pop(0)
                        dirrections.append(dirrection)
                if event.key == pygame.K_a:
                    if dirrections[-1] != "right":
                        dirrection = "left"
                        dirrections.pop(0)
                        dirrections.append(dirrection)
                if event.key == pygame.K_s:
                    if dirrections[-1] != "up":
                        dirrection = "down"
                        dirrections.pop(0)
                        dirrections.append(dirrection)
                if event.key == pygame.K_d:
                    if dirrections[-1] != "left":
                        dirrection = "right"
                        dirrections.pop(0)
                        dirrections.append(dirrection)
        pygame.display.update()
        



def drawScreen():
    for x in range(0, WINDOW_WIDTH, GRID_BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, GRID_BLOCK_SIZE):
            rect = pygame.Rect(x, y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
            if not (x, y) in snake:
                pygame.draw.rect(SCREEN, BLACK, rect)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
            elif (x,y) == snake[0]:
                pygame.draw.rect(SCREEN, (110,200,110), rect)
            else:
                pygame.draw.rect(SCREEN, GREEN, rect)
            if x == food[0] and y == food[1]:
                pygame.draw.rect(SCREEN, RED, rect)

            

def nextSnake(dir):
    # dirob = {"left": "right", "right": "left", "up": "down", "down": "up", 0: 0}
    #dirrections[-1] != dirob[dirrections[-2]]:
    if dir == "up":
        snake.insert(0, (snake[0][0], snake[0][1] - GRID_BLOCK_SIZE))
        snake.pop()
    if dir == "left":
        snake.insert(0, (snake[0][0] - GRID_BLOCK_SIZE, snake[0][1]))
        snake.pop()
    if dir == "down":
        snake.insert(0, (snake[0][0], snake[0][1] + GRID_BLOCK_SIZE))
        snake.pop()
    if dir == "right":
        snake.insert(0, (snake[0][0] + GRID_BLOCK_SIZE, snake[0][1]))
        snake.pop()


def updateScore():
    text = font.render(f"Score: {score}", True, (100,200,220))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/15))
    SCREEN.blit(text, text_rect)

def getFood():
    t = True
    while t:
        f = [random.randint(0, WINDOW_WIDTH // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE]
        for x, y in snake:
            if f[0] != x and f[1] != y:
                t = False

    return [random.randint(0, WINDOW_WIDTH // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT // GRID_BLOCK_SIZE - 1) * GRID_BLOCK_SIZE]
    

main()




