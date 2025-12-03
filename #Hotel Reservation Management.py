#Hotel Reservation Management
def startup():
    file_init()
    Current_role = None
    role_dict = {
    'manager' : manager_menu,
    'receptionist' : receptionist_menu,
    'accountant' : accountant_menu,
    'guest' : guest_menu,
    'housekeeping' : housekeeper_menu
    }    
    Current_Role = input("\033[33mPlease Enter Which Role are you?\033[0m (Options are : Manager, Receptionist, Accountant, Housekeeping, Guest) (Enter 1 to terminate program): ").lower()

    while Current_Role not in ['manager', 'receptionist', 'accountant','housekeeping','guest', '1']:
        print("\033[31mMake Sure Role inputted is between these 3\033[0m")
        Current_Role = input("\033[33mPlease Enter Which Role are you?\033[0m (Options are : Manager, Receptionist, Accountant, Housekeeping, Guest) (Enter 1 to terminate program): ").lower()

    if Current_Role != '1':
        role_dict[Current_Role]()
    
#file management 
def file_init():
    files_to_create = ["room.txt", "order_report.txt","booking.txt", "system_report.txt","guest.txt"]
    
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
    if not lists:
        with open(file_type,Typing_type) as file:
            file.write('')
        return
    
    is_2D_arr = False
    try:
        if isinstance(lists[0], list):
            is_2D_arr = True
    except (IndexError, TypeError):
        is_2D_arr = False
    
    try:
        with open(file_type, Typing_type) as file:
            if is_2D_arr:
                for row in lists:
                    row_str = [str(item) for item in row]
                    file.write(",".join(row_str) + "\n")
            else:
                lists_str = [str(item) for item in lists]
                file.write(",".join(lists_str) + "\n")

    except IOError as e:
        print(f"\033[31mError writing to file {file_type}: {e}\033[0m")
    except Exception as e:
        print(f"\033[31mUnexpected error: {e}\033[0m")
def input_date(prompt, allow_back=True,special=False,special_data=''):
    """Prompt for date in DD-MM-YYYY format. Returns list [day, month, year] or 'back'."""
    while True:
        if not special:
            resp = input(prompt).strip()
        else:
            resp = special_data.strip()
        if allow_back and resp.lower() == 'back':
            return 'back'
        try:
            parts = resp.split("-")
            if len(parts) != 3:
                raise ValueError
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            # Validate ranges
            if not (1 <= day <= 31):
                print("\033[31mDay must be between 1 and 31.\033[0m")
                if special:
                    return
                continue
            if not (1 <= month <= 12):
                print("\033[31mMonth must be between 1 and 12.\033[0m")
                if special:
                    return
                continue
            if not (len(str(year)) == 4):
                print("\033[31mYear must be 4 digits.\033[0m")
                if special:
                    return
                continue
            return parts
        except (ValueError, IndexError):
            print("\033[31mInvalid input / Date Format: (05-06-2008)\033[0m")
            continue
def calculate_check_out_date_from_check_in_date(check_in, how_many_days):
    # check_in = [day, month, year]
    check_in = [int(n) for n in check_in]
    day,month, year = check_in

    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Add days
    day += how_many_days

    # Handle day overflow month by month
    while day > month_days[month]:
        day -= month_days[month]
        month += 1
        if month > 12:
            month = 1
            year += 1

    return [day,month,year]
def check_if_two_date_range_intertwine(start1, end1, start2, end2, inclusive=True):
    """
    Determine whether two date ranges overlap.
    Each date must be a list/tuple [day, month, year] (ints or numeric strings).
    inclusive=True treats touching endpoints as overlapping (e.g. end1 == start2 -> True).
    Returns True if ranges intertwine/overlap, False otherwise.
    """
    def to_tuple(d):
        if not (isinstance(d, (list, tuple)) and len(d) == 3):
            raise ValueError("date must be [day,month,year]")
        day, month, year = int(d[0]), int(d[1]), int(d[2])
        return (year, month, day)  # lexicographic comparable

    s1, e1 = to_tuple(start1), to_tuple(end1)
    s2, e2 = to_tuple(start2), to_tuple(end2)


    # normalize so start <= end
    if s1 > e1:
        s1, e1 = e1, s1
    if s2 > e2:
        s2, e2 = e2, s2

    if inclusive:
        return not (e1 < s2 or e2 < s1)
    else:
        return not (e1 <= s2 or e2 <= s1)
def check_if_a_date_is_in_range(date1, start1, end1,month_only = False):
    def to_tuple(d):
        if not (isinstance(d, (list, tuple)) and len(d) == 3):
            raise ValueError("date must be [day,month,year]")
        day, month, year = int(d[0]), int(d[1]), int(d[2])
        if month_only:
            return (year, month)
        else:
            return (year, month, day)  # lexicographic comparable
    
    date1 = to_tuple(date1)
    start1 = to_tuple(start1)
    end1 = to_tuple(end1)
    
    # Normalize so start <= end
    if start1 > end1:
        start1, end1 = end1, start1
    
    # Check if date1 is within range (inclusive)
    return start1 <= date1 <= end1
def print_list_in_a_readable_manner(lists:list,header:list):
    cols = len(header)
    col_widths = [len(col) for col in header]
    for r in lists:
        for i in range(cols):
            col_widths[i] = max(col_widths[i], len(str(r[i])))

    print("Index".ljust(6), end=" ")
    for i, col in enumerate(header):
        print(col.ljust(col_widths[i] + 2), end="")
    print()

    for idx, row in enumerate(lists, start=1):
        print(str(idx).ljust(6), end=" ")
        for j in range(cols):
            val = str(row[j]) if j < len(row) else ""
            print(val.ljust(col_widths[j] + 2), end="")
        print()
    print()

#Manager Functions
def manager_menu(): #This is just the menu of the manager
    option_dict = {
        '1' : manager_manage,
        '2' : manager_system_summary,
        '3' : manager_generate,
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

def manager_manage():
    option_dict = {
        '1' : manager_add,
        '2' : manager_remove,
        '3' : manager_update,
        '4' : manager_menu,
    }
    room_list = decode_txt_File_to_list_of_data("room.txt")
    header = ['Room Special ID', 'Pricing','Cleaning_Status', "Room Type"]

    option_picked = None
    
    while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
        print(" ") #spacing reasons
        print("\033[33mWelcome You are Currently the Manager\033[0m")
        print("\033[33mThese are the current Rooms\033[0m")
        #Printing in a nice table format
        print_list_in_a_readable_manner(room_list,header)

        print()
        print("\033[33mWhat do you want to do?\033[0m")
        print("1. Add a Room")
        print("2. Remove a Room")
        print("3. Update a Room")
        print("4. Back")
        option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
    option_dict[option_picked]()

def manager_add():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    added_room_list = ['-','-','False',''] #, Room_Special_iD, Price, Cleaning Status, Room Type
    
    # Get room name first
    while not added_room_list[3]:
        added_room_list[3] = input("What's This Room Called?: ").strip()
        if not added_room_list[3]:
            print("\033[31mRoom name cannot be empty!\033[0m")
    
    # Get price
    while type(added_room_list[1]) != float: 
        try:
            price_input = input("What will the Price be for this room? (type: back to go back to menu): ").strip()
            if price_input.lower() == 'back':
                manager_manage()
                return
            
            price = float(price_input)
            if price < 0:
                print("\033[31mPrice cannot be negative!\033[0m")
                continue
            added_room_list[1] = price
        except ValueError:
            print("\033[31mInvalid Input - Please enter a valid number\033[0m")

    # Assign Room ID
    if len(room_list) < 1:
        added_room_list[0] = "0"
    else:
        added_room_list[0] = str(int(room_list[len(room_list) - 1][0]) + 1)

    from_array_to_txt_file_conversion([added_room_list], "room.txt", "a+")
    print("\033[32mSuccessfully Added a New Room\033[00m")
    manager_manage()

def manager_remove():
    room_data_List = decode_txt_File_to_list_of_data('room.txt')
    order_list = decode_txt_File_to_list_of_data("order_report.txt")
    if not room_data_List:
        print("\033[31mNo rooms to remove.\033[0m")
        manager_manage()
        return
    
    special_id_list = [data[0] for data in room_data_List]

    while True:
        try:
            temp_index = input("Please Enter the Special ID of the Room you want to delete (type: back to go back to menu): ") 
            if temp_index.lower() == 'back':
                manager_manage()
                return
            else:
                temp_index = str(int(temp_index))
        except ValueError:
            print("Invalid Input")
            continue
        if temp_index in special_id_list:
            room_data_List.pop(special_id_list.index(temp_index))
            break
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")

    order_lists = [n for n in order_list if n[-1] in ['-',''] and n[2] == temp_index]
    while True:
        yes_no = input(f"Are You Sure to Delete This room? (Unfinished Orders Tied: {len(order_lists)}) (type: back to go back to menu):  ")
        if yes_no.lower() in ['back','no']:
            manager_manage()
            return
        elif yes_no.lower() == 'yes':
            order_list = [n for n in order_list if n not in order_lists]
            from_array_to_txt_file_conversion(order_list,'order_report.txt','w')
            from_array_to_txt_file_conversion(room_data_List,"room.txt","w")
            print(f"\033[32mSuccessfully Removed a Room\033[00m")
            manager_manage()

def manager_update():
    room_data_List = decode_txt_File_to_list_of_data('room.txt')
    if not room_data_List:
        print("\033[31mNo rooms to Update.\033[0m")
        manager_manage()
        return
    
    special_id_list = [data[0] for data in room_data_List]
    
    while True:
        try:
            temp_index = input("Please Enter the Unique ID of the Room you want to Update (type: back to go back to menu): ") 
            if temp_index.lower() == 'back':
                manager_manage()
                return
            else:
                temp_index = str(int(temp_index))
        except ValueError:
            print("Invalid Input")
            continue
        if temp_index in special_id_list:
            temp_index = special_id_list.index(temp_index)
            break
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")

    while True:
        try:
            print("")
            print("\033[33mWhat do you want to update?\033[00m")
            print(f"1.Price (Currently: {room_data_List[temp_index][1]})")
            print(f"2.Cleaning Status (Currently: {room_data_List[temp_index][2]})")
            option = input("\033[33mEnter Here\033[00m (type: back to go back to menu): ")
            if option.lower() == 'back':
                manager_update()
                return
            else:
                option = int(option) 
        except:
            print("Invalid Input")
            continue

        if -1 < option < 3 and (option != 0):
            break
        print("\033[31mIndex must be between 1 and 2\033[0m")

    match option:
                
        case 1:
            while True:
                try:
                    x = input("Updated Price (type: back to go back to menu): ")
                    if x.lower() == 'back':
                        manager_update()
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
                        manager_update()
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
    manager_manage()

def manager_system_summary():
    room_list = decode_txt_File_to_list_of_data('room.txt')
    order_list = decode_txt_File_to_list_of_data('order_report.txt')
    guest_list = decode_txt_File_to_list_of_data("guest.txt")

    # Count rooms where the status is NOT empty or '-'
    occupied_rooms = [n for n in room_list if n[-1] not in ['', '-']]
    occupancy_rate = len(occupied_rooms) / len(room_list) * 100

    # Sum income, skipping empty or '-'
    total_income = sum(float(n[-1]) for n in order_list if n[-1] not in ['', '-'])

    print("")
    print("\033[33mView system summary\033[00m")
    print(f"1. Total Bookings: {len(order_list)}")
    print(f"2. Total Guests: {len(guest_list)}")
    print(f"3. Total Income: {total_income}")
    print(f"4. Total Rooms: {len(room_list)}")
    print()
    manager_menu()

def manager_generate():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    order_list = decode_txt_File_to_list_of_data("order_report.txt")

    while True:
        print(" ") #spacing reasons
        print("\033[33mWelcome You are Currently the Manager\033[0m")
        print("1. View Daily Performance Report")
        print("2. View Monthly Performance Report")
        print("3. Back")
        option_picked = str(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) 
        
        
        if option_picked in ['1','2','3']:
            break
        else:
            print("Invalid Input")
            continue

    match option_picked:
        case "1":

            while True:
                check_in = input_date("Date? (Format : DD-MM-YYYY) (type back to go back): ")

                if check_in == 'back':
                    manager_generate()
                    break
                else:
                    break

            check_in_check = [str(int(n)) for n in check_in]
            print()
            occupied_rooms = [n for n in order_list if check_if_a_date_is_in_range(check_in,n[3].split('-'),n[4].split('-'))]
            occupancy_rate = len(occupied_rooms) / len(room_list) * 100
            total_rooms = len(room_list)
            total_booking = len([n for n in order_list if n[3].split('-') == check_in_check])
            if total_booking == 0:
                total_income = 0
                avg_income_per_book = 0
            else:
                total_income = sum(float(n[-3]) for n in order_list if (n[3].split('-') == check_in_check))
                avg_income_per_book = total_income / total_booking
            check_out_tdy = len([n for n in order_list if n[4].split('-') == check_in_check])

            print(f"\033[33mHotel Daily Performance Report (Date: {check_in[0]},{check_in[1]},{check_in[2]})\033[0m")
            print(f"Total Rooms: {total_rooms}")
            print(f"Occupied Rooms: {len(occupied_rooms)}")
            print(f"Occupancy Rate: {occupancy_rate:.2f}%")
            print()
            print(f"Bookings Today: {total_booking}")
            print(f"Total Income: {total_income}")
            print(f"Average Income per Booking: {avg_income_per_book:.2f}")
            print()
            print(f"Check-ins Today: {total_booking}")
            print(f"Check-Outs Today: {check_out_tdy}")
            manager_generate()

        case "2":
            while True:
                check_in = input_date("Date? (Format : DD-MM-YYYY) (type back to go back): ")

                if check_in == 'back':
                    manager_generate()
                    break
                else:
                    break
            print()
            occupied_rooms = [n for n in order_list if check_if_a_date_is_in_range(check_in, n[3].split('-'), n[4].split('-'), True)]
            occupancy_rate = len(occupied_rooms) / len(room_list) * 100
            total_rooms = len(room_list)

            # Get month and year from check_in for comparison
            check_in_month_year = check_in[-2:]  # [month, year]
            check_in_month_year = [str(int(n)) for n in check_in_month_year]

            # Count bookings in this month
            total_booking = len([n for n in order_list if n[3].split('-')[-2:] == check_in_month_year])

            if total_booking == 0:
                total_income = 0
                avg_income_per_book = 0
            else:
                total_income = sum(float(n[-3]) for n in order_list if n[3].split('-')[-2:] == check_in_month_year)
                avg_income_per_book = total_income / total_booking

            check_out_tdy = len([n for n in order_list if n[4].split('-')[-2:] == check_in_month_year])

            print(f"\033[33mHotel Monthly Performance Report (Date: {check_in[1]},{check_in[2]})\033[0m")
            print(f"Total Rooms: {total_rooms}")
            print(f"Occupied Rooms: {len(occupied_rooms)}")
            print(f"Occupancy Rate: {occupancy_rate:.2f}%")
            print()
            print(f"Bookings Today: {total_booking}")
            print(f"Total Income: {total_income}")
            print(f"Average Income per Booking: {avg_income_per_book:.2f}")
            print()
            print(f"Check-ins Today: {total_booking}")
            print(f"Check-Outs Today: {check_out_tdy}")
            manager_generate()
        case "3":
            manager_menu()
#Receptionist Functions
def receptionist_menu(): #This is just the menu of the Receptionist
    option_dict = {
        '1' : receptionist_register,
        '2' : receptionist_manage_booking,
        '3' : receptionist_view_room_availability,
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

def receptionist_register():
    guest_List = decode_txt_File_to_list_of_data("guest.txt")
    header = ['Special_ID','Name', 'phone_number','email','address']

    while True:
        print(" ")
        print("\033[34mWelcome You are Currently the Receptionist\033[0m")
        print("\033[34mThese are the current Guests\033[0m")
        print("Index".ljust(10),end="")
        print_list_in_a_readable_manner(guest_List,header)


        print("\033[34mWhat do you want to do?\033[0m")
        print("1. Register a New Guest")
        print("2. Update a Existing Guest")
        print("3. Back to menu")
        option_picked = input("\033[34mEnter: \033[0m")
        
        if option_picked == '1':
            if len(guest_List) < 1 :
                receptionist_register_new_guest(0)
            else:
                latest_special_id = int(guest_List[len(guest_List) - 1][0])
                receptionist_register_new_guest(latest_special_id)
            return

        elif option_picked == '2':
            receptionist_update_guest()
            return
        
        elif option_picked == '3':
            receptionist_menu()
            return
        else:
            print("\033[31mInvalid Input\033[0m")
            continue

def receptionist_register_new_guest(latest_special_Id):
    print()
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

    input_List = [str(latest_special_Id+1),Name, phone_Number, email, address]
    from_array_to_txt_file_conversion([input_List], 'guest.txt', 'a+')
    print("\033[32mGuest registered successfully!\033[0m")
    receptionist_register()

def receptionist_update_guest():
    guest_data_List = decode_txt_File_to_list_of_data('guest.txt')
    if not guest_data_List:
        print("\033[31mNo Guests to Update.\033[0m")
        receptionist_manage_booking()
        return
    
    special_id_list = [data[0] for data in guest_data_List]
    
    while True:
        try:
            temp_index = input("Please enter the Unique ID of the Guest you want to edit (type: back to go back to menu): ")
            if temp_index.lower() == 'back':
                receptionist_register()
                return
            else:
                temp_index = str(int(temp_index))
        except ValueError:
            print("Invalid Input")
            continue

        if temp_index in special_id_list:
            temp_index = special_id_list.index(temp_index)
            break
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")
    
    while True:
        try:
            print("")
            print("\033[34mWhat do you want to update?\033[00m")
            print(f"1.Name (Currently: {guest_data_List[temp_index][1]})")
            print(f"2.Phone Number (Currently: {guest_data_List[temp_index][2]})")
            print(f"3.Email (Currently: {guest_data_List[temp_index][3]})")
            print(f"4.Address (Currently: {guest_data_List[temp_index][4]})")
            option = input("\033[34mEnter Here\033[00m (type: back to go back to menu): ")
            if option.lower() == 'back':
                receptionist_register()
                return
            else:
                option = int(option) 
        except:
            print("Invalid Input")
            continue

        if 0 < option < 5:
            break
        print("\033[31mIndex must be between 1 and 4\033[0m")

    match option:
        case 1:
            while True:
                try:
                    x = input("Updated Name (type: back to go back to menu): ")
                    if x.lower() == 'back':
                        receptionist_register()
                        return
                    else:
                        x = str(x)
                        break
                except:
                    print("Invalid Input")
                    continue
            

                
        case 2:
            while True:
                try:
                    x = input("Updated Phone Number (type: back to go back to menu): ")
                    if x.lower() == 'back':
                        receptionist_register()
                        return
                    else:
                        x = str(x)
                        break
                except:
                    print("Invalid Input")
                    continue

        case 3:
            while True:
                try:
                    x = input("Updated Email (type: back to go back to menu): ")
                    if x.lower() == 'back':
                        receptionist_register()
                        return
                    else:
                        x = str(x)
                        break
                except:
                    print("Invalid Input")
                    continue

        case 4:
            while True:
                try:
                    x = input("Updated Address (type: back to go back to menu): ")
                    if x.lower() == 'back':
                        receptionist_register()
                        return
                    else:
                        x = str(x)
                        break
                except:
                    print("Invalid Input")
                    continue

    guest_data_List[temp_index][option] = str(x)
    from_array_to_txt_file_conversion(guest_data_List,"guest.txt",'w')
    print(f"\033[32mSuccessfully Updated a Guest \033[00m")
    receptionist_register()

def receptionist_manage_booking():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    guest_list = decode_txt_File_to_list_of_data("guest.txt")
    order_Listz = decode_txt_File_to_list_of_data("order_report.txt")
    header = ["Room Special ID", 'Pricing','Cleaning_Status', 'Message']
    header2 = ['Special_ID','Name', 'phone_number','email','address']
    order_id_check = [row[0] for row in order_Listz]
    order_id_check_unfinished = [row[0] for row in order_Listz if row[-1] in ['-','']]

    option_picked = None
    
    while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
        print(" ") #spacing reasons
        print("\033[34mManaging Rooms\033[0m")
        print("\033[34mWhat do you want to do?\033[0m")
        print("1. Check IN a Room")
        print("2. Check Out a Room")
        print("3. Cancel a Order")
        print("4. Back")
        option_picked = str(input("\033[34mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
    
    match option_picked:
        case "1":
            # --- Get Check-In Date ---
            while True:
                check_in = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
                if check_in == 'back':
                    receptionist_manage_booking()
                    return
                else:
                    check_in = [int(n) for n in check_in]
                    break

            # --- Get Number of Days ---
            while True:
                days_booked = input("How Many Days Are you staying? (type back to go back): ")
                if days_booked == 'back':
                    receptionist_manage_booking()
                    return
                try:
                    days_booked = int(days_booked)
                    if days_booked <= 0:
                        print("Days must be greater than 0")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
                    continue

            # --- Calculate Check-Out Date ---
            check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

            # --- Find Available Rooms ---
            available_rooms = []
            available_rooms_ids = []
            for room in room_list:
                # room[0] is Room Special ID
                overlapping_orders = [
                    order for order in order_Listz
                    if (order[2] == room[0]) and (order[-1] in ['-', ''])
                    and (check_if_two_date_range_intertwine(check_in, check_out, order[3].split('-'), order[4].split('-')))
                ]
                
                if not overlapping_orders:
                    available_rooms.append(room)
                    available_rooms_ids.append(room[0])

            if not available_rooms:
                print("\033[31mNo rooms are available for this date range.\033[0m")
                receptionist_manage_booking()
                return

            # --- Display Available Rooms ---
            print()
            print(f"\033[34mAvailable Rooms ({check_in[0]},{check_in[1]},{check_in[2]} - {check_out[0]},{check_out[1]},{check_out[2]}):\033[0m")
            header = ["Room Special ID", "Pricing", "Cleaning_Status", "Message"]
            print_list_in_a_readable_manner(available_rooms,header)

            # --- Display Guests ---
            print("\033[34mCurrent Guests:\033[0m")
            header2 = ['Special_ID', 'Name', 'phone_number', 'email', 'address']
            print_list_in_a_readable_manner(guest_list,header2)

            # --- Select Guest ---
            print()
            print("\033[34mEnter The Remaining Credentials:\033[0m")
            guest_ids = [guest[0] for guest in guest_list]
            while True:
                guest_id = input("Enter Guest Special ID (type back to go back): ")
                if guest_id == 'back':
                    receptionist_manage_booking()
                    return
                if guest_id not in guest_ids:
                    print("Guest ID isn't registered!")
                    continue
                break

            # --- Select Room ---
            while True:
                room_id = input("Enter Room Special ID (type back to go back): ")
                if room_id == 'back':
                    receptionist_manage_booking()
                    return
                if room_id not in available_rooms_ids:
                    print("Room ID isn't available!")
                    continue
                break

            # --- Calculate Total Price ---
            room_index = next(i for i, r in enumerate(room_list) if r[0] == room_id)
            Total_Price = float(room_list[room_index][1]) * days_booked

            check_in = [str(n) for n in check_in]
            check_out = [str(n) for n in check_out]
            # --- Create Order ---
            order_list = [
                str(int(order_Listz[-1][0]) + 1) if order_Listz else "0",
                str(guest_id),
                str(room_id),
                '-'.join(check_in),
                '-'.join(check_out),
                str(Total_Price),
                str(days_booked),
                '-'
            ]

            from_array_to_txt_file_conversion(order_list, 'order_report.txt', "a+")
            print("\033[32mSuccessfully Checked In a Guest\033[0m")
            receptionist_manage_booking()

        case '2':
            if len(order_id_check_unfinished) < 1:
                print("\033[91mThere is no Unfinished Orders\033[0m")
                receptionist_manage_booking()
                return
            print(" ") #spacing reasons
            print("\033[34mManaging Rooms\033[0m")
            print("\033[34mThese are the current unfinished orders\033[0m")
            #Printing in a nice table format
            header = ["Order ID","Member ID", "Room ID", "Check IN date", "Check OUT date", "Total Price", "Total Days Booked", "Actual payed"]
            print_list_in_a_readable_manner(order_Listz,header)

            while True:
                order_id = input("Please Enter the Order Special ID (type back to go back): ")
                if order_id == 'back':
                    receptionist_manage_booking()
                    break
                if order_id not in order_id_check:
                    print("Order ID isnt Registered!")
                    continue
                else:
                    break

            while True:
                try:
                    actually_payed = input("Amount Actually Payed? (type: back to go back to menu): ")
                    if actually_payed.lower() == "back":
                        receptionist_manage_booking()
                        return
                    
                    actually_payed = str(float(actually_payed))
                    break

                except:
                    print("Invalid Input")
                    continue

            

            order_Listz[order_id_check.index(order_id)][-1] = actually_payed
            from_array_to_txt_file_conversion(order_Listz,'order_report.txt','w')
            print(f"\033[32mSuccessfully Check Out a Guest \033[00m")
            receptionist_manage_booking()
    
        case '3':
            if len(order_id_check_unfinished) < 1:
                print("\033[91mThere is no Unfinished Orders\033[0m")
                receptionist_manage_booking()
                return

            print(" ") #spacing reasons
            print("\033[34mManaging Rooms\033[0m")
            print("\033[34mThese are the current unfinished orders\033[0m")
            #Printing in a nice table format
            header = ["Order ID","Member ID", "Room ID", "Check IN date", "Check OUT date", "Total Price", "Total Days Booked", "Actual payed"]
            print_list_in_a_readable_manner(order_Listz,header)

            while True:
                order_id = input("Please Enter the Order Special ID (type back to go back): ")
                if order_id == 'back':
                    receptionist_manage_booking()
                    break
                if order_id not in order_id_check_unfinished:
                    print("Order ID isnt Registered!")
                    continue
                else:
                    break

            while True:
                yes_no = input("Are you Sure? (Yes or No) (type back to go back): ")
                if yes_no in ['back','no']:
                    receptionist_manage_booking()
                    break
                else:
                    break

            order_Listz.pop(order_id_check.index(order_id))
            from_array_to_txt_file_conversion(order_Listz,'order_report.txt','w')
            print("\033[32mSuccessfully deleted the order\033[00m")
            receptionist_manage_booking()
        case '4':
            receptionist_menu()

def receptionist_view_room_availability():
    room_list = decode_txt_File_to_list_of_data('room.txt')
    order_listz = decode_txt_File_to_list_of_data("order_report.txt")

    # correct headers
    header = ["Room Special ID", "Occupancy/Guest ID", "Pricing", "Cleaning_Status", "Message"]

    while True:
        check_in = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
        if check_in == 'back':
            receptionist_menu()
            return
        else:
            check_in = [int(n) for n in check_in]
            break

    # --- Get Number of Days ---
    while True:
        days_booked = input("How Many Days Are you staying? (type back to go back): ")
        if days_booked == 'back':
            receptionist_manage_booking()
            return
        try:
            days_booked = int(days_booked)
            if days_booked <= 0:
                print("Days must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

    # --- Calculate Check-Out Date ---
    check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

    # --- Find Available Rooms ---
    available_rooms = []
    available_rooms_ids = []
    for room in room_list:
        # room[0] is Room Special ID
        overlapping_orders = [
            order for order in order_listz
            if (order[2] == room[0]) and (order[-1] in ['-', ''])
            and (check_if_two_date_range_intertwine(check_in, check_out, order[3].split('-'), order[4].split('-')))
        ]
        
        if not overlapping_orders:
            available_rooms.append(room)
            available_rooms_ids.append(room[0])

    if not available_rooms:
        print("\033[31mNo rooms are available for this date range.\033[0m")
        receptionist_manage_booking()
        return
    
    print(" ") #spacing reasons
    print("\033[34mManaging Rooms\033[0m")
    print(f"\033[34mAvailable Rooms ({check_in[0]},{check_in[1]},{check_in[2]} - {check_out[0]},{check_out[1]},{check_out[2]}):\033[0m")
    header = ["Room Special ID", "Pricing", "Cleaning_Status", "Message"]
    print_list_in_a_readable_manner(available_rooms,header)

    while True:
        inputs = input("Enter Back to go Back: ")
        if inputs.lower() == 'back':
            receptionist_menu()
            break
        else:
            print("Invalid Input")

#Accountant Functions
def accountant_menu(): #This is just the menu of the Receptionist
    option_dict = {
        '1' : accountant_record_guest_payments,
        '2' : accountant_generate_income_and_outstanding_payment_reports,
        '3' : accountant_generate_monthly_financial_summary,
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

    print()
    option_dict[option_picked]() #calling the function 

def accountant_record_guest_payments():
    order_list = decode_txt_File_to_list_of_data("order_report.txt")
    income_header = ['Order ID','Guest ID','Room Id', 'Check In', 'CheckOut', 'Payment Due','Days Spent', 'Actually Payed']
    print("\033[35mWelcome You are Currently the Accountant\033[0m")
    print("\033[35mGuest Orders and Payments\033[0m")

    print_list_in_a_readable_manner(order_list,income_header)
    accountant_menu()
    pass

def accountant_generate_income_and_outstanding_payment_reports():
    order_list = decode_txt_File_to_list_of_data("order_report.txt")
    guest_list = decode_txt_File_to_list_of_data("guest.txt")
    guest_id_list = [n[0] for n in guest_list]
    income_header = ['Date','Guest ID','Guest Name','Room Id', 'Days Spent', 'Rate per Night', 'Total Income']

    while True:
        print("\033[35mWelcome You are Currently the Accountant\033[0m")
        print("\033[35mOutstanding and Income Reports\033[0m")
        print("1. Daily")
        print("2. Monthly")
        print("3. Yearly")
        print("4. Back")
        option_picked = str(input("\033[35mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        if option_picked in ['1','2','3','4']:
            break

    match option_picked:
        case '1':
            while True:
                date = input_date("Date? (Format : DD-MM-YYYY) (type back to go back): ")

                if date == 'back':
                    accountant_menu()
                    break
                else:
                    date = [str(int(n)) for n in date]
                    break

            income_report_list = []
            outstanding_report_list = []
            for row in order_list:
                if row[4].split('-') == date and row[-1] not in ['-',''] :
                    income_report_list.append([row[4],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-1]])
                elif row[3].split('-') == date and row[-1] in ['-',''] :
                    outstanding_report_list.append([row[3],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-3]])

            print()
            print("\033[35mIncome Report\033[0m")
            print_list_in_a_readable_manner(income_report_list,income_header)
            print("\033[35mOutstanding Report\033[0m")
            print_list_in_a_readable_manner(outstanding_report_list,income_header)
            accountant_menu()

        case '2':
            while True:
                date_input = input("Date? (Format : MM-YYYY) (type back to go back): ")
                date = input_date("",True,True,f'1-{date_input}')

                if date == 'back':
                    accountant_menu()
                    break
                else:
                    date = [str(int(n)) for n in date]
                    break
            income_report_list = []
            outstanding_report_list = []
            for row in order_list:
                if row[4].split('-')[1:] == date[1:] and row[-1] not in ['-',''] :
                    income_report_list.append([row[4],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-1]])
                elif row[3].split('-')[1:] == date[1:] and row[-1] in ['-',''] :
                    outstanding_report_list.append([row[3],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-3]])

            print()
            print("\033[35mIncome Report\033[0m")
            print_list_in_a_readable_manner(income_report_list,income_header)
            print("\033[35mOutstanding Report\033[0m")
            print_list_in_a_readable_manner(outstanding_report_list,income_header)
            accountant_menu()

        case '3':
            while True:
                date_input = input("Date? (Format : YYYY) (type back to go back): ")
                date = input_date("",True,True,f'1-1-{date_input}')

                if date == 'back':
                    accountant_menu()
                    break
                else:
                    date = [str(int(n)) for n in date]
                    break
            income_report_list = []
            outstanding_report_list = []
            for row in order_list:
                if row[4].split('-')[2:] == date[1:] and row[-1] not in ['-',''] :
                    income_report_list.append([row[4],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-1]])
                elif row[3].split('-')[2:] == date[1:] and row[-1] in ['-',''] :
                    outstanding_report_list.append([row[3],row[1],guest_list[guest_id_list.index(row[1])][1],row[2],row[-2],(float(row[-3]) / float(row[-2])),row[-3]])


            print()
            print("\033[35mIncome Report\033[0m")
            print_list_in_a_readable_manner(income_report_list,income_header)
            print("\033[35mOutstanding Report\033[0m")
            print_list_in_a_readable_manner(outstanding_report_list,income_header)
            accountant_menu()
        case '4':
            accountant_menu()

def accountant_generate_monthly_financial_summary():
    order_List = decode_txt_File_to_list_of_data("order_report.txt")
    while True:
        check_input = input("Date? (Format : MM-YYYY) (type back to go back): ")
        check_in = input_date("",True,True,f'1-{check_input}')

        if check_in == 'back':
            accountant_menu()
            break
        else:
            check_in = [str(int(n)) for n in check_in]
            break

    order_tied_to_date = [n for n in order_List if check_in[1:] == n[3].split('-')[1:]]
    total_reservations = len(order_tied_to_date)
    Total_Revenue = sum([float(n[-1]) for n in order_List if n[-1] not in ['','-']])
    Total_Outstanding = sum([float(n[-3]) for n in order_List if n[-1] in ['','-']])
    
    print()
    print("\033[35mWelcome You are Currently the Accountant\033[0m")
    print("\033[35mMonthly Financial Summary\033[0m")
    print(f'Total Reservations: {total_reservations}')
    print(f'Total Revenue: {Total_Revenue}')
    print(f'Total Outstanding: {Total_Outstanding}')
    accountant_menu()
    
    pass

#housekeeper
def housekeeper_menu(): #This is just the menu of the House Keeper
    option_dict = {
        '1' : housekeeper_update_room_cleaning_status,
        '2' : housekeeper_report_mauntenance_issues,
        '3' : housekeeper_view_daily_cleaning_schedule,
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

def housekeeper_update_room_cleaning_status():
    pass

def housekeeper_report_mauntenance_issues():
    pass

def housekeeper_view_daily_cleaning_schedule():
    pass

#  Guest 
def guest_menu(): #This is just the menu of the Receptionist
    option_dict = {
        '1' : guest_view_available_rooms,
        '2' : guest_make_cancel_reservation,
        '3' : guest_view_billing_summary_payment_history,
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

def guest_view_available_rooms():
    pass

def guest_make_cancel_reservation():
    pass

def guest_view_billing_summary_payment_history():
    pass

#Role dict
startup()
#Part to create the files if it havent been created