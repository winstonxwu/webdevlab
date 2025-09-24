import streamlit as st
import info as info


st.header("Favorite Media Quiz")

def quiz_section():
    st.subheader("1. What's your favorite movie genre?")
    mImage = info.movie_image
    st.image(mImage, width=200)
    movie_genre = st.radio("Choose a genre:", ('Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller')) #NEW
    if movie_genre == 'Comedy':
        st.write(f"{movie_genre}! My favorite genre is Comedy too, and my personal favorite is Dumb and Dumber!")
    else:
        st.write(f"{movie_genre}'s an interesting choice! I prefer Comedy, though.")
    num_movies = st.slider(f"How many {movie_genre} movies have you watched this year?", 0, 100, 10) #NEW
    if num_movies > 75:
        st.write("Wow, so many!")
    elif num_movies < 25:
        st.write("Just like me!")
    else:
        st.write("You must like movies a lot!")
    st.write('---')
    st.subheader("2. What's your favorite genre of music?")
    muImage = info.music_image
    st.image(muImage, width=200)
    music_genre = st.selectbox("Choose a music type:", ('Pop', 'Rock', 'Jazz', 'Classical', 'Rap', 'Country', 'Electronic')) #NEW
    st.write(f"You've got good taste!")
    if music_genre == 'Rap':
        st.write("That's my favorite, too! My favorite artists are MF DOOM and Mac Miller.")
    st.write('---')
    st.subheader("3. What are your favorite book genres?")
    bImage = info.book_image
    st.image(bImage, width=200)
    book_genre = st.multiselect("Select one or more:", ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Science Fiction', 'Biography', 'Self-Help']) #NEW
    if "Fantasy" in book_genre:
        st.write("I love fantasy books too! Have you read Eragon yet? The movies aren't great, but the books are amazing!")
    else:
        st.write(f"I don't read as much as I used to, but those might be worth checking out!")
    st.write('---')
    st.subheader("4. What's your favorite place to relax and enjoy a movie/album/book?")
    relax_place = st.text_input("Type your answer here:") #NEW
    if relax_place == "couch":
        st.write("Same here! There's nothing better than my couch.")
    elif relax_place:
        st.write(f"{relax_place} sounds like a great place to unwind! I prefer my couch.")
    else:
        st.write("Finding a good place to relax is important!")
    st.write('---')
    st.subheader("5. What's your favorite thing to snack on while relaxing?")
    snack = st.selectbox("Choose a snack:", ('Popcorn', 'Chips', 'Chocolate', 'Fruit', 'Pizza', 'Candy', 'Other'))
    if snack == "Pizza":
        st.write("As long as it's not Hawaiian!")
    if snack == "Other":
        other_snack = st.text_input("Type your favorite snack here:")
        if other_snack:
            st.write(f"{other_snack} sounds delicious!")
        else:
            st.write("I'm curious to know what your favorite snack is!")
    else:
        st.write(f"{snack} is a solid choice!")
    st.write('---')




    
quiz_section()