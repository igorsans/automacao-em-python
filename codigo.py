import pyautogui
import time
import pandas

def cadastrar(row, colName):
    val = tabela.loc[row, colName]
    if not pandas.isna(val):
        pyautogui.write(str(val))
    pyautogui.press("tab")

pyautogui.PAUSE = 0.1

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

pyautogui.press("tab")
pyautogui.write("formulario@gmail.com")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

tabela = pandas.read_csv("produtos.csv")

linha = 0

for linha in tabela.index:

    pyautogui.click(x=-808, y=238)
    cadastrar(linha, "codigo")
    cadastrar(linha, "marca")
    cadastrar(linha, "tipo")
    cadastrar(linha, "categoria")
    cadastrar(linha, "preco_unitario")
    cadastrar(linha, "custo")
    cadastrar(linha, "obs")
    pyautogui.press("enter")
    pyautogui.scroll(5000)