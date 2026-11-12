# Mean-Variance-Standard Deviation Calculator

Projeto em Python que utiliza NumPy para calcular média, variância, desvio padrão,
máximo, mínimo e soma de uma matriz 3 x 3.

## Requisitos

- Python 3
- NumPy

Instalação:

```bash
python -m pip install -r requirements.txt
```

## Executar

```bash
python main.py
```

## Testes locais

```bash
python -m unittest test_local.py
```

A função `calculate(data)` recebe uma lista com nove números e devolve um
dicionário com os resultados por coluna (`axis=0`), por linha (`axis=1`) e
para a matriz inteira.
