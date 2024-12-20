from string import Template
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, file in enumerate(photofiles):
    base, ext = os.path.splitext(file)
    newname = t.substitute(d=date, n=i, f=ext)
    print(f"{file} --> {newname}")
