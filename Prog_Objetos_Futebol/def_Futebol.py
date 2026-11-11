from abc import ABC, abstractmethod


class ProfissionalFutebol(ABC):
    def __init__(self,nome,cpf,clube="Sem clube"):
        self.nome = nome
        self.cpf = cpf
        self.clube = clube
    def get_nome(self):
        return self.nome
    def get_cpf(self):
        return self.cpf
    def get_clube(self):
        return self.clube
    def set_nome(self,novo):
        self.nome = novo
    def set_cpf(self,novo):
        novo=str(novo)
        if len(novo) == 11 and novo.isdigit():
            self.cpf = novo
        else:
            print ("O CPF deve ser de 11")
    def set_clube(self,novo):
        self.clube = novo

    @abstractmethod
    def calcular_desempenho(self):
        pass
    @abstractmethod
    def show_all(self):
        pass
class Jogador(ProfissionalFutebol):
    def __init__(self,nome,cpf,posicao,gols_marcados=0,partidas=30,num_camisa=10,clube="Sem clube"):
        super().__init__(nome,cpf,clube)
        self.gols_marcados = gols_marcados
        self.partidas = partidas
        self.posicao = posicao
        self.num_camisa = num_camisa
    def get_gols_marcados(self):
        return self.gols_marcados
    def get_partidas(self):
        return self.partidas
    def get_posicao(self):
        return self.posicao
    def set_gols_marcados(self,novo):
        self.gols_marcados = novo
    def get_num_camisa(self):
        return self.num_camisa
    def set_partidas(self,novo):
        self.partidas = novo
    def set_posicao(self,novo):
        self.posicao = novo
    def set_num_camisa(self,novo):
        self.num_camisa = novo
    def transfer(self,novo):
        print("\nO",self.nome,"saiu do",self.clube,"e se transferiu para o",novo)
        self.clube = novo
    def calcular_desempenho(self):
        desempenho=(self.gols_marcados/self.partidas)
        print("\nA quantidade de gols por partida do jogador é", desempenho)
    def show_all(self):
        print("\nO nome do jogador é:",self.nome)
        print("O cpf do jogador é:",self.cpf)
        print("A posição do jogador é:",self.posicao)
        print("O clube do jogador é:",self.clube)
        print("O numero da camisa do jogador é:",self.num_camisa)
        print("O total de gols marcados é:",self.gols_marcados)
        print("O total de partidas é:",self.partidas)
class Treinador(ProfissionalFutebol):
    def __init__(self,nome,cpf,jogos,vitorias,derrotas,empates=0,clube="Sem clube"):
        super().__init__(nome,cpf,clube,)
        self.jogos = jogos
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.empates = empates
    def get_jogos(self):
        return self.jogos
    def get_vitorias(self):
        return self.vitorias
    def get_derrotas(self):
        return self.derrotas
    def get_empates(self):
        return self.empates
    def set_jogos(self,jogos):
        self.jogos = jogos
    def set_vitorias(self,vitorias):
        self.vitorias = vitorias
    def set_derrotas(self,derrotas):
        self.derrotas = derrotas
    def set_empates(self,empates):
        self.empates = empates
    def calcular_desempenho(self):
        total=self.vitorias+self.derrotas+self.empates
        pontos = (self.vitorias * 3) + self.empates
        calculo = (pontos / (total * 3)) * 100
        print("\nA porcentagem de aproveitamento dele é:",calculo)
    def show_all(self):
        print("\nO nome do tecnico é:",self.nome)
        print("O cpf do tecnico é:",self.cpf)
        print("O clube do tecnico é:",self.clube)
        print("A quantidade de vitorias é:",self.vitorias)
        print("A quantidade de derrotas é:", self.derrotas)
        print("A quantidade de empates é:", self.empates)
    def invicto(self):
        if self.derrotas==0:
            print("\nO treinador está invicto")
        else:
            print("\nO tecnico não esta invicto")