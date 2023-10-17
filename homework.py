class Airport:
    def __init__(self, samolyot_turi, oy, uchish_shahri, qonish_shahri):
        self.samolyot_turi = samolyot_turi
        self.oy = oy
        self.uchish_shahri = uchish_shahri
        self.qonish_shahri = qonish_shahri

n1 = Airport(str(input("Enter the model: ")), str(input("Enter flight date: ")), str(input("Enter the flight city: ")), str(input("Enter lending city: ")))
n2 = Airport(str(input("Enter the model: ")), str(input("Enter flight date: ")), str(input("Enter the flight city: ")), str(input("Enter lending city: ")))
n3 = Airport(str(input("Enter the model: ")), str(input("Enter flight date: ")), str(input("Enter the flight city: ")), str(input("Enter lending city: ")))
n4 = Airport(str(input("Enter the model: ")), str(input("Enter flight date: ")), str(input("Enter the flight city: ")), str(input("Enter lending city: ")))


months = ["iyun", "iyul", "avgust"]

airports = [n1, n2, n3, n4]

for airport in airports:
    if airport.oy in months:
        print(f"Samalyot turi {airport.samolyot_turi}\nUchish oyi {airport.oy}\nUchish shahri {airport.uchish_shahri}\nQo'nish shahri {airport.qonish_shahri}")