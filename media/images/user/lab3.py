class person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        if hours == 7 and hours != 0:
            self.mood = "happy"
            print(self.mood)
        elif hours < 7 and hours != 0:
            self.mood = "tired"
            print(self.mood)
        elif hours > 7 and hours != 0:
            self.mood = "lazy"
            print(self.mood)
        else:
            print("hours must be more than zero")

    def eat(self, meals):
        if meals == 3 and meals != 0:
            self.health_rate = "100%"
            print(self.health_rate)
        elif meals == 2 and meals != 0:
            self.health_rate = "75%"
            print(self.health_rate)
        elif meals == 1 and meals != 0:
            self.health_rate = "50%"
            print(self.health_rate)
        else:
            print("meals shouid be between 1 and 3 meals ")

    def buy(self, items):
        if items * 10 > self.money:
            print("the money not enugh you need :{} pounds more than this salary".format(items * 10 - self.money))
        else:
            money = self.money - items * 10
            print(money)


class employee(person):
    def __init__(self, id, car, salary, distance_to_work):
        super(employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.salary = salary
        self.distance_to_work = distance_to_work
        if salary < 1000:
            print("salary must be ")
        else:
            self.salary = salary

    def work(self, hours):
        if hours == 8 and hours != 0:
            self.mood = "happy"
            print(self.mood)
        elif hours > 8 and hours != 0:
            self.mood = "tired"
            print(self.mood)
        elif hours > 8 and hours != 0:
            self.mood = "lazy"
            print(self.mood)
        else:
            print("hours must be more than zero")

    def drive(self):
        vlc = self.distance_to_work / 60
        self.car.run(self.distance_to_work, vlc)

    def refuel(self, gas=100):
        pass

    def send_email(self):
        pass


class office:
    def __init__(self, name, employees):
        self.office_name = name
        self.employees = employees

    def get_all_emps(self):
        pass

    def get_emps(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class car:
    def __init__(self, name, fuel_rate, velocity):
        self.car_name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

        if velocity > 200 or velocity < 0:
            print("velocity must be between 0 to 200")
        else:
            self.velocity = velocity
        if fuel_rate < 0 or fuel_rate > 100:
            print('Fuel_rate must be between 0 and 100')
        else:
            self.fuel_rate = fuel_rate

    def run(self, velocity, distance):
        if self.fuel_rate - distance <= 0:
            distance = distance - self.fuel_rate
            print("the reamain distanse {}".format(distance))


        else:
            self.fuel_rate = self.fuel_rate - distance
            self.velocity = velocity
            print("he arrive the distnation and the fuel rate after this distance will be {}".format(self.fuel_rate))
            print("and current velocity will be the input velocity {}".format(self.velocity))

    def stop(self, distance):

        self.velocity = 0
        print("remain distance is {}".format(distance))
        if distance == 0:
            print("you are in the distination Now")


viat = car("viat", 0, 200)
viat.run(100, 200)
emp = employee(2, "viat", 2000, 100)
emp.mood
ahmed = person("ahmed", 2000, "sad", 75)
ahmed.sleep(7)
ahmed.eat(3)
ahmed.buy(5)
