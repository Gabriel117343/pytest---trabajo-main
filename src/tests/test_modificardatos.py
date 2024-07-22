import pytest

from src.main import modificardatos, clientes,usuarios, idcliente, idusuario

def test_modificardatos():
 
    clientes = {
        1: [1, "12345678-9", "Juan", "Perez", "Calle 1", "123456789", "juan@example.com", "101", 1000, 0]
    }
    
    nuevos_datos = {
        "nombre": "Carlos",
        "apellido": "Gomez",
        "direccion": "Calle 2",
        "telefono": "987654321",
        "correo": "carlos@example.com",
        "deuda": 200,
        "monto_credito": 1500,
        "tipo": "102"
    }
    
    modificardatos(clientes, 1, nuevos_datos)
    
    cliente_modificado = clientes[1]
    assert cliente_modificado[2] == "Carlos"
    assert cliente_modificado[3] == "Gomez"
    assert cliente_modificado[4] == "Calle 2"
    assert cliente_modificado[5] == "987654321"
    assert cliente_modificado[6] == "carlos@example.com"
    assert cliente_modificado[9] == 200
    assert cliente_modificado[8] == 1500
    assert cliente_modificado[7] == "102"

def test_cliente_no_encontrado():
    clientes = {}
    nuevos_datos = {
        "nombre": "Carlos"
    }
    with pytest.raises(ValueError, match="ID de cliente no encontrado"):
        modificardatos(clientes, 1, nuevos_datos)
 
 