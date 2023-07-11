
class Mem:

    def __init__(self, Q, Sigma, delta, q0):
        self.Q = Q  # Conjunto de ESTADOS possíveis.
        self.Sigma = Sigma  # Alfabeto do autômato. (Símbolos que seu autômato irá ler)
        self.delta = delta  # Representação de transição de estados. Segue o exemplo do diagrama do automato.
        self.q0 = q0  # Estado inicial

    def run(self, w):
        q = self.q0
        output = ''
        try:
            while w != "":
                output += self.delta[q, w[0]][1]
                q = self.delta[(q, w[0])][0]
                w = w[1:]
            return print(f"{output}\n")
        except KeyError:
            print(f"\nERRO: Transição não listada / Símbolo não listado!\n")

    def runMore(self):
        while True:
            w = input("Input: ")
            if w == "":
                break
            else:
                Mem.run(self, w)

        def __repr__(self):
            return f"""---Mearly Machine (Deterministic finite automaton)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
    Transição dos estados e output: {self.delta}\nEstado inicial: {self.q0}\nEstados finais: {self.F}"""


Mem0 = Mem({0, 1, 2}, {'0', '1'},
           {(0, '0'): (1, '0'), (0, '1'): (2, '0'),
            (1, '0'): (1, '0'), (1, '1'): (2, '1'),
            (2, '0'): (1, '1'), (2, '1'): (2, '0')},
           0)

Mem0.runMore()
