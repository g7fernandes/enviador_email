
# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from getpass import getpass



def sendmail(fromaddr, toaddr, password, subject, body, filename, s_smtp, port_smtp , cc='')
    rcpt = cc.split(",") + toaddr.split(",") + [toaddr]
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    # With Copy
    msg['Cc'] = cc

    
    # storing the subject  
    msg['Subject'] = subject
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    #filename = "teste_anexo.txt"
    attachment = open(filename, "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session GMAIL 'smtp.gmail.com'
    s = smtplib.SMTP(s_smtp, port_smtp) 
    
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, password) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, rcpt, text) 
    
    # terminating the session 
    s.quit() 
    
    
print("Este programa envia emails usando SMTP.\nOs destinatários devem estar num arquivo .csv separado por vírgula na seguinte forma:")    
print("receptor@mail.com,caminho/para/o/arquivo/anexo.pdf\n")
print("Se o aquivo estiver na mesma pasta do programa, será apenas o nome dele.\n")
fromaddr = input("Email do remetente:\n")
print("Entre a senha para {}\n".format(fromaddr))
password = getpass()
adrfile = input("Caminho para o arquivo contendo os emails dos destinatários:\n ")
s_smtp = input("Entre o servidor SMTP: (ex. Gmail: smtp.gmail.com ; Unicamp: smtp.unicamp.br)\n")
port_smtp = input("Entre a porta de SMTP (Unicamp e Gmail: 587)\n")
port_smtp = int(port_smtp)

subject = input("Entre o assunto do email\n")
f = input("Entre o caminho do aquivo de texto .txt com o corpo do email\n")

body_plain = ''
with open(bodyf) as f:
    for line in f:
        body_plain = body_plain + line 


with open(adrfile) as f:
    for line in f:
        dest = line.split(',')
        sendmail(fromaddr, dest[0], password, subject, body_plain, dest[1], s_smtp, port_smtp)
        print("Email enviado para" + dest[0] + "\n")
        
            
print("Concluído!")
        




