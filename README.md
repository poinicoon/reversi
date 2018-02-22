# CNNを利用してリバーシのルールを学習させるプログラム

## 動作環境
### Pythonバージョン
```Python``` 3.5以上

### Pythonパッケージ
```numpy``` 1.14以上

```h5py``` 2.7以上

```tensorflow``` or ```tensorflow-gpu``` 1.5以上

```keras``` 2.1以上


## loop.sh
訓練を繰り返す。```Ctrl + C```で終了。

```$ ./loop.sh```

## start.py
ゲームをスタートさせる。

```$ python3 start.py```

## generate_model.py
モデルを作成する。

```$ python3 generate_model.py "モデル"```

## generate_traindata.py
訓練データを作成する。

```$ python3 generate_traindata.py "モデル" "訓練データX" "訓練データY"```

## generate_testdata.py
テストデータを作成する。

```$ python3 generate_testdata.py "モデル" "テストデータX" "テストデータY"```

## train.py
訓練する。

```$ python3 train.py "モデル" "訓練データX" "訓練データY" "テストデータX" "テストデータY"```

## model_test.py
訓練済みモデルをテストする。

```$ python3 model_test.py "モデル"```