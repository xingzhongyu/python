
from PIL import Image
import os
from fpdf import FPDF
import PIL.ImageOps
 
 
def exif_transpose(img):
    if not img:
        return img
 
    exif_orientation_tag = 274
 
    if hasattr(img, "_getexif") and isinstance(img._getexif(), dict) and exif_orientation_tag in img._getexif():
        exif_data = img._getexif()
        orientation = exif_data[exif_orientation_tag]
        print("方向")
        print(orientation)
        if orientation == 1:
            pass
        elif orientation == 2:
            img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            img = img.rotate(180)
        elif orientation == 4:
            img = img.rotate(180).transpose(PIL.Image.FLIP_LEFT_RIGHT)
        elif orientation == 5:
            img = img.rotate(-90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            img = img.rotate(-90, expand=True)
        elif orientation == 7:
            img = img.rotate(90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
        elif orientation == 8:
            img = img.rotate(90, expand=True)
 
    return img
 
 
def load_image_file(file):
    img = PIL.Image.open(file)
 
    if hasattr(PIL.ImageOps, 'exif_transpose'):
        img = PIL.ImageOps.exif_transpose(img)
    else:
        img = exif_transpose(img)
 
    return img
 
 
def getFileList(dir, Filelist, ext=None):
  
 
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if "jpg" in dir[-3:] or "JPG" in dir[-3:]:
                Filelist.append(dir)
 
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)
 
    return Filelist
 
 
def makePdf(pdfName, dir):  # listPages，以列表形式传入，方便批量合成
    listimage = getFileList(dir, [], "jpg")
 
    pdf = FPDF(orientation='P', unit='mm', format='A4')
 
    for page in listimage:
 
        cover = Image.open(page)
 
        pdf.add_page(orientation='P')
        new_img = load_image_file(page)
 
        width, height = cover.size
        new_img.save(page)
        if width / height > 210 / 297:
            pdf.image(page, x=0, y=0, w=210)
        else:
            left = (210 - 297 / height * width) / 2
            pdf.image(page, x=left, y=0, h=297)
    pdf.output(pdfName, "F")
 
 
if __name__ == '__main__':
    current_path = os.getcwd()
    print("当前目录" + current_path)
    file_list = os.listdir(".") 
    for name in file_list:
        path = os.path.join(current_path, name)
        print("遍历文件夹" + path)
        if os.path.isdir(path):
            print("生成pdf" + path)
            makePdf(name + ".pdf", path)
        else:
            print("跳过" + path)
