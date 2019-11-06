import requests
from bs4 import BeautifulSoup
#pegando o link da página que queremos pegar as ifnormações
result = requests.get("https://www.nexojornal.com.br/")
#print(result.status_code)
#print(result.headers)

#achando o conteúdo da pagina score
src = result.content

#trasnformando em um objeto Soup
soup = BeautifulSoup(src, "html")

#Encontrando todos os conteúdos com "a"
#links que queremos
urls = []
for b in soup.find_all("a"):
    print(b)
    print("\n")
    urls.append(b.get("href"))
    
    #loop das notícias e baixar o conteúdo da notícia, 
        
def palavraschaves(*args):
    text = 'asdfasdfasdfa'
    for i in args:
        if str(i) in text:
            print(i, 'está na noticia')
        else:
            print(i, 'nao esta')


    #urls.append(z.find["href"])

print(urls)

#print(links)
#print("\n")
"""
for i in links:
    if "Bolsonaro" in i.text:
        print(i)
        # o i tem um atributo em específico href, e da o conteúdo desse em espec[ifico]
        print(i.attrs["href"])
"""

a_tag = soup.find_all("a")
print(a_tag)
