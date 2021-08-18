#probandoclase
#declaracion de la clse
class Jarra:
    #metodo inicial de la clase el cual permite una vez instanciado el objeto o llamado construir el mismo con valores
    #definidos por defecto
    
    def __init__(self):
        #estamos declarando los atributos o caracteristicas que va a tener siempre disponible una instancia de nuestra clase
        #se le pone self delante para poder hacer referencia a ese dato desde cualquier lugar de mi codigo que instancie a esa clase
        self.altura = int(input('Altura de la jarra en cm '))#donde quiera que use el atributo self.altura hare referencia a lo pasado por parametro
        self.ancho = int(input('Ancho de la jarra en cm '))
        self.largo = int(input('Largo de la jarra en cm'))
        self.color = input('Color de la jarra')
        print(f'Esta creando una jarra {self.color} y de las siguientes dimensiones {self.altura} x {self.largo} x {self.ancho}')
    #ahora tendremos los metodos o funciones de la clase lo que podemos hacer con esta plantilla cada  vez que la instanciemos
    def beber(self): #todas las funciones creadas dentro de la clase deben tene como primer argumento o parametro self
    #para poder llamarla desde cualquier lugar como dijimos antes
        volumen = self.altura*self.ancho*self.largo
        print(f'Usted puede beber {volumen} cm cubicos de liquido')

#aqui creamos otra clase otro objeto pero va a heredar de la clase jarra, donde es que vemos la abstraccion aqui 
# desde el punto que utilizamos el objeto o la plantilla y no estamos preocupados en como lo hace y como esta hecho 
#simplemente lo uso a partir de lo que esta hecho

class JarraDeTe(Jarra):
    def plato(self):
        print('tengo plato')
    
    



probar = JarraDeTe()
probar.beber()
probar.plato()