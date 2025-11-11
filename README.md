## Integrantes:



## 🧠 Global Solution – Curva do Conhecimento no Futuro do Trabalho

### 📘 Descrição do Projeto

Este projeto faz parte da **Global Solution**, integrando conceitos de **Matemática Aplicada**, **Python** e **ODS (Objetivos de Desenvolvimento Sustentável)**.

O aplicativo interativo modela a **curva de aprendizado humano** usando funções matemáticas (exponencial e logística), mostrando como o conhecimento evolui ao longo do tempo e destacando a importância da **educação contínua** e da **requalificação profissional**.

O app foi construído em **Python com Streamlit**, permitindo ao usuário ajustar parâmetros, visualizar gráficos e interpretar os resultados automaticamente.

---

### 🚀 Funcionalidades

✅ Escolher o tipo de função de aprendizado:

* **Exponencial:** aprendizado rápido no início, depois estabiliza.
* **Logística:** aprendizado gradual, com pico de crescimento e estabilização.

✅ Ajustar parâmetros interativamente:

* `A`: valor máximo de conhecimento
* `b`: taxa de aprendizado
* `c`: ponto médio (para curva logística)
* `t_max`: tempo total de simulação

✅ Gerar três gráficos automáticos:

1. **Curva de Conhecimento K(t)**
2. **Derivada K'(t)** (velocidade de aprendizado)
3. **Integral ∫K(t)** (conhecimento acumulado)

✅ Interpretação automática dos resultados e conexão com os **ODS 4 e 8**.

### ⚙️ Instalação

1. Clone o repositório ou baixe os arquivos:

   ```bash
   git clone https://github.com/seuusuario/global-solution-dps.git
   cd global-solution-dps
   ```

2. Instale as dependências:

   ```bash
   pip install streamlit numpy matplotlib
   ```

3. Execute o aplicativo:

   ```bash
   streamlit run global_solution_app.py
   ```

4. O app abrirá automaticamente no navegador (ex: `http://localhost:8501`).

### 🌍 Conexão com os ODS

* **ODS 4 – Educação de Qualidade:**
  Promove a aprendizagem contínua e o desenvolvimento de habilidades para o futuro do trabalho.

* **ODS 8 – Trabalho Decente e Crescimento Econômico:**
  Valoriza a requalificação profissional e o aprendizado ao longo da vida, essenciais para o avanço tecnológico e econômico.
