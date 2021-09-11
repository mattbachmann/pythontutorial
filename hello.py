class Kuscheltier:
    greeting = "Hallo"
    
    def __init__(self, name):
        self.name = name        
        
    def hallo(self):
        print(f"{Kuscheltier.greeting} ich heisse {self.name}!")

def hallo(name= "Dumbo",greeting= "Hallo"):
    print(f"{greeting} ich heisse {name}!")    

dumbo = Kuscheltier("Dumbo")   
winnie = Kuscheltier("Winnie")
dumbo.hallo()
winnie.hallo()

winnie.name = "Super Winnie"
Kuscheltier.greeting = "Howdy"
winnie.hallo()
dumbo.hallo()
hallo("Bobo")
hallo()
