class Song:
    count = 0
    genres = []
    artists = []
    genre_count={}
    all_genres = []
    artist_count={}
    all_artists = []
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    @classmethod    
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    @classmethod 
    def add_to_genres(cls,genre):
        cls.genres.append(genre) if genre not in cls.genres else cls.genres
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist) if artist not in cls.artists else cls.genres
    @classmethod
    def add_to_genre_count(cls,genre):
        cls.all_genres.append(genre) 
        cls.genre_count= {x: cls.all_genres.count(x) for x in cls.all_genres}
    @classmethod
    def add_to_artist_count(cls,artist):
        cls.all_artists.append(artist) 
        cls.artist_count= {x: cls.all_artists.count(x) for x in cls.all_artists}



      
# ninety_nine = Song("99 Problems", "Jay-Z", "Rap")
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Raap")
# ninety = Song("99 Problems", "Jay-Z", "Rap")
# ninety_n = Song("99 Problems", "Jay-Z", "Raayp")
# ninety_ni = Song("99 Problems", "Jay-Z", "Rap")
# ninety_nine_problem = Song("99 Problems", "Jay-Z", "Raayp")

# print(Song.genre_count)
# print(Song.add_to_genres())