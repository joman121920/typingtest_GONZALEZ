import pygame
from pygame.locals import *
import sys
import time
import random
import pyjokes
import sys
import os

#Helper function to find the correct path.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class Game:

    def __init__(self):
        self.w = 960  
        self.h = 540  
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (0, 0, 0)
        self.RESULT_C = (255, 70, 70)
        self.INPUT_BOX_COLOR = (0, 0, 0)  #background for input box
        self.INPUT_BOX_BORDER_COLOR = (255, 192, 25)  # Border color for the input bo

        pygame.init()
        self.open_img = pygame.image.load(resource_path('images/type-speed-open.png'))
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load(resource_path('images/background.png'))
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Typing Test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        sentence = pyjokes.get_joke()
        if len(sentence) <= 75:
            return sentence

    def show_results(self, screen):
        if not self.end:
            # Calculate time
            self.total_time = time.time() - self.time_start

            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100

            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:' + str(round(self.total_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # Draw icon image
            self.time_img = pygame.image.load(resource_path('images/icon.png'))
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))

            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running = True
        timer_started = False  # Track if the timer has started

        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.INPUT_BOX_COLOR, (50, 250, 860, 50))  # Input box background
            pygame.draw.rect(self.screen, self.INPUT_BOX_BORDER_COLOR, (50, 250, 860, 50), 2)  # Border
            
            # Update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # Position of input box
                    if x >= 50 and x <= 910 and y >= 250 and y <= 300:  # Adjusted input box area
                        self.active = True
                        self.input_text = ''
                        timer_started = False  # Reset timer flag for new round

                    # Position of reset box
                    if x >= 360 and x <= 600 and y >= 390 and self.end:  # Adjusted reset box area
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if not timer_started:  # Start the timer on the first key press
                            self.time_start = time.time()
                            timer_started = True  # Timer is now running

                        # Handle Ctrl+A (Select All)
                        if event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.input_text = self.word  # Select all text from the word

                        # Handle Ctrl+Backspace (Clear Input)
                        elif event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.input_text = ''  # Clear the entire input

                        elif event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(
                                self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()
            clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)
        self.reset = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence
        self.word = self.get_sentence()
        if not self.word:
            self.reset_game()

        # Drawing heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Test"
        self.draw_text(self.screen, msg, 60, 60, self.HEAD_C)

        # Draw the rectangle for input box
        pygame.draw.rect(self.screen, self.INPUT_BOX_COLOR, (50, 250, 860, 50))  # Input box background
        pygame.draw.rect(self.screen, self.INPUT_BOX_BORDER_COLOR, (50, 250, 860, 50), 2)  # Border

        # Draw the sentence string
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

        pygame.display.update()


Game().run()
