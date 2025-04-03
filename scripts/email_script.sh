sudo apt-get install mailutils
mail -s "Testes executados com sucesso" $EMAIL_TO

# Verifica se o e-mail foi enviado com sucesso
if [ $? -eq 0 ]; then
    echo "✅ E-mail enviado com sucesso!"
else
    echo "❌ Falha ao enviar o e-mail."
    exit 1  # Para indicar erro no GitHub Actions
fi