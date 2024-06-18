# Guia de Configuração do Ambiente Docker para Django com PostgreSQL e Prometheus

## Passo 1: Preparando o ambiente

Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

## Passo 2: Preparar o ambiente Docker

### 2.1 Criar Diretório do Projeto

Crie um diretório para o seu projeto e navegue até ele:

```bash
mkdir apiCinema
cd apiCinema
```
### 2.2 Clonar o Projeto
Clone o projeto dentro do diretório criado anteriormente:

```bash
git clone https://github.com/Andre-Scalabrini/DockerComposeDjango.git
```

## Passo 3: Iniciar o projeto
Acesse o diretório do projeto que foi clonado:

```bash
cd "apiCinema"
```
Após acessar o diretório, inicie os containers e aguarde o fim do processo:

```bash
docker-compose up -d
```
Após o fim do processo, verifique se os containers estão rodando:

```bash
docker ps
```
## Passo 4: Configurar o Django


### 4.1 Aplicar Migrações
Acesse o contêiner do Django:

```bash
docker-compose exec web bash
```
Dentro do contêiner, aplique as migrações:

```bash
python manage.py migrate
```
### 4.2 Criar Superusuário
Ainda dentro do contêiner do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```
### 4.3 Acessar a Aplicação Django
Abra o navegador e acesse http://localhost:8000 para ver a aplicação Django em funcionamento.

Acesse a administração do Django em http://localhost:8000/admin e faça login com o superusuário criado.

## Passo 5: Verificar o Prometheus
### 5.1 Acessar o Prometheus
Abra o navegador e acesse http://localhost:9090 para verificar o Prometheus e suas métricas.

## Conclusão
Este guia detalha os passos necessários para configurar um ambiente Docker para uma aplicação Django com PostgreSQL e Prometheus. Siga cuidadosamente cada etapa para garantir uma instalação e configuração bem-sucedidas.
