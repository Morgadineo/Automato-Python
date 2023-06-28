import doctest


class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def __repr__(self):
        return f"DFA ({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F}"

    def run(self, w):
        q = self.q0
        while w != "":
            q = self.delta[(q, w[0])]
            w = w[1:]
        return print(q in self.F)


D0 = DFA({0, 1, 2}, {"a", "b"},
         {(0, "a"): 0, (0, "b"): 1,
          (1, "a"): 2, (1, "b"): 1,
          (2, "a"): 2, (2, "b"): 2},
         0,
         {0, 1})

D0.run("abbbb")
