def ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente):
    tipoTarjeta = "Clasica"
    if tipoCliente is "AAA":
        if montoEndeudamiento >= 20000:
            tipoTarjeta = "Gold"
    elif tipoCliente is "AA":
        if montoEndeudamiento >= 15000 and montoEndeudamiento < 20000:
            tipoTarjeta = "Platinum"
    elif tipoCliente is "A":
        if montoEndeudamiento >= 10000 and montoEndeudamiento < 15000:
            tipoTarjeta = "Internacional"
    elif tipoCliente is "B":
        if montoEndeudamiento >= 5000 and montoEndeudamiento < 10000:
            tipoTarjeta = "Club Miles"
    elif tipoCliente is "C":
        if montoEndeudamiento >= 3000 and montoEndeudamiento < 5000:
            tipoTarjeta = "Advantage"
    return "Tipo de tarjeta: %s " % tipoTarjeta