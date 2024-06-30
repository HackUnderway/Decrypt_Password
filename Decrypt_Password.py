import PyPDF2
pdfpass=PyPDF2.PdfReader('/home/jeyzeta/Desktop/OSINT1.pdf')
with open('/home/jeyzeta/Desktop/pass.txt','r',encoding='utf8') as f:
    for line in f:
        password = line.strip()
        if pdfpass.decrypt(password) != 0:
            print(f"Contraseña Encontrada!: {password}")
            break