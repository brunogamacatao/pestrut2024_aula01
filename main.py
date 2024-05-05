import os

cabecalho = '''
<html>
  <head><title>Album gerado em Python</title></head>
  <body>
    <h1>%s</h1>
    <ul>
'''

corpo = '<li><a href="fotos/%s"><img src="fotos/%s" width="200px"/></a></li>'

rodape = '''
    </ul>
  </body>
</html>
'''

nome  = input('Qual o nome do album? ')
pasta = input('Qual a pasta das imagens? ')

html = cabecalho % nome

for arquivo in os.listdir(pasta):
  html += corpo % (arquivo, arquivo)

html += rodape

arquivo = open('album.html', 'w')
arquivo.write(html)
arquivo.close()