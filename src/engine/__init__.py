"""Engine package init module."""
from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class GameSettings:
    """
    Game engine class.
    :param grid_size: The size of the field into which the game widow will be divided.
    :param frame_rate: The number of frames per second. The higher the frame rate, the faster the game will run.
    """

    window_height: int = 600
    window_width: int = 600
    grid_size: int = 30
    window_title: str = "Snake"
    frame_rate: int = 10
    snake_color: tuple[int, int, int] = (0, 255, 0)
    food_color: tuple[int, int, int] = (255, 0, 0)
    background_color: tuple[int, int, int] = (0, 0, 0)

    def __post_init__(self):
        """Assert that the game engine parameters are valid."""
        assert self.window_height % self.grid_size == 0, "Window height must be a multiple of grid size."
        assert self.window_width % self.grid_size == 0, "Window width must be a multiple of grid size."
        assert self.window_height >= self.grid_size, "Window height must be greater than or equal to grid size."
        assert self.window_width >= self.grid_size, "Window width must be greater than or equal to grid size."
        assert self.frame_rate > 0, "Frame rate must be greater than 0."

    @property
    def window_size(self):
        """Get the window size."""
        return self.window_width, self.window_height

    def get_random_grid_coordinates(self) -> tuple[int, int]:
        """Get random grid coordinates."""
        return (randint(0, (self.window_width // self.grid_size) - 1) * self.grid_size,
                randint(0, (self.window_height // self.grid_size) - 1) * self.grid_size)


GAME_SETTINGS = GameSettings()
