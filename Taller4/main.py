class Carro:
    puertas=4
    carros=0

    def __init__(self, referencia, peso = 4, marca = "Ford", motor = None):
        self._referencia = referencia
        self._peso = peso #Peso en toneladas
        self._marca = marca
        self._motor = motor
        Carro.carros=Carro.carros+1

    def getPeso(self):
        return self._peso

    def getReferencia(self):
        return self._referencia

    @staticmethod
    def carro_mas_pesado(carros):
        aux_ref=carros[0].getReferencia()
        aux_peso=carros[0].getPeso()
        for carro in carros:
            if (carro.getPeso() > aux_peso):
                aux_ref=carro.getReferencia()
                aux_peso=carro.getPeso()

        return aux_ref

if __name__ == "__main__":
    carro0=Carro(" ")
    carro1=Carro("Tracker")
    carro2=Carro("Sandero Stepway", 3 ,"Renault","v8")
    carro3=Carro("Picanto", 2,"Kia")

    print(Carro.carro_mas_pesado([carro1, carro2 ,carro3]))
#a) ¿Cuál es el peso del carro1? Explique porque
# Rta/ El peso del carro1 es 0 dado que en los argumentos no se especifica el valor del peso. Por ende se inicializa el valor en 0 dado que es un dato numérico
#b) ¿Cuál es el motor del carro3? Explique porque
# Rta/ El motor del carro3 es None. Porque de acuerdo con la definición de la clase el atributo motor se inicializa en None y adicionalmente en los argumentos de carro3 no se especifica el motor.
#c) ¿Cuál es la marca del carro0 ( En caso de que este no estuviera comentado en la línea 30)?
#Justifique lo que sucede
# Rta/ La marca de carro0 es Ford dado que es el valor del atributo por defecto que se define en la clase Carro. Esto sucede dado que no se especifican argumentos y se toma el valor por defecto definido en la clase.
#d) ¿Qué imprime la línea 35? Justifique
# Rta/ La línea 35 imprime aquel carro cuyo peso es el máximo entre los tres carros: carro1, carro2 y carro3 del arreglo. En este caso el método definido carro_mas_pesado de manera iterativa por el ciclo for busca comparar y almcacenar mediante el atributo peso de cada instancia aquel que sea mayor al que se guarda como quien tiene el peso máximo, esto sucede una y otra vez hasta que encuentra y nos dice la referencia cuyo peso es el mayor de todos. Es así como imprime Stepway como el carro cuya referencia tiene el mayor peso.
#- Modifique el constructor de la clase de la siguiente manera:
#Linea original
#- def init (self, referencia, peso = 1, marca = "Ford", motor = None):
#Linea nueva
#- def init (self, referencia, peso = 4, marca = "Ford", motor = None):
#e) ¿Qué imprime la línea 35 después del cambio? Explique
# Rta/ Con la modificación del constructor de la clase la línea 35 imprime aquel carro cuyo peso es el mayor. Al modificar los argumentos, más especificamente el peso a un valor de 4 aquellas instancias creadas que no espefician el valor de peso en sus argumentos toman el valor de peso = 4 por defecto. Es así como al imprimir nuevamente la línea 35 se obtiene el resultado de Tracker en lugar de Stepway como se veía anteriormente.
#f) ¿Cómo modificar el constructor de Carro, para que pueda recibir indefinido número de parámetros
# Rta/ En este caso podemos hacer uso de argumentos variables como *args y **kwargs. Con ellos es posible recibir un número indefinido de parámetros bien sean palabras clave o no sean palabras clave (keywords and non-keyworded arguments). Se debe tener en cuenta que **kwargs se maneja como diccionario.
#g) Revisa el siguiente código e identifique los errores que vea en el hasta que logre correrlo, luego de esto responda las siguientes preguntas

class Punto:
    def __init__(self, x, y=0, *args, **kwargs):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, radio, *args, **kwargs):
        self.radio = radio
        self.punto = Punto(*args,**kwargs)


cir = Circulo(10,1,1,2,3,4)
print(cir.radio)
print(cir.punto.x)
print(cir.punto.y)

#h) ¿Qué sucede si elimino el argumento *kwargs de las clases?
# Rta/ Al el argumento **kwargs se generan los resultados que se esperan 10, 1, 1. No se generan cambios. Si se elimina el argumento *args se produce error, porque se están ingresando más argumentos que los que la clase tiene por definición en el constuctor.
#i) ¿Si en la clase Circulo envió mas de 3 atributos esto ocasionaría un error? En caso que si como soluciono este utilizando *args o *kwargs
#Rta/ Sí, se ocasionaría error ya que la clase circulo llama la clase punto. Esta clase no cuenta con arugmentos *args ni **kwargs. Este error es posible de solucionar al agregar estos agrumentos en el constructor de la clase punto.
