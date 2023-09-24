from itertools import cycle
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Grid, Center, Middle
from textual import events
from textual.widgets import Footer, Header, Static

from rich.panel import Panel
from rich.text import Text


class ChessBoardTile(Static):
    def watch_mouse_over(self, value):
        prev_background_color = self.styles.background

        if not value:
            self.styles.background = "lightgreen"
        else:
            self.styles.background = prev_background_color


class TerminalChess(App):
    CSS_PATH = "python-chess.tcss"

    def compose(self) -> ComposeResult:
        yield Header(name="Xadrez no Terminal", show_clock=True)
        with Middle():
            with Center():
                with Container(classes="container"):
                    with Grid(classes="board"):
                        control = True
                        for tile in range(64):
                            # TODO Melhorar a lógica disso. Tornar conciso, resumir
                            if control:
                                if tile % 2:
                                    yield ChessBoardTile(classes="white-board-item")
                                else:
                                    yield ChessBoardTile(classes="black-board-item")
                            else:
                                if tile % 2:
                                    yield ChessBoardTile(classes="black-board-item")
                                else:
                                    yield ChessBoardTile(classes="white-board-item")

                            if tile % 8 == 7:
                                control = not control


if __name__ == "__main__":
    app = TerminalChess()
    app.run()
