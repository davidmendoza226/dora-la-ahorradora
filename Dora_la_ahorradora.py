import json
from datetime import datetime
try:
    with open("historial.json", "r") as archivo:
        historial=json.load(archivo)
except FileNotFoundError:
    historial=[]
saldo=0
for mov in historial:
    if mov["tipo"] =="ingreso":
        saldo += mov["monto"]
    elif mov["tipo"] == "gasto":
        saldo -= mov["monto"]
    
def pedir_numero(mensaje):
    while True:
        try:
            monto=int(input(mensaje))
            if monto < 0:
                print("No se admiten numeros negativos")
                continue
            return monto
        except ValueError:
            print("Solo se admiten numeros")
            
def repetir(mensaje2):
    while True:
        try:
            sel=int(input(mensaje2))
            if sel in (1, 2):
                return sel 
        except ValueError:
            print("Solo se admiten numeros")    
        
print("Calculadora de Gastos")
while True:
    accion=pedir_numero("""Ingrese el tipo de operacion:
                 (1) Ingresar saldo
                 (2) Ingresar gasto
                 (3) Consultar movimientos
                 (4) Historial de gastos
                 (5) historial de ingresos
                 (6) salir
                 """)
    if accion == 1:
        tipo="ingreso"
        monto=pedir_numero("Por favor ingresa el monto: ")
        descripcion=input("Por favor ingresa el concepto: ")
        fecha=datetime.now().strftime("%Y, %m, %d, %H, %M")
        historial.append({"tipo": tipo,"monto":monto, "concepto":descripcion, "fecha": fecha})
        saldo += monto
        print(f"Tu nuevo saldo es de ${saldo}")
        with open("historial.json","w") as archivo:
            json.dump(historial, archivo, indent=4)
    elif accion == 2:
        tipo="gasto"
        monto=pedir_numero("Por favor ingresa el monto: ")
        descripcion=input("Por favor ingresa el concepto: ")
        fecha=datetime.now().strftime("%Y, %m, %d, %H, %M")
        historial.append({"tipo": tipo,"monto":monto, "concepto":descripcion, "fecha": fecha})
        saldo -= monto
        print(f"Tu nuevo saldo es de ${saldo}")
        with open("historial.json","w") as archivo:
            json.dump(historial, archivo, indent=4)  
    elif accion == 3:
        print("Historial de movimientos")
        historial_ordenado=sorted(historial, key=lambda m: datetime.strptime(m["fecha"], "%Y, %m, %d, %H, %M"))
        for mov in historial_ordenado:
            print(f"- {mov['fecha']} - {mov['concepto']} - {mov['monto']} - {mov['tipo']}")
        print("----------------------------------------------------------")
        print(f"""Saldo final
                ${saldo}""")      
    elif accion == 4:
        print("Historial de gastos")
        historial_ordenado=sorted(historial, key=lambda m: datetime.strptime(m["fecha"], "%Y, %m, %d, %H, %M"))
        for mov in historial_ordenado:
            if mov["tipo"]=="gasto":
                print(f"- {mov['fecha']} - {mov['concepto']}: {mov['monto']}")
    elif accion == 5:
        print("Historial de ingresos")
        historial_ordenado=sorted(historial, key=lambda m: datetime.strptime(m["fecha"], "%Y, %m, %d, %H, %M"))
        for mov in historial_ordenado:
            if mov["tipo"]=="ingreso":
                print(f"- {mov['fecha']} - {mov['concepto']}: {mov['monto']}")  
    elif accion == 6:
        print("Gracias por utilizar la calculadora")
        print("Fin del programa")
        break
    else:
        print("Opcion no valida, ingresar una opcion valida")
    
    repeticion=repetir("Deseas realizar otra operacion?: (1) Si| (2) No ")
    
    if repeticion == 1:
        continue
    elif repeticion == 2:
        print("Gracias por utilizar la calculadora")
        print("Fin del programa")
        break
    else:
        print("Opcion no valida, ingresar una opcion valida")

