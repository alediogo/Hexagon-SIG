import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# -------------------------------------------------------------------
# TAREFA 1: CONEXÃO E CONSULTA
# -------------------------------------------------------------------

# Usa o cache do Streamlit para rodar a consulta SÓ UMA VEZ
@st.cache_data
def load_data():
    # Informações de conexão
    nome_do_servidor = r"DESKTOP-KMJFI1B\MSSQLSERVER2"
    connection_string = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=' + nome_do_servidor + ';'
        r'DATABASE=AdventureWorks2022;'
        r'Trusted_Connection=yes;'
        r'TrustServerCertificate=yes;'
    )
    
    # Consulta SQL
    query = """
        SELECT
            h.OrderDate,
            p.Name AS ProductName,
            sp.Name AS RegionName,
            d.LineTotal  -- Usar LineTotal para vendas por produto
        FROM
            Sales.SalesOrderHeader AS h
        JOIN
            Sales.SalesOrderDetail AS d ON h.SalesOrderID = d.SalesOrderID
        JOIN
            Production.Product AS p ON d.ProductID = p.ProductID
        JOIN
            Person.Address AS a ON h.ShipToAddressID = a.AddressID
        JOIN
            Person.StateProvince AS sp ON a.StateProvinceID = sp.StateProvinceID;
    """
    
    try:
        cnxn = pyodbc.connect(connection_string)
        print("Buscando dados no banco...") 
        df = pd.read_sql_query(query, cnxn)
        cnxn.close()
        
        # TAREFA 2: Manipulação de Dados (Pandas)
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        # Extração Ano e Mês para os filtros/gráficos
        df['Ano'] = df['OrderDate'].dt.year
        df['MesAno'] = df['OrderDate'].dt.to_period('M')
        
        return df

    except pyodbc.Error as ex:
        print(f"Erro na conexão ou consulta: {ex}")
        return None

# Carregamento dos dados
df = load_data()

if df is None:
    st.error("Erro ao carregar os dados do banco. Verifique o terminal.")
else:
    # -------------------------------------------------------------------
    # TAREFA 3 e 4: DASHBOARD STREAMLIT
    # -------------------------------------------------------------------

    st.set_page_config(layout="wide") # Deixa o dashboard mais largo
    st.title("Dashboard de Vendas - AdventureWorks 📈")

    # --- FILTROS (SIDEBAR) ---
    st.sidebar.header("Filtros")
    
    # Filtro de Região
    regioes = st.sidebar.multiselect(
        "Selecione a Região:",
        options=df['RegionName'].unique(),
        default=df['RegionName'].unique()
    )
    
    # Filtro de Produto
    produtos = st.sidebar.multiselect(
        "Selecione o Produto:",
        options=df['ProductName'].unique(),
        default=df['ProductName'].unique()
    )
    
    # Filtro de Ano
    anos = st.sidebar.multiselect(
        "Selecione o Ano:",
        options=df['Ano'].unique(),
        default=df['Ano'].unique()
    )

    # --- APLICAÇÃO DE FILTROS AO DATAFRAME ---
    df_filtrado = df[
        df['RegionName'].isin(regioes) &
        df['ProductName'].isin(produtos) &
        df['Ano'].isin(anos)
    ]

    # --- KPI (Total de Vendas) ---
    total_vendas = df_filtrado['LineTotal'].sum()
    st.header("Vendas Totais no Período")
    st.metric(label="Total de Vendas", value=f"R$ {total_vendas:,.2f}")

    st.divider() # Linha divisória

    # --- GRÁFICOS (TAREFA 3) ---
    
    # 1. Gráfico de Barras: Vendas por Produto
    st.header("Top 10 Produtos por Venda")
    vendas_por_produto = df_filtrado.groupby('ProductName')['LineTotal'].sum().nlargest(10).sort_values()
    
    fig_produtos = px.bar(
        vendas_por_produto,
        x='LineTotal',
        y=vendas_por_produto.index,
        orientation='h',
        title="Vendas por Produto"
    )
    st.plotly_chart(fig_produtos, use_container_width=True)
    
    
    # 2. Gráfico de Linhas: Vendas ao Longo do Tempo
    st.header("Vendas ao Longo do Tempo")
    vendas_no_tempo = df_filtrado.groupby('MesAno')['LineTotal'].sum().reset_index()
    # Converção MesAno para string para o Plotly entender
    vendas_no_tempo['MesAno'] = vendas_no_tempo['MesAno'].astype(str) 
    
    fig_tempo = px.line(
        vendas_no_tempo,
        x='MesAno',
        y='LineTotal',
        title="Vendas Mensais"
    )
    st.plotly_chart(fig_tempo, use_container_width=True)