# -*- coding: utf-8 -*-

"""
ゲームを開始するプログラム。
"""

from modules.field import Field
from modules.game import Game
# from player import PlayerHuman, PlayerTrained, PlayerMax
from modules.player import PlayerRandom

field_size = (6, 6)


def play_game():
    field = Field(field_size)
    players = (PlayerRandom(0, field_size), PlayerRandom(1, field_size))

    game = Game(field, players, show=True)
    winner, _, _ = game.start()

    return winner


if __name__ == "__main__":
    print("winner: ", end="")
    print(play_game())
