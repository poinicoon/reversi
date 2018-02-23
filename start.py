"""
ゲームを開始するプログラム。
利用したいプレイヤープログラムをインポートする。
"""

from modules.field import Field
from modules.game import Game
# from player import PlayerHuman, PlayerTrained, PlayerMax
from modules.player import PlayerRandom

field_size = (6, 6)


def play_game():
    """
    ゲームを開始する。
    :param players: 使用したいプレイヤープログラムを格納する。
    :return:
    """
    field = Field(field_size)

    players = (PlayerRandom(0, field_size),
               PlayerRandom(1, field_size))

    game = Game(field, players)
    winner, _, _ = game.start()

    return winner


def main():
    winner = play_game()
    print("winner: ", end="")
    print(winner)


if __name__ == "__main__":
    main()
