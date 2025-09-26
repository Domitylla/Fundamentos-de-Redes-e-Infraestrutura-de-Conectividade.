class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def get_maior_lado(self):
        return max(self.lado_a, self.lado_b, self.lado_c)

    def equilatero(self):
        return self.lado_a == self.lado_b == self.lado_c

    def isosceles(self):
        lados = [self.lado_a, self.lado_b, self.lado_c]
        return len(set(lados)) == 2

    def escaleno(self):
        lados = [self.lado_a, self.lado_b, self.lado_c]
        return len(set(lados)) == 3