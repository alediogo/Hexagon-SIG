# Desafio de BI: Dashboard de Vendas AdventureWorks

Este projeto é uma solução para o Teste de Habilidade (BI) da Hexagon.
O objetivo foi criar um dashboard interativo com Streamlit, consumindo dados da base AdventureWorks via SQL Server.

O dashboard exibe:
* KPI de Vendas Totais no período filtrado.
* Gráfico de barras com as vendas por produto.
* Gráfico de linhas com as vendas ao longo do tempo.
* Filtros interativos por Região, Produto e Ano.

---


## 🚀 Como Rodar o Projeto

### Pré-requisitos

* **Python 3.11+**
* **SQL Server** (com a base AdventureWorks restaurada).
    * *Nota: O script de conexão (`app.py`) precisará ser ajustado com as credenciais (Servidor e Driver) do seu banco de dados local.*

### Passos para Execução

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/alediogo/Hexagon-SIG.git](https://github.com/alediogo/Hexagon-SIG.git)
    cd Hexagon-SIG
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o dashboard:**
    ```bash
    streamlit run app.py
    ```

4.  O dashboard abrirá automaticamente no seu navegador.