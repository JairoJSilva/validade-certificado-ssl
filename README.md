
# 📄 **Documentação – Verificação e Relatório de Certificados SSL**

## 📌 Objetivo

Automatizar a verificação da validade de certificados SSL de serviços web listados em um arquivo (`urls.txt`), gerar um relatório com informações de emissão e expiração dos certificados, e enviar esse relatório por e-mail.

---

## ⚙️ Funcionamento

1. Leitura de URLs a partir do arquivo `urls.txt`
2. Conexão com cada host via SSL (porta 443)
3. Coleta das datas de emissão e expiração do certificado
4. Geração do relatório completo
5. Envio do relatório por e-mail via SMTP

---

## 📁 Estrutura de Arquivos

| Arquivo     | Função                                                         |
|------------|----------------------------------------------------------------|
| script.py   | Código principal do monitor SSL                                |
| urls.txt   | Lista de hosts/domínios para análise (um por linha)             |

---

## ✉️ Parâmetros de Configuração

| Variável              | Descrição                                     |
|-----------------------|-----------------------------------------------|
| `EMAIL_REMETENTE`     | Endereço que enviará o e-mail                  |
| `EMAIL_DESTINATARIO`  | Destinatário do relatório                      |
| `EMAIL_SENHA`         | **Senha de aplicativo** do remetente           |
| `SERVIDOR_SMTP`       | Servidor SMTP para envio                       |
| `PORTA_SMTP`          | Porta de conexão (ex: 587 para STARTTLS)       |

⚠️ **Atenção:** utilize sempre senhas de app geradas pelo provedor.

---

## 🧩 Estrutura do Código

### `check_ssl_certificate(hostname)`
- Conecta ao host via SSL
- Extrai `notBefore` e `notAfter`
- Retorna as datas no formato `DD-MM-YYYY`
- Em caso de erro, retorna mensagem explicativa

### `send_email(subject, body)`
- Monta e envia um e-mail (texto simples)
- Usa autenticação SMTP com STARTTLS

### `main()`
- Lê o arquivo `urls.txt`
- Inclui texto introdutório fixo
- Percorre cada URL aplicando `check_ssl_certificate()`
- Gera relatório formatado
- Envia o relatório por e-mail

---

## 📝 Exemplo de `urls.txt`

