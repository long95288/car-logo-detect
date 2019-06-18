import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'data/Annotations'  # 标签集路径
txtsavepath = 'data/ImageSets'  # 保存的路径
total_xml = os.listdir(xmlfilepath)  # 所有的xml
# print(total_xml)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data/ImageSets/trainval.txt', 'w') # 训练
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
fval = open('data/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    print(name)
    if i in trainval:
        ftrainval.write(name)  # 只是写入名字
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
