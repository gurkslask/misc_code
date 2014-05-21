import time, shutil

def main():
    string1 = r'C:\ProgramData\Radius Control Systems\Uni-View\MIRV\Data\Popup\Popup ANA\PFF05_GT12222.txt'
    string2 = r"C:\ProgramData\Radius Control Systems\Uni-View\MIRV\Data\Popup\Popup ANA\\P"
    string3 = r'.BLW'
    with open(string1, mode='r', encoding="ansi") as a_file:#Skriv ner till en fil
        for i in a_file:
            print(i[:-1])
            



if __name__ == '__main__':
    main()