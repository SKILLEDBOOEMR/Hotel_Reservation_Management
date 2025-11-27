#Hotel Reservation Management
def startup():
    file_init()
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
#file management 
def file_init():
    files_to_create = ["room.txt", "order_Report.txt","booking.txt", "system_report.txt","guest.txt"]
    
    for file_name in files_to_create:
        try:
            open(file_name, 'x').close()
        except FileExistsError:
            pass
        except Exception as e:
            print(f"Error creating {file_name}: {e}")

#Universal Functions
def decode_txt_File_to_list_of_data(file_type):
        try:
            res_list = []

            with open(file_type, 'r+') as file_txt:
                if file_txt.read() == '':
                    return []
                
                else:
                    file_txt.seek(0)
                    for line in file_txt:
                        res_list.append(line.strip().split(','))
                    return res_list
        except Exception:
            print("Error at Decoding ")
def return_number_of_row_In_txt(file_type):
    with open(file_type, 'r') as file:
        count = 0
        for line in file:
            count += 1
        return count
def from_array_to_txt_file_conversion(lists, file_type, Typing_type):
    is_2D_arr = False
    try:
        lists[0][0]
        is_2D_arr = True
    except (IndexError, TypeError):
        is_2D_arr = False
    
    with open(file_type, Typing_type) as file:
        if is_2D_arr:
            for row in lists:
                file.write(",".join(row) + "\n")
        else:
            file.write(",".join(lists) + "\n")
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
        room_list = decode_txt_File_to_list_of_data("room.txt")
        header = ['Occupancy', 'Pricing','Cleaning_Status']

        option_picked = None
        
        while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
            print(" ") #spacing reasons
            print("\033[33mWelcome You are Currently the Manager\033[0m")
            print("\033[33mThese are the current Rooms\033[0m")
            #Printing in a nice table format
            print("Index".ljust(10),end="")
            for col in header:
                print(col.ljust(20),end="")
            print()

            for i, row in enumerate(room_list,start=1):
                print(str(i).ljust(10),end='')
                for col in row :
                    print(str(col).ljust(20),end="")
                print()

            print()
            print("\033[33mWhat do you want to do?\033[0m")
            print("1. Add a Room")
            print("2. Remove a Room")
            print("3. Update a Room")
            print("4. Back")
            option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
        option_dict[option_picked]()

    def manage_add(self):
        added_room_list = ['-','-','False'] 
        while type(added_room_list[1]) != float: 
            try:
                added_room_list[1] = input("What will The Price be for this room? (type: back to go back to menu): ")
                if added_room_list[1].lower() == 'back':
                    self.manage()
                    return
                else:
                    added_room_list[1] = float(added_room_list[1])
            except:
                print("Invalid Input")
        added_room_list[1] = str(added_room_list[1])
        
        from_array_to_txt_file_conversion([added_room_list], "room.txt", "a+")
        print("\033[32mSuccessfully Added a New Room\033[00m")

        self.manage()

    def manage_remove(self):
        room_data_List = decode_txt_File_to_list_of_data('room.txt')
        if not room_data_List:
            print("\033[31mNo rooms to remove.\033[0m")
            self.manage()
            return

        while True:
            try:
                temp_index = input("Please Enter the Index of the Room you want to delete (type: back to go back to menu): ") 
                if temp_index.lower() == 'back':
                    self.manage()
                    return
                else:
                    temp_index = int(temp_index) - 1
            except ValueError:
                print("Invalid Input")
                continue
            if 0 <= temp_index < len(room_data_List):
                break
            print(f"\033[31mIndex must be between 1 and {len(room_data_List)}\033[0m")

        room_data_List.pop(temp_index)
        from_array_to_txt_file_conversion(room_data_List,"room.txt","w")
        print(f"\033[32mSuccessfully Removed a Room index {temp_index + 1}\033[00m")
        self.manage()

    def manage_update(self):
        room_data_List = decode_txt_File_to_list_of_data('room.txt')
        if not room_data_List:
            print("\033[31mNo rooms to Update.\033[0m")
            self.manage()
            return
        
        while True:
            try:
                temp_index = input("Please Enter the Index of the Room you want to Update (type: back to go back to menu): ") 
                if temp_index.lower() == 'back':
                    self.manage()
                    return
                else:
                    temp_index = int(temp_index) - 1
            except ValueError:
                print("Invalid Input")
                continue
            if 0 <= temp_index < len(room_data_List):
                break
            print(f"\033[31mIndex must be between 1 and {len(room_data_List)}\033[0m")

        while True:
            try:
                print("")
                print("\033[33mWhat do you want to update?\033[00m")
                print(f"1.Occupancy (Currently: {room_data_List[temp_index][0]})")
                print(f"2.Price (Currently: {room_data_List[temp_index][1]})")
                print(f"3.Cleaning Status (Currently: {room_data_List[temp_index][2]})")
                option = input("\033[33mEnter Here\033[00m (type: back to go back to menu): ")
                if option.lower() == 'back':
                    self.manage_update()
                    return
                else:
                    option = int(option) - 1
            except:
                print("Invalid Input")
                continue

            if -1 < option < 3:
                break
            print("\033[31mIndex must be between 1 and 3\033[0m")
    
        match option:
            case 0:
                while True:
                    try:
                        x = input("Updated occupancy (type: back to go back to menu): ")
                        if x.lower() == 'back':
                            self.manage_update()
                            return
                        else:
                            x = str(x)
                            break
                    except:
                        print("Invalid Input")
                        continue
                

                    
            case 1:
                while True:
                    try:
                        x = input("Updated Price (type: back to go back to menu): ")
                        if x.lower() == 'back':
                            self.manage_update()
                            return
                        else:
                            x = float(x)
                            break
                    except:
                        print("Invalid Input")
                        continue
                

            case 2:
                while True:
                    try:
                        x = input("Updated Cleaning Status (ONLY TRUE OR FALSE!) (type: back to go back to menu): ")
                        if x.lower() == 'back':
                            self.manage_update()
                            return
                        elif x.lower() == 'true':
                            x = 'True'
                            break
                        elif x.lower() == 'false':
                            x = 'False'
                            break
                        else:
                            print("Invalid Input")
                            continue
                    except:
                        print("Invalid Input")
                        continue
                
        room_data_List[temp_index][option] = str(x)
        from_array_to_txt_file_conversion(room_data_List,"room.txt","w")
        print(f"\033[32mSuccessfully Updated a Room index {temp_index + 1}\033[00m")
        self.manage()

    def system_summary(self):
        print("")
        print("\033[33mView system summary\033[00m")
        print("1.")
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
        room_list = decode_txt_File_to_list_of_data("guest.txt")
        header = ['Name', 'phone_number','email','address']
    
        while True:
            print(" ")
            print("\033[34mWelcome You are Currently the Receptionist\033[0m")
            print("\033[34mThese are the current Guests\033[0m")
            print("Index".ljust(10),end="")
            for col in header:
                print(col.ljust(30),end="")
            print()

            for i, row in enumerate(room_list,start=1):
                print(str(i).ljust(10),end='')
                for col in row:
                    print(str(col).ljust(30),end="")
                print()
            print()

            print("\033[34mWhat do you want to do?\033[0m")
            print("1. Register a New Guest")
            print("2. Update a Existing Guest")
            print("3. Back to menu")
            option_picked = input("\033[34mEnter: \033[0m")
            
            if option_picked == '1':
                self.register_new_guest()
                return

            elif option_picked == '2':
                self.update_guest()
                return
            
            elif option_picked == '3':
                self.menu()
                return
            else:
                print("\033[31mInvalid Input\033[0m")
                continue

    def register_new_guest(self):
        print("\033[34mCurrently creating Account\033[0m")
        Name = input("Enter Guest Name: ")
        while True:
            try:
                phone_Number = input("Enter Guest Phone Number: ")
                int(phone_Number)
                break
            except ValueError:
                print("\033[31mInvalid Input - enter numbers only\033[0m")

        email = input("Enter Guest Email: ")
        address = input("Enter Guest Address: ")

        input_List = [Name, phone_Number, email, address]
        from_array_to_txt_file_conversion([input_List], 'guest.txt', 'a+')
        print("\033[32mGuest registered successfully!\033[0m")

    def update_guest(self):
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