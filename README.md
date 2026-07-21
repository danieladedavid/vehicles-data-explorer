# Análise Interativa de Anúncios de Veículos

Este projeto consiste em um aplicativo web desenvolvido com **Streamlit** para realizar uma análise exploratória interativa de um conjunto de dados de anúncios de veículos.

O aplicativo permite visualizar informações por meio de gráficos interativos criados com **Plotly Express**, possibilitando explorar a distribuição de variáveis, comparar diferentes tipos de veículos e analisar a relação entre preço e quilometragem.

Além do aplicativo, o projeto inclui um notebook com a análise exploratória inicial dos dados.

---

## Funcionalidades

- Visualização de uma amostra do conjunto de dados.
- Seleção da quantidade de linhas exibidas na tabela.
- Gráfico de barras com a quantidade de anúncios por tipo de veículo.
- Histograma da distribuição da quilometragem por tipo de veículo.
- Comparação da distribuição dos preços entre dois tipos de veículos selecionados pelo usuário.
- Opção para normalizar o histograma de preços.
- Gráfico de dispersão mostrando a relação entre preço e quilometragem.
- Seleção do tipo de veículo para análise no gráfico de dispersão.

---

## Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- Plotly Express
- Jupyter Notebook

---

## Estrutura do projeto

```text
.
├── app.py
├── vehicles.csv
├── requirements.txt
├── README.md
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml
```

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/danieladedavid/vehicles-data-explorer.git
```

2. Acesse a pasta do projeto:

```bash
cd vehicles-data-explorer
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o aplicativo:

```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no navegador.

---

## Aplicação

Acesse o aplicativo publicado no Render:

[Vehicles Data Explorer](https://vehicles-data-explorer.onrender.com)

---

## Repositório

[GitHub — vehicles-data-explorer](https://github.com/danieladedavid/vehicles-data-explorer)

---

## Autora

**Daniela de David**

Projeto desenvolvido como parte do curso de Ciência de Dados.

