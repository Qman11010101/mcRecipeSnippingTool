#!/usr/bin/env python3

import os
from PIL import Image, ImageChops
import glob
import shutil

print("作業を行っています。このウィンドウが消えるまでお待ち下さい")

# ディレクトリの作成
os.makedirs("recipeImages", exist_ok=True)
os.makedirs("recipepictemp", exist_ok=True)

allimg = glob.glob("*.png")

# レシピ画像とそれ以外を選り分ける
for chosenImg in allimg:
    chkImg = Image.open(chosenImg)
    pxch = chkImg.load()
    colorpx = (198, 198, 198)
    imgwidth, imgheight = chkImg.size  # 画像のWidthとHeightを取得
    if imgwidth == 854 and imgheight == 480:  # 画像サイズが854*480であれば次の判定へ
        if pxch[304, 110] == colorpx and pxch[544, 230] == colorpx and pxch[304, 230] == colorpx and pxch[544, 110] == colorpx:  # 画像の四隅のpxの色を判定
            shutil.copy2(chosenImg, "recipepictemp/" + chosenImg)  # レシピ画像ディレクトリへコピー
    chkImg.close()  # 開いた画像を閉じる

# 作業ディレクトリをレシピ画像ディレクトリにする
os.chdir("./recipepictemp")

# 画像の加工
recipeImages = glob.glob("*")
for chosenRecipeImg in recipeImages:
    # 画像の上側の切り出し
    imgAbove = Image.open(chosenRecipeImg)
    cutImgAbove = (304, 110, 544, 230)
    imgCuttedAbove = imgAbove.crop(cutImgAbove)
    imgCuttedAbove.save("../recipeImages/above_" + chosenRecipeImg)

    # 画像の下側の切り出し
    imgUnder = Image.open(chosenRecipeImg)
    cutImgUnder = (304, 240, 544, 360)
    imgCuttedUnder = imgUnder.crop(cutImgUnder)
    imgCuttedUnder.save("../recipeImages/under_" + chosenRecipeImg)

    # 加工が終わった画像を元の画像ディレクトリへ
    shutil.move(chosenRecipeImg, "../"+chosenRecipeImg)

# あとかたづけ
os.chdir("../")  # 作業ディレクトリを元のディレクトリにする
os.rmdir("./recipepictemp")  # 作業に使ったディレクトリの削除
os.chdir("./recipeImages")
allRecIm = glob.glob("*.png")
genim = Image.new("RGB", (240, 120), (198, 198, 198))
genim.save("match.png", "PNG")
imgmatch = Image.open("match.png")
while allRecIm != []:
    imgcompared = Image.open(allRecIm[0])
    if ImageChops.difference(imgcompared, imgmatch).getbbox() == None:
        os.remove(allRecIm[0])
    allRecIm.pop(0)

os.remove("match.png")
