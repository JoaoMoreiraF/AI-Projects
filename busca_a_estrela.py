# Model Estado
class Estado:

    def __init__(self, nome, custo_estimado):
        self.nome = nome
        self.heuristica = 0
        self.custo_estimado = custo_estimado
        self.vizinhos = []

    def addVizinhos(self, vizinhos):
        for i in vizinhos:
            self.vizinhos.append({
                "estado": i[0],
                "custo": i[1],
            })

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "{}: {}".format(self.nome, self.heuristica)


#Funções
def escolher_estado(fronteira):
    menor_custo = fronteira[0]
    for i in fronteira:
        if i['custo'] < menor_custo['custo']:
            menor_custo = i
    fronteira.remove(menor_custo)
    return menor_custo


def busca(estado_inicial, destino):
    fronteira = [{
        'estado': estado_inicial,
        'custo': 0,
        'pai': None
    }]

    explorado = set()

    while True:

        if len(fronteira) <= 0:
            return False

        escolhido = escolher_estado(fronteira)
        explorado.add(escolhido['estado'])

        if escolhido['estado'] == destino:
            return escolhido

        for i in escolhido['estado'].vizinhos:
            custo_caminho = i['custo'] + escolhido['custo'] + i['estado'].custo_estimado

            if i['estado'] in explorado:
                continue

            else:
                flag = False
                for n in fronteira:
                    if i['estado'] == n['estado']:
                        flag = True

                        if n['custo'] > custo_caminho:
                            fronteira.remove(n)
                            fronteira.append({
                                'estado': i['estado'],
                                'custo': custo_caminho,
                                'pai': escolhido
                            })
                            i['estado'].heuristica = custo_caminho

                if not flag:
                    fronteira.append({
                        'estado': i['estado'],
                        'custo': custo_caminho,
                        'pai': escolhido
                    })
                    i['estado'].heuristica = custo_caminho


# BUSCA
joao_pessoa = Estado("João Pessoa", 460)
santa_rita = Estado("Santa Rita", 451)
mamanguape = Estado("Mamanguape", 380)
itabaiana = Estado("Itabaiana", 360)
guarabira = Estado("Guarabira", 340)
areia = Estado("Areia", 316)
campina_grande = Estado("Campina Grande", 300)
picui = Estado("Picui", 250)
soledade = Estado("Soledade", 243)
coxixola = Estado("Coxixola", 232)
patos = Estado("Patos", 122)
monteiro = Estado("Monteiro", 195)
catole_do_rocha = Estado("Catolé do Rocha", 110)
pombal = Estado("Pombal", 55)
itaporanga = Estado("Itaporanga", 65)
sousa = Estado("Sousa", 20)
cajazeiras = Estado("Cajazeiras", 0)

#Adicionando vizinhos
joao_pessoa.addVizinhos([[campina_grande, 125], [itabaiana, 68], [santa_rita, 26]])
santa_rita.addVizinhos([[joao_pessoa, 26], [mamanguape, 38]])
mamanguape.addVizinhos([[santa_rita, 38], [guarabira, 42]])
itabaiana.addVizinhos([[joao_pessoa, 68], [campina_grande, 65]])
guarabira.addVizinhos([[mamanguape, 42], [areia, 41]])
areia.addVizinhos([[guarabira, 41], [campina_grande, 40]])
campina_grande.addVizinhos([[areia, 40], [joao_pessoa, 125], [itabaiana, 65], [coxixola, 128], [soledade, 58]])
picui.addVizinhos([[soledade, 69]])
soledade.addVizinhos([[picui, 69], [campina_grande, 58], [patos, 117]])
coxixola.addVizinhos([[campina_grande, 128], [monteiro, 83]])
patos.addVizinhos([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.addVizinhos([[coxixola, 83], [itaporanga, 224]])
catole_do_rocha.addVizinhos([[pombal, 57]])
pombal.addVizinhos([[catole_do_rocha, 57], [pombal, 71], [sousa, 56]])
itaporanga.addVizinhos([[patos, 108], [monteiro, 108], [cajazeiras, 121]])
sousa.addVizinhos([[pombal, 56], [cajazeiras, 43]])
cajazeiras.addVizinhos([[itaporanga, 121], [sousa, 43]])

estado = busca(joao_pessoa, cajazeiras)

caminho = []

while estado is not None:
    caminho.append(estado['estado'])
    estado = estado['pai']

caminho.reverse()

print(caminho)