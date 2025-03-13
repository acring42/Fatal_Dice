#make a function that sets the default values instead of writing them twice
import pygame, random, sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fatal Dice")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
GRAY = (128, 128, 128)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 100)

# Dice class
class Dice:
    def __init__(self, name, values):
        self.name = name
        self.values = values

dice_sets = {
    "D6": Dice("D6", list(range(1, 7))),
    "D8": Dice("D8", list(range(1, 9))),
    "D10": Dice("D10", list(range(1, 11))),
    "D12": Dice("D12", list(range(1, 13))),
    "D20": Dice("D20", list(range(2, 21))) #D20 wont have a 1 to avoid losing in the first round
}

def get_dice(stage):
    if stage < 4:
        return dice_sets["D20"]
    elif stage < 9:
        return dice_sets["D12"]
    elif stage < 14:
        return dice_sets["D10"]
    elif stage < 19:
        return dice_sets["D8"]
    else:
        return dice_sets["D6"]

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_text_title(text, x, y, color=BLACK):
    label = title_font.render(text, True, color)
    screen.blit(label, (x, y))

def roll_dice(stage):
    dice_set = get_dice(stage)
    dice1, dice2 = random.choice(dice_set.values), random.choice(dice_set.values)
    return dice1, dice2, dice_set.name

def set_dice():
    score = 0
    stage = 0
    dice1, dice2, dice_name = 0, 0, "D20"
    return score, stage, dice1, dice2, dice_name

# create main menu and game functions
# - main menu will have a Play button and a Quit Button
# - play will contain game loop and on loss, will go back to main menu

def main_menu():
    running = True
    while running:
        screen.fill(BLACK)

        #play_button = pygame.Rect(50, 300, 150, 50)
        #quit_button = pygame.Rect(250, 300, 150, 50)
        #pygame.draw.rect(screen, BLUE, play_button)
        #pygame.draw.rect(screen, RED, quit_button)
        draw_text_title("Fatal Dice", 135, 85, RED)

        play_button = pygame.Rect(250, 200, 100, 50)
        quit_button = pygame.Rect(250, 300, 100, 50)
        pygame.draw.rect(screen, BLUE, play_button)
        pygame.draw.rect(screen, RED, quit_button)
        draw_text("Play", 275, 214, WHITE)
        draw_text("Quit", 273, 314, WHITE) #275 just looks off. Text looks slightly right

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    play()
                if quit_button.collidepoint(event.pos):
                    running = False
    
    pygame.quit()
    sys.exit()


def play():
    running = True
    score, stage, dice1, dice2, dice_name = set_dice()

    while running:
        screen.fill(GRAY)
        draw_text(f"Stage: {stage+1}", 50, 50)
        draw_text(f"Score: {score}", 50, 100)
        draw_text(f"Dice: {dice_name}", 50, 150)
        draw_text(f"Rolls: {dice1} and {dice2}", 50, 200)
        
        roll_button = pygame.Rect(50, 300, 150, 50)
        quit_button = pygame.Rect(250, 300, 150, 50)
        pygame.draw.rect(screen, GREEN, roll_button)
        pygame.draw.rect(screen, RED, quit_button)
        draw_text("Roll Dice", 75, 315, WHITE)
        draw_text("Quit", 297, 315, WHITE)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if roll_button.collidepoint(event.pos):
                    dice1, dice2, dice_name = roll_dice(stage)
                    if dice1 == 1 or dice2 == 1:
                        game_over(stage, score)
                    else:
                        score += dice1 + dice2 + stage
                        stage += 1
                if quit_button.collidepoint(event.pos):
                    running = False
    
    pygame.quit()
    sys.exit()

def game_over(stage, score):
    running = True
    
    while running:
        screen.fill(GREEN)
        
        draw_text_title("Game Over", 115, 25, RED)
        draw_text(f"Stage: {stage+1}", 251, 110)
        draw_text(f"Final Score: {score}", 207, 160)

        playAgain_button = pygame.Rect(200, 225, 200, 50)
        quit_button = pygame.Rect(250, 300, 100, 50)
        pygame.draw.rect(screen, BLUE, playAgain_button)
        pygame.draw.rect(screen, RED, quit_button)
        draw_text("Play Again", 240, 239, WHITE)
        draw_text("Quit", 273, 314, WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgain_button.collidepoint(event.pos):
                    play()
                if quit_button.collidepoint(event.pos):
                    running = False
    
    pygame.quit()
    sys.exit()


main_menu()
#play()
#game_over()
