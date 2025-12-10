<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Business Intelligence](https://img.shields.io/badge/Business%20Intelligence-Dashboard-success?style=for-the-badge)

</div>

# 📊 Dashboard de Vendas AdventureWorks

Uma solução de **Business Intelligence as Code** (BI como Código). Este projeto substitui ferramentas de BI tradicionais por uma aplicação web ágil em Python, conectando-se diretamente ao Data Warehouse para gerar insights em tempo real.

O dashboard consome dados da base pública **AdventureWorks** via SQL Server e apresenta KPIs de vendas, análise de produtos e tendências temporais.

## 🎯 Objetivo do Projeto

Demonstrar a capacidade de construir pipelines de análise ponta-a-ponta:
1.  **Extração:** Conexão segura com banco de dados corporativo (**SQL Server**).
2.  **Processamento:** Manipulação de Dataframes com **Pandas**.
3.  **Visualização:** Criação de interface interativa e filtros dinâmicos com **Streamlit**.

## 🛠 Tech Stack

* **Frontend/UI:** Streamlit (Python)
* **Database:** Microsoft SQL Server (Base AdventureWorks2019)
* **Conector:** PyODBC
* **Análise de Dados:** Pandas & Plotly (Visualizações)

## 🚀 Funcionalidades

* **KPIs em Tempo Real:** Vendas Totais, Margem Média e Volume de Pedidos.
* **Filtros Dinâmicos:** Barra lateral para filtrar por Ano, Região e Categoria de Produto (impacta todos os gráficos).
* **Visualizações:**
    * Gráfico de Barras: Top Produtos mais vendidos.
    * Gráfico de Linhas: Evolução temporal das vendas.
* **Tabelas:** Visualização detalhada dos dados brutos filtrados.

## 📦 Como Executar Localmente

1.  Clone o repositório.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure a string de conexão no arquivo `app.py` ou `.env` para apontar para seu SQL Server local.
4.  Rode a aplicação:
    ```bash
    streamlit run app.py
    ```
5.  O dashboard abrirá automaticamente no seu navegador (http://localhost:8501).

## 🖼️ Preview

![Dashboard funcionando](./desafio/athena_query.png)
