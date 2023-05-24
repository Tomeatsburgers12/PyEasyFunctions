import pygame
from pynput import keyboard


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def create(self):
        pygame.init()
        canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Canvas")
        canvas.fill(self.color)
        pygame.display.update()
        return canvas


class GameLoop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def end(self):
        pygame.quit()


def get_input(key_name):
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key[key_name]:
                return True


