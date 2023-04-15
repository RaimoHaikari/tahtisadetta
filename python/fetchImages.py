# %%
# How to Preprocess Images for Text OCR in Python
# https://www.youtube.com/watch?v=ADV-AjAXHdc
from urllib.request import urlopen

import cv2

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Luetaan netistä kuvatiedosto
def url_to_image(url, readFlag = cv2.IMREAD_COLOR):

    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(
        bytearray(resp.read()),
        dtype="uint8"
    )
    image = cv2.imdecode(image, readFlag)

    return image


# Minkä kokoinen pala alkuperäisestä kuvasta leikataan
def get_crop_size(img, targetHeight, targetWidth):

    hRatio = targetHeight / img.shape[0]
    wRatio = targetWidth / img.shape[1]

    cropRatio = hRatio if hRatio > wRatio else wRatio

    cropHeight = int(targetHeight/cropRatio)
    cropHeight = cropHeight if cropHeight < img.shape[0] else img.shape[0]

    cropWidth = int(targetWidth/cropRatio)
    cropWidth = cropWidth if cropWidth < img.shape[1] else img.shape[1]

    return (cropHeight, cropWidth)

# Leikataan kuvasta cropSize parametrin määrittämän alueen kokoinen pala
def crop_image(img, hTarget, wTarget):

    cropSize = get_crop_size(img, hTarget, wTarget)

    y = int((img.shape[0] - cropSize[0]) / 2)
    x = int((img.shape[1] - cropSize[1]) / 2)
    h = cropSize[0]
    w = cropSize[1]

    crop = img[y:y+h, x:x+w]

    return crop

# Kutistetaan kuva tavoitekokokoon
# img = cv2.resize(img, (WIDTH, HEIGHT))
def resize_image(croppedImg, hTarget, wTarget):

    #fx = wTarget / croppedImg.shape[1]
    #fy = hTarget / croppedImg.shape[0]

    return cv2.resize(
        croppedImg,
        (wTarget,hTarget)
    )



hTarget = 900
wTarget = 600

csvFile = "./arvostelut.csv"
movies = pd.read_csv(csvFile)  
# movies = movies[['img','nodeJS']]

movies_dict = movies.to_dict('records')

for r in movies_dict:

    image_file = r['nodeJS']
    saveAs = f"./{r['img']}"

    img = url_to_image(image_file)
    croppedImg = crop_image(img, hTarget, wTarget)
    resizedImg = resize_image(croppedImg, hTarget, wTarget)

    cv2.imwrite(
        saveAs,
        resizedImg
    )



# image_file = "https://m.media-amazon.com/images/M/MV5BZjI4ZWQwYzctMGJlMi00OTE1LWFkNjMtY2VlOGQxZmVhNDYyXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_.jpg"

"""
img = url_to_image(image_file)

croppedImg = crop_image(img, hTarget, wTarget)
resizedImg = resize_image(croppedImg, hTarget, wTarget)

cv2.imwrite(
    "./suede.jpg",
    resizedImg
)

"""





# %%
