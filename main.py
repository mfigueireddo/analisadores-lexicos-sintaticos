import sys
from parser import parser
import os

def carregar_entrada(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {caminho_arquivo}")
        sys.exit(1)

def salvar_saida(codigo, caminho_saida):
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    header = '''\
def ligar(namedevice):
    print(namedevice + " ligado!")

def desligar(namedevice):
    print(namedevice + " desligado!")

def alerta(namedevice, msg):
    print(namedevice + " recebeu o alerta:\\n")
    print(msg)

def alerta(namedevice, msg, var):
    print(namedevice + " recebeu o alerta:\\n")
    print(msg + " " + str(var))
    '''
    full_code = header + '\n\n'

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(full_code)
        for linha in codigo:
            f.write(linha)

    print(f"[SUCESSO] Código gerado em: {caminho_saida}")

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_obs>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]

    # Extrai o nome do arquivo de entrada
    nome_entrada = os.path.splitext(os.path.basename(caminho_entrada))[0]

    # Substitui "entrada" por "saida"
    nome_saida = nome_entrada.replace("entrada", "saida")

    # Define o caminho de saída
    caminho_saida = os.path.join("saidas", f"{nome_saida}.py")

    # Garante que o diretório de saída existe
    os.makedirs("saidas", exist_ok=True)

    # Lê o código ObsAct de entrada
    codigo_obsact = carregar_entrada(caminho_entrada)

    # Analisa e traduz o código usando o parser
    codigo_gerado = parser.parse(codigo_obsact)

    # Salva o código traduzido em outro arquivo
    salvar_saida(codigo_gerado, caminho_saida)


if __name__ == "__main__":
    main()
