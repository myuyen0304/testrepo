'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''
import Rectangle as rect
menu = {
    1: '1- Đọc dữ liệu từ file input.db',
    2: '2- Thêm mới hình chữ nhật',
    3: '3- Hiển thị danh sách hình chữ nhật',
    4: '4- Lưu danh sách hình chữ nhật xuống file demo4output.db',
    'Others': 'Thoát'
}
def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])
while(True):
    print_menu()
    chon = ''
    try:
        chon = int(input('Nhap tuy chon:'))
    except:
        print('Nhap sai dinh dang, hãy nhap lai: ')
        continue
    #Kiem ttra cac lua chon
    if chon == 1:
        #Doc du lieu tu file input.db
        fr = open('D:\\Ky 1 Nam 3\\LTPTDL1\\Thuc hanh\\Lab1\\hcn\\input.db', mode='r',encoding='utf-8')
        dsHCN = []
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        fr.close()
    elif chon == 2:
        #Them moi hinh chu nhat
        cr = float(input('Nhap chieu rong: '))
        cd = float(input('Nhap chieu dai: '))
        hcn = rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif chon == 3:
        #Hien thi danh sach hinh chu nhat
        if dsHCN.count == 0:
            print('Danh sach hinh chu nhat rong')
        else:
            for item in dsHCN:
                item.display()
    elif chon == 4:
        #Luu danh sach hinh chu nhat xuong file demo4output.db
        fw = open('D:\\Ky 1 Nam 3\\LTPTDL1\\Thuc hanh\\Lab1\\hcn\\demo4output.db', mode='w', encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
    else:
        print('Ket thuc chuong trinh')
        break