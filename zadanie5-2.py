import random

class Media:
    def __init__(self, title, year, genre, plays=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
    
    def play(self):
        self.plays += 1
    
    def add_views(self, count):
        self.plays += count
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}, Plays: {self.plays}"


class Movie(Media):
    def __init__(self, title, year, genre, plays=0):
        super().__init__(title, year, genre, plays)


class TVSeries(Media):
    def __init__(self, title, year, genre, episodes, seasons, plays=0):
        super().__init__(title, year, genre, plays)
        self.episodes = episodes
        self.seasons = seasons
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}, S{self.seasons:02d} E{self.episodes:02d}, Plays: {self.plays}"


class MediaDatabase:
    def __init__(self):
        self.media_list = []
    
    def add_media(self, media):
        self.media_list.append(media)
    
    def get_all_media(self):
        return self.media_list
    
    def get_movies(self):
        return sorted([media for media in self.media_list if isinstance(media, Movie)], key=lambda m: m.title)
    
    def get_series(self):
        return sorted([media for media in self.media_list if isinstance(media, TVSeries)], key=lambda s: s.title)
    
    def find_media(self, title):
        for media in self.media_list:
            if media.title.lower() == title.lower():
                return media
        return None
    
    def search_media(self, query):
        query = query.lower()
        return [media for media in self.media_list if query in media.title.lower()]
    
    def generate_views(self):
        if self.media_list:
            media = random.choice(self.media_list)
            views = random.randint(1, 100)
            media.add_views(views)
            print(f"{media.title} gained {views} new views! Total plays: {media.plays}")
    
    def generate_multiple_views(self, times=10):
        for _ in range(times):
            self.generate_views()

    def top_titles(self, n=5):
        sorted_media = sorted(self.media_list, key=lambda m: m.plays, reverse=True)
        return sorted_media[:n]
    
    def display_media(self):
        for media in self.media_list:
            print(media)


db = MediaDatabase()
db.add_media(Movie("Inception", 2010, "Sci-Fi"))
db.add_media(Movie("The Dark Knight", 2008, "Action"))
db.add_media(Movie("Interstellar", 2014, "Sci-Fi"))

db.add_media(TVSeries("Breaking Bad", 2008, "Crime", 62, 5))
db.add_media(TVSeries("Game of Thrones", 2011, "Fantasy", 73, 8))

db.generate_multiple_views()

top_titles = db.top_titles(3)
print("\nTop 3 Most Popular Titles:")
for media in top_titles:
    print(media)