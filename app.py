from SRC.extraction import load_data 
import streamlit as st 

st.set_page_config(layout = 'wide')
def main():
    df_raw = load_data()
    st.dataframe(df_raw)

if __name__ == '__main__':
    main()