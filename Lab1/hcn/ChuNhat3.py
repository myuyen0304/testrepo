import Rectangle as rect
fr = open('D:\\Ky 1 Nam 3\\LTPTDL1\\Thuc hanh\\Lab1\\hcn\\input.db', mode='r',encoding='utf-8')
listRectangle = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    cr = float(ds[0])
    cd = float(ds[1])
    hcn = rect.Rectangle(cr, cd)
    listRectangle.append(hcn)
fr.close()
fw = open('output.db',mode='w',encoding='utf-8')
for item in listRectangle:
    fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
fw.close()