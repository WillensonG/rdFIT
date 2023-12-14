import pytest
from selenium import webdriver
from pages.login_page import LoginPage  

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Ajusta la ruta al chromedriver
    yield driver
    driver.quit()

def test_acceso_usuario_exitoso(browser):
    # Inicializa el objeto Page Object para la página de inicio de sesión
    login_page = LoginPage(browser)
    
    # Navega a la página de inicio de sesión
    login_page.open_login_page()

    # Ingresa las credenciales y realiza el inicio de sesión
    login_page.login('usuario_prueba', 'contrasena123')

    # Verifica si el usuario ha iniciado sesión correctamente
    assert login_page.is_user_logged_in()

def test_acceso_usuario_fallido(browser):
    login_page = LoginPage(browser)
    
    login_page.open_login_page()
    
    # Ingresa credenciales incorrectas y trata de iniciar sesión
    login_page.login('usuario_incorrecto', 'contrasena_incorrecta')

    # Verifica si se muestra un mensaje de error
    assert login_page.is_error_message_displayed()
