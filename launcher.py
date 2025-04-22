import os
import subprocess

class Launcher:
    def run(self, script_path):
        # Correct the subprocess.run call
        subprocess.run(["python", script_path], check=True)

    def main(self):
        print("Menú:\n" \
        "1. Ejecutar ejercicio 1\n" \
        "2. Ejecutar ejercicio 2\n" \
        "3. Ejecutar ejercicio 3\n" \
        "4. Ejecutar ejercicio 4\n" \
        "5. Salir")
        while True:
            n = input("Seleccione una de las opciones mencionadas antes: ")
            if n == "1":
                self.run("Ej1/main.py")
            if n == "2":
                self.run("Ej2/main.py")
            if n == "3":
                self.run("Ej3/main.py")
            if n == "4":
                self.run("Ej4/main.py")
            if n == "5":
                break