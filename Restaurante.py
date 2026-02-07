from Modelos.Avaliacao import Avaliacao

class Resturante:
    resturantes = []

    def __init__(self, nome, categoria):                    #    Métodos especiais
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avalicao = []
        Resturante.resturantes.append(self)

    def __str__(self):                                      #    Métodos especiais
        return f'{self._nome} | {self._categoria} | {self._cliente}'
    
    @classmethod
    def listar_restaurentes(cls):                           #    Métodos próprios
        print(f'{'Nome do Restaurante':<25} | {'Categoria do Restaurante':<25} | {'Clientes':<25} | {'Avaliação':<25} | {'Status'}')
        for restaurante in cls.resturantes:
            print(f'{restaurante._nome:<25} | {restaurante._categoria:<25} | {restaurante.nome_clientes:<25} | {restaurante.media_avaliacoes:<25} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'
    
    def alternar_estado(self):                               #    Métodos para os objetos            
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):              #    Métodos próprios
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avalicao.append(avaliacao)

    @property
    def media_avaliacoes(self):                             #    Métodos próprios
        if not self._avalicao: return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avalicao)
        quantidade_de_notas = len(self._avalicao)
        media = round(soma_das_notas / quantidade_de_notas, 1) # (1 = quantidade de casas decimais)
        return media


    @property
    def nome_clientes(self):
        if not self._avalicao:
            return '-'
    
        nome = [f'{pessoa._cliente}'for pessoa in self._avalicao]
        return ''.join(nome)

            