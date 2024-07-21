import pytest
from src.main import ingresardatos, clientes, idcliente


def setup_function():
    global clientes, idcliente
    clientes = {}
    idcliente = 0


def simular_input(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))


def verificar_cliente(
    cliente,
    id_cliente,
    run,
    nombre,
    apellido,
    direccion,
    fono,
    correo,
    tipo,
    monto,
    deuda=0,
):
    assert cliente[0] == id_cliente  # ID del cliente
    assert cliente[1] == run
    assert cliente[2] == nombre
    assert cliente[3] == apellido
    assert cliente[4] == direccion
    assert cliente[5] == fono
    assert cliente[6] == correo
    assert cliente[7] == tipo
    assert cliente[8] == monto
    assert cliente[9] == deuda


def test_crear_cliente(monkeypatch):
    setup_function()
    # Datos de prueba
    run = "12345678-9"
    nombre = "Juan"
    apellido = "Perez"
    direccion = "Calle Falsa 123"
    fono = "987654321"
    correo = "juan.perez@example.com"
    tipo = "101"
    monto = "10000"

    # Simular inputs del usuario
    simular_input(
        monkeypatch, [run, nombre, apellido, direccion, fono, correo, tipo, monto]
    )

    # Ejecutar la función
    ingresardatos()

    # Verificaciones
    assert 1 in clientes, "El cliente no se ha agregado al diccionario."
    cliente = clientes[1]
    verificar_cliente(
        cliente, 1, run, nombre, apellido, direccion, fono, correo, tipo, monto
    )


def test_crear_clientes_multiple(monkeypatch):
    setup_function()
    # Datos de prueba para el primer cliente
    run1 = "12345678-9"
    nombre1 = "Juan"
    apellido1 = "Perez"
    direccion1 = "Calle Falsa 123"
    fono1 = "987654321"
    correo1 = "juan.perez@example.com"
    tipo1 = "101"
    monto1 = "10000"

    # Datos de prueba para el segundo cliente
    run2 = "98765432-1"
    nombre2 = "Maria"
    apellido2 = "Gomez"
    direccion2 = "Avenida Siempreviva 742"
    fono2 = "123456789"
    correo2 = "maria.gomez@example.com"
    tipo2 = "102"
    monto2 = "20000"

    # Simular inputs del usuario para el primer cliente
    simular_input(
        monkeypatch,
        [run1, nombre1, apellido1, direccion1, fono1, correo1, tipo1, monto1],
    )
    ingresardatos()

    # Simular inputs del usuario para el segundo cliente
    simular_input(
        monkeypatch,
        [run2, nombre2, apellido2, direccion2, fono2, correo2, tipo2, monto2],
    )
    ingresardatos()

    # Verificar que ambos clientes se hayan agregado al diccionario
    assert 1 in clientes, "El primer cliente no se ha agregado al diccionario."
    assert 2 in clientes, "El segundo cliente no se ha agregado al diccionario."

    # Verificar el primer cliente
    cliente1 = clientes[1]
    verificar_cliente(
        cliente1, 1, run1, nombre1, apellido1, direccion1, fono1, correo1, tipo1, monto1
    )

    # Verificar el segundo cliente
    cliente2 = clientes[2]
    verificar_cliente(
        cliente2, 2, run2, nombre2, apellido2, direccion2, fono2, correo2, tipo2, monto2
    )


@pytest.mark.parametrize(
    "cliente_invalid_datos",
    [
        [
            "",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "",
            "987654321",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "",
            "juan.perez@example.com",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "",
            "101",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "",
            "10000",
        ],
        [
            "12345678-9",
            "Juan",
            "Perez",
            "Calle Falsa 123",
            "987654321",
            "juan.perez@example.com",
            "101",
            "",
        ],
    ],
)
def test_crear_cliente_invalid_data(monkeypatch, cliente_invalid_datos):
    setup_function()
    # Simular inputs del usuario
    simular_input(monkeypatch, cliente_invalid_datos)
    with pytest.raises(ValueError):
        ingresardatos()
