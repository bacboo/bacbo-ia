import streamlit as st
import random

st.title("🎲 IA de Entradas para Bac Bo")

resultados = st.text_area("Digite os últimos resultados (um por linha):", 
"""
Player
Player
Banker
Player
Empate
Player
Banker
Player
""")

lista = resultados.strip().split('\n')

player_wins = lista.count("Player")
banker_wins = lista.count("Banker")
empates = lista.count("Empate")

st.write(f"📊 Total de rodadas: {len(lista)}")
st.write(f"🧍‍♂️ Player: {player_wins}")
st.write(f"🏦 Banker: {banker_wins}")
st.write(f"🤝 Empates: {empates}")

ultimos = lista[-3:]
sugestao = ""

if ultimos.count("Player") == 3:
    sugestao = "⚠️ Três vitórias seguidas do Player. Apostar no BANKER!"
elif ultimos.count("Banker") == 3:
    sugestao = "⚠️ Três vitórias seguidas do Banker. Apostar no PLAYER!"
elif "Empate" in ultimos:
    sugestao = "🚫 Empate recente. Melhor AGUARDAR."
else:
    sugestao = random.choice(["🔥 Apostar em PLAYER", "🔥 Apostar em BANKER"])

st.subheader(sugestao)

