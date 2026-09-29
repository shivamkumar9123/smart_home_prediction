#1 Smart Home Device Profile

# 1. Device name
device_name = "Smart Thermostat"

# 2. Current temperature
current_temp = 24.5

# 3. Online status
is_online = True

# 4. Available modes
modes = ["Heat", "Cool", "Auto", "Eco"]

# 5. Device location
location = ("Living Room", 2, [-45, 85])

# 6. Device information
device_info = {
    "name": "Smart Thermostat",
    "model_no": "ST-2024",
    "install_year": 2024,
    "is_online": True
}

# Print the type of each variable
print("Device Name:", type(device_name))
print("Current Temperature:", type(current_temp))
print("Online Status:", type(is_online))
print("Modes:", type(modes))
print("Location:", type(location))
print("Device Information:", type(device_info))


#2.Restaurant Order Receipt
order = {
    "customer_name": "Riya",
    "table_number": 4,
    "items": ["Pasta", "Pizza", "Coke"],
    "total_bill": 42.50
}

print(
    f"Order for {order['customer_name']} "
    f"(Table {order['table_number']}): "
    f"{order['items'][0]} is the first item, "
    f"total: ${order['total_bill']:.2f}"
)
#3 Traffic Speed Camera
speed = 85
speed_limit = 55

over_speed = speed - speed_limit

if over_speed >= 30:
    print("Fine: Reckless")
elif over_speed >= 10 and over_speed <= 29:
    print("Fine: Speeding")
elif over_speed >= 1 and over_speed <= 9:
    print("Warning")
else:
    print("OK")
#4  Rocket Launch Countdown
import time

countdown = [5, 4, 3, 2, 1, "Liftoff!"]

for value in countdown:
    print(value)
    time.sleep(1)
#5. Marathon Runner Times
runners = ["Kabir", "Riya", "Aman", "Neha"]

finish_times = ["3:45:12", "4:02:30", "3:55:45", "4:10:20"]

for runner, time in zip(runners, finish_times):
    print(f"{runner} finished in {time}")

# 6. Treasure Hunt Map
grid = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "T"],
    [".", ".", ".", ".", "."]
]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "T":
            print(f"Treasure found at ({row}, {col})")

#B. Python Functions and Classes

#1. Recipe Portion Calculator
def scale_recipe(ingredient, quantity, unit="grams"):
    return f"{quantity} {unit} of {ingredient}"


# Giving all three arguments
print(scale_recipe("flour", 250, "grams"))

# Using default unit
print(scale_recipe("sugar", 100))

#2. Hotel Room Booking — Keyword-Only Arguments
def book_room(*, guest_name, check_in, check_out):
    return (
        f"Booking confirmed for {guest_name} "
        f"from {check_in} to {check_out}."
    )


print(book_room(
    guest_name="Riya",
    check_in="2026-09-25",
    check_out="2026-09-28"
))

#3. Sports Team Roster — Inheritance + super()
class Player:
    def __init__(self, name, jersey_number, position):
        self.name = name
        self.jersey_number = jersey_number
        self.position = position

    def intro(self):
        return (
            f"I am {self.name}, jersey number {self.jersey_number}, "
            f"and I play {self.position}."
        )


class Captain(Player):
    def __init__(self, name, jersey_number, position, years_as_captain):
        super().__init__(name, jersey_number, position)
        self.years_as_captain = years_as_captain

    def intro(self):
        return (
            f"I am {self.name}, jersey number {self.jersey_number}, "
            f"and I play {self.position}. "
            f"I have been captain for {self.years_as_captain} years."
        )


player1 = Player("Aman", 10, "Forward")
captain1 = Captain("Kabir", 7, "Midfielder", 3)

print(player1.intro())
print(captain1.intro())

#4. Online Quiz Scorer — *args, **kwargs + Decorator
def track_attempts(func):
    attempts = 0

    def wrapper(*args, **kwargs):
        nonlocal attempts
        attempts += 1

        print(f"Attempt number: {attempts}")

        return func(*args, **kwargs)

    return wrapper


@track_attempts
def submit_answers(*answers, **student_info):
    print(f"Student: {student_info['name']}")
    print(f"Roll No: {student_info['roll_no']}")
    print(f"Answers: {answers}")


submit_answers("A", "B", "C", "D", name="Riya", roll_no=12)

submit_answers("B", "A", "C", "A", name="Riya", roll_no=12)

submit_answers("A", "A", "B", "D", name="Riya", roll_no=12)

#5. School Management System — Capstone
def log_enrollment(func):
    def wrapper(*args, **kwargs):
        student = func(*args, **kwargs)

        print(f"New student enrolled: {student.name}")

        return student

    return wrapper


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade})"


class Scholar(Student):
    def __init__(self, name, grade, scholarship_amount):
        super().__init__(name, grade)
        self.scholarship_amount = scholarship_amount

    def __repr__(self):
        return (
            f"Scholar(name='{self.name}', "
            f"grade={self.grade}, "
            f"scholarship_amount={self.scholarship_amount})"
        )


@log_enrollment
def enroll_student(name, grade, *, section, **extra_info):

    if "scholarship_amount" in extra_info:
        return Scholar(
            name,
            grade,
            extra_info["scholarship_amount"]
        )

    return Student(name, grade)


student1 = enroll_student(
    "Aman",
    10,
    section="A"
)

student2 = enroll_student(
    "Riya",
    12,
    section="B",
    scholarship_amount=25000
)

print(student1)
print(student2)
