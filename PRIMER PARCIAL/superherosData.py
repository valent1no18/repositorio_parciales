class superheroesMarvel:
    def __init__(self, name, nameReal, año, esVillano, biografia):
        self.name = name
        self.nameReal = nameReal
        self.año = año
        self.esVillano = esVillano
        self.biografia = biografia

    def __str__(self):
        return f"Nombre: {self.name} - Nombre real: {self.nameReal} - Año de aparición: {self.año} - Es villano: {self.esVillano} - Biografia: {self.biografia}"


def order_by_name(personaje):
    return personaje.name 

def order_by_nameReal(personaje):
    return personaje.nameReal

def order_by_año(personaje):
    return personaje.año



personajesMarvel = [
    ("Spider-Man", "Peter Parker", "Adquirió poderes arácnidos tras ser mordido por una araña radiactiva.", 1962, False),
    ("Iron Man", "Tony Stark", "Millonario genio que crea una armadura para salvar su vida y combatir el crimen.", 1963, False),
    ("Captain America", "Steve Rogers", "Soldado mejorado con un suero especial durante la Segunda Guerra Mundial.", 1941, False),
    ("Thor", "Thor Odinson", "Dios del trueno asgardiano que lucha por la justicia en la Tierra y los Nueve Reinos.", 1962, False),
    ("Loki", "Loki Laufeyson", "Dios del engaño, hermano adoptivo de Thor, conocido por su astucia y ambigüedad moral.", 1949, True),
    ("Black Widow", "Natasha Romanoff", "Ex espía rusa que se redime y se une a los Vengadores como heroína.", 1964, False),
    ("Hulk", "Bruce Banner", "Científico que se transforma en un monstruo verde tras exposición a rayos gamma.", 1962, False),
    ("Thanos", "Thanos", "Titán loco que busca el equilibrio universal mediante la destrucción masiva.", 1973, True),
    ("Doctor Strange", "Stephen Strange", "Ex cirujano que se convierte en el Hechicero Supremo.", 1963, False),
    ("Green Goblin", "Norman Osborn", "Empresario corrompido por un suero experimental, enemigo de Spider-Man.", 1964, True),
    ("Wolverine", "Logan", "Mutante con garras retráctiles y factor curativo.", 1974, False),
    ("Magneto", "Erik Lehnsherr", "Mutante con poder de controlar el magnetismo, líder de los mutantes rebeldes.", 1963, True),
    ("Storm", "Ororo Munroe", "Mutante capaz de controlar el clima.", 1975, False),
    ("Cyclops", "Scott Summers", "Líder de los X-Men, dispara rayos ópticos.", 1963, False),
    ("Jean Grey", "Jean Grey", "Mutante con poderes telepáticos y telequinéticos.", 1963, False),
    ("Professor X", "Charles Xavier", "Poderoso telépata, fundador de los X-Men.", 1963, False),
    ("Deadpool", "Wade Wilson", "Mercenario con factor curativo y humor irreverente.", 1991, False),
    ("Venom", "Eddie Brock", "Periodista que se fusiona con un simbionte alienígena.", 1988, True),
    ("Black Panther", "T'Challa", "Rey de Wakanda, guerrero con traje de vibranium.", 1966, False),
    ("Ant-Man", "Scott Lang", "Puede encogerse y comunicarse con hormigas.", 1979, False),
    ("Wasp", "Janet van Dyne", "Puede encogerse y volar, miembro fundadora de los Vengadores.", 1963, False),
    ("Vision", "Vision", "Sintetizoide creado por Ultrón, miembro de los Vengadores.", 1968, False),
    ("Scarlet Witch", "Wanda Maximoff", "Mutante con poderes de alteración de la realidad.", 1964, False),
    ("Quicksilver", "Pietro Maximoff", "Mutante con supervelocidad.", 1964, False),
    ("Ultron", "Ultron", "IA rebelde que busca la extinción humana.", 1968, True),
    ("Falcon", "Sam Wilson", "Aliado de Captain America, vuela con alas mecánicas.", 1969, False),
    ("Winter Soldier", "Bucky Barnes", "Ex compañero de Captain America, convertido en asesino cibernético.", 1941, False),
    ("Hawkeye", "Clint Barton", "Arquero experto, miembro de los Vengadores.", 1964, False),
    ("Nick Fury", "Nick Fury", "Director de S.H.I.E.L.D., coordinador de los Vengadores.", 1963, False),
    ("Groot", "Groot", "Ser arbóreo con capacidad de regeneración.", 1960, False),
    ("Rocket Raccoon", "Rocket", "Mapache modificado, experto en armas y tecnología.", 1976, False),
    ("Gamora", "Gamora", "Asesina entrenada, hija adoptiva de Thanos.", 1975, False),
    ("Drax", "Drax the Destroyer", "Busca venganza contra Thanos por la muerte de su familia.", 1973, False),
    ("Star-Lord", "Peter Quill", "Líder de los Guardianes de la Galaxia.", 1976, False),
    ("Nebula", "Nebula", "Hija adoptiva de Thanos, rival de Gamora.", 1985, False),
    ("Yondu", "Yondu Udonta", "Líder de los saqueadores, figura paterna para Star-Lord.", 1969, False),
    ("Ronan", "Ronan the Accuser", "Acusador Kree, enemigo de los Guardianes.", 1967, True),
    ("Mantis", "Mantis", "Empática con habilidades de combate.", 1973, False),
    ("Shuri", "Shuri", "Hermana de Black Panther, genio de la tecnología.", 2005, False),
    ("Killmonger", "Erik Stevens", "Rival de T'Challa por el trono de Wakanda.", 1998, True),
    ("Red Skull", "Johann Schmidt", "Líder de Hydra, enemigo de Captain America.", 1941, True),
    ("Abomination", "Emil Blonsky", "Enemigo de Hulk, monstruo gamma.", 1967, True),
    ("Sabretooth", "Victor Creed", "Mutante con garras y factor curativo, enemigo de Wolverine.", 1977, True),
    ("Juggernaut", "Cain Marko", "Imparable cuando está en movimiento.", 1965, True),
    ("Beast", "Henry McCoy", "Mutante con fuerza y agilidad sobrehumanas.", 1963, False),
    ("Colossus", "Piotr Rasputin", "Mutante que puede convertir su cuerpo en acero.", 1975, False),
    ("Baron Zemo", "Helmut Zemo", "Enemigo recurrente del Capitán América, líder de los Maestros del Mal.", 1973, True),
    ("Iceman", "Bobby Drake", "Mutante capaz de manipular el hielo.", 1963, False),
    ("Angel", "Warren Worthington III", "Mutante con alas, miembro original de los X-Men.", 1963, False),
    ("Psylocke", "Elizabeth Braddock", "Mutante con poderes telepáticos y habilidades de combate.", 1976, False),
    ("Emma Frost", "Emma Frost", "Mutante telépata, ex villana convertida en heroína.", 1980, False),
    ("Bishop", "Lucas Bishop", "Mutante viajero del tiempo, absorbe energía.", 1991, False),
    ("Cable", "Nathan Summers", "Mutante del futuro, experto en armas y estrategia.", 1990, False),
    ("Domino", "Neena Thurman", "Mutante con suerte sobrenatural.", 1992, False),
    ("Omega Red", "Arkady Rossovich", "Mutante ruso con tentáculos letales.", 1992, True),
    ("Silver Surfer", "Norrin Radd", "Herald de Galactus, viaja por el cosmos.", 1966, False),
    ("Galactus", "Galactus", "Devorador de mundos, entidad cósmica.", 1966, True),
    ("Doctor Doom", "Victor Von Doom", "Genio científico y hechicero, enemigo de los 4 Fantásticos.", 1962, True),
    ("Human Torch", "Johnny Storm", "Puede envolverse en llamas y volar.", 1961, False),
    ("Invisible Woman", "Sue Storm", "Puede volverse invisible y crear campos de fuerza.", 1961, False),
    ("Mr. Fantastic", "Reed Richards", "Puede estirar su cuerpo a voluntad.", 1961, False),
    ("The Thing", "Ben Grimm", "Fuerza sobrehumana y piel de roca.", 1961, False),
    ("She-Hulk", "Jennifer Walters", "Abogada y prima de Hulk, obtiene poderes gamma.", 1980, False),
    ("Moon Knight", "Marc Spector", "Vigilante con múltiples personalidades.", 1975, False),
    ("Blade", "Eric Brooks", "Cazador de vampiros mitad humano, mitad vampiro.", 1973, False),
    ("Ghost Rider", "Johnny Blaze", "Motociclista con cabeza en llamas, espíritu de venganza.", 1972, False),
    ("Kingpin", "Wilson Fisk", "Señor del crimen de Nueva York.", 1967, True),
    ("Electro", "Max Dillon", "Enemigo de Spider-Man, controla la electricidad.", 1964, True),
    ("Sandman", "Flint Marko", "Puede transformar su cuerpo en arena.", 1963, True),
    ("Rhino", "Aleksei Sytsevich", "Enemigo de Spider-Man, fuerza y resistencia sobrehumanas.", 1966, True),
    ("Vulture", "Adrian Toomes", "Enemigo de Spider-Man, usa alas mecánicas.", 1963, True),
    ("Mysterio", "Quentin Beck", "Maestro de la ilusión, enemigo de Spider-Man.", 1964, True),
    ("Shocker", "Herman Schultz", "Enemigo de Spider-Man, usa guantes vibratorios.", 1967, True),
    ("Kraven", "Sergei Kravinoff", "Cazador obsesionado con Spider-Man.", 1964, True),
    ("Lizard", "Curt Connors", "Científico que se transforma en lagarto gigante.", 1963, True),
    ("Morbius", "Michael Morbius", "Científico convertido en vampiro viviente.", 1971, True),
    ("Black Cat", "Felicia Hardy", "Ladrona experta, interés amoroso de Spider-Man.", 1979, False),
    ("Silver Sable", "Silver Sablinova", "Mercenaria y líder de Wild Pack.", 1985, False),
    ("Jessica Jones", "Jessica Jones", "Investigadora privada con super fuerza.", 2001, False),
    ("Luke Cage", "Carl Lucas", "Piel irrompible y fuerza sobrehumana.", 1972, False),
    ("Iron Fist", "Danny Rand", "Experto en artes marciales con puño místico.", 1974, False),
    ("Daredevil", "Matt Murdock", "Abogado ciego con sentidos aumentados.", 1964, False),
    ("Elektra", "Elektra Natchios", "Asesina experta, interés amoroso de Daredevil.", 1981, False),
    ("Punisher", "Frank Castle", "Vigilante que busca venganza contra el crimen.", 1974, False),
    ("Moonstone", "Karla Sofen", "Psiquiatra con poderes de energía.", 1985, True),
    ("Taskmaster", "Tony Masters", "Puede imitar cualquier habilidad física.", 1980, True),
    ("Mandarin", "Mandarín", "Enemigo de Iron Man, usa anillos de poder.", 1964, True),
    ("Pepper Potts", "Virginia Potts", "Asistente y pareja de Tony Stark.", 1963, False),
    ("War Machine", "James Rhodes", "Piloto de armadura militarizada.", 1979, False),
    ("Rescue", "Pepper Potts", "Versión heroica de Pepper Potts con armadura.", 2009, False),
    ("Happy Hogan", "Harold Hogan", "Guardaespaldas y amigo de Tony Stark.", 1963, False),
    ("Agent Coulson", "Phil Coulson", "Agente de S.H.I.E.L.D., enlace con los Vengadores.", 2008, False),
    ("Maria Hill", "Maria Hill", "Agente de alto rango en S.H.I.E.L.D.", 2005, False),
    ("Sif", "Sif", "Guerrera asgardiana, aliada de Thor.", 1964, False),
    ("Heimdall", "Heimdall", "Guardián del Bifrost en Asgard.", 1962, False),
    ("Hela", "Hela", "Diosa de la muerte asgardiana.", 1964, True),
    ("Odin", "Odin Borson", "Padre de Thor y rey de Asgard.", 1962, False),
    ("Valkyrie", "Brunnhilde", "Guerrera asgardiana, líder de las valquirias.", 1970, False),
    ("Enchantress", "Amora", "Hechicera asgardiana, enemiga de Thor.", 1964, True),
    ("Beta Ray Bill", "Beta Ray Bill", "Aliado de Thor, digno de portar Mjolnir.", 1983, False),
    ("Korg", "Korg", "Guerrero de roca, amigo de Thor.", 1962, False),
    ("Grandmaster", "En Dwi Gast", "Elder del universo, amante de los juegos.", 1989, True),
    ("Howard the Duck", "Howard", "Pato antropomórfico de otro universo.", 1973, False),
    ("Ant Man", "Hank Pym", "Científico que inventó las partículas Pym y fue el primer Ant-Man.", 1962, False)
]