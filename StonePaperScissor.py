# rock paper scissors  

import random

rock = "r"
paper = "p"
scissors = "s"

# r>s, s>p, p>r
# SPR == stone paper scissors

class SPR:
    
    computer_output = []
    user_output = []
    
    def playy(self):
        self.computer_win = 0
        self.user_win = 0
        
        for i in range(100):
            computer = random.choice(["r", "p", "s"])
            user = random.choice(["r", "p", "s"])
            
            SPR.computer_output.append(computer)
            SPR.user_output.append(user)
            
            if (computer == "r" and user == "s") or (computer == "s" and user == "p") or (computer == "p" and user == "r"):
                self.computer_win += 1
            else:
                self.user_win += 1
    
    def calculate_occurences(self):
        
        self.overall_rock = 0
        self.overall_papers = 0
        self.overall_scissors = 0
        
        self.overall_output = SPR.computer_output + SPR.user_output
        
        for i in self.overall_output:
            if i == "r":
                self.overall_rock += 1
            elif i == "p":
                self.overall_papers += 1
            elif i == "s":
                self.overall_scissors += 1
        
        self.computer_rock = 0
        self.computer_papers = 0
        self.computer_scissors = 0
        
        for j in SPR.computer_output:
            if j == "r":
                self.computer_rock += 1
            elif j == "p":
                self.computer_papers += 1
            elif j == "s":
                self.computer_scissors += 1
 
        self.user_rock = 0
        self.user_papers = 0
        self.user_scissors = 0
        
        for j in SPR.user_output:
            if j == "r":
                self.user_rock += 1
            elif j == "p":
                self.user_papers += 1
            elif j == "s":
                self.user_scissors += 1
 
    
    def display(self):
        # occurences percentage
        print(f"The percentage of computer winning is {self.computer_win/100}")
        print(f"The percentage of user winning is {self.user_win/100}")
        print("")
        
        # overall rock paper scissors occurences
        print(f"Percentage of getting rock overall is {self.overall_rock/len(self.overall_output)}")
        print(f"Percentage of getting papers overall is {self.overall_papers/len(self.overall_output)}")
        print(f"Percentage of getting scissors overall is {self.overall_scissors/len(self.overall_output)}")
        print("")
        
        # rock paper scissors occurences when computer
        print(f"Percentage of getting rock in computer is {self.computer_rock/100}")
        print(f"Percentage of getting papers in computer is {self.computer_papers/100}")
        print(f"Percentage of getting scissors in computer is {self.computer_scissors/100}")
        print("")
              
        # rock paper scissors occurences when user
        print(f"Percentage of getting rock in user is {self.user_rock/100}")
        print(f"Percentage of getting papers in user is {self.user_papers/100}")
        print(f"Percentage of getting scissors in user is {self.user_scissors/100}")

    
class1 = SPR()
class1.playy()
class1.calculate_occurences()
class1.display()
