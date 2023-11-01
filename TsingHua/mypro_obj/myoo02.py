class Person:

    def work(self):
        print('working hard')

def play_game(s):
    print('{} is playing hard'.format(s))
Person.play_game = play_game;
p = Person()
p.work()
p.play_game()