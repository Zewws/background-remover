import main.py
dr = getpath()
pics = getpicslist(dr)
if len(pics)%2 != 0:
    raise CustomError('Количество картинок и фонов не совпадает')
if 'result' not in os.listdir(dr):
    os.mkdir(dr+'result')
    
j=0
print('\nНачало обработки\n')
for i in range(0, len(pics), 2):
    j+=1
    pose = Image.open(dr+pics[i])
    back = Image.open(dr+pics[i+1])
    new = remove(pose, back)
    new.save(dr+'result\\' + pics[i])
    print('Обработана картинка №' + str(j) + ' из ' + str(int(len(pics)/2)) + ' (' + pics[i] + ')\n')
    
print('Все картинки обработаны')
