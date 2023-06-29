import traceback


class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # Conjunto de ESTADOS possíveis.
        self.Sigma = Sigma  # Alfabeto do autômato. (Símbolos que seu autômato irá ler)
        self.delta = delta  # Representação de transição de estados. Segue o exemplo do diagrama do automato.
        self.q0 = q0  # Estado inicial
        self.F = F  # Estados finais

    def run(self, w):
        q = self.q0
        try:
            while w != "":
                q = self.delta[(q, w[0])]
                w = w[1:]
            return print(f"{q in self.F}\n")
        except KeyError:
            print(f"\nERRO: Input fora do alfabeto!\n")

    def runMore(self):
        while True:
            w = input("Input: ")
            if w == "":
                break
            else:
                DFA.run(self, w)

    def __repr__(self):
        return f"""---DFA (Deterministic finite automaton)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
Transição dos estados: {self.delta}\nEstado inicial: {self.q0}\nEstados finais: {self.F}"""


# Automato com 2 símbolos no alfabeto
D0 = DFA({0, 1, 2}, {"a", "b"},
         {(0, "a"): 0, (0, "b"): 1,
          (1, "a"): 2, (1, "b"): 1,
          (2, "a"): 2, (2, "b"): 2},
         0,
         {0, 1})

# Automato com 3 símbolos, onde o símbolo "c" não pode vir depois de "b".
D1 = DFA({0, 1, 2}, {"a", "b", "c"},
         {(0, "a"): 0, (0, "b"): 1, (0, "c"): 0,
          (1, "a"): 2, (1, "b"): 1, (1, "c"): 2,
          (2, "a"): 2, (2, "b"): 2, (2, "c"): 2},
         0,
         {0, 1})

# Automato com 3 símbolos, onde "c" só pode vir depois de "b" e nada deve vir depois de "c"
D2 = DFA({0, 1, 2, 3}, {"a", "b", "c"},
         {(0, "a"): 0, (0, "b"): 1, (0, "c"): 3,
          (1, "a"): 3, (1, "b"): 1, (1, "c"): 2,
          (2, "a"): 3, (2, "b"): 3, (2, "c"): 2,
          (3, "a"): 3, (3, "b"): 3, (3, "c"): 3},
         0,
         {0, 1, 2})
