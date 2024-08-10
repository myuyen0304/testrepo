import Rectangle as rect 
menu_options = {
    1: 'Them moi hinh chu nhat',
    2: 'Hien thi danh sach hinh chu nhat',
    3: 'Tinh tong dien tich cac hinh chu nhat',
    4: 'Hien thi cac hinh chu nhat co chu vi nho nhat',
    'Other': 'Thoat chuong trinh'
}
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
        
# Khai báo biến lưu trữ những hình chữ nhật
dsHCN = []
while (True):
    print_menu()
    userChoice = ''
    try: 
        userChoice = int(input('Nhap tuy chon: '))
    except:
        print('Nhap sai dinh dang, hay nhap lai: ')
        continue
    #Check what choice was entered and act accordingly
    if userChoice == 1:
        cr = float(input('Nhap chieu rong:'))
        cd = float(input('Nhap chieu dai: '))
        hcn= rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif userChoice == 2:
        for item in dsHCN:
            item.display()
    elif userChoice == 3:
        dientich = 0.0
        for item in dsHCN:
            dientich = dientich + item.area()
        print(f'Tong dien tich la: {dientich}')
    elif userChoice == 4:
        if dsHCN.count == 0:
            print('Danh sach rong')
        else:
            chuvi= dsHCN[0].perimeter()
            for item in dsHCN:
                if chuvi > item.perimeter():
                    chuvi = item.perimeter()
            for item in dsHCN:
                if item.perimeter() == chuvi:
                    item.display()
    else:
        print('Thoat khoi chuong trinh')
        break

