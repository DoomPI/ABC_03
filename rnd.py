# --------------------------------------------
from random import randint


class RandomInt:
    def __init__(self, first, last):
        if first <= last:
            self.first = first
            self.last = last
        else:
            self.first = last
            self.last = first

    def Get(self):
        return randint(self.first, self.last)


class RandomString:
    def __init__(self, t):
        self.t = t

    # Случайный выбор названия фильма/имени режиссёра
    def Get(self):
        film_names = [
            "Star wars",
            "The Godfather",
            "Harry Potter",
            "Rear Window",
            "Vertigo",
            "Moonlight",
            "Pinocchio",
            "Hoop Dreams",
            "Psycho",
            "Forest Gump"
        ]
        random_film = film_names[randint(0, 9)]
        if self.t == "film name":
            return random_film

        director_names = [
            "Steven Spielberg",
            "Alfred Hitchcock",
            "Stanley Kubrick",
            "Quentin Tarantino",
            "Akira Kurosawa",
            "John Ford",
            "Billy Wilder",
            "Charles Chaplin",
            "Peter Jackson",
            "Federico Fellini"
        ]
        random_director = director_names[randint(0, 9)]
        if self.t == "director name":
            return random_director
