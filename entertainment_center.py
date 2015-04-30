import fresh_tomatoes
import media

#create a couple of Movie objects

starwars_ep7 = media.Movie ("Star Wars: The Force Awakens", "A long time ago in a galaxy far, far away....", 150,
                            "A long anticipated masterpiece!",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/2/28/Starwarsviitheforceawakens.jpg/220px-Starwarsviitheforceawakens.jpg",
                            "https://www.youtube.com/watch?v=OMOVFvcNfvE",
                            "PG-13")

#starwars_ep7.show_info()
#starwars_ep7.show_trailer()

frozen = media.Movie ("Frozen", "A snow queen and her sister (&Olaf)", 100,
                      "Best animated film ever",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=TbQm5doF_Uc",
                      "G")

#frozen.show_info()
#frozen.show_trailer()

toy_story = media.Movie ("Toy Story", "A story of a boy and his toys that come to life", 120,
                         "A wonderful journey back to childhood",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                         "G")

#toy_story.show_info()
#toy_story.show_trailer()

avatar = media.Movie ("Avatar", "A marine on an alien planet", 135,
                      "Visually epic!",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=_Tkc5pQp_JE",
                      "PG-13")

#avatar.show_info()
#avatar.show_trailer()

school_of_rock = media.Movie ("School of Rock", "Rocking school teacher", 122,
                      "School's out on this great movie!",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                      "PG-13")

#school_of_rock.show_info()
#school_of_rock.show_trailer()

ratatouille = media.Movie ("Ratatouille", "A rodent becomes a chef", 111,
                      "Wonderfully heartwarming tail!",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                      "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                      "G")

#ratatouille.show_info()
#ratatouille.show_trailer()

hunger_games = media.Movie ("Hunger Games", "A young woman begins a quest to save the world", 142,
                      "A thrilling adventure!",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                      "https://www.youtube.com/watch?v=eO0T9A3kdqc",
                      "PG-13")

#hunger_games.show_info()
#hunger_games.show_trailer()

midnight_in_paris = media.Movie ("Midnight in Paris", "A screenwriter falls in love with Paris", 140,
                      "A lighthearted and warm movie!",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                      "https://www.youtube.com/watch?v=FAfR8omt-CY",
                      "G")

#midnight_in_paris.show_info()
#midnight_in_paris.show_trailer()


#create array of movies
movies = [starwars_ep7, frozen, toy_story, avatar, school_of_rock, ratatouille, hunger_games, midnight_in_paris]

#call open_movies_page function 
fresh_tomatoes.open_movies_page(movies)
