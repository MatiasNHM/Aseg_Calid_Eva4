import pytest
from src.main import sumar, ValFecha, ValCorreo, ValContrasena

#Ejemplos
def test_sumar():
    assert sumar(6,6)==12

#Ejemplos
def test_sumar_2():
    assert sumar(16,16)==32

#Ejemplos
@pytest.mark.parametrize(
    "input_a, input_b, esperado",
    [
        (2,3,5),
        (5,5,10),
        (3,3,6),
        (sumar(4,2),10,16),
    ]
)
#Ejemplos
def test_sumar_3(input_a, input_b, esperado):
    assert sumar(input_a, input_b) == esperado




#Eva 4
def test_fecha_valido():
    assert ValFecha(9, 14) is True

def test_mes_invalido():
    assert ValFecha(15, 27) is False

def test_mes_invalido1():
    assert ValFecha(0, 5) is False

def test_mes_invalido2():
    assert ValFecha(-1, 50) is False

def test_dia_invalido():
    assert ValFecha(4, 50) is False

def test_texto_invalido2():
    assert ValFecha(9, "abc") is False
    
def test_fecha_expirada():
    assert ValFecha(5, 21) is False

#############

def test_correo_valido():
    assert ValCorreo("hola@hotmail.com") is True

def test_correo_arroba():
    assert ValCorreo("aaaa_a.com") is False

def test_correo_arroba1():
    assert ValCorreo("aaaa@a@a.com") is False

def test_correo_numero():
    assert ValCorreo(123) is False

def test_correo_dominio():
    assert ValCorreo("aaa@inacapmail.com") is False

#############
def test_contrasena_con_valido():
    assert ValContrasena('ASDASDasdasdasd123123#$$#') is True

def test_contrasena_val_con_comillas():
    assert ValContrasena('ASDASDasda""""asdasd"12332') is True

def test_contrasena_entero():
    assert ValContrasena(123) is False

def test_contrasena_booleano():
    assert ValContrasena(True) is False

def test_contrasena_corta():
    assert ValContrasena("1") is False

def test_contrasena_larga():
    assert ValContrasena("adfadfasdfasdfasdfasdfasdfdafasdfasdfasfasf") is False

def test_contrasena_numeros():
    assert ValContrasena("12311231312312313") is False
    
def test_contrasena_mayusculas():
    assert ValContrasena("ASDASDADADASDASDASDASD") is False

def test_contrasena_minusulas():
    assert ValContrasena("asdasdadadasdasdasd") is False

def test_contrasena_may_num():
    assert ValContrasena("AAAAAAAA1234567") is False

def test_contrasena_min_num():
    assert ValContrasena("aaaaaaaaaa1234567") is False

def test_contrasena_min_may():
    assert ValContrasena("aaaaaaaaAAAAAAAAAA") is False

