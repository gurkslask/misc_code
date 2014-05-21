import time, shutil

def main():
    string1 = r'C:\ProgramData\Radius Control Systems\Uni-View\MIRV\Data\Popup\Popup ANA\PFF05_GT1.BLW'
    string2 = r"C:\ProgramData\Radius Control Systems\Uni-View\MIRV\Data\Popup\Popup ANA\\P"
    string3 = r'.BLW'
    with open(r'C:\temp\MIRV_org_ana.txt', mode='r') as a_file:#Skriv ner till en fil
        for i in a_file:
            print(i[:-1])
            shutil.copy(string1 , string2 + i[:-1] + string3)



if __name__ == '__main__':
    main()