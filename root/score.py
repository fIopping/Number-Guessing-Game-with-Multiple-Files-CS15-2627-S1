

def lose_points(points):
    points -= 10
    if points < 0:
        points = 0
    return points

def points_accepting(points):
    if points >= 80:
        print("Excellent!")
    elif points >= 50:
        print("Good!")
    elif points >= 0:
        print("Keep Practicing!")
        





