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
            print(f"\nERRO: Transição não listada / Símbolo não listado!\n")

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

# Autômato com 3 símbolos onde não importa a ordem.
D3 = DFA({0}, {"a", "b", "c"},
         {(0, "a"): 0, (0, "b"): 0, (0, "c"): 0},
         0,
         {0})

# Autômato com 3 símbolos onde b e c podem vir alternados.
D4 = DFA({0, 1, 2}, {"a", "b", "c"},
         {(0, "a"): 0, (0, "b"): 1, (0, "c"): 1,
          (1, "a"): 2, (1, "b"): 1, (1, "c"): 1,
          (2, "a"): 2, (2, "b"): 2, (2, "c"): 2},
         0,
         {0, 1})

# Autômato com 3 símbolos que permite "abcba". Permite transições de "c" para "b", onde "b" pode ir para "a" e repetir.
D5 = DFA({0, 1, 2, 3}, {"a", "b", "c"},
         {(0, "a"): 0, (0, "b"): 1, (0, "c"): 3,
          (1, "a"): 0, (1, "b"): 1, (1, "c"): 2,
          (2, "a"): 3, (2, "b"): 1, (2, "c"): 2,
          (3, "a"): 3, (3, "b"): 3, (3, "c"): 3},
         0,
         {0, 1, 2})

# Modelo de Autômato retirado da UFMG. Autômato aceita qualquer entrada terminada em 1
D6 = DFA({0, 1, 2}, {"0", "1"},
         {(0, "0"): 0, (0, "1"): 1,
          (1, "0"): 2, (1, "1"): 1,
          (2, "0"): 1, (2, "1"): 1},
         0,
         {1})

# 1) Projete um autômato para reconhecer a linguagem: L = {w ∈ {0, 1}* | w tem um número impar de 1s}

D7 = DFA({0, 1}, {"0", "1"},
         {(0, "0"): 0, (0, "1"): 1,
          (1, "0"): 1, (1, "1"): 0},
         0,
         {1})

# 2) Projete um autômato finito que reconheça a linguagem L = {w ∈ {0, 1}∗ | w contém a sub-cadeia 001}.

D8 = DFA({0, 1, 2, 3}, {"0", "1"},
         {(0, "0"): 1, (0, "1"): 0,
          (1, "0"): 2, (1, "1"): 0,
          (2, "0"): 2, (2, "1"): 3,
          (3, "0"): 3, (3, "1"): 3},
         0,
         {3})

# 3) Projeto um autômato finito que reconheça cadeias, binárias que, quando interpretada como números
# são divisíveis por 6: L = {w ∈ {0, 1}* | w representa um binário divisível por 6. }

D9 = DFA({0, 1, 2, 3, 4, 5}, {"0", "1"},
         {(0, "0"): 0, (0, "1"): 1,
          (1, "0"): 2, (1, "1"): 3,
          (2, "0"): 4, (2, "1"): 5,
          (3, "0"): 0, (3, "1"): 1,
          (4, "0"): 2, (4, "1"): 3,
          (5, "0"): 4, (5, "1"): 5},
         0,
         {0})

D10 = DFA({"a", "b", "c", "d", "e", "f"}, {"0", "1"},
          {("a", "0"): "b", ("a", "1"): "c",
           ("b", "0"): "a", ("b", "1"): "d",
           ("c", "0"): "e", ("c", "1"): "f",
           ("d", "0"): "e", ("d", "1"): "f",
           ("e", "0"): "e", ("e", "1"): "f",
           ("f", "0"): "f", ("f", "1"): "f"},
          "a",
          {"c", "d", "e"})

D10_min = DFA({"a", "b", "c"}, {"0", "1"},
          {("a", "0"): "a", ("a", "1"): "b",
           ("b", "0"): "b", ("b", "1"): "c",
           ("c", "0"): "c", ("c", "1"): "c"},
          "a",
          {"b"})

