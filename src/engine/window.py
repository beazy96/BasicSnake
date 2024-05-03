"""Game window module."""
import sys

import pygame

from src.engine import GAME_SETTINGS
from src.engine.snake import Snake, Direction, Food


class GameWindow:
    """Game window class."""

    def __init__(self) -> None:
        """Initialize the game window."""
        self.window = self._get_window()
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()

    @staticmethod
    def _get_window() -> pygame.Surface:
        """Get the game window."""
        window = pygame.display.set_mode(GAME_SETTINGS.window_size)
        pygame.display.set_caption(GAME_SETTINGS.window_title)
        return window

    @staticmethod
    def _quit_game() -> None:
        """Quit the game."""
        pygame.quit()
        sys.exit()

    def _handle_events(self) -> None:
        """Handle the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            if event.type == pygame.KEYDOWN:
                self._handle_key_event(event)

    def _handle_key_event(self, key_event: pygame.event.Event) -> None:
        """Handle the key event."""
        if key_event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
            self.snake.direction = Direction.UP
        elif key_event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
            self.snake.direction = Direction.RIGHT
        elif key_event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
            self.snake.direction = Direction.DOWN
        elif key_event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
            self.snake.direction = Direction.LEFT

    def handle_game_incidents(self) -> None:
        """Handle the game incidents."""
        self._handle_events()
        if self.snake.check_collision():
            # Display game over message
            self._quit_game()
        if self.snake.head.colliderect(self.food.get_rectangle):
            self.snake.grow()
            self.food.spawn_new_food()

    def draw_game_window(self) -> None:
        """Draw the game window."""
        self.window.fill(GAME_SETTINGS.background_color)
        self.snake.draw_body(self.window)
        self.food.draw_food(self.window)
        pygame.display.update()

    def run(self) -> None:
        """Run the game window."""
        while True:
            self.handle_game_incidents()
            self.draw_game_window()
            self.clock.tick(GAME_SETTINGS.frame_rate)
            self.snake.update_position()


if __name__ == "__main__":
    game_window = GameWindow()
    game_window.run()
