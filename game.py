import pygame, random, time
from mosquito import Mosquito
from bee import Bee
from settings import *

class Game:
    def __init__(self, assets):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mosquito Killer")
        self.clock = pygame.time.Clock()

        # Load images
        bg_img = pygame.image.load(assets["bg"]).convert()
        self.bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.hand_img = pygame.image.load(assets['hand']).convert_alpha()
        self.mosquito_imgs = [pygame.image.load(assets[f'mosquito{i+1}']).convert_alpha() for i in range(5)]
        self.bee_img = pygame.image.load(assets['bee']).convert_alpha()

        # Load sounds
        self.hit_sound = pygame.mixer.Sound(assets['hit'])
        self.damage_sound = pygame.mixer.Sound(assets['damage'])
        pygame.mixer.music.load(assets['bg_music'])
        pygame.mixer.music.play(-1)  # Loop background music

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.mosquitoes = pygame.sprite.Group()
        self.bees = pygame.sprite.Group()

        self.assets = assets
        self.reset_game()

    def reset_game(self):
        """Reset all elements for a fresh start."""
        self.all_sprites.empty()
        self.mosquitoes.empty()
        self.bees.empty()

        # Create mosquitoes
        for _ in range(NUM_MOSQUITOES):
            m = Mosquito(random.choice(self.mosquito_imgs))
            self.all_sprites.add(m)
            self.mosquitoes.add(m)

        # Create bees
        for _ in range(NUM_BEES):
            b = Bee(self.bee_img)
            self.all_sprites.add(b)
            self.bees.add(b)

        self.score = 0
        self.start_time = time.time()
        self.running = False  # Not running until Start button clicked
        self.game_over = False

    def start_screen(self):
        """Display start screen with button."""
        font = pygame.font.SysFont(None, 70)
        title_text = font.render("🐝 Mosquito Killer 🦟", True, (0, 0, 0))
        small_font = pygame.font.SysFont(None, 40)
        start_text = small_font.render("Press ENTER to Start", True, (255, 255, 255))
        
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
            pygame.draw.rect(self.screen, (0, 150, 0), (SCREEN_WIDTH // 2 - 120, 350, 240, 60), border_radius=20)
            self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 365))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.running = True
                    self.start_time = time.time()
                    return  # Exit start screen

    def update(self, hand_pos, hand_closed):
        self.all_sprites.update()

        if hand_pos:
            hand_rect = self.hand_img.get_rect(center=hand_pos)
            if hand_closed:
                # Mosquito hit = +1 point
                for m in self.mosquitoes:
                    if hand_rect.colliderect(m.rect):
                        self.score += 1
                        self.hit_sound.play()
                        m.rect.x = random.randint(50, SCREEN_WIDTH - 50)
                        m.rect.y = random.randint(50, SCREEN_HEIGHT - 200)

                # Bee hit = -2 points and play damage sound
                for b in self.bees:
                    if hand_rect.colliderect(b.rect):
                        self.score -= 2
                        self.damage_sound.play()
                        b.rect.x = random.randint(50, SCREEN_WIDTH - 50)
                        b.rect.y = random.randint(50, SCREEN_HEIGHT - 200)

        # Timer
        elapsed = time.time() - self.start_time
        remaining = max(0, GAME_DURATION - elapsed)
        if remaining <= 0:
            self.running = False
            self.game_over = True

        self.draw(hand_pos, remaining)

    def draw(self, hand_pos, remaining):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprites.draw(self.screen)
        if hand_pos:
            self.screen.blit(self.hand_img, self.hand_img.get_rect(center=hand_pos))

        font = pygame.font.SysFont(None, 40)
        score_text = font.render(f"Score : {self.score}", True, (0, 0, 0))
        time_text = font.render(f"Time left : {round(remaining, 1)}", True, (0, 0, 0))
        self.screen.blit(score_text, (20, 20))
        self.screen.blit(time_text, (700, 20))

        pygame.display.flip()
        self.clock.tick(FPS)

    def game_over_screen(self):
        """Display Game Over screen with final score."""
        font = pygame.font.SysFont(None, 70)
        over_text = font.render("Game Over!", True, (200, 0, 0))
        score_font = pygame.font.SysFont(None, 50)
        score_text = score_font.render(f"Your Score: {self.score}", True, (0, 0, 0))
        small_font = pygame.font.SysFont(None, 40)
        restart_text = small_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        while True:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(over_text, (SCREEN_WIDTH // 2 - over_text.get_width() // 2, 200))
            self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
            pygame.draw.rect(self.screen, (0, 0, 150), (SCREEN_WIDTH // 2 - 200, 400, 400, 60), border_radius=20)
            self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 415))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return 'restart'
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()
