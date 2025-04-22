from app import App

if __name__ == "__main__":
    size = int(input("Ingrese la cantidad piedras: "))  
    app = App(size)
    app.run()