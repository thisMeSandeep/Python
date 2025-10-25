class Duck:
    def __init__(self) -> None:
        self.sound="Quack Quack"

    def talk(self):
        print(f"{self.sound}, {self.sound}....")    


class Human:
    def __init__(self) -> None:
        self.sound="Hehe"

    def talk(self):
        print(f"{self.sound}, {self.sound}.....")          


def call_talk(obj):
    obj.talk()        


duck=Duck()
human=Human()

call_talk(duck)
call_talk(human)