# 📚 Trabalho G2 — Analisadores Léxicos e Sintáticos (2025.1)

Este projeto tem como objetivo desenvolver um **analisador léxico e sintático** que recebe arquivos `.obs` como entrada e gera como saída um arquivo `.py` correspondente.

---

## 🎯 Objetivo

- Ler um arquivo com extensão `.obs`.
- Analisar sua estrutura sintática e léxica.
- Gerar um arquivo Python `.py` com o conteúdo traduzido.

---

## 🗂️ Estrutura do Projeto

- **`main.py`**  
  Gerencia a leitura do arquivo `.obs` e a escrita do arquivo `.py`, além de acionar o analisador.

- **`parser.py`**  
  Define a **gramática** da linguagem `.obs` e formata o código Python gerado com base nas regras sintáticas.

- **`lexer.py`**  
  Define os **tokens léxicos** da linguagem, utilizando expressões regulares para identificar palavras-chave, identificadores, símbolos, etc.

---

## ▶️ Execução

Execute o projeto com o seguinte comando no terminal:

```bash
$ python main.py entradas/entrada1.obs
