class Pa:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # Estados possíveis.
        self.Sigma = Sigma  # Alfabeto do autômato. (Símbolos que seu autômato irá ler)
        self.L = 'Z'
        self.delta = delta  # Representação de transição de estados e output da transição.
        self.q0 = q0  # Estado inicial
        self.F = F

    def run(self, w):
        w += ' '
        q = self.q0
        l = self.L
        try:
            while w != '' or l != '':
                if l[0] == self.delta[(q, w[0])][1]: l = l[1:]
                l = self.delta[q, w[0]][2] + l
                q = self.delta[(q, w[0])][0]
                w = w[1:]
            return print(f"{q in self.F and l == ''}\n")
        except KeyError:
            print(f"False\n")
        except IndexError:
            print("False\n")

    def runMore(self):
        while True:
            w = input("Input: ")
            if w == '':
                break
            else:
                Pa.run(self, w)

        def __repr__(self):
            return f"""---Autômato de Pilha (Pushdown Automata)---\nEstados possiveis: {self.Q}\nAlfabeto: {self.Sigma}
    Transição dos estados: {self.delta}\nEstado inicial: {self.q0}\nPilha inicial: {self.L}"""


Pa0 = Pa({0, 1, 2}, {'a', 'b'},
         {(0, 'a'): (0, '', 'B'), (0, 'b'): (1, 'B', ''), (0, ' '): (2, 'Z', ''),
          (1, 'b'): (1, 'B', ''), (1, ' '): (2, 'Z', '')},
         0,
         {2})

Pa0.runMore()
