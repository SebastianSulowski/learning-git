class Films:
    def __init__(self, title, year, genre, number_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_plays = number_plays
        self.plays = 0

    def play_movie(self, step=1):
        self.plays += step

    def __str__(self):
        return f"{self.title} ({self.year})"


class Serial(Films):
    def __init__(self, episodes, seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episodes = episodes
        self.seasons = seasons
        self.plays = 0

    def play_episode(self, step=1):
        self.plays += step

    def __str__(self):
        return f"{self.title} ({self.year}) S{self.seasons:02}E{self.episodes:02}"
