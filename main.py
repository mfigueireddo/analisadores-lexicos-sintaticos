import sys
from parser import parser, codigo_gerado
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

        '''
        f.write("def ligar(device):\n")
        f.write("    print(f\"{device} ligado!\")\n\n")

        f.write("def desligar(device):\n")
        f.write("    print(f\"{device} desligado!\")\n\n")

        f.write("def alerta(device, msg):\n")
        f.write("    print(f\"{device} recebeu o alerta:\\n{msg}\")\n\n")

        f.write("def alerta_com_valor(device, msg, var):\n")
        f.write("    print(f\"{device} recebeu o alerta:\\n{msg} {var}\")\n\n")

        f.write("# --- Código traduzido ---\n")
        '''

        for linha in codigo:
            f.write(linha + "\n")

    print(f"[SUCESSO] Código gerado em: {caminho_saida}")

def main():
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_obs>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    caminho_saida = "saida/saida.py"

    # Lê o código ObsAct de entrada
    codigo_obsact = carregar_entrada(caminho_entrada)

    # Analisa e traduz o código usando o parser
    parser.parse(codigo_obsact)

    # Salva o código traduzido em outro arquivo
    salvar_saida(codigo_gerado, caminho_saida)

if __name__ == "__main__":
    main()
