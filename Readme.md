# マインクラフトレシピ画像切り取りツール

## 概要

このツールはNot Enough Itemsで表示されるクラフティングレシピの画像を切り取ることができます。

## 用法

1.Not Enough Itemsを事前に導入したMinecraftをデフォルトのウィンドウサイズで起動します。  
2.適当なワールドでレシピを表示します。  
3.F2を押してスクリーンショットを撮影します。  
4.スクリーンショットが存在するディレクトリでこのツールを起動します。  
5.recipeImagesフォルダが生成され、そこに切り取られた画像が保存されます。  

## 注意事項

容量が大きすぎる画像がフォルダに入っていた場合、それを読み込んで停止してしまいます。  
(実例: JourneyMapで全世界の地図をScreenshotsフォルダに出力(そのときの画像の大きさは21504*10240、サイズは30.3MB)し、そのまま該当フォルダで当アプリを起動した結果、エラーが発生し強制終了した)  
サイズの上限は確認していませんが、極端に大きな画像があった場合は予め取り除くようにしてください。

## その他

言語:Python  
ライセンス:MIT  
サイズ:240*120  
形式:png  
特記事項:NEIではレシピは上下に2つ表示されるので、画像が2枚できます。その際、何も描かれていない灰色の画像が生成される場合があります。

## 更新履歴

更新履歴の年月日の表記はyyyy.mm.ddです

### 2018.11.12

ライブラリのインポートに関するソースコードを一部修正  
Readmeのライセンス表記に関する間違いを修正  
Readmeの改行ミスを修正  
その他、軽微な修正  
リリース「v1.1」  
個人的メモの項目を追加

### 2018.11.04

ライセンスをGPLからMITに変更

### 2018.10.23

Readmeの一部修正

### 2018.10.22

更新履歴・Readmeの一部修正  
メッセージの追加  
リリース「Stable Release 1.0」及びタグ「1.0」の削除  
リリース「v1.0」

### 2018.10.21

リリース「Stable Release 1.0」

### 2018.10.15

読み込む画像のサイズを854*480に限定することに成功  
書き忘れ追加

### 2018.10.14

ソースにコメントを多数追加  
読み込む画像のサイズを854*480に限定しようとして失敗

### 2018.09.08

Readmeに軽微な修正を追加

### 2018.09.01

ソースコード、Windows上で実行可能な形式のファイル、Readmeを公開

## 目標

・今のままではレシピが1つのみ表示されたときには1枚何も表示されない灰色の画像ができてしまうため、その画像を検出して自動的に削除する機能を追加したい。  
・現在はNEIのクラフティングレシピにしか対応していないため、今後他のModで追加される機械やかまどのレシピなどにも対応できる別バージョンを作りたい。  
・動作が重い(時間がかかる)ため、コードの最適化などで実行速度を上昇させたい。具体的には写真の移動を削減したい。  
・画像読み込みに伴うエラーを起こさないようにしたい。

## 個人的メモ

・できれば画像読み込みエラーのkillとコード最適化は同時に出してv2.0としてリリース。特にコードが最適化できた場合は必ずバージョンを1上げる  
・画像検出削除機能はバージョンを0.1上げる