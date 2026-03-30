import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 530
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eye Tracking")

# Define romantic colors
BACKGROUND_COLOR = (255, 105, 180)  # Hot Pink
EYE_COLOR = (0, 0, 0)  # Black
PUPIL_COLOR = (220, 20, 60)  # Crimson Red
OUTLINE_COLOR = (255, 240, 245)  # Lavender Blush
MOUTH_COLOR = (220, 20, 60)  # Crimson Red
TONGUE_COLOR = (255, 0, 0)  # Red

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill(BACKGROUND_COLOR)
    
    # Draw eyes function
    def draw_eye(eye_x, eye_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y
        distance = min(math.sqrt(distance_x**2 + distance_y**2), 30)
        angle = math.atan2(distance_y, distance_x)
        
        pupil_x = eye_x + (math.cos(angle) * distance)
        pupil_y = eye_y + (math.sin(angle) * distance)
        
        # Draw eye outline
        pygame.draw.circle(screen, OUTLINE_COLOR, (eye_x, eye_y), 52)
        # Draw light pink eye
        pygame.draw.circle(screen, EYE_COLOR, (eye_x, eye_y), 50)
        # Draw crimson pupil
        pygame.draw.circle(screen, PUPIL_COLOR, (int(pupil_x), int(pupil_y)), 15)
    
    # Draw both eyes
    draw_eye(200, 200)
    draw_eye(330, 200)
    
    # Draw mouth (curved smile)
    pygame.draw.arc(screen, MOUTH_COLOR, (200, 220, 130, 80), 0, math.pi, 2)
    
    # Draw tongue (small triangle)
    tongue_points = [(265, 280), (255, 300), (275, 300)]
    pygame.draw.polygon(screen, TONGUE_COLOR, tongue_points)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()





