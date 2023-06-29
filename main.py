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


""" O char passado entre aspas duplas, é o alfabeto do seu Autômato. Você pode alterar ele para outros valores
caso queira outro formato de Input."""

"""Os números passado como 0, 1 e 2 representam os estados do autômato. Eles seguem o modelo do autômato."""

D0 = DFA({0, 1, 2}, {"a", "b"},
         {(0, "a"): 0, (0, "b"): 1,
          (1, "a"): 2, (1, "b"): 1,
          (2, "a"): 2, (2, "b"): 2},
         0,
         {0, 1})

D0.runMore()
