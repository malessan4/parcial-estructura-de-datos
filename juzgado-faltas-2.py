"""
Utilizando TADs programamos un juzgado de faltas. Del juzgado se conoce el número de juzgado, dirección,
juez a cargo y las multas pertenecientesa ese juzgado. De cada multa se conoce: número de acta, dominio,
fecha de emision, importe, fecha de vencimiento, código QR.

Definir la funcion buscar_multa la cuál recibe dos parametros, un juzgado y un dominio, que retorna las
multas por su dominio.

Definir la funcion imprimir_multas que recibe como parametro un juzgado, un dominio y una fecha de emision,
la funcion imprime todas las multas que se encuentren con esta emision y dominio.


"""

class Juzgado():
    def __init__(self, nro_juzgado, direccion, juez_cargo, multas):
        self.nro_juzgado = nro_juzgado
        self.direccion = direccion
        self.juez_cargo = juez_cargo
        self.multas = multas


class Multa ():
    def __init__(self, nro_acta, dominio, fecha_emision, importe, fecha_venci, codigo):
        self.nro_acta = nro_acta
        self.dominio = dominio
        self.fecha_emision = fecha_emision
        self.importe = importe
        self.fecha_venci = fecha_venci
        self.codigo = codigo

def buscar_multa(juzgado, dominio):
    multas_encontradas = []
    for multa in juzgado.multas:
        if multa.dominio == dominio:
            multas_encontradas.append(multa)
        return multas_encontradas
    
def imprimir_multas(juzgado, dominio, fecha_emision):
    multas_filtradas = []
    for multa in juzgado.multas:
        if multa.dominio == dominio and multa.fecha_emision == fecha_emision:
            multas_filtradas.append(multa)
    if multas_filtradas:
        for multa in multas_filtradas:
            print(f"Acta: {multa.nro_acta}, Importe: {multa.importe}, Vencimiento: {multa.fecha_venci}, Código QR: {multa.codigo}")        
    else:
        print("No hay multas para ese dominio")
        
multa1 = Multa(1, "ABC123", "2024-10-01", 5000, "2024-11-01", "QR123")
multa2 = Multa(2, "XYZ789", "2024-10-01", 3000, "2024-11-01", "QR456")
multa3 = Multa(3, "ABC123", "2024-10-05", 4500, "2024-11-05", "QR789")

juzgado = Juzgado(1, "Calle Falsa 123", "Juez Perez", [multa1, multa2, multa3])      
        


resultado = imprimir_multas(juzgado, "ABC1234", "2024-10-01")