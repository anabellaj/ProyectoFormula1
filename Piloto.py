
class Piloto:
    def __init__(self,id,permanentNumber,code,team,firstName,lastName,dateOfBirth,nationality, score):
        self.id = id
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
        self.score = score

    def mostrar(self):
        print(f"Nombre: {self.firstName} {self.lastName}\nFecha de nacimiento: {self.dateOfBirth}\nNacionalidad: {self.nationality}\nCodigo: {self.code}\nPuntaje: {self.score}")