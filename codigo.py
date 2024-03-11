
import pyautogui
import time
pyautogui.PAUSE = 0.3 #pausar entre os comandos



# abrir o navegador
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")

# colocar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pausa para o site carregar
time.sleep(2)

# fazer login
pyautogui.click(x=686, y=394)
pyautogui.write("yanaraujo@gamail.com")

# escrever a senha
pyautogui.press("tab")
pyautogui.write("kkkkkkkkkkkkkkkkkkkkkkk")

# clicar no botão de logar
pyautogui.click(x=916, y=561)
time.sleep(2)

# importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    # cadastro de produto
    pyautogui.click(x=656, y=277)
    
    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    
    # categoria
    categoria = (str(tabela.loc[linha, "categoria"]))
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    # preço
    preco = (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    # custo
    custo = (str(tabela.loc[linha, "custo"]))
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar

    pyautogui.press("enter")
    pyautogui.scroll(5000)
