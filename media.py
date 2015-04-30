import webbrowser

#Video class containing title, storyline, duration, review (parent of Movie class) 
class Video():
    """ This class provides a way to store video related information"""

    #constructor
    def __init__(self, video_title, video_storyline, video_duration, video_review):
        #print(#Video Constructor Called")
        self.title = video_title
        self.storyline = video_storyline
        self.duration = video_duration
        self.review = video_review

    #print variables
    def show_info(self):
        print("Storyline - "+self.storyline)
        print("Duration - "+str(self.duration))
        print("Review - "+self.review)

#Movie class containing title, storyline, duration, review, poster, trailer, rating
class Movie(Video):
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #constructor
    def __init__(self, movie_title, movie_storyline, movie_duration, movie_review, poster_image, trailer_youtube, movie_rating):
        #print(#Movie Constructor Called")
        Video.__init__(self, movie_title, movie_storyline, movie_duration, movie_review)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    #open trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    #print variables
    def show_info(self):
        print("Storyline - "+self.storyline)
        print("Duration - "+str(self.duration))
        print("Review - "+self.review)
        print("Rating - "+self.rating)
