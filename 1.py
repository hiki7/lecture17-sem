import random


class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_random_track(self):
        track = random.choice(self.tracklist)
        track_index = self.tracklist.index(track)
        print(f"Воспроизводится трек {track_index + 1}: {track}")


album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                     "Hallomann"])
print("Название:", album4.title)
print("Исполнитель:", album4.artist)
print("Год:", album4.release_year)
print("Жанр:", album4.genre)
print("Треки:", album4.tracklist)
album4.play_random_track()