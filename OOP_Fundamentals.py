#1. City Infrastructure Management System
#Task 1: Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")

    def __str__(self):
        return (f"Registration Number: {self.registration_number}, "
                f"Type: {self.type}, Owner: {self.owner}")

def main():
    vehicle1 = Vehicle("ABC123", "Sedan", "Alice")
    vehicle2 = Vehicle("XYZ789", "SUV", "Bob")

    print("Initial Vehicle Details:")
    print(vehicle1)
    print(vehicle2)
    
    print("\nUpdating owners...")
    vehicle1.update_owner("Charlie")
    vehicle2.update_owner("David")

    print("\nUpdated Vehicle Details:")
    print(vehicle1)
    print(vehicle2)

main()

#Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

    def __str__(self):
        return (f"Event Name: {self.name}, Date: {self.date}, "
                f"Participants: {self.participant_count}")

def main():
    event = Event("Tech Conference", "2024-09-15")

    print("Initial Event Details:")
    print(event)

    print("\nAdding participants...")
    event.add_participant()
    event.add_participant()

    print("\nUpdated Event Details:")
    print(event)
    
    print("\nTotal participants:")
    print(event.get_participant_count())

main()
