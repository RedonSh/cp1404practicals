from musician import Musician


class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        if isinstance(musician, Musician):
            self.musicians.append(musician)

    def __str__(self):
        musician_info = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_info})"

    def play(self):
        play_info = []
        for musician in self.musicians:
            play_info.append(musician.play())
        return "\n".join(play_info)
