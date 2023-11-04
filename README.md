# WebScraping

Este é um projeto pessoal que visa a coleta de dados financeiros de empresas listadas na bolsa de valores B3 (antiga Bovespa) no site Infomoney. O projeto foi desenvolvido em Django e utiliza a biblioteca BeautifulSoup para fazer a raspagem de dados.

## Visão Geral do Projeto

O projeto consiste em três principais funcionalidades:

1. Listagem de URLs: Os usuários podem visualizar uma lista de URLs que representam as páginas de empresas e ações na bolsa. Cada URL é construída com base nos dados inseridos pelo usuário (nome da empresa e nome da ação).

2. Cadastro de URLs: Os usuários podem cadastrar novas URLs. Ao fornecer o nome da empresa e o nome da ação, o sistema cria a URL da página correspondente no site Infomoney e a salva no banco de dados.

3. Raspagem de Dados: O sistema realiza raspagem de dados financeiros das páginas das empresas e ações cadastradas. Os dados raspados incluem informações como o título, valor da ação, variação, mínimo do dia, máximo do dia e volume de negociação. As informações raspadas são então apresentadas ao usuário.

## Configuração e Execução

Para executar este projeto em sua própria máquina, siga estas etapas:

1. Certifique-se de ter Python e Django instalados em seu ambiente.

2. Clone este repositório em sua máquina:


```
git clone 
cd 
```

3. Instale as dependências necessárias, incluindo o Django e BeautifulSoup:

```
pip install django
pip install beautifulsoup4
pip requests
```

4. Realize as migrações do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```
6. Acesse o aplicativo em seu navegador em http://localhost:8000/.

## Uso do Aplicativo

1. Acesse a página inicial do aplicativo.
2. Você verá as urls disponiveis para uso(http://127.0.0.1:8000/lista_urls/,http://127.0.0.1:8000/cadastrar_url/,http://127.0.0.1:8000/raspagem_dados/)
3. Para cadastrar uma nova URL, acesse a url(http://127.0.0.1:8000/cadastrar_url/ preencha o formulário com o nome da empresa e o nome da ação e clique no botão "Cadastrar URL" 
4. Após o cadastro, você será redirecionado para a página de raspagem de dados, onde os dados financeiros das empresas cadastradas são exibidos.

## Observações

1. Este projeto é destinado apenas para fins de demonstração e aprendizado
2. Este projeto pode ser estendido adicionando mais funcionalidades, como agendamento de raspagem
