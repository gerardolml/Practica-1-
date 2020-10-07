from functools import reduce


class Matriz:
    _A = None
    _n = 0
    _T = None
    _I = None
    _det = 0
    """Constructor de la clase"""

    def __init__(self, x):
        self._A = [[float(z) for z in y.split(',')] for y in x.split('|')]
        if (len(self._A) == list(set([len(y) for y in self._A]))[0]) and len(set([len(y) for y in self._A])) == 1:
            self._n = len(self._A)
            self.A = self._A
            self.n = self._n
            self.T = self._T
            self.I = self._I
        else:
            print("Matriz erronea")

    def t(self):
        lf = []
        for i in range(self.n):
            lc = []
            for j in range(self.n):
                lc.append(self.A[j][i])
            lf.append(lc)
        self._T = self.T = lf

    @staticmethod
    def show(A):
        print("\n".join(["\t".join([str(y) for y in x]) for x in A]))

    def determinante(self):
        signo = 1
        for i in range(self.n - 2):
            while self.A[i][i] == 0:
                signo = signo * -1
                if self.A[i][i] == 0 and self.A[i + 1][i] != 0:
                    x = [y for y in self.A[i]]
                    self.A[i] = self.A[i + 1]
                    self.A[i + 1] = x
                elif self.A[-1][-1] == 0:
                    x = [y for y in self.A[0]]
                    self.A[0] = self.A[-1]
                    self.A[-1] = x
        A = self.A[:]
        for j in range(self.n - 1):
            for i in range(j + 1, self.n):
                A[i] = [a + b for a, b in zip([-A[i][j] / A[j][j] * x for x in A[j]], A[i])]
        _det = signo * reduce(lambda x, y: x * y, [A[i][i] for i in range(self.n)])
        return _det

    def inversa(self):
        self.I = self.A[:]
        # if det== 0:
        # print("La matriz no tiene inversa")
        for i in range(self.n):
            cero = [0.0] * self.n
            for j in range(self.n):
                if i == j:
                    cero[i] = 1.0
            self.I[i].extend(cero)
        for i in range(self.n):
            while self.I[i][i] == 0:
                if self.I[i][i] == 0 and self.I[i + 1][i] != 0:
                    x = [y for y in self.I[i]]
                    self.I[i] = self.I[i + 1]
                    self.I[i + 1] = x
                elif self.I[-1][-1] == 0:
                    x = [y for y in self.I[0]]
                    self.I[0] = self.I[-1]
                    self.I[-1] = x
            for j in range(self.n):
                if i != j:
                    x = round(self.I[j][i] / self.I[i][i], 5)
                    for k in range(2 * (self.n)):
                        self.I[j][k] = round(self.I[j][k] - x * self.I[i][k], 5)
        for i in range(self.n):
            x = self.I[i][i]
            for j in range(2 * (self.n)):
                self.I[i][j] = round(self.I[i][j] / x, 5)
        self._I = self.I