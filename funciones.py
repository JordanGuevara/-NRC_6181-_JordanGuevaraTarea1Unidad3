def union(user,extension):
    """
    Método que une el usuario y la extension que va a usar

    Parametros:
    ----------
    user: str
    extension: str

    Retorna:
    --------
    return gmail
        Retorna lo encapsulado 
    """
    gmail=user+extension
    return gmail
    
def calcular(cantidad):
    """
    Método que calcula el precio a pagar con el IVA

    Parametro:
    ----------
    cantidad:float

    Retorna:
    -------_
    return cantidad+((cantidad*12)/100)
        Retorna el resultado
    """
    return cantidad+((cantidad*12)/100)