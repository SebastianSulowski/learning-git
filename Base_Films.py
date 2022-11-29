class Films:
    def __init__(self, title, year, genre, number_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.number_plays = number_plays

        self.play = 0

    def play(self, step=1):
        self.play += step
        Films.play()

    def __str__(self):
        return f"{self.title} {self.year}"


class Serial(Films):
    def __init__(self, episodes, seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episodes = episodes
        self.seasons = seasons

        self.play = 0

    def play(self, step=1):
        self.play += step
        Serial.play()

    def __str__(self):
        return f"{self.title}S{self.seasons:02}E{self.episodes:02}"