PERIOD = ". "
COMMA = ", "
FLY = "fly"
SPIDER = "spider"
BIRD = "bird"
CAT = "cat"
DOG = "dog"
HORSE = "horse"


def main():
    paragraph1()
    paragraph2()
    paragraph3()
    paragraph4()
    paragraph5()
    paragraph6()


def paragraph1():
    action(FLY + PERIOD)
    question()


def paragraph2():
    action(SPIDER + COMMA)
    print("That wriggled and iggled and jiggled inside her. ")
    purpose(SPIDER, FLY)
    question()


def paragraph3():
    action(BIRD + COMMA)
    print("How absurd to swallow a bird. ")
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph4():
    action(CAT + COMMA)
    print("Imagine that to swallow a cat. ")
    purpose(CAT, BIRD)
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph5():
    action(DOG + COMMA)
    print("What a hog to swallow a dog. ")
    purpose(DOG, CAT)
    purpose(CAT, BIRD)
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph6():
    action(HORSE)
    print("She died of course. ")


def action(food):
    assert isinstance(food, str)
    print("There was an old woman who swallowed a", food)


def purpose(predator, food):
    """ the purpose why the old woman swallowed the predator

    :param predator: the name of the predator
    :param food: the name of the food
    :return:
    """
    assert isinstance(predator, str)
    assert isinstance(food, str)
    print("She swallowed the", predator, "to catch the", food + ", ")


def question():
    print("I don't know why she swallowed that fly, ")
    print("Perhaps she'll dies. ")
    print()


if __name__ == '__main__':
    main()
