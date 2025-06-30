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

    with open(caminho_saida, "w", encoding="utf-8") as f:

        # Escreve as funções obrigatórias da linguagem ObsAct (em Python)

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

    # Extrai o nome do arquivo de entrada (ex: entrada1.obs → entrada1)
    nome_base = os.path.splitext(os.path.basename(caminho_entrada))[0]

    # Define o caminho de saída: saidas/entrada1.py
    caminho_saida = os.path.join("saidas", f"{nome_base}.py")

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
