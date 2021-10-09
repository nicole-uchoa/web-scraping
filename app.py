from urllib.request import urlopen
from bs4 import BeautifulSoup
import wget

html = urlopen("https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss")
pag1 = BeautifulSoup(html, 'html.parser')
link1 = pag1.find('a', {'class':'alert-link internal-link'}).get('href')
html2 = urlopen(link1)
pag2 =  BeautifulSoup(html2, 'html.parser')
link2 = pag2.find('a', {'class':'btn btn-primary btn-sm center-block internal-link'}).get('href')

wget.download(link2)
print(link2)

