class ErrorSalario(Exception):
    def __init__(self, salario):
        self.salario = salario

    def __str__(self):
        return (f"El salario {self.salario} no se encuentra en el rango de 1000 y 2000. ")


def repetir():
    respuesta = input("Si desea validar otra opcion eliga 's', sino presione cualquier tecla ").lower()
    return respuesta  == "s"



def ValidarSalario():
    
    try:
        salario1 = float(input("Porfavor ingrese el salario: "))
        if salario1 < 1000 or salario1 > 2000:
            raise(ErrorSalario(salario1))
           
        else:
            print ("salario correcto")


    except ValueError:
        print("Profavor ingrese un salario valido")

   

    except Exception as e:
        print ("ha ocurrido un error", e)




def main():

    while True:   
        ValidarSalario()
        if not repetir():
            break
        
 

main()