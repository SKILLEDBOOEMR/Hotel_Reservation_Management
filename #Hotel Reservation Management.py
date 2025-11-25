#Hotel Reservation Management
def startup():
    Current_role = None
    role_dict = {
    'manager' : Manager,
    'receptionist' : Receptionist,
    'accountant' : Accountant,
    'guest' : Guest,
    'housekeeping' : Housekeeping
    }    
    #This function is to start the app or reset :)
    print(" ") #spacing reasons
    Current_Role = input("\033[33mPlease Enter Which Role are you?\033[0m (Options are : Manager, Receptionist, Accountant, Housekeeping, Guest) (Enter 1 to terminate program): ").lower()

    while Current_Role not in ['manager', 'receptionist', 'accountant','housekeeping','guest', '1']:
        print("\033[31mMake Sure Role inputted is between these 3\033[0m")
        Current_Role = input("\033[33mPlease Enter Which Role are you?\033[0m (Options are : Manager, Receptionist, Accountant, Housekeeping, Guest) (Enter 1 to terminate program): ").lower()

    if Current_Role != '1':
        role_dict[Current_Role]()

#file management 
def file_init():
    open("room.txt", 'x') 
    #The room file have one purpose and a functionality
    # The code is being read line by line so one room is one line
    #The manager is the only one who could add, update, remove a room 
    open("financial_report.txt","x")
    open("system_report" ,"x")


class Manager:
    def __init__(self):
        self.menu()
        pass
    
    def menu(self): #This is just the menu of the manager
        option_dict = {
            '1' : self.manage,
            '2' : self.system_summary,
            '3' : self.generate,
            '4' : startup,
        } # This is a list to direct the next part when they pick 1-2-3

        print(" ") #spacing reasons
        print("\033[33mWelcome You are Currently the Manager\033[0m")
        print("1. Manage Room Records (Add, Update, Remove)")
        print("2. View system summary (total bookings, occupancy rate, income).")
        print("3. Generate daily and monthly performance reports.")
        print("4. Back")
        option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[31mMake sure number is inputted and between 1-4\033[0m")
            print("Welcome You are Currently the Manager")
            print("1. Manage Room Records (Add, Update, Remove)")
            print("2. View system summary (total bookings, occupancy rate, income).")
            print("3. Generate daily and monthly performance reports.")
            print("4. Back")
            option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        option_dict[option_picked]() #calling the function 

    def manage(self):
        option_dict = {
            '1' : self.manage_add,
            '2' : self.manage_remove,
            '3' : self.manage_update,
            '4' : self.menu,
        }

        print(" ") #spacing reasons
        print("\033[33mWelcome You are Currently the Manager\033[0m")
        print("1. Add a Room")
        print("2. Remove a Room")
        print("3. Update a Room")
        print("4. Back")
        option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[31mMake sure number is inputted and between 1-4\033[0m")
            print("Welcome You are Currently the Manager")
            print("1. Add a Room")
            print("2. Remove a Room")
            print("3. Update a Room")
            print("4. Back")
            option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))
        option_dict[option_picked]()

    def manage_add(self):
        print("hello :)")

    def manage_remove(self):
        print("hello :)")

    def manage_update(self):
        print("hello :)")

    def system_summary(self):
        print("bing bong")
        pass

    def generate(self):
        print("bing bong")
        pass

class Receptionist:
    def __init__(self):
        self.menu()
        pass

    def menu(self): #This is just the menu of the Receptionist
        option_dict = {
            '1' : self.register,
            '2' : self.manage_booking,
            '3' : self.view_room_availability,
            '4' : startup,
        } # This is a list to direct the next part when they pick 1-2-3

        print(" ") #spacing reasons
        print("\033[34mWelcome You are Currently the Receptionist\033[0m")
        print("1. Register guests and update information.")
        print("2. Manage bookings (check-in, check-out, cancellations).")
        print("3. View room availability list.")
        print("4. Back")
        option_picked = str(input("\033[34mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[34mWelcome You are Currently the Receptionist\033[0m")
            print("1. Register guests and update information.")
            print("2. Manage bookings (check-in, check-out, cancellations).")
            print("3. View room availability list.")
            print("4. Back")
            option_picked = str(input("\033[34mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        option_dict[option_picked]() #calling the function 

    def register(self):
        pass

    def manage_booking(self):
        pass

    def view_room_availability(self):
        pass

class Accountant:
    def __init__(self):
        self.menu()
        pass

    def menu(self): #This is just the menu of the Receptionist
        option_dict = {
            '1' : self.record_guest_payments,
            '2' : self.generate_income_and_outstanding_payment_reports,
            '3' : self.generate_monthly_financial_summary,
            '4' : startup,
        } # This is a list to direct the next part when they pick 1-2-3

        print(" ") #spacing reasons
        print("\033[35mWelcome You are Currently the Accountant\033[0m")
        print("1. Record guest payments")
        print("2. Generate income and outstanding payment reports.")
        print("3. Generate monthly financial summary")
        print("4. Back")
        option_picked = str(input("\033[35mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[35mWelcome You are Currently the Accountant\033[0m")
            print("1. Record guest payments")
            print("2. Generate income and outstanding payment reports.")
            print("3. Generate monthly financial summary")
            print("4. Back")
            option_picked = str(input("\033[35mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        option_dict[option_picked]() #calling the function 

    def record_guest_payments(self):
        pass

    def generate_income_and_outstanding_payment_reports(self):
        pass

    def generate_monthly_financial_summary(self):
        pass

class Housekeeping:
    def __init__(self):
        self.menu()
        pass

    def menu(self): #This is just the menu of the Receptionist
        option_dict = {
            '1' : self.update_room_cleaning_status,
            '2' : self.report_mauntenance_issues,
            '3' : self.view_daily_cleaning_schedule,
            '4' : startup,
        } # This is a list to direct the next part when they pick 1-2-3

        print(" ") #spacing reasons
        print("\033[36mWelcome You are Currently the Housekeeping\033[0m")
        print("1. Update room cleaning status.")
        print("2. Report maintenance issues.")
        print("3. View daily cleaning schedule.")
        print("4. Back")
        option_picked = str(input("\033[36mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[36mWelcome You are Currently the Housekeeping\033[0m")
            print("1. Update room cleaning status.")
            print("2. Report maintenance issues.")
            print("3. View daily cleaning schedule.")
            print("4. Back")
            option_picked = str(input("\033[36mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        option_dict[option_picked]() #calling the function 

    def update_room_cleaning_status(self):
        pass

    def report_mauntenance_issues(self):
        pass

    def view_daily_cleaning_schedule(self):
        pass

class Guest:
    def __init__(self):
        self.menu()
        pass

    def menu(self): #This is just the menu of the Receptionist
        option_dict = {
            '1' : self.view_available_rooms,
            '2' : self.make_cancel_reservation,
            '3' : self.view_billing_summary_payment_history,
            '4' : startup,
        } # This is a list to direct the next part when they pick 1-2-3

        print(" ") #spacing reasons
        print("\033[40mWelcome You are Currently the Guest\033[0m")
        print("1. View available rooms.")
        print("2. Make or cancel reservations")
        print("3. View billing summary and payment history")
        print("4. Back")
        option_picked = str(input("\033[40mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print("\033[40mWelcome You are Currently the Guest\033[0m")
            print("1. View available rooms.")
            print("2. Make or cancel reservations")
            print("3. View billing summary and payment history")
            print("4. Back")
            option_picked = str(input("\033[40mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        option_dict[option_picked]() #calling the function 

    def view_available_rooms(self):
        pass

    def make_cancel_reservation(self):
        pass

    def view_billing_summary_payment_history(self):
        pass

#Role dict
startup()
#Part to create the files if it havent been created