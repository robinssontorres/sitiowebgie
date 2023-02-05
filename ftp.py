from ftplib import FTP   

ftp=FTP()
ftp.connect('ftp.gie.pe', 21)
ftp.login('rtorresgie@gie.pe', 'Peru07128020')


#listar archivos

files=ftp.dir()
print(files)

#subir archivos

try:
    ftp.storbinary("STOR", open('/sitiowebgie', 'rb'))
except Exception as e:
    pass    

