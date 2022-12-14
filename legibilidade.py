#fórmula de Coleman-Liau = 0,0588 * L - 0,296 * S - 15,8
#sendo L a média de letras por 100 palavras e S a média de sentenças por 100 palavras no texto.
from cs50 import get_string
import re

texto = get_string("Digite o texto: ")
#retirar pontuações do texto
res = re.sub(r'[^\w\s]', '', texto)  
palavras = 0
letras = 0
#contar palavras e letras do texto sem pontuação
for i in res.split():
    palavras += 1
    letras = len(i)+letras
#contar sentenças
sentenças = texto.count("?") + texto.count(".") + texto.count("!")
#aplicar fórmula de Coleman-Liau
L = (letras/palavras)*100
S = (sentenças/palavras)*100
nivel = round(0.0588*L-0.296*S-15.8)
#imprimir nível em 3 opções conf. instrução do exercício
if 1 <= nivel <= 16:
    print(f"Nível: {nivel}")
elif nivel < 1:
    print("Nível: Menor que 1")
elif nivel > 16:
    print("Nível: 16+")
    
#a contagem das letras, palavras e sentenças do texto também poderia ser feita conforme abaixo:
letters = 0
words = 1
sentences = 0

for char in texto:
  if char.isalpha():
    letters += 1
  if char.isspace():
    words += 1
  if char == '.' or char == '!' or char == '?':
    sentences += 1
