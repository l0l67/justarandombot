import random

def flip():
    face = random.random()
    if face <= 0.5:
        face = 1
    else:
        face = 0
    print(face)
    return face
