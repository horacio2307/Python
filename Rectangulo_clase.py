class Rectangulo:  #Clase rectangulo

    def __init__(self, _base,_altura) :  #Creador de los atributos de la clase

        self.base=_base     #self.base  toma el valor que le pasamos al prametro _base
        self.altura=_altura

    def area(self):     #Creamos un metodo o funcion de la clase 

        area=self.base*self.altura         #area = multiplicacion de la base y la altura, valores asignados en el creador

        print("El area es :\t", area)

        return area     #La funcion retorna el valor de area

    def perimetro(self):

        perimetro=2*(self.base+self.altura)

        print("El perimetro es :\t", perimetro)

        return perimetro

Figura=Rectangulo(2,3)  #Creamos el objeto *Figura* de la clase *Rectangulo* y le pasamos los paremtros de 2 y 3
Fig=Rectangulo(4,8)
a=Figura.area()     #a=valor retornado por el metodo area del objeto Figura
b=Fig.perimetro()  #b=valor retornado por el metodo perimetro del objeto Fug

print(a+b)
