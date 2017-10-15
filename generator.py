#!/usr/bin/env python3

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
import collections
import subprocess
import random

file_name = "demo.mid"

class Generator:
    def __init__(self):
        self.note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.sequence = []

    def generate(self):
        rand_list = []
        for i in range(1500):
            note = random.choice(self.note)
            if i<500:
                number = random.randrange(1,5)
            elif i>=500 and i<800:
                number = random.randrange(5,10)
            elif i>=800 and i<1000:
                number = random.randrange(10,15)
            else:
                number = random.randrange(15, 18)
            rand_list.append(note + str(number))

        print(rand_list)
        self.sequence = rand_list
        notes = NoteSeq(' '.join(self.sequence))
        midi = Midi(1, tempo=500)
        midi.seq_notes(notes, track=0)
        midi.write(file_name)
        subprocess.call(["timidity", file_name])

def choice_if_list(item):
    if isinstance(item, collections.Iterable):
        return random.choice(item)
    else:
        return item

def gen_midi(filename, note_list, tempo=120):
    midi = Midi(tempo)
    midi.seq_notes(note_list)
    midi.write(filename)

def random_notes(pitch_list, octave_list, duration,
                 number_of_notes, volume=120):
    result = NoteSeq()
    for x in range(0, number_of_notes):
        pitch = random.choice(pitch_list)
        octave = choice_if_list(octave_list)
        dur = choice_if_list(duration)
        vol = choice_if_list(volume)
        result.append(Note(pitch, octave, dur, vol))
    return result

def random1():
    chromatic = range(0, 12)
    durations = [1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 1]
    notes = random_notes(chromatic,
                          range(1, 9),
                          durations,
                          100,
                          range(0, 128, 20))
    print(notes)
    gen_midi("random1.mid", notes)

def main():
    generator = Generator()
    generator.generate()
    chromatic_notes = random_notes(range(0, 12), range(5, 7), [0.25, 0.5, 1], 5)
    print(chromatic_notes)
    pentatonic_notes = random_notes([0, 2, 4, 7, 9], 5, 0.5, 5)
    print(pentatonic_notes)
    random1()

if __name__=="__main__":
    main()

