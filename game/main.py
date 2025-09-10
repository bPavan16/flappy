import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

MIN_WIDTH = 800
MIN_HEIGHT = 600

window = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT), pygame.RESIZABLE)

# Load the original image
original_bg = pygame.image.load("game/assets/background.png")

# Scale the image to fit the window
GAME_ASSETS = {
    "SKYLINE": pygame.transform.scale(original_bg, (MIN_WIDTH, MIN_HEIGHT))
}

def handle_events():
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.VIDEORESIZE:
            # Update assets when window is resized
            GAME_ASSETS["SKYLINE"] = pygame.transform.scale(original_bg, event.size)

def main():
    
    PLAY = True

    while PLAY:

        handle_events()
        
        window.fill((0, 0, 0))

        window.blit(GAME_ASSETS["SKYLINE"], (0, 0))

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()