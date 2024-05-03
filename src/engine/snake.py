"""Module for the Snake class."""
from enum import Enum

import pygame

from src.engine import GAME_SETTINGS


class Direction(Enum):
    """Direction enumeration."""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Food:
    """Food class."""

    def __init__(self) -> None:
        """Initialize the food object."""
        self._food = self._spawn_food()

    @property
    def get_rectangle(self) -> pygame.Rect:
        """Get food rectangle."""
        return self._food

    @staticmethod
    def _spawn_food() -> pygame.Rect:
        """Spawn the food."""
        # TODO: handle the case when the food spawns on the snake
        return pygame.Rect(*GAME_SETTINGS.get_random_grid_coordinates(), GAME_SETTINGS.grid_size,
                           GAME_SETTINGS.grid_size)

    def spawn_new_food(self) -> None:
        """Spawn new food."""
        self._food = self._spawn_food()

    def draw_food(self, window: pygame.Surface):
        """Draw the food."""
        pygame.draw.rect(window, GAME_SETTINGS.food_color, self._food)

    @property
    def get_coordinates(self) -> tuple[int, int]:
        """Get the coordinates of the food."""
        return self._food.x, self._food.y


class Snake:
    """Snake class."""

    def __init__(self, direction: Direction = Direction.RIGHT) -> None:
        """Initialize the snake object."""
        self.body = self.spawn_snake()
        self.direction = direction

    @property
    def head(self) -> pygame.Rect:
        """Get the head of the snake."""
        return self.body[0]

    @property
    def length(self) -> int:
        """Get the length of the snake."""
        return len(self.body)

    @staticmethod
    def spawn_snake() -> list[pygame.Rect]:
        """Spawn the snake."""
        snake_body = []
        head_x_position, head_y_position = GAME_SETTINGS.get_random_grid_coordinates()
        snake_body.append(pygame.Rect(head_x_position, head_y_position, GAME_SETTINGS.grid_size,
                                      GAME_SETTINGS.grid_size))
        snake_body.append(pygame.Rect(head_x_position - GAME_SETTINGS.grid_size, head_y_position,
                                      GAME_SETTINGS.grid_size, GAME_SETTINGS.grid_size))
        return snake_body

    def draw_body(self, window: pygame.Surface) -> None:
        """Draw the snake."""
        for segment in self.body:
            pygame.draw.rect(window, GAME_SETTINGS.snake_color, segment)

    def update_position(self) -> None:
        """Update the position of the snake. Cannot move in the direction opposite to the current direction."""
        for i in range(self.length - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        if self.direction == Direction.UP:
            self.body[0].y -= GAME_SETTINGS.grid_size
        elif self.direction == Direction.RIGHT:
            self.body[0].x += GAME_SETTINGS.grid_size
        elif self.direction == Direction.DOWN:
            self.body[0].y += GAME_SETTINGS.grid_size
        elif self.direction == Direction.LEFT:
            self.body[0].x -= GAME_SETTINGS.grid_size

    def grow(self) -> None:
        """Grow the snake."""
        self.body.append(pygame.Rect(self.body[-1].x, self.body[-1].y,
                                     GAME_SETTINGS.grid_size, GAME_SETTINGS.grid_size))

    def check_collision(self, ) -> bool:
        """Check if the snake has collided with the walls or itself."""
        return self._check_wall_collision() or self._check_self_collision()

    def _check_wall_collision(self) -> bool:
        """Check if the snake has collided with the walls."""
        return (not GAME_SETTINGS.window_size[0] > self.head.x >= 0
                or not GAME_SETTINGS.window_size[1] > self.head.y >= 0)

    def _check_self_collision(self) -> bool:
        """Check if the snake has collided with itself."""
        return any(segment.colliderect(self.head) for segment in self.body[1:])

    def _check_food_collision(self, food: Food) -> bool:
        """Check if the snake has collided with the food."""
        return self.head.colliderect(food.get_rectangle)



