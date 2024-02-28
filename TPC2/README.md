# TPC2 - Conversão de Formato Markdown (MD) para Formato HTML

> 📅 2024-02-21

> 👤 Diogo Gomes Matos, A100741

## Enunciado

O objetivo deste trabalho prático foi tirar proveito de Expressões Regulares (*REGEX*) de modo a identificar padrões do formato Markdown e convertê-los para os correspondentes elementos em formato HTML, tirando proveito da biblioteca `re` de python.

Foram apenas trabalhados os padrões mais comuns do Markdown, nomeadamente:

- **Títulos:** `# This is a Title`, `## This is a Subtitle`, etc
- **Negrito:** `**this is bold**`
- **Itálico:** `*this is in italics*`
- **Listas:** `-  this is an unordered list element`, `1. this is an ordered list element`
- **Images:** `![this is an image title](this is an image url)`
- **Links:** `[this is a link text](this is a link url)`

A minha solução recebe como argumento um caminho para um ficheiro Markdown e escreve o resultado num ficheiro HTML com o mesmo nome na mesma diretoria onde se encontra `main.py`.
