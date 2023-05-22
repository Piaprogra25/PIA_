class Frase:
    def __init__(self,idfrase, texto_frase, autor, stars_calif):
        self.idfrase = idfrase
        self.texto = texto_frase
        self.autor = autor
        self.stars_calif = stars_calif

    def imprimir_info(self):
        print(f"Id Frase: {self.idfrase}")
        print(f"Texto Frase: {self.texto_frase}")
        print(f"Autor: {self.autor}")
        print(f"Calificacion en Estrellas: {self.stars_calif}")

    def stasrs_calif(self):
        
        pass
