import streamlit as st
import info as info
import pandas as pd


st.header("Favorite Media Quiz")

def quiz_section():
    st.subheader("1. What's your favorite movie genre?")
    movie_genre = st.radio("Choose a genre:", ('Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller'))
    if movie_genre == 'Comedy':
        st.write(f"{movie_genre}! My favorite genre is Comedy too, and my personal favorite is Dumb and Dumber!")
    else:
        st.write(f"{movie_genre}'s an interesting choice! I prefer Comedy, though.")
    num_movies = st.slider(f"How many {movie_genre} movies have you watched this year?", 0, 100, 10)
    if num_movies > 75:
        st.write("Wow, so many!")
    elif num_movies < 25:
        st.write("Just like me!")
    else:
        st.write("You must like movies a lot!")
    st.write('---')
    st.subheader("2. What's your favorite genre of music?")
    music_genre = st.selectbox("Choose a music type:", ('Pop', 'Rock', 'Jazz', 'Classical', 'Rap', 'Country', 'Electronic'))
    st.write(f"You've got good taste!")
    if music_genre == 'Rap':
        st.write("That's my favorite, too! My favorite artists are MF DOOM and Mac Miller.")
    st.write('---')
    st.subheader("3. What are your favorite book genres?")
    book_genre = st.multiselect("Select one or more:", ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Science Fiction', 'Biography', 'Self-Help'])
    
    if "Fantasy" in book_genre:
        st.write("I love fantasy books too! Have you read Eragon yet? The movies aren't great, but the books are amazing!")
    else:
        st.write(f"I don't read as much as I used to, but those might be worth checking out!")
    st.write('---')


    
quiz_section()