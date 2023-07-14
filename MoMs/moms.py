class Mom:

    def __init__(self, Q, Sigma, delta, q0):
        self.Q = Q  # Conjunto de estados possíveis e output
        self.Sigma = Sigma  # Alfabeto do autômato. (Símbolos que seu autômato irá ler)
        self.delta = delta  # Transição de estados
        self.q0 = q0  # Estado inicial

    def run(self, w):
        q = self.q0
        output = '' + self.Q[q]
        try:
            while w != "":
                q = self.delta[(q, w[0])]
                output += self.Q[q]
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
                Mom.run(self, w)

        def __repr__(self):
            return f"""---Mearly Machine (Deterministic finite automaton)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
    Transição dos estados e output: {self.delta}\nEstado inicial: {self.q0}\nEstados finais: {self.F}"""


Mom0 = Mom({0: "0", 1: "0", 2: "0", 3: "1", 4: "1"}, {"0", "1"},
           {(0, "0"): 1, (0, "1"): 2,
            (1, "0"): 1, (1, "1"): 3,
            (2, "0"): 4, (2, "1"): 2,
            (3, "0"): 4, (3, "1"): 1,
            (4, "0"): 1, (4, "1"): 3},
           0)

Mom0.runMore()