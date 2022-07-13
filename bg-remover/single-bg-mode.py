import _main_

dr = _main_.getpath()
pics = _main_.getpicslist(dr)
if 'result' not in os.listdir(dr):
    os.mkdir(dr+'result')
    
print('\nНачало обработки\n')
back = Image.open(dr+pics[0])
for i in range(1, len(pics)):
    a=time.time()
    pose = Image.open(dr+pics[i])
    new = _main_.remove(pose,
                 back)
    new.save(dr+'result\\' + pics[i])
    times.append(time.time()-a)
    print('Обработана картинка №' + str(i) + ' из ' + str(len(pics)-1) + ' (' + pics[i] + ')\n')

print('Все картинки обработаны')