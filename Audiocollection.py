class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return f'Название трека "{self.name}" - продолжительностью {self.duration} минут'


class Album:
    def __init__(self, name, group, list_track):
        self.name = name
        self.group = group
        self.list_track = []

    def get_tracks(self, track):
        return Track.show(track)

    def add_track(self, track):
        self.list_track.append(track)

    def get_duration(self):
        all_duration = 0
        for track in self.list_track:
            all_duration += track.duration
        return all_duration


sound1 = Track('Твоя песня', 3.6)
sound2 = Track('Вторая песня', 3.3)
sound3 = Track('Третья песня', 3.7)
sound4 = Track('Твоя песня', 3.0)
sound5 = Track('Вторая песня', 3.1)
sound6 = Track('Третья песня', 3.9)

album1 = Album('Первый альбом', 'First group', [])
album2 = Album('Второй альбом', 'Second group', [])

album1.add_track(sound1)
album1.add_track(sound2)
album1.add_track(sound3)
album2.add_track(sound4)
album2.add_track(sound5)
album2.add_track(sound6)

# print(album1.__dict__)
# print(album1.get_tracks(sound1))


print(album2.get_duration())







