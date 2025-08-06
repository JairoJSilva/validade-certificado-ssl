📄 Documentação – Verificação e Relatório de Certificados SSL
📌 Objetivo do Script
Esse script Python automatiza o processo de verificação de validade de certificados SSL de serviços web listados em um arquivo (urls.txt), gera um relatório contendo as datas de início e expiração de cada certificado, e envia esse relatório por e-mail para um destinatário definido.

⚙️ Visão Geral do Funcionamento
Leitura de URLs a partir de um arquivo (urls.txt)

Conexão segura via SSL com cada host (porta 443)

Extração das informações do certificado (data de emissão e expiração)

Montagem de um relatório descritivo

Envio do relatório por e-mail através do servidor SMTP definido nas configurações

📁 Estrutura dos Arquivos
Arquivo	Finalidade
script.py	Código-fonte principal do verificador/enviador
urls.txt	Lista de domínios ou hosts (um por linha) a serem verificados
 
✉️ Configurações de E-mail
Dentro do script, configure os seguintes parâmetros:

Variável	Descrição
EMAIL_REMETENTE	Conta que será usada para enviar o e-mail
EMAIL_DESTINATARIO	Conta que receberá o relatório
EMAIL_SENHA	Senha de aplicativo do remetente
SERVIDOR_SMTP	Servidor SMTP
PORTA_SMTP	Porta de conexão (587 para STARTTLS típico)
 
⚠️ Importante: utilize sempre SENHAS DE APLICATIVO para maior segurança.

🔍 Funções Principais
check_ssl_certificate(hostname)
Estabelece uma conexão SSL com o host na porta 443.

Coleta o certificado digital apresentado pelo servidor.

Converte as datas (notBefore, notAfter) para o formato DD-MM-YYYY.

Retorna (data_inicio, data_vencimento) ou uma mensagem de erro.

send_email(subject, body)
Monta o corpo do e-mail (texto simples).

Realiza autenticação e envio via SMTP.

Pode ser usada para envio do relatório final ou alertas de erro.

main()
Lê as URLs do arquivo urls.txt.

Insere um texto institucional explicativo no início do relatório.

Para cada URL chama check_ssl_certificate() e compõe o relatório.

Por fim chama send_email() enviando o relatório completo.

📝 Exemplo de Conteúdo do urls.txt
 
CopiarEditar
google.com meusite.com.br exemplo.org
🚀 Como Executar
Instale o Python 3.x na máquina.

Instale dependências (opcional, já são nativas do Python):

bash
CopiarEditar
pip install --upgrade pip
Coloque o arquivo urls.txt no mesmo diretório do script.

Edite as configurações de e-mail no topo do script.

Execute:

bash
CopiarEditar
python script.py
✅ Resultados Esperados
Caso tudo esteja correto, o destinatário receberá um e-mail com um relatório semelhante a:

markdown
CopiarEditar
Segue abaixo o relatório com a validade dos certificados digitais vinculados aos serviços WEB da Urbana-PE... -------------------------------------------------- URL: google.com Início da validade: 10-06-2024 Vencimento: 05-09-2024 -------------------------------------------------- URL: meusite.com.br Status: Erro: [descrição do erro] --------------------------------------------------
🔐 Boas Práticas de Segurança
Nunca versionar scripts com senhas. Use variáveis de ambiente.

Utilize senha de app para autenticação SMTP.

Considere rodar o script periodicamente via cron (Linux) ou Agendador de Tarefas (Windows).

📅 Agendamento
Para deixar agendado a execução do script semanalmente inclua a linha abaixo no cron.

cron
CopiarEditar
0 8 * * * /usr/bin/python3 /caminho/script.py
