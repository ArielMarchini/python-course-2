import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
# 1.
notes = notes.split('-')
print(dir(notes))
# Yes, it is iterable

# 2.
for note in notes:
    note = note.split(',')
    winsound.Beep(freqs.get(note[0]), int(note[1]))