from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club
datosClub = open("data/datos_clubs.txt", "r") 
lista = datosClub.readlines()
lista = [l.replace("\n", "").split(";") for l in lista]
for l in lista:  
    club = Club(nombre = l[0], deporte=l[1], \
        fundacion= l[2])
    # se agrega los objetos
    # a la sesión
    session.add(club)

# Se crean objeto de tipo Jugador
datosJugador = open("data/datos_jugadores.txt", "r") 
lista1 = datosJugador.readlines()
lista1 = [l.replace("\n", "").split(";") for l in lista1]
for l in lista1:  
    club = session.query(Club).filter_by(nombre=l[0]).one()
    jugador = Jugador(nombre = l[3], dorsal= l[2], posicion= l[1], \
        club= club)
    # se agrega los objetos
    # a la sesión
    session.add(jugador)





# se confirma las transacciones
session.commit()
