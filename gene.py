
# coding: utf-8

# In[ ]:





import os

impath = '/ssd/zhenghonghui/FaceRecognition/New_MSCeleb1M_align'

cnt = 0
label = {}
fw1 = open(impath + '_train.txt', 'w')
fw2 = open(impath + '_val.txt', 'w')
for r, d, f in os.walk(impath):
    if len(d) != 0:
        continue

    cls_name = r.split('/')[-1]
    if cls_name not in label:
        label[cls_name] = cnt
        cnt += 1

    for fi in f[:-2]:
        if fi.endswith('.jpg'):
            fw1.write(os.path.join(cls_name, fi) + ' ' + str(label[cls_name]) + '\n')
    for fi in f[-2:]:
        if fi.endswith('.jpg'):
            fw2.write(os.path.join(cls_name, fi) + ' ' + str(label[cls_name]) + '\n')
fw1.close()
fw2.close()

print 'have %d class' % cnt

