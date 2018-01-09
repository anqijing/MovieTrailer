import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://vignette2.wikia.nocookie.net/fantheories/images"
    "/4/43/Toy-Story-Theme-Song-6.jpg/revision/latest?cb=20140624192735",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://i.ytimg.com/vi/rK47YM-NiNQ/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

captain_jack_sparrow = media.Movie(
    "Captain Jack Sparrow",
    "The advanture of Captain Jack Sparrow at sea",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/"
    "Jack_Sparrow_In_Pirates_of_the_Caribbean-_At_World%27s_End.JPG",
    "https://www.youtube.com//watch?v=1xo3af_6_Jk")

# Create movie list
movies = [toy_story, avatar, captain_jack_sparrow]
# Open movie website
fresh_tomatoes.open_movies_page(movies)
