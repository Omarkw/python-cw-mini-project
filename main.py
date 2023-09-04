# write your code here

def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20

def rackets_cost(racket_barnd):
    if racket_barnd == "Nox":
        return 140
    elif racket_barnd == "Bullpadel":
        return 100
    elif racket_barnd == "Siux":
        return 200

def padel_balls_cost(ball_boxes):
    if ball_boxes == "1":
        return 2
    elif ball_boxes == "2":
        return 3.5
    elif ball_boxes == "3":
        return 5

def padel_game_cost():
    court_type = input("court type indoor: \ outdoor\n")
    racket_barnd = input("racket brand: Nox \ Siux \ Bullpadel\n")
    ball_boxes = input("number of ball boxes: 1 \ 2 \ 3\n")
    price = padel_court_cost(court_type) + rackets_cost(racket_barnd) + padel_balls_cost(ball_boxes)
    return "the price is " + str(price) + "\n\n\n\n\n\n"

print(padel_game_cost())
