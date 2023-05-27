import requests # python3 -m pip install requests beautifulsoup4 selenium
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://activision.helpshift.com/login/"
urlAdmin = "https://activision.helpshift.com/admin/"


client = requests.Session()



# Configura la ruta al controlador de Microsoft Edge WebDriver
edge_driver_path = 'C:\\Users\\casa\\Documents\\GitHub\\PythonCode\\Scrappers\\edgewebdriver.exe'  


# Configura las opciones del navegador Edge
edge_options = webdriver.EdgeOptions()

# Inicializa el controlador del navegador Edge
driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
    
html = client.get('https://activision.helpshift.com/login/').content
soup = BeautifulSoup(html, 'html.parser')

csrf = soup.find('input',{'name':'_csrf_token'}).get('value')
print(csrf)


payload = {
    'username': '************',
    'password': '********',
    '_csrf_token': csrf
}

client.post(url, data=payload)





# Navega a la página web deseada
driver.get('https://activision.helpshift.com/admin/issues/0-4093/')


# Obtener el contenido HTML después de que la página haya cargado completamente
html = driver.page_source

# Cerrar el controlador del navegador
driver.quit()


# Continúa con el scraping usando BeautifulSoup
#html = client.get('https://activision.helpshift.com/admin/issues/0-4093/').content

soup = BeautifulSoup(html, 'html.parser')

#print(soup)

hsql_builder = soup.find('div', {'class': 'hs-page'})

print(hsql_builder)
