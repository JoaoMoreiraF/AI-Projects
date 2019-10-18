import re
import string

expressãoRegular = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ']+"

texto = open('shakespeare.txt').read().lower()

texto2 = re.findall(expressãoRegular, texto)

def bigrama(texto, palavras_count, anterior):
    palavras_count = 0
    anterior = 0

    




