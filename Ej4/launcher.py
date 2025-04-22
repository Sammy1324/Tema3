from polynomial import Polynomial
import random

class Launcher:

    def create_polynomial(self):
        """Crea un polinomio de forma aleatoria."""
        poly = Polynomial()
        for i in range(3):
            coef = random.randint(1, 10)
            exp = random.randint(0, 5)
            poly.agregar_termino(coef, exp)
        return poly
    
    def substract_polynomial(self, poly1, poly2):
        """Resta dos polinomios."""
        result = Polynomial()
        for exp in poly1.terminos.keys():
            result.agregar_termino(poly1.terminos[exp], exp)
        for exp in poly2.terminos.keys():
            result.agregar_termino(-poly2.terminos[exp], exp)
        return result
    
    def delete_term_from_polynomial(self, poly):
        """Elimina un polinomio."""
        if not poly.terminos:
            return None
        exp = random.choice(list(poly.terminos.keys()))
        del poly.terminos[exp]
        return poly
    
    def find_if_exists_term(self, poly, exp):
        """Verifica si existe un término en el polinomio."""
        return exp in poly.terminos
        
    def main(self):
        """Ejecuta el launcher."""
        poly1 = self.create_polynomial()
        poly2 = self.create_polynomial()
        print(f"Polinomio 1: {poly1}")
        print(f"Polinomio 2: {poly2}")
        
        result = self.substract_polynomial(poly1, poly2)
        print(f"Resta: {result}")
        
        poly1 = self.delete_term_from_polynomial(poly1)
        print(f"Polinomio 1 después de eliminar un término: {poly1}")
        
        exp = random.choice(list(poly2.terminos.keys()))
        exists = self.find_if_exists_term(poly2, exp)
        print(f"¿El término con exponente {exp} existe en el polinomio 2? {'Sí' if exists else 'No'}")