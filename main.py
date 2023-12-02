import pypandoc
from pypandoc.pandoc_download import download_pandoc
download_pandoc()

output = pypandoc.convert_file('Teste.odt','epub', outputfile = 'teste.epub')
