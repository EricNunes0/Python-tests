# mainpy
# Lembrar de adicionar um texto em um arquivo text.txt
from mrjob.job import MRJob
import re
palavra_regex = re.compile(r"[\w']+")

class WordAmount(MRJob):
    def mapper(self, _, line):
        for p in palavra_regex.findall(line):
            yield (p.lower(), 1)

    def reducer(self, p, qtd):
        yield (p, sum(qtd))

if __name__ == "__main__":
    WordAmount.run()
