class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(" "+"_" * 29)
        for line in self.lyrics:
            line= " ".join(["|",line])
            for count in range(len(line), 31):
                if count == 30:
                    line = "".join([line,"|"])
                else:
                    line = "".join([line," "])
            print(line)
        print(" "+"-" * 29)

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()