
class Piloto:
    def __init__(self,id,permanentNumber,code,team,firstName,lastName,dateOfBirth,nationality):
        self.id = id
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality

    def mostrar(self):
        print(self.id,self.permanentNumber,self.code,self.team,self.firstName,self.lastName,self.dateOfBirth,self.nationality)
        