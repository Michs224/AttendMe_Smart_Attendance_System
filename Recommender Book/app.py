import pickle
import streamlit as st
import numpy as np
import pandas as pd
from pathlib import Path

# Load data and models
model = pickle.load(open(str(Path(__file__).resolve().parent / "model.pkl"), "rb")) 
book_names = pickle.load(open(str(Path(__file__).resolve().parent / "bookNames.pkl"), "rb")) 
final_rating = pickle.load(open(str(Path(__file__).resolve().parent / "finalRating.pkl"), "rb"))
book_pivot = pickle.load(open(str(Path(__file__).resolve().parent / "bookPivot.pkl"), "rb")) 

st.set_page_config(
    page_title="LibraLink Recommender System",
    page_icon=":books:",
    layout="wide"
)

# Function rack code
def fetch_rack_code(book_name):
    rack_code = final_rating.loc[final_rating['Book-Title'] == book_name, 'Storage-Rack'].values
    if len(rack_code) > 0:
        return rack_code[0]
    else:
        return ''

# Function poster URL
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['Book-Title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['Image-URL-L']
        poster_url.append(url)

    return poster_url

# Function recommend book
def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=11)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url


st.title('LibraLink: Book Recommender System')

# Sidebar for book selection
selected_books = st.sidebar.selectbox("Type or select a book", book_names)

# Display info buku yang dipilihk
st.sidebar.subheader('Selected Book:')
st.sidebar.write(f"**Title:** {selected_books}")
rack_code = fetch_rack_code(selected_books)
st.sidebar.write(f"**Rack Code:** {rack_code.capitalize() if rack_code else 'Not available'}")

command_container = st.empty()
command_container.markdown('<p style="font-size: 24px;">To see book recommendations, click the "Show Recommendations" button:</p>', unsafe_allow_html=True)


if st.sidebar.button('Show Recommendations'):
    command_container.empty()

    # Ambil Recommendations
    recommended_books, poster_url = recommend_book(selected_books)

    # Display recommended books
    st.subheader('Recommended Books:')
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)

    for i in range(10):
        with locals()[f'col{i+1}']:
            st.markdown(
                f"""
                <div style="border: 2px solid #4682B4; border-radius: 10px; padding: 10px; margin: 10px; text-align: center; box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);">
                    <img src="{poster_url[i]}" alt="{recommended_books[i]}" style="max-width: 100%; border-radius: 10px;">
                    <p style="font-weight: bold; margin-top: 10px;">Title: {recommended_books[i]}</p>
                    <p>Rack Code: {fetch_rack_code(recommended_books[i]).capitalize()}</p>
                </div>
                """, unsafe_allow_html=True
            )
