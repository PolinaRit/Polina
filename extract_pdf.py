from PyPDF2 import PdfReader

pdf = 'ПЗ Первый CI-конвейер для Микросервисов.pdf'
reader = PdfReader(pdf)
with open('assignment_text.txt', 'w', encoding='utf-8') as out:
    for p in reader.pages:
        t = p.extract_text()
        if t:
            out.write(t + '\n\n')
print('extracted')
