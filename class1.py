import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.image.load('penguin.png')  
pygame.image.save(penguin_image, 'penguin.png') 
 # Save the image to ensure it's in the correct format
penguin_image = pygame.transform.scale(penguin_image, (100, 100))

text = pygame.font.SysFont('Arial', 30).render('Hello, Pygame!', True, (255, 255, 255))
pygame.color.Color('black')
 text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))

  def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, (200, 200))
        display_surface.blit(text, (150, 50))

        pygame.display.update()