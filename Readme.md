# Minecraftレシピ画像切り取りツール

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
(実例: JourneyMapで全世界の地図をScreenshotsフォルダに出力(そのときの画像の大きさは21504*10240、サイズは30.3MB)し、そのまま該当フォルダで当ソフトを起動した結果、エラーが発生し強制終了した)  
サイズの上限は確認していませんが、極端に大きな画像(純粋なMinecraftのスクリーンショットでないものなど)があった場合は可能な限り予め取り除くようにしてください。  
エラーが発生した場合、まずはサイズが大きすぎる画像が紛れ込んでいないか確かめてください。

## その他

言語:Python  
ライセンス:MIT  
画像サイズ:240*120  
形式:png  
特記事項:NEIではレシピは上下に2つ表示されるので、画像が2枚できます。

## 更新履歴

更新履歴の年月日の表記はyyyy.mm.ddです

### 2019.02.22

Readmeに一部追記・修正

### 2019.01.24

ソースコードの最適化による高速化(ファイル移動の削減に成功)  
Pillowのライセンスの表記(追加し忘れてましたごめんなさい)  
リリース「v2.0」  
過去のリリース「v1.0」「v1.1」、及びタグ「v1.0」「v1.1」をライセンスの問題から削除  
灰色一色の画像を削除する機能を追加(ほぼ完成)  
リリース「v2.1」  
Readmeの注意事項等に追記、その他一部修正

### 2018.12.19

名称表記を「マインクラフト」から「Minecraft」に変更

### 2018.12.14

ソース内のシングルクォーテーションをダブルクォーテーションに変更

### 2018.11.14

目標を追加

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
SSHキーテストコミット(変更点なし)

### 2018.09.01

ソースコード、Windows上で実行可能な形式のファイル、Readmeを公開

## Pillowのライセンス

Software License  

The Python Imaging Library (PIL) is  

    Copyright © 1997-2011 by Secret Labs AB  
    Copyright © 1995-2011 by Fredrik Lundh  

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:  

Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.  

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.  

## 目標

・現在はNEIのクラフティングレシピにしか対応していないため、今後他のModで追加される機械やかまどのレシピなどにも対応できる別バージョンを作りたい。  
・画像読み込みに伴うエラーを起こさないようにしたい。  
・重複した画像を削除できるようにしたい

## 個人的メモ

・エラー殺しはバージョンを0.1上げる
・Pillowのライセンスなんもわからん(どれを表記すれば良いのかわからなかったので全文引っ張ってきた、問題は無いと思うが最適な表記方法があったら誰か教えてください)