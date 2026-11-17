全部Claudeさんに言いなりになって作った習作です。このレーティング計算には実際にお世話になっていました。

# AtCoder レーティング計算ツール

過去のパフォーマンス履歴から現在のレーティングを計算し、目標レーティングに届くために必要なパフォーマンスを表示するWebアプリです。

https://rating-tool-qecwgpkizjmxgj4hhedmps.streamlit.app/

## できること
- 過去のパフォーマンス（古い順）を入力すると、現在のレーティングを表示します。
- 目標レーティングに届くために、今後1・2・3・5・8・10回で必要な平均パフォーマンスを表示します。

## 使い方
1. AtCoderの成績表のパフォーマンスを、古い順にカンマか改行で区切って入力します。
2. 目標レーティングを入力します。

## 計算方法
AtCoderのレーティング計算式（パフォーマンスの重み付き平均と、参加回数による補正）を実装しています。必要なパフォーマンスは二分探索で求めています。
公式の計算を再現した近似のため、実際のレーティングと数ポイントの誤差が出ることがあります（自分の履歴では1の差でした）。

## 構成
- `app.py`: 画面（Streamlit）
- `rating.py`: 計算ロジック
- `test_rating.py`: テスト（実際のレーティングと照合）
- `requirements.txt`: 依存ライブラリ

## ローカルでの実行（Windows / PowerShell）
```
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt pytest
streamlit run app.py
```
テストは `pytest` で実行できます。