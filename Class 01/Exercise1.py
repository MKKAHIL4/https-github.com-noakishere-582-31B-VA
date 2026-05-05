class Friend:
    def __init__(self, name, age, city, hobby, job):
        self.name = name
        self.age = age
        self.city = city
        self.hobby = hobby
        self.job = job
    
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Hobby:", self.hobby)
        print("Job:", self.job)
        
    def greet(self):
     print("Hello", self.name)
            
friend1 = Friend("Micheal", 32, "Montreal", "Programming", "Student")
                     
friend1.show_info()
friend1.greet()
        
           