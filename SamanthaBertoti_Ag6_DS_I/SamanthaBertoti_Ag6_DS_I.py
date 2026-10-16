"""
app.py
Calcula o desconto no preço de um produto conforme a faixa de valor.

Regras:
    - Até R$ 200,00  -> 5% de desconto
    - R$ 200 a R$ 300 -> 10% de desconto
    - Acima de R$ 300 -> 15% de desconto
"""

# ---------- ENTRADA DE DADOS ----------
preco = float(input("Digite o preço do produto: R$ "))

# ---------- CÁLCULO DO DESCONTO ----------
# Faixa 1: até R$ 200 -> 5%
if preco <= 200:
    desconto = preco * 0.05

# Faixa 2: de R$ 200 até R$ 300 -> 10%
elif preco <= 300:
    desconto = preco * 0.10

# Faixa 3: acima de R$ 300 -> 15%
else:
    desconto = preco * 0.15

# ---------- CÁLCULO DO PREÇO FINAL ----------
preco_final = preco - desconto

# ---------- SAÍDA ----------
print(f"Preço original: R$ {preco:.2f}") 
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")