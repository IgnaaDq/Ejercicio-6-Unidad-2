
class ViajeroFrecuente:
	__numero_viajero = ""
	__DNI = ""
	__Nombre = ""
	__millas_acum = 0

	def __init__(self,num,dni,nom,millas):
		self.__numero_viajero = num
		self.__DNI = dni
		self.__Nombre = nom
		self.__millas_acum = int(millas)

	def getnum(self) :
		return self.__numero_viajero

	def getdni(self):
		return self.__DNI

	def getnombre(self):
		return self.__Nombre

	def getmillas(self):
		return self.__millas_acum

	def cantidadTotaldeMillas (self):
		return self.__millas_acum

	def acumularMillas (self,millas_rec):
		self.__millas_acum = self.__millas_acum + millas_rec
		return self.__millas_acum

	def canjearMillas (self,millas_canjear):
		if(self.__millas_acum >= millas_canjear):
			self.__millas_acum = self.__millas_acum - millas_canjear
			print("\n Se canjearon las millas. Sus millas acumuladas ahora son:{}".format(self.__millas_acum))
		else:
			print("\n Error: No posee suficientes millas para canjear.")
			return self.__millas_acum

	def __gt__(self,otro):
		return self.__millas_acum > otro.__millas_acum

	def __add__(self,cant):
		return ViajeroFrecuente(self.__numero_viajero,self.__DNI,self.__Nombre,self.__millas_acum + cant)

	def __sub__(self,cant):
		return ViajeroFrecuente(self.__numero_viajero,self.__DNI,self.__Nombre,self.__millas_acum - cant)
