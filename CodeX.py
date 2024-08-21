import streamlit as st
import pickle as pk
import pandas as pd
import requests


def fetch_poster(movie_id):
    # For a API Id
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=91034b6fe54f4857833288bae5c8a42a'
        response = requests.get(url)
        data = response.json()
        poster_path = data.get("poster_path")
        # Poster path
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path


# Recommender function

def recommender(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[0:5]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters


# Load the movie dictionary and similarity matrix
movies_dict = pk.load(open('movies_Dict.pkl', 'rb'))
similarity = pk.load(open('similarity.pkl', 'rb'))

# Convert the movie dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

st.title('MOVIE RECOMMENDER SYSTEM')

# Movie selection dropdown
Movie_Select = st.selectbox(
    "Select Your Movie?",
    movies['title'].values,
    placeholder="Enter Your Selected Movie..."
)

st.write("You selected:", Movie_Select)

# Buttion
if st.button("Recommend",type="primary"):
    name,poster = recommender(Movie_Select)
    st.write(name)


    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])


    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:

        st.text(name[4])
        st.image(poster[4])

