import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Curva de Aprendizado - Global Solution", page_icon="📈")

st.title("📘 Global Solution – Curva do Conhecimento no Futuro do Trabalho")
st.write("""
Este aplicativo modela **a curva de aprendizado humano** ao longo do tempo, 
mostrando como o conhecimento cresce, se estabiliza e a importância da **requalificação contínua**.
""")

# Escolha de função
tipo = st.radio("Escolha o tipo de função de aprendizado:",
                ["Exponencial", "Logística"])

# Parâmetros
A = st.slider("Valor máximo de conhecimento (A)", 50, 200, 100)
b = st.slider("Taxa de aprendizado (b)", 0.05, 1.0, 0.2)
t_max = st.slider("Tempo máximo (t_max)", 10, 100, 50)
t = np.linspace(0, t_max, 500)

if tipo == "Exponencial":
    K = A * (1 - np.exp(-b * t))
    K_prime = A * b * np.exp(-b * t)
    integral = np.cumsum(K) * (t[1] - t[0])
    st.latex(r"K(t) = A(1 - e^{-bt})")
else:
    c = st.slider("Ponto médio (c)", 0, 50, 10)
    K = A / (1 + np.exp(-b * (t - c)))
    K_prime = A * (b * np.exp(-b * (t - c))) / ((1 + np.exp(-b * (t - c)))**2)
    integral = np.cumsum(K) * (t[1] - t[0])
    st.latex(r"K(t) = \frac{A}{1 + e^{-b(t - c)}}")

# Gráficos
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

axs[0].plot(t, K, color='blue')
axs[0].set_title("Curva de Conhecimento K(t)")
axs[0].set_xlabel("Tempo (t)")
axs[0].set_ylabel("Nível de Conhecimento")
axs[0].grid(True)

axs[1].plot(t, K_prime, color='orange')
axs[1].set_title("Velocidade de Aprendizado K'(t)")
axs[1].set_xlabel("Tempo (t)")
axs[1].set_ylabel("Taxa de Aprendizado")
axs[1].grid(True)

axs[2].plot(t, integral, color='green')
axs[2].set_title("Conhecimento Acumulado ∫K(t)")
axs[2].set_xlabel("Tempo (t)")
axs[2].set_ylabel("Conhecimento Acumulado")
axs[2].grid(True)

plt.tight_layout()
st.pyplot(fig)

# Resumo e interpretação
st.subheader("📊 Interpretação Automática")
if tipo == "Exponencial":
    st.write(f"""
    - **Fase inicial intensa:** aprendizado rápido (K'(0) = {A*b:.2f})  
    - **Estabilização:** o conhecimento tende ao limite {A:.1f}.  
    - Essa curva é comum em treinamentos práticos curtos e intensivos.
    """)
else:
    t_peak = t[np.argmax(K_prime)]
    st.write(f"""
    - **Pico de aprendizado:** ocorre por volta de t ≈ {t_peak:.1f}.  
    - Após esse ponto, os ganhos de conhecimento diminuem.  
    - Representa processos de aprendizado equilibrados e sustentáveis.
    """)

st.markdown("""
---
### 🌍 Conexão com os ODS
**ODS 4 – Educação de Qualidade:** o aprendizado contínuo promove igualdade de oportunidades.  
**ODS 8 – Trabalho Decente e Crescimento Econômico:** a requalificação garante adaptação e empregabilidade no futuro do trabalho.
""")
