import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":
    # Variáveis de ambiente do GitHub Actions
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    email_to = os.getenv('EMAIL_TO')  # Defina o destinatário

    # Caminho para o relatório de testes
    report_path = "test-reports/results.xml"

    # Lê o conteúdo do relatório XML
    try:
        with open(report_path, "r") as file:
            test_results = file.read()
    except FileNotFoundError:
        test_results = "Nenhum relatório de testes encontrado."

    # Criando o e-mail
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_to
    msg["Subject"] = "Relatório de Testes - GitHub Actions"

    # Texto do e-mail
    body = f"""
    Olá,

    Segue o relatório de testes gerado pelo GitHub Actions.

    Resumo:
    - Repositório: {os.getenv('GITHUB_REPOSITORY')}
    - Workflow: {os.getenv('GITHUB_WORKFLOW')}
    - Job: {os.getenv('GITHUB_JOB')}
    - Commit: {os.getenv('GITHUB_SHA')}
    - Autor: {os.getenv('GITHUB_ACTOR')}

    Relatório de Testes:
    {test_results}

    Atenciosamente,
    Pipeline CI/CD
    """

    msg.attach(MIMEText(body, "plain"))

    # Envio do e-mail
    try:
        server = smtplib.SMTP(smtp_server, int(smtp_port))
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, email_to, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
