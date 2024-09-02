import panda as pd 
import plotly.express as px 
import streamlit as st 



def rod1_question_09():
    df_grouped = df1[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    df_grouped

    ax = sns.barplot(
        data = df_grouped,
        x = 'seller_type',
        y = 'count'
    )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Tipos de Vendendores',
        xlabel = 'Tipos de Vendedores',
        ylabel = 'Quantidade'
    );

    st.pyplot(fig)

    return 


def rod1_question_13():

    unico_dono = df1[df1['owner'] == '1st owner'].shape[0]
    unico_dono

    df_grouped = df1.groupby('owner').agg(
        qty = pd.NamedAgg('id', 'count')
    ).sort_values('qty').reset_index()

    ax = sns.barplot(
        data=df_grouped,
        x = 'owner',
        y = 'qty'
    )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Motos por tipo de dono',
        xlabel = 'Tipo de Dono',
    return 


def rod1_question_14():
    df1['km_class'] = df1['km_driven'].apply( lambda km_driven: create_km_class(km_driven) )
    len(df1['km_class'].unique())
    df_grouped = df1[['km_class', 'selling_price']].groupby('km_class')

    df_grouped = df_grouped.mean().sort_values('selling_price', ascending=False).reset_index()

    ax = sns.barplot(
        data = df_grouped,
        x = 'km_class',
        y = 'selling_price'
    )

    ax.set(
        title = 'Média de Preço das Motocicletas agrupadas por classe',
        xlabel = 'Classe de Quilemtros percorridos (5 mil Km percorrido por classe)',
        ylabel = 'Preço Médio de venda'
    )
    return 