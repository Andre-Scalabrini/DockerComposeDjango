# Utiliza uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /code

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o contêiner
COPY . .

# Expõe a porta que a aplicação irá rodar
EXPOSE 8000

# Define o comando padrão para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
