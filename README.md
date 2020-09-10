数理計画問題(Mathematical programming problem)を用いたリソースにおける優先業務選択補助システム
==============================

## Target

災害時における優先業務の選定をリソースに関する数理計画問題によってモデル化する．
1. 各業務に関する変数を0~1の連続値にした場合，現時点のリソースで各業務を通常時に比べ，どのくらいの割合で行うことができるかを出力する．
2. 各業務に関する変数を0または1の離散値にした場合，現時点のリソースでどの業務を優先的に選択すべきかを出力する．

## Project Organization

    .
    ├── README.md          <- プロジェクトの全体像
    ├── uploads            <- 入力データが置かれるディレクトリ
    ├── templates          <- htmlファイルのためのディレクトリ
    │   ├── index.html
    │   └── result.html
    ├── model              <- 定式化に関するディレクトリ
    │   └── mp.py          <- 数理計画問題のモジュール
    └── main.py            <- システムのメインプログラム

## Usage

### Step1

[Docker](https://www.docker.com/) で環境を作成します．事前に[公式ドキュメント](https://docs.docker.com/)を参照しローカル環境にDockerを導入してください．以下はDockerがインストールされており，DockerHubのアカウントを持っていることを想定しています．

### Step2

以下のコマンドをターミナルで実行して下さい．
```shell
git clone git@github.com:kunifuohbc/ohbc_mp_for_resource.git
```

### Step3

main.pyのあるディレクトリに移動して下さい．

### Step4

以下のコマンドをターミナルで実行して下さい．
```shell
docker pull kunifuohbc/ohbc_mp
docker run -p 3000:3000 -v $(pwd):/work kunifuohbc/ohbc_mp
```
### Step4

ブラウザにhttp://localhost:3000/を入力して下さい．

### Step5

以下のデモのように結果を取得できます．
![mp_demo1](https://user-images.githubusercontent.com/70554494/92748686-57c4b100-f3c0-11ea-899d-28f97bde292f.gif)

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)


