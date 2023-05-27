import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hello Streamlit")
st.header("My App")
st.write("SW_6 Lernjournal Streamlit")

@st.cache
def fetch_and_clean_data(url):
    column_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
    data = pd.read_csv(url, names=column_names)
    return data

def main():
    st.title('Kurismel: My Streamlit App')

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

    # get the session state
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False

    if 'data' not in st.session_state:
        st.session_state.data = None

    if 'selected_columns' not in st.session_state:
        st.session_state.selected_columns = []

    if st.button('Load Dataset') or st.session_state.data_loaded:
        st.session_state.data_loaded = True
        st.session_state.data = fetch_and_clean_data(url)
        st.write('Here is the dataset I loaded from the Internet:')

        if not st.session_state.selected_columns:
            # Initialize selected_columns with all columns
            st.session_state.selected_columns = st.session_state.data.columns.tolist()

    if st.session_state.data_loaded:
        st.write('Select columns to display:')
        all_columns = st.session_state.data.columns.tolist()
        st.session_state.selected_columns = [col for col in all_columns if st.checkbox(col, value=col in st.session_state.selected_columns)]
        
        if st.button('Reload Data'):
            st.table(st.session_state.data[st.session_state.selected_columns])

if __name__ == "__main__":
    main()
