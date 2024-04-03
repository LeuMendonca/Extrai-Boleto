import os
from PyPDF2 import PdfReader

listInvoice = os.listdir()
baseDirectory = os.getcwd()

for invoice in listInvoice:

    # Pegando a extensão do arquivo
    arquivo , extensao = os.path.splitext(invoice)

    # Ignorando os arquivos .py da pasta
    if  extensao == '.py':
        continue
    
    fileExtract = PdfReader(f'{baseDirectory}\{invoice}')

    totalPages = len(fileExtract.pages)

    for numPage in range(0,totalPages):
        print('-' * 10 , arquivo , '-' * 10)
        print(fileExtract.pages[numPage].extract_text().split('\n'))