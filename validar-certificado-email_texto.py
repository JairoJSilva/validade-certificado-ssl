import ssl
import socket
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURAÇÕES DE E-MAIL ---

EMAIL_REMETENTE = "jairo.silva@urbana-pe.com.br"
EMAIL_DESTINATARIO = "chamados@urbana-pe.com.br"
EMAIL_SENHA = "SUA-SENHA-DE-EMAIL"  # Use uma senha de app, não a senha da sua conta!
SERVIDOR_SMTP = "email-ssl.com.br"
#SERVIDOR_SMTP = "smtplw.com.br"
PORTA_SMTP = 587

def check_ssl_certificate(hostname):
    """
    Verifica o certificado SSL para um determinado hostname e retorna
    a data de início e a data de expiração.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return not_before.strftime('%d-%m-%Y'), not_after.strftime('%d-%m-%Y')
    except Exception as e:
        return None, f"Erro: {e}"

def send_email(subject, body):
    """
    Envia um e-mail com o assunto e corpo fornecidos.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_DESTINATARIO
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP) as server:
            server.starttls()  # Inicia a conexão segura
            server.login(EMAIL_REMETENTE, EMAIL_SENHA)
            server.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, msg.as_string())
        
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

def main():
    """
    Função principal que lê as URLs de um arquivo, gera o relatório e envia por e-mail.
    """
    arquivo_urls = "urls.txt"
    relatorio = []
    
    try:
        with open(arquivo_urls, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        relatorio.append(f"Erro: O arquivo '{arquivo_urls}' não foi encontrado.")
        send_email("Relatório de Certificados SSL - Erro", "\n".join(relatorio))
        return 
        
    # --- NOVO TEXTO ADICIONADO AQUI ---
    
    texto_extra = "Segue abaixo o relatório com a validade dos certificados digitais vinculados aos serviços WEB da Urbana-PE. Favor, verificar as das datas de expiração e, caso algum certificado esteja próximo do vencimento, realizar ou solicitar sua renovação imediata, a fim de garantir a continuidade dos serviços."

    relatorio.append(texto_extra)
    relatorio.append("\n") # Adiciona uma linha em branco para separar o texto do relatório
    
    # ---------------------------------
    
    relatorio.append("Relatório de Certificados SSL:")
    relatorio.append("-" * 50)
    
    for url in urls:
        inicio, vencimento = check_ssl_certificate(url)
        
        if inicio and vencimento and not "Erro" in vencimento:
            relatorio.append(f"URL: {url}")
            relatorio.append(f"  Início da validade: {inicio}")
            relatorio.append(f"  Vencimento: {vencimento}")
            relatorio.append("-" * 50)
        else:
            relatorio.append(f"URL: {url}")
            relatorio.append(f"  Status: {vencimento}")
            relatorio.append("-" * 50)

    # Converte a lista de linhas em uma única string e envia o e-mail
    relatorio_completo = "\n".join(relatorio)
    send_email("Relatório de Certificados SSL", relatorio_completo)

if __name__ == "__main__":
    main()
