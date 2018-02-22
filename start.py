'''
ゲームを開始するプログラム。
プレイヤープログラムをインポートし、players変数にセットする。
盤面サイズは、field_size変数で設定する。
'''

from module.field import Field
from module.game import Game
# from player import PlayerHuman, PlayerTrained, PlayerMax
from module.player import PlayerRandom

field_size = (6, 6)

def play_game():
    field = Field(field_size)
    players = (PlayerRandom(0, field_size), PlayerRandom(1, field_size))

    game = Game(field, players, show=True)
    winner, fields, coords = game.start()

    return winner, fields, coords


if __name__ == "__main__":

    winner, _, _ = play_game()

    print("Winner: " + str(winner))
    print()
