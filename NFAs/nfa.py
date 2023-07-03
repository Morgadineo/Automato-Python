class NFA:

    def __init__(self, Q, Sigma, delta, S, F):
        self.Q = Q  # Conjunto de estados
        self.Sigma = Sigma  # Conjunto de símbolos
        self.delta = delta  # Relação de transição
        self.S = S  # Lista de estados iniciais possíveis
        self.F = F  # Lista de estados finais possíveis

    def __repr__(self):
        return f"""---NFA (Non-deterministic finite automaton)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
Transição dos estados: {self.delta}\nEstados iniciais: {self.S}\nEstados finais: {self.F}"""

    def do_delta(self, q, x):
        try:
            return self.delta[(q, x)]
        except KeyError:
            return set({})

    def run(self, w):
        P = self.S
        while w != "":
            Pnew = set({})
            for q in P:
                Pnew = Pnew | self.do_delta(q, w[0])
            w = w[1:]
            P = Pnew
        return print(f"{(P & self.F) != set({})}\n")

    def runMore(self):
        while True:
            w = input("Input: ")
            if w == "":
                break
            else:
                NFA.run(self, w)

    def DFA(self):
        pass


# Automato de exemplo
N0 = NFA({0, 1, 2}, {"0", "1"},  # Estados possíveis / Alfabeto
         {(0, "0"): {0},  # Relação de transição
          (0, "1"): {0, 1},
          (1, "0"): {2},
          (1, "1"): {2}},
         {0},  # Estado inicial
         {2})  # Estado final

# Automato "a" e "b" com 2 entradas para "a" onde o input deve terminar com "a"
N1 = NFA({0, 1, 2}, {"a", "b"},  # Estados possíveis / Alfabeto
         {(0, "a"): {0, 1},  # Relação de transição
          (0, "b"): {2},
          (1, "a"): {0, 1},
          (1, "b"): {2},
          (2, "b"): {2},
          (2, "a"): {3}},
         {0, 1},  # Estado inicial
         {3})  # Estado final

