
class Mem:

    def __init__(self, Q, Sigma, delta, q0):
        self.Q = Q  # Estados possíveis. OPCIONAL
        self.Sigma = Sigma  # Alfabeto do autômato. (Símbolos que seu autômato irá ler)
        self.delta = delta  # Representação de transição de estados e output da transição.
        self.q0 = q0  # Estado inicial

    def run(self, w):
        q = self.q0
        output = ''
        try:
            while w != "":
                output += self.delta[q, w[0]][0]
                q = self.delta[(q, w[0])][1]
                w = w[1:]
            return print(f"{output}\n")
        except KeyError:
            print(f"\nERRO na criação do autômato: Símbolo não listado/Estado Inesistente \n")

    def runMore(self):
        while True:
            w = input("Input: ")
            if w == "":
                break
            else:
                Mem.run(self, w)

        def __repr__(self):
            return f"""---Mearly Machine (Deterministic finite automaton)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
    Transição dos estados e output: {self.delta}\nEstado inicial: {self.q0}\n"""


# O valor de cada chave em delta é ('Valor do output', Próximo estado)
Mem0 = Mem({0, 1, 2}, {'0', '1'},
           {(0, '0'): ('0', 1), (0, '1'): ('0', 2),
            (1, '0'): ('0', 1), (1, '1'): ('1', 2),
            (2, '0'): ('1', 1), (2, '1'): ('0', 2)},
           0)

Mem1 = Mem({0, 1, 2, 3, 4}, {'0', '1'},
           {(0, '0'): ('1', 1), (0, '1'): ('1', 2),
            (1, '0'): ('0', 3), (1, '1'): ('1', 2),
            (2, '0'): ('0', 1), (2, '1'): ('0', 3),
            (3, '0'): ('1', 4), (3, '1'): ('0', 4),
            (4, '0'): ('1', 4), (4, '1'): ('0', 4)},
           0)

Mem2 = Mem({0}, {'0', '1'},
           {(0, '0'): ('00', 0), (0, '1'): ('11', 0)},
           0)

