import random


def random_person_not_myself(list_of_people, me, exclude_list):
    exclude_list = exclude_list or []
    list_of_people_without_me = [p for p in list_of_people if p != me and p.user.username not in exclude_list]
    if not list_of_people_without_me:
        return None
    return random.choice(list_of_people_without_me)


def perform_draw(event, exclusions=None):
    fail = True
    iterations = 0
    if not exclusions:
        exclusions = {}
    # just give it some large number that it never reaches, just in case
    while fail and iterations < 1000:
        iterations += 1
        print("Iteration {}".format(iterations))
        fail = False

        gift_givers = list(event.participant_set.all())
        gift_receivers = gift_givers.copy()
        draw = {}

        for giver in gift_givers:
            receiver = random_person_not_myself(gift_receivers, giver, exclusions.get(giver.user.username))
            if not receiver:
                fail = True
            draw[giver] = receiver
            gift_receivers = [p for p in gift_receivers if p != receiver]

    for giver, receiver in draw.items():
        giver.buys_present_for = receiver
        giver.save()
