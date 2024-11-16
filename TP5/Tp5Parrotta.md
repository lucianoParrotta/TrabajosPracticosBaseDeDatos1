# TP N 5 - Normalizacion (Luciano Parrotta)

### Determinar las Dependencias Funcionales (DFs)

  **DF1:** (año_olimpiada) -> pais_olimpiada
	La restricción d indica que en un año determinado, los juegos olímpicos se celebran en un único país.

  **DF2:** (nombre_deportista) -> pais_deportista
	La restricción c dice que cada deportista representa siempre al mismo país en cualquier juego olímpico.

  **DF3:** (año_olimpiada, nombre_deportista) -> nombre_disciplina, asistente
	La restriccion e, en un juego olímpico específico, un deportista participa en una única disciplina, y la restriccion f, un deportista tiene un asistente en cada juego olímpico específico.

  **DF4:** (año_olimpiada, nombre_deportista) -> pais_deportista
	Como cada deportista representa siempre al mismo país ,esto implica que conociendo el año y el deportista, se puede determinar su país.
### Determinar las Claves Candidatas

  - La combinación (año_olimpiada, nombre_deportista) determina 
    - pais_olimpiada, 
    - pais_deportista,
    - nombre_disciplina, 
    - asistente,
   
    Según las Dependencias Funcionales DFs 1 2 y 4
    Por lo tanto, la clave candidata es:
	 
        - (año_olimpiada, nombre_deportista), 
    ya que puede identificar de forma única cada registro en la relación y asegura que no haya duplicados. No hay una combinación de atributos más pequeña que logre lo mismo.


### Diseño en tercera Forma Norma (3FN)
1.	**Tabla 'Olimpiada':**
    - año_olimpiada Clave primaria (único año para una olimpiada )
    - pais_olimpiada
2.	**Tabla 'Deportista'**:
    - nombre_deportista Clave primaria (el deportista siempre representa el mismo pais)
    - pais_deportista
3.	**Tabla 'Participacion'**:
    - (año_olimpiada, nombre_deportista) Clave primaria compuesta
    - nombre_disciplina
    - asistente


    *(año_olimpiada, nombre_deportista) Clave primaria compuesta* : Un deportista puede participar en varios juegos olímpicos en diferentes años, entonces año_olimpiada permite identificar el año que participo el deportista y a su vez cada deportista solo compite en una disciplina en cada juego olímpico específico, de modo que: nombre_deportista en combinación con año_olimpiada identifica de manera única su participación en una disciplina particular.
