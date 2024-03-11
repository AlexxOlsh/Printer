from classes import Document, InkjetPrinter, LaserPrinter


if __name__ == '__main__':
    answer = None
    while answer != 0:
        try:
            answer = int(input('На каком принтере напечатать документ? \n 1: Лазерный \n 2: Струйный \n 0: Выйти \n'))
            doc = Document('Some text')
            if answer == 1:
                laser = LaserPrinter()
                print(doc.print_document(laser))
            if answer == 2:
                ink = InkjetPrinter()
                print(doc.print_document(ink))
        except ValueError:
            print('Введите число! \n')


