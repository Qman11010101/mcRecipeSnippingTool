import os
import PIL.Image
import os.path
import random
import glob
import shutil


if os.path.exists('pictures') == False:
    os.mkdir('pictures')

if os.path.exists('pictemp') == False:
    os.mkdir('pictemp')

while glob.glob('*.png') != []:
    files = []
    files = glob.glob('*.png')

    rdcf = random.choice(files)

    imga = PIL.Image.open(rdcf)
    boxa = (304, 110, 544, 230)
    imca = imga.crop(boxa)
    imca.save('pictures/u_'+rdcf)

    imgb = PIL.Image.open(rdcf)
    boxb = (304, 240, 544, 360)
    imcb = imgb.crop(boxb)
    imcb.save('pictures/l_'+rdcf)

    shutil.move(rdcf, 'pictemp/'+rdcf)

os.chdir('./pictemp')

while glob.glob('*.png') != []:
    filesa = []
    filesa = glob.glob('*.png')
    rdcfa = random.choice(filesa)
    shutil.move(rdcfa, '../'+rdcfa)

os.chdir('../')
os.rmdir('./pictemp')