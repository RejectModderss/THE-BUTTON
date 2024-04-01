import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
BUTTON_RADIUS = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE BUTTON")
button = pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), BUTTON_RADIUS)

counter = 0
reset_chance = 0
max_counter = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 36)

reset_responses = [
    "Are you even trying?",
    "Better luck next time!",
    "Oops! Try again.",
    "Is that all you got?",
    "I've seen snails click faster!",
    "My grandma clicks faster than you!",
    "You call that clicking?"
]

five_click_responses = [
    "Congrats! You finally got {counter} clicks!",
    "Keep going!",
    "Nice job!",
    "Wow, {counter} clicks! You must be so proud.",
    "You've reached {counter} clicks. Do you want a medal?",
    "Hooray, {counter} clicks! Let's throw a party.",
    "You've clicked {counter} times. Your finger must be tired."
]
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((mouse_pos[0] - WIDTH // 2)**2 + (mouse_pos[1] - HEIGHT // 2)**2) < BUTTON_RADIUS**2:
                counter += 1
                reset_chance += 1
                if counter > max_counter:
                    max_counter = counter
                if random.randint(1, 100) <= reset_chance:
                    counter = 0
                    reset_chance = 0
                    message = random.choice(reset_responses)
                elif counter % 5 == 0 and counter != 0:
                    message = random.choice(five_click_responses).replace("{counter}", str(counter))

    screen.fill((0, 0, 0))

    if ((mouse_pos[0] - WIDTH // 2)**2 + (mouse_pos[1] - HEIGHT // 2)**2) < BUTTON_RADIUS**2:
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), BUTTON_RADIUS)
    else:
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), BUTTON_RADIUS)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), BUTTON_RADIUS, 2)

    text = font.render(str(counter), True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    max_text = font.render(f"Max: {max_counter}", True, WHITE)
    screen.blit(max_text, (WIDTH // 2 - max_text.get_width() // 2, 10))

    if 'message' in locals():
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()