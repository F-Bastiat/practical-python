# bounce.py
#
# Exercise 1.5
def bounce(height, bounces, recall=0.6):
    print([height] + [round(height := height * recall, 4) for bounce in range(bounces)])

bounce(100, 10)