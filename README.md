# CNNを利用してリバーシのルールを学習させるプログラム

## start.py
ゲームをスタートさせる。
```$ python3 start.py```

## generate_model.py
モデルを作成する。
$ python3 generate_model.py "モデル"

## generate_traindata.py
訓練データを作成する。
$ python3 generate_traindata.py "モデル" "訓練データX" "訓練データY"

## generate_testdata.py
テストデータを作成する。
$ python3 generate_testdata.py "モデル" "テストデータX" "テストデータY"

## train.py
訓練する。
$ python3 train.py "モデル" "訓練データX" "訓練データY" "テストデータX" "テストデータY"

## model_test.py
訓練済みモデルをテストする。
$ python3 model_test.py "モデル"