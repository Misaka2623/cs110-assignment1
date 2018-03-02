"""
spec: http://allisonobourn.com/110/spring18/homework/1/spec.pdf

This program is to print a song to the console.
"""


PERIOD = ". "
COMMA = ", "
FLY = "fly"
SPIDER = "spider"
BIRD = "bird"
CAT = "cat"
DOG = "dog"
HORSE = "horse"


def main():
    """ The main function of this program.
    """
    paragraph1()
    paragraph2()
    paragraph3()
    paragraph4()
    paragraph5()
    paragraph6()


def paragraph1():
    """ Prints the first paragraph of the song.
    """
    action(FLY + PERIOD)
    question()


def paragraph2():
    """ Prints the second paragraph of the song.
    """
    action(SPIDER + COMMA)
    print("That wriggled and iggled and jiggled inside her. ")
    purpose(SPIDER, FLY)
    question()


def paragraph3():
    """ Prints the third paragraph of the song.
    """
    action(BIRD + COMMA)
    print("How absurd to swallow a bird. ")
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph4():
    """ Prints the fourth paragraph of the song.
    """
    action(CAT + COMMA)
    print("Imagine that to swallow a cat. ")
    purpose(CAT, BIRD)
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph5():
    """ Prints the fifth paragraph of the song.
    """
    action(DOG + COMMA)
    print("What a hog to swallow a dog. ")
    purpose(DOG, CAT)
    purpose(CAT, BIRD)
    purpose(BIRD, SPIDER)
    purpose(SPIDER, FLY)
    question()


def paragraph6():
    """ Prints the sixth paragraph of the song.
    """
    action(HORSE)
    print("She died of course. ")


def action(food):
    """ Prints the action of the old woman.

    :param food: the animal that the old woman ate.
    """
    assert isinstance(food, str)
    print("There was an old woman who swallowed a", food)


def purpose(predator, food):
    """ Prints the purpose why the old woman swallowed the predator

    :param predator: the name of the predator
    :param food: the name of the food
    """
    assert isinstance(predator, str)
    assert isinstance(food, str)
    print("She swallowed the", predator, "to catch the", food + ", ")


def question():
    """ Prints the last sentences of some paragraphs.
    """
    print("I don't know why she swallowed that fly, ")
    print("Perhaps she'll dies. ")
    print()


if __name__ == '__main__':
    main()
