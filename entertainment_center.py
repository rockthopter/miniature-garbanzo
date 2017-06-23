"""Creates instances of Movie and passes them as a list to create a website."""
import media
import fresh_tomatoes

big_lebowski = media.Movie("The Big Lebowski",
                           "",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcRBYp315X-0pNvI-Dvqj8FR0AGdF39VCprXpurd0cQel__e17CP",  # NOQA
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

gangs_of_new_york = media.Movie("Gangs of New York",
                                "story",
                                "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=qHVUPri5tjA")

the_mummy = media.Movie("The Mummy",
                        "",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/The_mummy.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=h3ptPtxWJRs")

apocalypse = media.Movie("Apocalypse Now",
                         "",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=FTjG-Aux_yQ")

jurassic = media.Movie("Jurassic Park",
                       "",
                       "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=QWBKEmWWL38")

anchorman = media.Movie("Anchorman",
                        "",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=-T3wnP91OnI")

#  Store all instances in a list.
movies = [big_lebowski, gangs_of_new_york,
          the_mummy, apocalypse, jurassic, anchorman]
#  Create movie website in default browser.
fresh_tomatoes.open_movies_page(movies)
