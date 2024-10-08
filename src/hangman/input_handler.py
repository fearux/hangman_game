from hangman.renderer import Renderer


class InputHandler:

    def __init__(self, renderer: Renderer, valid_letters: str):
        self._valid_letters = valid_letters
        self._renderer = renderer

    def get_player_input(self) -> str:
        self._renderer.display_enter_message()
        player_input = input().lower()

        while not self._is_valid_input(player_input):
            self._renderer.display_incorrect_input_message()
            self._renderer.display_enter_message()
            player_input = input().lower()

        return player_input

    def _is_valid_input(self, player_input: str) -> bool:
        return len(player_input) == 1 and player_input in self._valid_letters
