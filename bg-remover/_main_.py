from PIL import Image
import os, time

class CustomError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)
    
def getpath():
    path = input('Путь к папке с картинками: ')
    if ':\\' not in path:
            raise CustomError('Путь введён неправильно. Пример правильного пути: C:\\Users\\User\\Images')
    if path[len(path)-1] != '\\':
        path += '\\'
    try:
        os.listdir(path)
    except FileNotFoundError:
        print('Указанная папка не найдена')
    else:
        return path

def getpicslist(path):
    pics = os.listdir(path)
    i = 0
    while i<=len(pics)-1:
        if '.png' not in pics[i] and '.jpg' not in pics[i]:
            pics.remove(pics[i])
            i-=1
        else:
            i+=1
    if pics == []:
        raise CustomError('В папке ' + path + ' не нашлись картинки')
    if len(pics) == 1:
        raise CustomError('Недостаточно картинок')
    print()
    print(pics)
    for i in pics:
        if '.png' not in i and '.jpg' not in i:
            print(i+' should be deleted from list')
    return pics

def remove(img1, img2):
    size = img1.getbbox()
    if size != img2.getbbox():
        print('Размеры изображений не совпадают')
    else:
        a=time.time()
        for x in range(size[0], size[2]):
            for y in range(size[1], size[3]): 
                if img1.getpixel((x, y)) == img2.getpixel((x, y)):
                    img1.putpixel((x, y), (255, 255, 255))
        print('Фон убран за ' + str(round(time.time()-a, 2)) + 'секунд.')
    return img1
