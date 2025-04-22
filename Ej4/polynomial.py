class Polynomial:
    def __init__(self):
        self.terminos = {}  
    def agregar_termino(self, coef, exp):
        if exp in self.terminos:
            self.terminos[exp] += coef
        else:
            self.terminos[exp] = coef

    def __str__(self):
        if not self.terminos:
            return "0"
        partes = []
        for exp in sorted(self.terminos.keys(), reverse=True):
            coef = self.terminos[exp]
            if coef != 0:
                parte = f"{coef}x^{exp}" if exp != 0 else f"{coef}"
                partes.append(parte)
        return " + ".join(partes)

    def evaluar(self, x):
        return sum(coef * (x ** exp) for exp, coef in self.terminos.items())

    def __add__(self, otro):
        resultado = Polynomial()
        for exp, coef in self.terminos.items():
            resultado.agregar_termino(coef, exp)
        for exp, coef in otro.terminos.items():
            resultado.agregar_termino(coef, exp)
        return resultado
