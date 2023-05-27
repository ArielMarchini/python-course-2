class MusicNotes:
    def __init__(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.num_octave = 5
        self.times = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times >= self.num_octave * len(self.notes):
            raise StopIteration
        result = self.notes[self.times // self.num_octave] * (2 ** (self.times % self.num_octave))
        self.times += 1
        return result


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
