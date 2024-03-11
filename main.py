from classes import Document, InkjetPrinter, LaserPrinter


if __name__ == '__main__':
    answer = None
    while answer != 0:
        try:
            answer = int(input('На каком принтере напечатать документ? \n 1: Лазерный \n 2: Струйный \n 0: Выйти \n'))
            if answer == 1:
                laser = LaserPrinter()
                doc = Document(laser)
                print(doc.print_document())
            if answer == 2:
                ink = InkjetPrinter()
                doc = Document(ink)
                print(doc.print_document())
        except ValueError:
            print('Введите число! \n')


