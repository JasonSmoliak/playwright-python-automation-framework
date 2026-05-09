def countdown_generator(start):

    while start > 0:

        yield start

        start -= 1
