import random

conjuntoDeParticipantes = input("Ingrese los participantes (separados por coma): ").title()
conjuntoDeParticipantes = conjuntoDeParticipantes.split(",")
conjuntoDeParticipantes = {participante.strip() for participante in conjuntoDeParticipantes}
conjuntoDeParticipantes = (random.sample(tuple(conjuntoDeParticipantes), len(conjuntoDeParticipantes)))
aQuienRegala = {}
regaladoAux = ""
if len(conjuntoDeParticipantes)>=3:
    for participante in conjuntoDeParticipantes:
        regaladoAux = random.sample(conjuntoDeParticipantes,1)[0]
        while (regaladoAux == participante) or (regaladoAux in aQuienRegala.values()):
            regaladoAux = random.sample(conjuntoDeParticipantes,1)[0]
        aQuienRegala[participante] = regaladoAux

for regalador, regalado in aQuienRegala.items():
    print(f"{regalador} -> {regalado}")