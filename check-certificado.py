import ssl
import socket
from datetime import datetime

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

def main():
    """
    Função principal que lê as URLs de um arquivo e exibe os resultados.
    """
    # Define o nome do arquivo de texto com a lista de URLs
    arquivo_urls = "urls.txt"
    
    try:
        with open(arquivo_urls, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]  # Lê cada linha, remove espaços e linhas vazias
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_urls}' não foi encontrado.")
        return
        
    print("Verificando certificados SSL para as URLs listadas no arquivo...")
    print("-" * 50)
    
    for url in urls:
        inicio, vencimento = check_ssl_certificate(url)
        
        if inicio and vencimento and not "Erro" in vencimento:
            print(f"URL: {url}")
            print(f"  Início da validade: {inicio}")
            print(f"  Vencimento: {vencimento}")
            print("-" * 50)
        else:
            print(f"URL: {url}")
            print(f"  Status: {vencimento}")
            print("-" * 50)

if __name__ == "__main__":
    main()
