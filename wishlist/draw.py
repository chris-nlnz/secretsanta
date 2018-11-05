import random


def random_person_not_myself(list_of_people, me):
    list_of_people_without_me = [p for p in list_of_people if p != me]
    if not list_of_people_without_me:
        return None
    return random.choice(list_of_people_without_me)


def perform_draw(event):
    fail = True
    iterations = 0
    # just give it some large number that it never reaches, just in case
    while fail and iterations < 1000:
        iterations += 1
        print("Iteration {}".format(iterations))
        fail = False

        gift_givers = list(event.participant_set.all())
        gift_receivers = gift_givers.copy()
        draw = {}

        for giver in gift_givers:
            receiver = random_person_not_myself(gift_receivers, giver)
            if not receiver:
                fail = True
            draw[giver] = receiver
            gift_receivers = [p for p in gift_receivers if p != receiver]
    return draw