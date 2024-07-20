# Gabriel
#pytest test_funcion_adicional.py -s --tb=short

import pytest
import re

from src.main import ingresoUsuarios, usuarios

# Patrones para validación
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PASSWORD_PATTERN = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"  # Ejemplo de contraseña segura
NAME_PATTERN = r"^[A-Za-z\s]+$"

@pytest.fixture
def user_input():
    # Valores que se simularán como entrada del usuario.
    return {
        "username": "nuevo_usuario",
        "password": "pass", # esto hara que falle la validacion de la contraseña
        "first_name": "Nombre",
        "last_name": "Apellido",
        "email": "correo@valido.com"
    }

@pytest.fixture
def expected_user():
    # Valores esperados para el usuario registrado.
    return {
        "username": "nuevo_usuario",
        "password": "Password123",
        "first_name": "Nombre",
        "last_name": "Apellido",
        "email": "correo@valido.com"
    }

def test_ingreso_usuarios_valido(monkeypatch, user_input, expected_user):
    inputs = iter(user_input.values())
    
    # Reemplazar 'input' y 'getpass.getpass' con valores predefinidos
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('getpass.getpass', lambda _: user_input["password"])

    # Llamada a la función ingresoUsuarios()
    ingresoUsuarios()

    # Verificación de que el usuario se haya agregado correctamente
    assert user_input["username"] in usuarios, "El usuario no se ha agregado correctamente."

    # Recuperación de los datos del usuario
    usuario = usuarios.get(user_input["username"])

    # Comprobación de los datos del usuario usando regex
    assert re.match(NAME_PATTERN, usuario[3]), f"Nombre inválido: {usuario[3]}"
    assert re.match(NAME_PATTERN, usuario[4]), f"Apellido inválido: {usuario[4]}"
    assert re.match(EMAIL_PATTERN, usuario[5]), f"Correo electrónico inválido: {usuario[5]}"
    assert re.match(PASSWORD_PATTERN, usuario[2]), f"Contraseña inválida: {usuario[2]}"
    
    # Comprobaciones adicionales con valores directos
    assert usuario[1] == expected_user["username"], "Nombre de usuario incorrecto."
    assert usuario[2] == expected_user["password"], "Contraseña incorrecta."
    assert usuario[3] == expected_user["first_name"], "Nombre incorrecto."
    assert usuario[4] == expected_user["last_name"], "Apellido incorrecto."
    assert usuario[5] == expected_user["email"], "Correo electrónico incorrecto."

# Casos de prueba con entradas inválidas

@pytest.mark.parametrize(
    "invalid_input",
    [
        # Casos válidos
        {"username": "usuario_valido1", "password": "Valid1Pass", "first_name": "Carlos", "last_name": "Pérez", "email": "carlos.perez@dominio.com"},
        {"username": "usuario_valido2", "password": "Secure1Pass", "first_name": "Ana", "last_name": "Martínez", "email": "ana.martinez@dominio.com"},
        {"username": "usuario_valido3", "password": "Strong1Pass", "first_name": "Luis", "last_name": "García", "email": "luis.garcia@dominio.com"},
        
        # Casos inválidos
        {"username": "usuario_invalido1", "password": "short", "first_name": "Laura", "last_name": "Fernández", "email": "laura.fernandez@dominio.com"},
        {"username": "usuario_invalido2", "password": "Valid2Pass", "first_name": "Juan", "last_name": "Gómez", "email": "juan.gomez@dominio"}
    ]
)
def test_ingreso_usuarios(monkeypatch, invalid_input):
    inputs = iter(invalid_input.values())
    
    # Reemplazar 'input' y 'getpass.getpass' con valores predefinidos
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('getpass.getpass', lambda _: invalid_input["password"])

    # Llamada a la función ingresoUsuarios()
    ingresoUsuarios()

    # Verificación de que el usuario no se haya agregado (si es un caso inválido)
    if invalid_input["username"].startswith("usuario_invalido"):
        assert invalid_input["username"] not in usuarios, f"El usuario {invalid_input['username']} no debería haberse agregado."
    else:
        assert invalid_input["username"] in usuarios, f"El usuario {invalid_input['username']} debería haberse agregado."