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
    files_to_create = ["room.txt", "order_report.txt", "system_report.txt","guest.txt","Cleaning_Report.txt"]
    
    for file_name in files_to_create:
        try:
            open(file_name, 'x').close()
        except FileExistsError:
            pass
        except Exception as e:
            print(f"Error creating {file_name}: {e}")

#Built in function replacements (RAHHHHHH WHY?)
def _strip(s):
    if not s:
        return s

    start = 0
    end = len(s) - 1

    # Strip from the left
    while start <= end and s[start] in (' ', '\t', '\n', '\r'):
        start += 1

    # Strip from the right
    while end >= start and s[end] in (' ', '\t', '\n', '\r'):
        end -= 1

    return s[start:end+1]
def _append(lists, thing_to_add):
    new_list = lists + [thing_to_add,]
    return new_list
def _split(string,thing_to_split_it_with):
    word = ''
    res_list = []
    for char in string:
        if char == thing_to_split_it_with :
            res_list = _append(res_list,thing_to_add=word)
            word = ""
        else:
            word += char

    res_list = _append(res_list,word)
    return res_list

def _len(string):
    count = 0
    for i in string:count += 1
    return count

def _join(lists, what_to_split_with):
    if not lists:
        return ""
    
    res = ""
    for i in range(_len(lists)):
        res += str(lists[i])

        if i < _len(lists) - 1:
            res += what_to_split_with
    return res

def _ljust(string, width):
    s_len = _len(string)
    if s_len >= width:
        return string
    
    res = string
    for _ in range(width - s_len):
        res += " "
    return res

def _pop(lists, index):
    new_list = []
    for i in range(_len(lists)):
        if i != index:
            new_list = _append(new_list, lists[i])
    return new_list

def _remove(lists, target_item):
    new_list = []
    found = False
    for i in range(_len(lists)):
        if lists[i] == target_item and not found:
            found = True
            continue
        new_list = _append(new_list, lists[i])
    return new_list

def _find_index(lists, target):
    for i in range(_len(lists)):
        if lists[i] == target:
            return i
    return -1

def _sum(iterable):
    total = 0.0
    for item in iterable:
        total += float(item)
    return total

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
                        res_list = _append(res_list,_split(_strip(line),','))

                    return res_list
        except Exception:
            print("Error at Decoding ")

def from_array_to_txt_file_conversion(lists, file_type, Typing_type):
    if not lists:
        with open(file_type,Typing_type) as file:
            file.write('')
        return
    
    is_2D_arr = False
    try:
        if isinstance(lists[0], list): #I cant recreate isinstance without type()
            is_2D_arr = True
    except (IndexError, TypeError):
        is_2D_arr = False
    
    try:
        with open(file_type, Typing_type) as file:
            if is_2D_arr:
                for row in lists:
                    row_str = [str(item) for item in row] #I cant also make a int into a string without built in
                    file.write(_join(row_str,",") + "\n")
            else:
                lists_str = [str(item) for item in lists]
                file.write(_join(lists_str,",") + "\n")

    except IOError as e:
        print(f"\033[31mError writing to file {file_type}: {e}\033[0m")
    except Exception as e:
        print(f"\033[31mUnexpected error: {e}\033[0m")
def input_date(prompt, allow_back=True, special=False, special_data=''):
    while True:
        if not special:
            resp = input(prompt)
        else:
            resp = special_data
            
        if allow_back and resp.lower() == 'back':
            return 'back'
            
        try:
            parts = _split(resp, "-")
            if _len(parts) != 3:
                raise ValueError
                
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            
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
                
            if not (_len(str(year)) == 4):
                print("\033[31mYear must be 4 digits.\033[0m")
                if special:
                    return
                continue
                
            return parts
            
        except (ValueError, IndexError):
            print("\033[31mInvalid input / Date Format: (05-06-2008)\033[0m")
            if special:
                return
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
    Determine whether two date ranges overlap using manual functions.
    """
    def to_tuple(d):
        if not (isinstance(d, (list, tuple)) and _len(d) == 3):
            raise ValueError("date must be [day,month,year]")
        
        day, month, year = int(d[0]), int(d[1]), int(d[2])
        return (year, month, day)  

    s1, e1 = to_tuple(start1), to_tuple(end1)
    s2, e2 = to_tuple(start2), to_tuple(end2)

    # Normalize so start <= end
    if s1 > e1:
        s1, e1 = e1, s1
    if s2 > e2:
        s2, e2 = e2, s2

    

    if inclusive:
        # Overlap if neither range ends before the other begins
        return not (e1 < s2 or e2 < s1)
    else:
        # Overlap only if they dont touch at the exact same day
        return not (e1 <= s2 or e2 <= s1)
def check_if_a_date_is_in_range(date1, start1, end1, month_only=False):
    def to_tuple(d):
        if not (isinstance(d, (list, tuple)) and _len(d) == 3):
            raise ValueError("date must be [day,month,year]")
            
        day, month, year = int(d[0]), int(d[1]), int(d[2])
        
        if month_only:
            return (year, month)
        else:
            return (year, month, day)
    
    date1 = to_tuple(date1)
    start1 = to_tuple(start1)
    end1 = to_tuple(end1)
    
    if start1 > end1:
        start1, end1 = end1, start1
    
    return start1 <= date1 <= end1
def print_list_in_a_readable_manner(data, header):
    if not data:
        print("No data to display.")
        return

    column_length = 25
    cols = _len(header)  

    #remove the headers edge like /n or space
    header = [_strip(str(h)) for h in header]

    #print header
    print(_join([h.ljust(column_length) for h in header],"|"))

    #print separator
    print(_join(list("-" * column_length for _ in range(cols)),"+"))

    #print rows
    for row in data:
        row_cells = []
        for i in range(cols):
            #convert to string to handle missing columns
            val = str(_strip(row[i] if i < _len(row) else ""))
            row_cells = _append(row_cells,val.ljust(column_length))

        print(_join(row_cells,"|"))




#Manager Functions
def manager_menu(): #This is just the menu of the manager,
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
    added_room_list = ['-', '-', 'True', '']
    
    while not added_room_list[3]:
        added_room_list[3] = _strip(input("What's This Room Called?: "))
        if not added_room_list[3]:
            print("\033[31mRoom name cannot be empty!\033[0m")
    
    while not isinstance(added_room_list[1], float): 
        try:
            price_input = _strip(input("What will the Price be for this room? (type: back to go back to menu): "))
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

    if _len(room_list) < 1:
        added_room_list[0] = "0"
    else:
        last_room = room_list[_len(room_list) - 1]
        added_room_list[0] = str(int(last_room[0]) + 1)

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
    
    special_id_list = []
    for data in room_data_List:
        special_id_list = _append(special_id_list, data[0])

    while True:
        try:
            temp_index = _strip(input("Please Enter the Special ID of the Room you want to delete (type: back to go back to menu): "))
            if temp_index.lower() == 'back':
                manager_manage()
                return
            else:
                temp_index = str(int(temp_index))
        except ValueError:
            print("Invalid Input")
            continue
            
        found_idx = -1
        for i in range(_len(special_id_list)):
            if special_id_list[i] == temp_index:
                found_idx = i
                break
        
        if found_idx != -1:
            room_data_List = _pop(room_data_List, found_idx)
            break
            
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")

    order_lists = []
    for n in order_list:
        if n[-1] in ['-', ''] and n[2] == temp_index:
            order_lists = _append(order_lists, n)
            
    while True:
        yes_no = _strip(input(f"Are You Sure to Delete This room? (Unfinished Orders Tied: {_len(order_lists)}) (type: back to go back to menu):  "))
        if yes_no.lower() in ['back', 'no']:
            manager_manage()
            return
        elif yes_no.lower() == 'yes':
            for target in order_lists:
                order_list = _remove(order_list, target)
            
            from_array_to_txt_file_conversion(order_list, 'order_report.txt', 'w')
            from_array_to_txt_file_conversion(room_data_List, "room.txt", "w")
            print(f"\033[32mSuccessfully Removed a Room\033[00m")
            manager_manage()
            return

def manager_update():
    room_data_List = decode_txt_File_to_list_of_data('room.txt')
    if not room_data_List:
        print("\033[31mNo rooms to Update.\033[0m")
        manager_manage()
        return
    
    special_id_list = []
    for data in room_data_List:
        special_id_list = _append(special_id_list, data[0])
    
    while True:
        try:
            temp_input = _strip(input("Please Enter the Unique ID of the Room you want to Update (type: back to go back to menu): "))
            if temp_input.lower() == 'back':
                manager_manage()
                return
            else:
                temp_input = str(int(temp_input))
        except ValueError:
            print("Invalid Input")
            continue
            
        found_idx = _find_index(special_id_list, temp_input)
        if found_idx != -1:
            temp_index = found_idx
            break
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")

    while True:
        try:
            print("")
            print("\033[33mWhat do you want to update?\033[00m")
            print(_join(["1.Price (Currently: ", room_data_List[temp_index][1], ")"], ""))
            print(_join(["2.Cleaning Status (Currently: ", room_data_List[temp_index][2], ")"], ""))
            
            option_input = _strip(input("\033[33mEnter Here\033[00m (type: back to go back to menu): "))
            if option_input.lower() == 'back':
                manager_update()
                return
            else:
                option = int(option_input) 
        except ValueError:
            print("Invalid Input")
            continue

        if 0 < option < 3:
            break
        print("\033[31mIndex must be between 1 and 2\033[0m")

    match option:
        case 1:
            while True:
                try:
                    x_input = _strip(input("Updated Price (type: back to go back to menu): "))
                    if x_input.lower() == 'back':
                        manager_update()
                        return
                    else:
                        x = float(x_input)
                        break
                except ValueError:
                    print("Invalid Input")
                    continue

        case 2:
            while True:
                x_input = _strip(input("Updated Cleaning Status (ONLY TRUE OR FALSE!) (type: back to go back to menu): "))
                if x_input.lower() == 'back':
                    manager_update()
                    return
                elif x_input.lower() == 'true':
                    x = 'True'
                    break
                elif x_input.lower() == 'false':
                    x = 'False'
                    break
                else:
                    print("Invalid Input")
                    continue
            
    room_data_List[temp_index][option] = str(x)
    from_array_to_txt_file_conversion(room_data_List, "room.txt", "w")
    print(_join(["\033[32mSuccessfully Updated a Room index ", str(temp_index + 1), "\033[00m"], ""))
    manager_manage()

def manager_system_summary():
    room_list = decode_txt_File_to_list_of_data('room.txt')
    order_list = decode_txt_File_to_list_of_data('order_report.txt')
    guest_list = decode_txt_File_to_list_of_data("guest.txt")

    occupied_count = 0
    for n in room_list:
        if n[-1] not in ['', '-']:
            occupied_count += 1
    
    total_rooms = _len(room_list)
    if total_rooms > 0:
        occupancy_rate = (occupied_count / total_rooms) * 100
    else:
        occupancy_rate = 0

    income_values = []
    for n in order_list:
        if n[-1] not in ['', '-']:
            income_values = _append(income_values, n[-1])
    
    total_income = _sum(income_values)

    print("")
    print("\033[33mView system summary\033[00m")
    print(_join(["1. Total Bookings: ", str(_len(order_list))], ""))
    print(_join(["2. Total Guests: ", str(_len(guest_list))], ""))
    print(_join(["3. Total Income: ", str(total_income)], ""))
    print(_join(["4. Total Rooms: ", str(total_rooms)], ""))
    print(_join(["5. Occupancy Rate: ", str(occupancy_rate), "%"], ""))
    print()
    manager_menu()

def manager_generate():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    order_list = decode_txt_File_to_list_of_data("order_report.txt")

    while True:
        print(" ")
        print("\033[33mWelcome You are Currently the Manager\033[0m")
        print("1. View Daily Performance Report")
        print("2. View Monthly Performance Report")
        print("3. Back")
        option_picked = _strip(input("\033[33mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) 
        
        valid_options = ['1', '2', '3']
        is_valid = False
        for opt in valid_options:
            if option_picked == opt:
                is_valid = True
                break
        
        if is_valid:
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
                    return
                else:
                    break

            check_in_check = []
            for n in check_in:
                check_in_check = _append(check_in_check, str(int(n)))

            print()
            
            occupied_rooms = []
            for n in order_list:
                if check_if_a_date_is_in_range(check_in, _split(n[3], '-'), _split(n[4], '-')):
                    occupied_rooms = _append(occupied_rooms, n)
            
            total_rooms = _len(room_list)
            occupied_len = _len(occupied_rooms)
            occupancy_rate = (occupied_len / total_rooms * 100) if total_rooms > 0 else 0
            
            today_bookings = []
            for n in order_list:
                if _split(n[3], '-') == check_in_check:
                    today_bookings = _append(today_bookings, n)
            
            total_booking = _len(today_bookings)
            
            if total_booking == 0:
                total_income = 0
                avg_income_per_book = 0
            else:
                income_list = []
                for n in today_bookings:
                    income_list = _append(income_list, n[-3])
                total_income = _sum(income_list)
                avg_income_per_book = total_income / total_booking
            
            check_out_count = 0
            for n in order_list:
                if _split(n[4], '-') == check_in_check:
                    check_out_count += 1

            print(_join(["\033[33mHotel Daily Performance Report (Date: ", check_in[0], "-", check_in[1], "-", check_in[2], ")\033[0m"], ""))
            print(_join(["Total Rooms: ", str(total_rooms)], ""))
            print(_join(["Occupied Rooms: ", str(occupied_len)], ""))
            print(_join(["Occupancy Rate: ", str(occupancy_rate), "%"], ""))
            print()
            print(_join(["Bookings Today: ", str(total_booking)], ""))
            print(_join(["Total Income: ", str(total_income)], ""))
            print(_join(["Average Income per Booking: ", str(avg_income_per_book)], ""))
            print()
            print(_join(["Check-ins Today: ", str(total_booking)], ""))
            print(_join(["Check-Outs Today: ", str(check_out_count)], ""))
            manager_generate()

        case "2":
            while True:
                check_in = input_date("Date? (Format : DD-MM-YYYY) (type back to go back): ")
                if check_in == 'back':
                    manager_generate()
                    return
                else:
                    break
            print()
            
            occupied_rooms = []
            for n in order_list:
                if check_if_a_date_is_in_range(check_in, _split(n[3], '-'), _split(n[4], '-'), True):
                    occupied_rooms = _append(occupied_rooms, n)
            
            total_rooms = _len(room_list)
            occupied_len = _len(occupied_rooms)
            occupancy_rate = (occupied_len / total_rooms * 100) if total_rooms > 0 else 0

            check_in_month_year = [str(int(check_in[1])), str(int(check_in[2]))]

            month_bookings = []
            for n in order_list:
                parts = _split(n[3], '-')
                if [str(int(parts[1])), str(int(parts[2]))] == check_in_month_year:
                    month_bookings = _append(month_bookings, n)
            
            total_booking = _len(month_bookings)

            if total_booking == 0:
                total_income = 0
                avg_income_per_book = 0
            else:
                income_list = []
                for n in month_bookings:
                    income_list = _append(income_list, n[-3])
                total_income = _sum(income_list)
                avg_income_per_book = total_income / total_booking

            check_out_month_count = 0
            for n in order_list:
                parts = _split(n[4], '-')
                if [str(int(parts[1])), str(int(parts[2]))] == check_in_month_year:
                    check_out_month_count += 1

            print(_join(["\033[33mHotel Monthly Performance Report (Date: ", check_in[1], "-", check_in[2], ")\033[0m"], ""))
            print(_join(["Total Rooms: ", str(total_rooms)], ""))
            print(_join(["Occupied Rooms: ", str(occupied_len)], ""))
            print(_join(["Occupancy Rate: ", str(occupancy_rate), "%"], ""))
            print()
            print(_join(["Total Bookings this Month: ", str(total_booking)], ""))
            print(_join(["Total Monthly Income: ", str(total_income)], ""))
            print(_join(["Average Income per Booking: ", str(avg_income_per_book)], ""))
            print()
            print(_join(["Total Check-ins: ", str(total_booking)], ""))
            print(_join(["Total Check-Outs: ", str(check_out_month_count)], ""))
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
    header = ['Special_ID', 'Name', 'phone_number', 'email', 'address']

    while True:
        print(" ")
        print("\033[34mWelcome You are Currently the Receptionist\033[0m")
        print("\033[34mThese are the current Guests\033[0m")
        
        print_list_in_a_readable_manner(guest_List, header)

        print("\033[34mWhat do you want to do?\033[0m")
        print("1. Register a New Guest")
        print("2. Update a Existing Guest")
        print("3. Back to menu")
        option_picked = _strip(input("\033[34mEnter: \033[0m"))
        
        if option_picked == '1':
            guest_len = _len(guest_List)
            if guest_len < 1:
                receptionist_register_new_guest(0)
            else:
                last_guest = guest_List[guest_len - 1]
                latest_special_id = int(last_guest[0])
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
    password = input("Enter Guest Password")

    input_List = [str(latest_special_Id+1),Name, phone_Number, email, address,password]
    from_array_to_txt_file_conversion([input_List], 'guest.txt', 'a+')
    print("\033[32mGuest registered successfully!\033[0m")
    receptionist_register()

def receptionist_update_guest():
    guest_data_List = decode_txt_File_to_list_of_data('guest.txt')
    if not guest_data_List:
        print("\033[31mNo Guests to Update.\033[0m")
        receptionist_manage_booking()
        return
    
    special_id_list = []
    for data in guest_data_List:
        special_id_list = _append(special_id_list, data[0])
    
    while True:
        try:
            temp_input = _strip(input("Please enter the Unique ID of the Guest you want to edit (type: back to go back to menu): "))
            if temp_input.lower() == 'back':
                receptionist_register()
                return
            else:
                temp_input = str(int(temp_input))
        except ValueError:
            print("Invalid Input")
            continue

        found_idx = _find_index(special_id_list, temp_input)
        if found_idx != -1:
            temp_index = found_idx
            break
        print(f"\033[31mSpecial ID Dont Exists!\033[0m")
    
    while True:
        try:
            print("")
            print("\033[34mWhat do you want to update?\033[00m")
            print(_join(["1.Name (Currently: ", guest_data_List[temp_index][1], ")"], ""))
            print(_join(["2.Phone Number (Currently: ", guest_data_List[temp_index][2], ")"], ""))
            print(_join(["3.Email (Currently: ", guest_data_List[temp_index][3], ")"], ""))
            print(_join(["4.Address (Currently: ", guest_data_List[temp_index][4], ")"], ""))
            print(_join(["5.Password"], ""))

            option_input = _strip(input("\033[34mEnter Here\033[00m (type: back to go back to menu): "))
            if option_input.lower() == 'back':
                receptionist_register()
                return
            else:
                option = int(option_input) 
        except ValueError:
            print("Invalid Input")
            continue

        if 0 < option < 6:
            break
        print("\033[31mIndex must be between 1 and 5\033[0m")

    match option:
        case 1 | 2 | 3 | 4 | 5:
            labels = ["", "Name", "Phone Number", "Email", "Address","Password"]
            while True:
                x = _strip(input(_join(["Updated ", labels[option], " (type: back to go back to menu): "], "")))
                if x.lower() == 'back':
                    receptionist_register()
                    return
                else:
                    break

    guest_data_List[temp_index][option] = str(x)
    from_array_to_txt_file_conversion(guest_data_List, "guest.txt", 'w')
    print(f"\033[32mSuccessfully Updated a Guest \033[00m")
    receptionist_register()

def receptionist_manage_booking():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    guest_list = decode_txt_File_to_list_of_data("guest.txt")
    order_Listz = decode_txt_File_to_list_of_data("order_report.txt")
    
    order_id_check = []
    for row in order_Listz:
        order_id_check = _append(order_id_check, row[0])

    order_id_check_unfinished = []
    for row in order_Listz:
        if row[-1] in ['-', '']:
            order_id_check_unfinished = _append(order_id_check_unfinished, row[0])

    option_picked = None
    while option_picked not in ['1', '2', '3', '4']:
        print(" ")
        print("\033[34mManaging Rooms\033[0m")
        print("\033[34mWhat do you want to do?\033[0m")
        print("1. Check IN a Room")
        print("2. Check Out a Room")
        print("3. Cancel a Order")
        print("4. Back")
        option_picked = _strip(input("\033[34mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

    match option_picked:
        case "1":
            while True:
                check_in_raw = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
                if check_in_raw == 'back':
                    receptionist_manage_booking()
                    return
                check_in = []
                for n in check_in_raw:
                    check_in = _append(check_in, int(n))
                break

            while True:
                days_input = _strip(input("How Many Days Are you staying? (type back to go back): "))
                if days_input == 'back':
                    receptionist_manage_booking()
                    return
                try:
                    days_booked = int(days_input)
                    if days_booked <= 0:
                        print("Days must be greater than 0")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")

            check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

            available_rooms = []
            available_rooms_ids = []
            for room in room_list:
                overlapping = False
                for order in order_Listz:
                    if (order[2] == room[0]) and (order[-1] in ['-', '']):
                        if check_if_two_date_range_intertwine(check_in, check_out, _split(order[3], '-'), _split(order[4], '-')):
                            overlapping = True
                            break
                
                if not overlapping:
                    available_rooms = _append(available_rooms, room)
                    available_rooms_ids = _append(available_rooms_ids, room[0])

            if _len(available_rooms) == 0:
                print("\033[31mNo rooms are available for this date range.\033[0m")
                receptionist_manage_booking()
                return

            print(_join(["\n\033[34mAvailable Rooms (", str(check_in[0]), ",", str(check_in[1]), ",", str(check_in[2]), " - ", str(check_out[0]), ",", str(check_out[1]), ",", str(check_out[2]), "):\033[0m"], ""))
            print_list_in_a_readable_manner(available_rooms, ["Room Special ID", "Pricing", "Cleaning_Status", "Message"])

            print("\033[34mCurrent Guests:\033[0m")
            print_list_in_a_readable_manner(guest_list, ['Special_ID', 'Name', 'phone_number', 'email', 'address'])

            guest_ids = []
            for guest in guest_list:
                guest_ids = _append(guest_ids, guest[0])

            while True:
                guest_id = _strip(input("Enter Guest Special ID (type back to go back): "))
                if guest_id == 'back':
                    receptionist_manage_booking()
                    return
                if _find_index(guest_ids, guest_id) == -1:
                    print("Guest ID isn't registered!")
                    continue
                break

            while True:
                room_id = _strip(input("Enter Room Special ID (type back to go back): "))
                if room_id == 'back':
                    receptionist_manage_booking()
                    return
                if _find_index(available_rooms_ids, room_id) == -1:
                    print("Room ID isn't available!")
                    continue
                break

            room_idx = -1
            for i in range(_len(room_list)):
                if room_list[i][0] == room_id:
                    room_idx = i
                    break
            
            total_price = float(room_list[room_idx][1]) * days_booked

            new_order = [
                str(int(order_Listz[_len(order_Listz)-1][0]) + 1) if order_Listz else "0",
                str(guest_id),
                str(room_id),
                _join([str(n) for n in check_in], "-"),
                _join([str(n) for n in check_out], "-"),
                str(total_price),
                str(days_booked),
                '-'
            ]

            from_array_to_txt_file_conversion(new_order, 'order_report.txt', "a+")
            print("\033[32mSuccessfully Checked In a Guest\033[0m")
            receptionist_manage_booking()

        case '2':
            if _len(order_id_check_unfinished) < 1:
                print("\033[91mThere is no Unfinished Orders\033[0m")
                receptionist_manage_booking()
                return

            print_list_in_a_readable_manner(order_Listz, ["Order ID", "Member ID", "Room ID", "Check IN", "Check OUT", "Price", "Days", "Paid"])

            while True:
                order_id = _strip(input("Please Enter the Order Special ID (type back to go back): "))
                if order_id == 'back':
                    receptionist_manage_booking()
                    return
                if _find_index(order_id_check, order_id) == -1:
                    print("Order ID isnt Registered!")
                    continue
                break

            while True:
                pay_input = _strip(input("Amount Actually Payed? (type: back to go back to menu): "))
                if pay_input.lower() == "back":
                    receptionist_manage_booking()
                    return
                try:
                    actually_payed = str(float(pay_input))
                    break
                except ValueError:
                    print("Invalid Input")

            target_idx = _find_index(order_id_check, order_id)
            order_Listz[target_idx][-1] = actually_payed
            from_array_to_txt_file_conversion(order_Listz, 'order_report.txt', 'w')
            print(f"\033[32mSuccessfully Check Out a Guest \033[00m")
            receptionist_manage_booking()

        case '3':
            if _len(order_id_check_unfinished) < 1:
                print("\033[91mThere is no Unfinished Orders\033[0m")
                receptionist_manage_booking()
                return

            print_list_in_a_readable_manner(order_Listz, ["Order ID", "Member ID", "Room ID", "Check IN", "Check OUT", "Price", "Days", "Paid"])

            while True:
                order_id = _strip(input("Please Enter the Order Special ID (type back to go back): "))
                if order_id == 'back':
                    receptionist_manage_booking()
                    return
                if _find_index(order_id_check_unfinished, order_id) == -1:
                    print("Order ID isnt Registered or is already finished!")
                    continue
                break

            confirm = _strip(input("Are you Sure? (Yes or No) (type back to go back): "))
            if confirm.lower() in ['yes', 'y']:
                target_idx = _find_index(order_id_check, order_id)
                order_Listz = _pop(order_Listz, target_idx)
                from_array_to_txt_file_conversion(order_Listz, 'order_report.txt', 'w')
                print("\033[32mSuccessfully deleted the order\033[00m")
            
            receptionist_manage_booking()

        case '4':
            receptionist_menu()

def receptionist_view_room_availability():
    room_list = decode_txt_File_to_list_of_data('room.txt')
    order_listz = decode_txt_File_to_list_of_data("order_report.txt")

    header = ["Room Special ID", "Pricing", "Cleaning_Status", "Message"]

    while True:
        check_in_raw = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
        if check_in_raw == 'back':
            receptionist_menu()
            return
        
        check_in = []
        for n in check_in_raw:
            check_in = _append(check_in, int(n))
        break

    while True:
        days_input = _strip(input("How Many Days Are you staying? (type back to go back): "))
        if days_input == 'back':
            receptionist_manage_booking()
            return
        try:
            days_booked = int(days_input)
            if days_booked <= 0:
                print("Days must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number.")

    check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

    available_rooms = []
    for room in room_list:
        overlapping = False
        for order in order_listz:
            if (order[2] == room[0]) and (order[-1] in ['-', '']):
                order_start = _split(order[3], '-')
                order_end = _split(order[4], '-')
                if check_if_two_date_range_intertwine(check_in, check_out, order_start, order_end):
                    overlapping = True
                    break
        
        if not overlapping:
            available_rooms = _append(available_rooms, room)

    if _len(available_rooms) == 0:
        print("\033[31mNo rooms are available for this date range.\033[0m")
        receptionist_manage_booking()
        return
    
    print(" ")
    print("\033[34mManaging Rooms\033[0m")
    
    date_range_str = _join([
        "(", str(check_in[0]), ",", str(check_in[1]), ",", str(check_in[2]), 
        " - ", 
        str(check_out[0]), ",", str(check_out[1]), ",", str(check_out[2]), ")"
    ], "")
    
    print(_join(["\033[34mAvailable Rooms ", date_range_str, ":\033[0m"], ""))
    print_list_in_a_readable_manner(available_rooms, header)

    while True:
        choice = _strip(input("Enter Back to go Back: "))
        if choice.lower() == 'back':
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
    
    guest_id_list = []
    for n in guest_list:
        guest_id_list = _append(guest_id_list, n[0])
        
    income_header = ['Date', 'Guest ID', 'Guest Name', 'Room Id', 'Days Spent', 'Rate per Night', 'Total Income']

    while True:
        print("\033[35mWelcome You are Currently the Accountant\033[0m")
        print("\033[35mOutstanding and Income Reports\033[0m")
        print("1. Daily")
        print("2. Monthly")
        print("3. Yearly")
        print("4. Back")
        option_picked = _strip(input("\033[35mPlease pick one just state the number\033[0m (eg 1,2,3,4): "))

        if option_picked in ['1', '2', '3', '4']:
            break

    if option_picked == '4':
        accountant_menu()
        return

    # Handle Date Input based on selection
    while True:
        if option_picked == '1':
            date_raw = input_date("Date? (Format : DD-MM-YYYY) (type back to go back): ")
        elif option_picked == '2':
            m_y = _strip(input("Date? (Format : MM-YYYY) (type back to go back): "))
            date_raw = input_date("", True, True, _join(['1-', m_y], "")) if m_y != 'back' else 'back'
        elif option_picked == '3':
            y = _strip(input("Date? (Format : YYYY) (type back to go back): "))
            date_raw = input_date("", True, True, _join(['1-1-', y], "")) if y != 'back' else 'back'

        if date_raw == 'back':
            accountant_menu()
            return
        
        target_date = []
        for n in date_raw:
            target_date = _append(target_date, str(int(n)))
        break

    income_report_list = []
    outstanding_report_list = []

    for row in order_list:
        check_in_parts = _split(row[3], '-')
        check_out_parts = _split(row[4], '-')
        
        # Determine if row matches time period criteria
        match = False
        if option_picked == '1':
            is_income_match = (check_out_parts == target_date)
            is_out_match = (check_in_parts == target_date)
        elif option_picked == '2':
            is_income_match = (check_out_parts[1:] == target_date[1:])
            is_out_match = (check_in_parts[1:] == target_date[1:])
        else: # Yearly
            is_income_match = (check_out_parts[2:] == target_date[2:])
            is_out_match = (check_in_parts[2:] == target_date[2:])

        # Get Guest Name
        g_idx = _find_index(guest_id_list, row[1])
        g_name = guest_list[g_idx][1] if g_idx != -1 else "Unknown"
        
        # Calculate Rate
        days = float(row[-2])
        total_val = float(row[-3])
        rate = total_val / days if days > 0 else 0

        # Categorize into Income or Outstanding
        if is_income_match and row[-1] not in ['-', '']:
            income_report_list = _append(income_report_list, [row[4], row[1], g_name, row[2], row[-2], rate, row[-1]])
        elif is_out_match and row[-1] in ['-', '']:
            outstanding_report_list = _append(outstanding_report_list, [row[3], row[1], g_name, row[2], row[-2], rate, row[-3]])

    print("\n\033[35mIncome Report\033[0m")
    print_list_in_a_readable_manner(income_report_list, income_header)
    print("\n\033[35mOutstanding Report\033[0m")
    print_list_in_a_readable_manner(outstanding_report_list, income_header)
    accountant_menu()

def accountant_generate_monthly_financial_summary():
    order_List = decode_txt_File_to_list_of_data("order_report.txt")
    
    while True:
        check_input = _strip(input("Date? (Format : MM-YYYY) (type back to go back): "))
        check_in_raw = input_date("", True, True, _join(['1-', check_input], ""))

        if check_in_raw == 'back':
            accountant_menu()
            return
        else:
            check_in = []
            for n in check_in_raw:
                check_in = _append(check_in, str(int(n)))
            break

    order_tied_to_date = []
    for n in order_List:
        order_start_parts = _split(n[3], '-')
        if check_in[1:] == order_start_parts[1:]:
            order_tied_to_date = _append(order_tied_to_date, n)
            
    total_reservations = _len(order_tied_to_date)

    revenue_values = []
    for n in order_tied_to_date:
        if n[-1] not in ['', '-']:
            revenue_values = _append(revenue_values, n[-1])
    total_revenue = _sum(revenue_values)

    outstanding_values = []
    for n in order_tied_to_date:
        if n[-1] in ['', '-']:
            outstanding_values = _append(outstanding_values, n[-3])
    total_outstanding = _sum(outstanding_values)
    
    print()
    print("\033[35mWelcome You are Currently the Accountant\033[0m")
    print("\033[35mMonthly Financial Summary\033[0m")
    print(_join(['Total Reservations: ', str(total_reservations)], ""))
    print(_join(['Total Revenue: ', str(total_revenue)], ""))
    print(_join(['Total Outstanding: ', str(total_outstanding)], ""))
    
    accountant_menu()

#housekeeper
def housekeeper_menu(): #This is just the menu of the House Keeper
    option_dict = {
        '1' : housekeeper_update_room_cleaning_status,
        '2' : housekeeper_report_maintenance_issues,
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
    #Room ID, cleaned date
    room_list = decode_txt_File_to_list_of_data("room.txt")
    cleaning_list = decode_txt_File_to_list_of_data("Cleaning_Report.txt")
    room_list_id = [x[0] for x in room_list]

    while True:
        print(" ") #spacing reasons
        print("\033[36mWelcome You are Currently the Housekeeping\033[0m")
        dates = input_date("Please enter the Date you're going to clean (Enter back to go back) (format = dd-mm-yyyy):")
        if dates == "back":
            housekeeper_menu()
            return

        header = ['Room Special ID', 'Pricing', 'Cleaning_Status', 'Room Type']

        # get cleaned room IDs for that date
        cleaned_ids = [x[0] for x in cleaning_list if x[1] == _join(dates,"-")]

        # filter uncleaned rooms
        room_list = [room for room in room_list if room[0] not in cleaned_ids]

        if _len(room_list) == 0:
            print("\033[36mNo Room uncleaned at this date\033[0m")
            continue

        room_list_id = [x[0] for x in room_list]

        print_list_in_a_readable_manner(room_list, header)

        while True:
            room_id_cleaned = input("Enter the Room ID you want to Clean: ")
            if room_id_cleaned in room_list_id:
                break
            print("Room ID doesn't exist!")

        cleaning_list = _append(cleaning_list, [room_id_cleaned, dates])
        from_array_to_txt_file_conversion(cleaning_list, 'Cleaning_Report.txt', 'w')

        print(f"\033[36mSuccesfully Cleaned room {room_id_cleaned} at {dates}\033[0m")
        housekeeper_menu()
        return

def housekeeper_report_maintenance_issues():
    system_report = decode_txt_File_to_list_of_data("system_report.txt")

    print(" ") #spacing reasons
    issue = input("\033[36mEnter the reported Issue\033[0m")
    system_report = _append(system_report,issue)
    from_array_to_txt_file_conversion(system_report,"system_report.txt",'w')
    print("Succesfully Added Maintenance issues: ")
    housekeeper_menu()

def housekeeper_view_daily_cleaning_schedule():
    #Room ID, cleaned date
    room_list = decode_txt_File_to_list_of_data("room.txt")
    cleaning_list = decode_txt_File_to_list_of_data("Cleaning_Report.txt")
    room_list_id = [x[0] for x in room_list]

    print(" ") #spacing reasons
    print("\033[36mWelcome You are Currently the Housekeeping\033[0m")
    dates = input_date("Please enter the Date you want to see schedule for  (Enter back to go back) (format = dd-mm-yyyy):")
    if dates == "back":
        housekeeper_menu()
        return
    
    print("")
    print(f"\033[36mUncleaned Room at date {dates}\033[0m")
    header = ['Room Special ID', 'Pricing', 'Cleaning_Status', 'Room Type']

    # get cleaned room IDs for that date
    cleaned_ids = [x[0] for x in cleaning_list if x[1] == _join(dates,"-")]

    # filter uncleaned rooms
    room_list = [room for room in room_list if room[0] not in cleaned_ids]

    if _len(room_list) == 0:
        print("\033[36mNo Room uncleaned at this date\033[0m")
        housekeeper_menu()

    room_list_id = [x[0] for x in room_list]

    print_list_in_a_readable_manner(room_list, header)
    housekeeper_menu()
            

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
    room_list = decode_txt_File_to_list_of_data("room.txt")
    order_Listz = decode_txt_File_to_list_of_data("order_report.txt")


    while True:
        check_in_raw = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
        if check_in_raw == 'back':
            guest_menu()
            return
        check_in = []
        for n in check_in_raw:
            check_in = _append(check_in, int(n))
        break

    while True:
        days_input = _strip(input("How Many Days Are you staying? (type back to go back): "))
        if days_input == 'back':
            guest_menu()
            return
        try:
            days_booked = int(days_input)
            if days_booked <= 0:
                print("Days must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number.")

    check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

    available_rooms = []
    available_rooms_ids = []
    for room in room_list:
        overlapping = False
        for order in order_Listz:
            if (order[2] == room[0]) and (order[-1] in ['-', '']):
                if check_if_two_date_range_intertwine(check_in, check_out, _split(order[3], '-'), _split(order[4], '-')):
                    overlapping = True
                    break
        
        if not overlapping:
            available_rooms = _append(available_rooms, room)
            available_rooms_ids = _append(available_rooms_ids, room[0])

    if _len(available_rooms) == 0:
        print("\033[40mNo rooms are available for this date range.\033[0m")
        receptionist_manage_booking()
        return

    print(_join(["\n\033[40mAvailable Rooms (", str(check_in[0]), ",", str(check_in[1]), ",", str(check_in[2]), " - ", str(check_out[0]), ",", str(check_out[1]), ",", str(check_out[2]), "):\033[0m"], ""))
    print_list_in_a_readable_manner(available_rooms, ["Room Special ID", "Pricing", "Cleaning_Status", "Message"])
    guest_menu()

def guest_make_cancel_reservation():
    guest_list = decode_txt_File_to_list_of_data("guest.txt")
    guest_list_name = [x[1] for x in guest_list]
    order_list = decode_txt_File_to_list_of_data("order_report.txt")
    order_list_id = [x[0] for x in order_list]
    room_list = decode_txt_File_to_list_of_data("room.txt")
    guest_order = []

    while True:
        guest_name = input("Plese enter your Guest Name (Make sure its accurate!) (Enter back to go back): ")
        if guest_name.lower() == "back":
            guest_menu()
            return
        
        elif guest_name in guest_list_name:
            break

        else:
            print("No such Guest Exists!")

    while True:
        guest_pass = input(f"Password (Case Sensitive!) (Enter back to go back): ")
        if guest_pass == guest_list[_find_index(guest_list_name,guest_name)][-1]:

            guest_id = guest_list[_find_index(guest_list_name,guest_name)][0]
            guest_unfinished_order = [x for x in order_list if x[1] == guest_id and x[-1] != '-']
            guest_unfinshed_order_id = [x[0] for x in guest_unfinished_order]
            break
        elif guest_pass == 'back':
            guest_make_cancel_reservation()
            return
        else:
            print("Incorrect password !")

    while True:
        print("")
        print("Welcome you are currently the Guest!")
        print("1. Make a Reservation")
        print("2. Remove a Reservation")
        option_picked = input("Please choose an option (1,2) (Enter back to go back): ")

        if option_picked not in ['1','2']:
            print("Invalid Input!")
        elif option_picked.lower() == 'back':
            guest_menu()
            return
        else:
            break

    if option_picked == '2':
                
        while True:
            print("Current Unfinished Order !")
            header = ['Order ID','Guest ID','Room Id', 'Check In', 'CheckOut', 'Payment Due','Days Spent', 'Actually Payed']
            if _len(guest_unfinished_order) == 0:
                print("This guest have no unfinished Orders!")
                guest_make_cancel_reservation()

            print_list_in_a_readable_manner(guest_unfinished_order,header)
            print("")

            order_id = input("Enter the Order ID to delete (Enter back to go back): ")
            if order_id == 'back':
                guest_make_cancel_reservation() 
                return

            yes_no = input("Are you sure?: ")

            if yes_no.lower() == "yes":
                if order_id in guest_unfinshed_order_id:
                    order_list = _remove(order_list,order_list[_find_index(order_list_id,order_id)])
                    from_array_to_txt_file_conversion(order_list,'order_report.txt','w')
                    print("Succesfully remove this Order!")
                    guest_make_cancel_reservation()

            if yes_no.lower() == "no":
                continue

    if option_picked == '1':
        while True:
            check_in_raw = input_date("Check In Date? (Format: DD-MM-YYYY) (type back to go back): ")
            if check_in_raw == 'back':
                guest_make_cancel_reservation()
                return
            
            check_in = []
            for n in check_in_raw:
                check_in = _append(check_in, int(n))
            break

        while True:
            days_input = _strip(input("How Many Days Are you staying? (type back to go back): "))
            if days_input == 'back':
                guest_make_cancel_reservation()
                return
            
            try:
                days_booked = int(days_input)
                if days_booked <= 0:
                    print("Days must be greater than 0")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number.")

        check_out = calculate_check_out_date_from_check_in_date(check_in, days_booked)

        available_rooms = []
        available_rooms_ids = []
        for room in room_list:
            overlapping = False
            for order in order_list:
                if (order[2] == room[0]) and (order[-1] in ['-', '']):
                    if check_if_two_date_range_intertwine(check_in, check_out, _split(order[3], '-'), _split(order[4], '-')):
                        overlapping = True
                        break
            
            if not overlapping:
                available_rooms = _append(available_rooms, room)
                available_rooms_ids = _append(available_rooms_ids, room[0])

        if _len(available_rooms) == 0:
            print("\033[40mNo rooms are available for this date range.\033[0m")
            guest_make_cancel_reservation()
            return

        print(_join(["\n\033[40mAvailable Rooms (", str(check_in[0]), ",", str(check_in[1]), ",", str(check_in[2]), " - ", str(check_out[0]), ",", str(check_out[1]), ",", str(check_out[2]), "):\033[0m"], ""))
        print_list_in_a_readable_manner(available_rooms, ["Room Special ID", "Pricing", "Cleaning_Status", "Message"])

        while True:
            room_id = _strip(input("Enter Room Special ID (type back to go back): "))
            if room_id == 'back':
                guest_make_cancel_reservation()
                return
            if _find_index(available_rooms_ids, room_id) == -1:
                print("Room ID isn't available!")
                continue
            break

        room_idx = -1
        for i in range(_len(room_list)):
            if room_list[i][0] == room_id:
                room_idx = i
                break
        
        total_price = float(room_list[room_idx][1]) * days_booked

        new_order = [
            str(int(order_list[_len(order_list)-1][0]) + 1) if order_list else "0",
            str(guest_id),
            str(room_id),
            _join([str(n) for n in check_in], "-"),
            _join([str(n) for n in check_out], "-"),
            str(total_price),
            str(days_booked),
            '-'
        ]

        from_array_to_txt_file_conversion(new_order, 'order_report.txt', "a+")
        print("\033[32mSuccessfully reservedt\033[0m")
        guest_make_cancel_reservation()
            


def guest_view_billing_summary_payment_history():
    pass

#Role dict
startup()
#Part to create the files if it havent been created