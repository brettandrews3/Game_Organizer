"""
I'm wanting to write a simple program that will catalog my Switch games.
This may end up being based on class inheritance, dictionaries, lists,
or something else. I'll figure it out as I go along.
"""

# Let's try a dictionary first to define the Switch game's components:

game = {
        'Title': 'Name of Game',
        'Publisher': 'Name of Publisher',
        'Format': 'Physical | Digital',
        'Genre': 'Adventure | Platformer | Metroidvania | RPG | Shooter',
        'Own': 'Yes | No',
        'Played': 'Yes | No',
        'Active': 'Yes | No',
        'Finished': 'Yes | No',
        'Review': '1 - 5'
}
print(game)
#TODO: Try adding a game to this list.

# Here, I'm defining a function that can scale with the questions needed for this organizer:
def game_feature(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print(f'You chose {answer}.')
    return answer

# Here's my list of game attribute questions.

title = game_feature('What is the game\'s title', 'None')
publisher = game_feature('Who is the publisher', 'indie')
game_format = game_feature('Is this game physical or digital', 'digital')
genre = game_feature('What genre would you give this,', "I don't know")
own = game_feature('Do you currently own this game,', 'Yes')
played = game_feature('Have you played this game yet,', 'No')
active = game_feature('Are you actively playing this game', 'No')
finished = game_feature('Did you complete the game?', 'No')
review = game_feature('How would you rate this game(1-5)', '4')
