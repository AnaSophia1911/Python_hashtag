# automação simples em python feita no intensivão de python da hashtag treinamentos.
#o objetivo é após rodar o código abrir o navegador, digitar o link, fazer login e cadastrar os produtos no banco de dados produtos.csv


import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 5 
#abrindo o edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(10)
#digitando o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(10)
#digitando o email e senha
pyautogui.click(x=453, y=364)
pyautogui.write("faketoyota@gmail.com")
pyautogui.press("tab")
pyautogui.write("root1234")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(10)
#cadastrando os produtos
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=497, y=241)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

print("Todos os produtos cadastrados com sucesso!")