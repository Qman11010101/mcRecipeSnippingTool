#Made by Kjuman Enobikto
#Twitter: @QmanEnobikto

import os
import PIL
from PIL import Image
from os import path
import glob
import shutil

#作業中の文字
print("作業を行っています。このウィンドウが消えるまでお待ち下さい")

#プログラム中で使うディレクトリの作成

#完成したレシピ画像を入れるディレクトリ
if path.exists("recipeImages") == False:
    os.mkdir("recipeImages")

#一時的にレシピ画像と思われる画像(サイズがW854H480であるもの)を入れておくディレクトリ
if path.exists("recipepictemp") == False:
    os.mkdir("recipepictemp")

allimg = []
allimg = glob.glob("*.png")

#レシピ画像とそれ以外を選り分ける
while glob.glob("*.png") != []: #ディレクトリのpng画像がなくなるまで繰り返す

    if allimg == []: #allimgが空になったらbreakして次のフェーズへ
        break
    
    chosenImg = allimg[0] #リストallimgの一番最初を取り出す

    chkImgSize = Image.open(chosenImg) #画像を開く
    imgwidth, imgheight = chkImgSize.size #画像のWidthとHeightを取得
    if (imgwidth == 854 and imgheight == 480):
        shutil.copy2(chosenImg, "recipepictemp/"+chosenImg) #画像サイズが854*480であればレシピ画像ディレクトリへコピー
    
    chkImgSize.close() #開いた画像を閉じる
    allimg.pop(0) #コピー元の画像をallimgリストから削除

#作業ディレクトリをレシピ画像ディレクトリにする
os.chdir("./recipepictemp")

#画像の加工
while glob.glob("*") != []: #中身が空になるまで繰り返す
    recipeImages = []
    recipeImages = glob.glob("*")

    chosenRecipeImg = recipeImages[0] #リストrecipeImagesの一番最初を取り出す

    #画像の上側の切り出し
    imgAbove = Image.open(chosenRecipeImg)
    cutImgAbove = (304, 110, 544, 230)
    imgCuttedAbove = imgAbove.crop(cutImgAbove)
    imgCuttedAbove.save("../recipeImages/above_"+chosenRecipeImg)

    #画像の下側の切り出し
    imgUnder = Image.open(chosenRecipeImg)
    cutImgUnder = (304, 240, 544, 360)
    imgCuttedUnder = imgUnder.crop(cutImgUnder)
    imgCuttedUnder.save("../recipeImages/under_"+chosenRecipeImg)

    #加工が終わった画像を元の画像ディレクトリへ
    shutil.move(chosenRecipeImg, "../"+chosenRecipeImg)

#あとかたづけ
os.chdir("../") #作業ディレクトリを元のディレクトリにする
os.rmdir("./recipepictemp") #作業に使ったディレクトリの削除