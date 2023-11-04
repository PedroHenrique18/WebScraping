from django.shortcuts import render,redirect
from .models import URL
from bs4 import BeautifulSoup
import requests



def lista_urls(request):
    urls = URL.objects.all()
    return render(request, 'page.html', {'urls': urls})


def cadastrar_url(request):
    if request.method == 'POST':
        nome_empresa = request.POST['nome_empresa']
        nome_acao = request.POST['nome_acao']

        # Construa a URL com base nos dados recebidos
        url = f'https://www.infomoney.com.br/cotacoes/b3/acao/{nome_empresa}-{nome_acao}/'

        # Salve a URL no banco de dados
        URL.objects.create(url=url)

        return redirect('raspagem_dados')  # Redirecione para a página que lista as URLs após o cadastro

    return render(request, 'cadastrar_url.html')  # Renderize um formulário para o usuário preencher

def raspagem_dados(request):
    # Recupere as URLs do banco de dados
    urls = URL.objects.all()

    dados = []

    for url in urls:
        url_completa = url.url

        # Enviar uma solicitação HTTP GET para a URL
        pagina = requests.get(url_completa)

        # Analisar o conteúdo HTML da página
        site = BeautifulSoup(pagina.content, 'html.parser')

        # Encontrar as informações que deseja extrair
        h1_element = site.find('h1')
        h1_text = h1_element.text.strip()

        line_info = site.find('div', class_='line-info')
        value = line_info.find('div', class_='value').find('p').text.strip()
        variation = line_info.find('div', class_="percentage").find('p').text.strip()
        minimo = line_info.find('div', class_='minimo').find('p').text.strip()
        maximo = line_info.find('div', class_='maximo').find('p').text.strip()
        volume = line_info.find('div', class_='volume').find('p').text.strip()

        # Crie um dicionário com os dados
        dado = {
            'titulo': h1_text,
            'valor': value,
            'variacao': variation,
            'minimo_dia': minimo,
            'maximo_dia': maximo,
            'volume': volume,
        }

        dados.append(dado)

    return render(request, 'dados_raspagem.html', {'dados': dados})
