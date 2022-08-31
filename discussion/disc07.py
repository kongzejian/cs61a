class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self, item):
        self.items.append(item)
        self.size+=1



    def pop(self):
        min=self.items[0]
        min_index=0
        for i in range(self.size):
            if self.items[i]<min:
                min=self.items[i]
                min_index=i
        self.items.pop(min_index)
        self.size-=1
        return min
      
      
 class Email:
    def __init__(self,msg,sender_name,recipient_name):
        self.msg=msg
        self.sender_name=sender_name
        self.recipient_name=recipient_name


class Server:
    def __init__(self):
        self.clients={}

    def send(self,email):
        self.clients[email.recipient_name].receive(email)

    def register_client(self,client,client_name):
        self.clients[client_name]=client

class Client:
    def __init__(self,server,name):
        self.inbox=[]
        self.server=server.register_client(self,self.name)
        self.name=name


    def compose(self,msg,recipient_name):
        email=Email(msg,self.name,recipient_name)
        self.server.send(email)

    def receive(self,email):
        self.inbox.append(email)
        
 class Cat(Pet):
    def __init__(self,name,owner,lives=9):
        Pet.__init__(self,name,owner)
        self.lives=lives
    def talk(self):
        print(self.name+' says meow! ')

    def lose_life(self):
        self.lives-=1
        if self.lives==0:
            self.is_alive=False
            print(self.name+' has no more lives to lose')
            
 class NisyCat(Cat):
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)
    def __repr__(self):
        return "NoisyCat({},{})".format(repr(self.name),repr(self.owner))
        
        
        
  
