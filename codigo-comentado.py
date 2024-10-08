# Passo 1 entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login

 #pip install pyautogui
import pyautogui
import time


# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
    # pyautogui.click(x=0,y=0, clicks=1)
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho de teclado (Crtl, C)

pyautogui.PAUSE = 0.1

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)
# Passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pausa de 2 segundos no codigo
time.sleep(2)

pyautogui.press("tab")
pyautogui.write("formulario@gmail.com")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

# Passo 3: Importar a base de dados
    # pandas
        # pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto

def cadastrar(row, colName):
    val = tabela.loc[row, colName]
    if not pandas.isna(val):
        pyautogui.write(str(val))
    pyautogui.press("tab")

linha = 0

for linha in tabela.index:

    pyautogui.click(x=-808, y=238)
    #codigo
    cadastrar(linha, "codigo")
    #marca
    cadastrar(linha, "marca")
    #tipo
    cadastrar(linha, "tipo")
    #categoria
    cadastrar(linha, "categoria")
    #preço unitario
    cadastrar(linha, "preco_unitario")
    #custo
    cadastrar(linha, "custo")
    #observação
    cadastrar(linha, "obs")

    #clicar no botão enviar
    pyautogui.press("enter")


    #scrolar para cima positivo para cima negativo para baixo
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar os produtos