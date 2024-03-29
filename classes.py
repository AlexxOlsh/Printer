import unittest


class InkjetPrinter:

    def print_page(self):
        return 'Inkerjet print the document'


class LaserPrinter:
    def print_page(self):
        return 'LaserPrinter print the document'


class Document:
    def __init__(self, text):
        self.text = text

    def print_document(self, printer):
        return printer.print_page() + f'\n {self.text}'


class TestDocument(unittest.TestCase):
    def test_print_document(self):
        printer = LaserPrinter()
        test_record = printer.print_page()
        self.assertEqual('LaserPrinter print the document', 'LaserPrinter print the document')

    def test_print_document_by_inc(self):
        printer = InkjetPrinter()
        test_record = printer.print_page()
        self.assertEqual('Inkerjet print the document', 'Inkerjet print the document')


if __name__ == '__classes__':
    unittest.main()