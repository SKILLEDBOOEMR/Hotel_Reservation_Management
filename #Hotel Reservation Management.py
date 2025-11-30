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
def input_date(prompt, allow_back=True):
    """Prompt for date in DD-MM-YYYY format. Returns list [day, month, year] or 'back'."""
    while True:
        resp = input(prompt).strip()
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
                continue
            if not (1 <= month <= 12):
                print("\033[31mMonth must be between 1 and 12.\033[0m")
                continue
            if not (len(str(year)) == 4):
                print("\033[31mYear must be 4 digits.\033[0m")
                continue
            return parts
        except (ValueError, IndexError):
            print("\033[31mInvalid input / Date Format: (05-06-2008)\033[0m")
            continue
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
    header = ['Room Special ID','Occupancy', 'Pricing','Cleaning_Status', "Room Type"]

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

def manager_add():
    room_list = decode_txt_File_to_list_of_data("room.txt")
    added_room_list = ['-','-','False','-',''] #Occupancy, Price, Cleaning Status, Room_Special_iD, Room Type
    
    # Get room name first
    while not added_room_list[4]:
        added_room_list[4] = input("What's This Room Called?: ").strip()
        if not added_room_list[4]:
            print("\033[31mRoom name cannot be empty!\033[0m")
    
    # Get price
    while type(added_room_list[2]) != float: 
        try:
            price_input = input("What will the Price be for this room? (type: back to go back to menu): ").strip()
            if price_input.lower() == 'back':
                manager_manage()
                return
            
            price = float(price_input)
            if price < 0:
                print("\033[31mPrice cannot be negative!\033[0m")
                continue
            added_room_list[2] = price
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
            print(f"1.Price (Currently: {room_data_List[temp_index][2]})")
            print(f"2.Cleaning Status (Currently: {room_data_List[temp_index][3]})")
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
            
    room_data_List[temp_index][option+1] = str(x)
    from_array_to_txt_file_conversion(room_data_List,"room.txt","w")
    print(f"\033[32mSuccessfully Updated a Room index {temp_index + 1}\033[00m")
    manager_manage()

def manager_system_summary():
    print("")
    print("\033[33mView system summary\033[00m")
    print("1.")
    pass

def manager_generate():
    print("bing bong")
    pass

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
    header = ['Special_ID''Name', 'phone_number','email','address']

    while True:
        print(" ")
        print("\033[34mWelcome You are Currently the Receptionist\033[0m")
        print("\033[34mThese are the current Guests\033[0m")
        print("Index".ljust(10),end="")
        for col in header:
            print(col.ljust(30),end="")
        print()

        for i, row in enumerate(guest_List,start=1):
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
                receptionist_manage_booking()
                return
            else:
                temp_index = str(int(temp_index) - 1)
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
    order_Listz = decode_txt_File_to_list_of_data("order_Report.txt")
    header = ["Room Special ID"'Occupancy Guest ID', 'Pricing','Cleaning_Status', 'Message']
    header2 = ['Special_ID''Name', 'phone_number','email','address']

    option_picked = None
    
    while option_picked not in ['1', '2', '3', '4']: #Checking if the input is valid or not
        print(" ") #spacing reasons
        print("\033[34mManaging Rooms\033[0m")
        print("\033[34mThese are the current Rooms\033[0m")

        # correct headers
        header = ["Room Special ID", "Occupancy/Guest ID", "Pricing", "Cleaning_Status", "Message"]

        # compute column widths from header + data
        cols = len(header)
        rows = room_list if room_list else []
        col_widths = [len(header[i]) for i in range(cols)]
        for r in rows:
            for i in range(min(cols, len(r))):
                col_widths[i] = max(col_widths[i], len(str(r[i])))

        # print header
        print("Index".ljust(6), end=" ")
        for i, col in enumerate(header):
            print(col.ljust(col_widths[i] + 2), end="")
        print()

        # print rows
        for i, row in enumerate(rows, start=1):
            print(str(i).ljust(6), end=" ")
            for j in range(cols):
                val = str(row[j]) if j < len(row) else ""
                print(val.ljust(col_widths[j] + 2), end="")
            print()

        print()

        print("\033[34mThese are the current Guests\033[0m")
        # correct guest headers
        header2 = ['Special_ID', 'Name', 'phone_number', 'email', 'address']

        cols2 = len(header2)
        rows2 = guest_list if guest_list else []
        col_widths2 = [len(header2[i]) for i in range(cols2)]
        for r in rows2:
            for i in range(min(cols2, len(r))):
                col_widths2[i] = max(col_widths2[i], len(str(r[i])))

        print("Index".ljust(6), end=" ")
        for i, col in enumerate(header2):
            print(col.ljust(col_widths2[i] + 2), end="")
        print()

        for i, row in enumerate(rows2, start=1):
            print(str(i).ljust(6), end=" ")
            for j in range(cols2):
                val = str(row[j]) if j < len(row) else ""
                print(val.ljust(col_widths2[j] + 2), end="")
            print()
        print()

        guest_id_check = [row[0] for row in guest_list]
        room_id_check = [row[0] for row in room_list]
        order_id_check = [row[0] for row in order_Listz]
    

        print("\033[34mWhat do you want to do?\033[0m")
        print("1. Check IN a Room")
        print("2. Check Out a Room")
        print("3. Cancel a Order")
        print("4. Back")
        option_picked = str(input("\033[34mPlease pick one just state the number\033[0m (eg 1,2,3,4): ")) #input than changing the input into string
    
    match option_picked:
        case "1":
            while True:
                guest_id = input("Please Enter the Guest Special ID (type back to go back): ")
                if guest_id == 'back':
                    receptionist_manage_booking()
                    break
                if guest_id not in guest_id_check:
                    print("Guest ID isnt Registered!")
                    continue
                else:
                    break

            while True:
                try:
                    room_id = input("Please Enter the Room Special ID (type back to go back): ")
                    if room_id == 'back':
                        receptionist_manage_booking()
                        break

                    if room_id not in room_id_check:
                        print("Room ID isnt Registered!")
                        continue

                    # find the room index using the id lookup list (room_list contains rows)
                    r_count = room_id_check.index(room_id)

                    # occupancy is stored at index 0 (use '-' or '' to mean available)
                    occ = str(room_list[r_count][1]) if len(room_list[r_count]) > 0 else ''
                    if occ in ('-', ''):
                        break
                    else:
                        print("Room is already Occupied!")
                        continue

                except Exception:
                    print("Invalid input")
                    continue

            while True:
                try:
                    days_booked = input("How Many Days Are you staying? (type back to go back): ")
                    if days_booked == 'back':
                        receptionist_manage_booking()
                        break

                    days_booked = str(int(days_booked))
                    break

                except:
                    print("Invalid input")
                    continue

            while True:
                check_in = input_date("Check In Date? (Format : DD-MM-YYYY) (type back to go back): ")
                if check_in == 'back':
                    receptionist_manage_booking()
                    break
                else:
                    break


            for i,row in enumerate(room_id_check):
                if row == room_id:
                    r_count = i

            Total_Price = float(room_list[r_count][2]) * float(days_booked) #Calculates the Prices
            room_list[r_count][0] = str(guest_id)

            #Order ID, Member ID, Room ID, Check IN date, Check OUT date, Total Price, Total Days Booked, Actual payed
            order_list = ['',str(guest_id),str(room_id),'-'.join(check_in),"-",str(Total_Price),days_booked,'-']

            # Assign Order ID
            if len(order_Listz) < 1:
                order_list[0] = "0"
            else:
                order_list[0] = str(int(order_Listz[len(order_Listz) - 1][0]) + 1)

            from_array_to_txt_file_conversion(room_list,'room.txt',"w")
            from_array_to_txt_file_conversion(order_list,'order_Report.txt',"a+")
            print(f"\033[32mSuccessfully Check In a Guest \033[00m")
            receptionist_manage_booking()

        case '2':
            order_lists = decode_txt_File_to_list_of_data("order_Report.txt")
            print(" ") #spacing reasons
            print("\033[34mManaging Rooms\033[0m")
            print("\033[34mThese are the current unfinished orders\033[0m")
            #Printing in a nice table format
            header = ["Order ID","Member ID", "Room ID", "Check IN date", "Check OUT date", "Total Price", "Total Days Booked", "Actual payed"]
            print("Index".ljust(10),end="")
            for col in header:
                print(col.ljust(20),end="")
            print()

            for i, row in enumerate(order_lists,start=1):
                if row[4] == '-':
                    print(str(i).ljust(10),end='')
                    for col in row :
                        print(str(col).ljust(20),end="")
                    print()

            print()

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
                check_out = input_date("Check OUT Date (Format: 00-00-0000) (type: back to go back to menu): ") 
                if check_out == 'back':
                    receptionist_manage_booking()
                    return
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

            

            order_Listz[order_id_check.index(order_id)][4] = check_out
            order_Listz[order_id_check.index(order_id)][-1] = actually_payed

            order_idx = order_id_check.index(order_id)
            room_id_of_order = order_Listz[order_idx][2]

            if room_id_of_order in room_id_check:
                room_idx = room_id_check.index(room_id_of_order)
                room_list[room_idx][2] = "-"      # reset price/placeholder
                room_list[room_idx][3] = "False"  # mark as not occupied / cleaned
            else:
                print("\033[31mWarning: Room ID referenced by order not found in room list.\033[0m")

            from_array_to_txt_file_conversion(order_Listz,'order_Report.txt','w')
            from_array_to_txt_file_conversion(room_list,'room.txt','w')
            print(f"\033[32mSuccessfully Check Out a Guest \033[00m")
            receptionist_manage_booking()
    pass

def receptionist_view_room_availability():
    pass

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

    option_dict[option_picked]() #calling the function 

def accountant_record_guest_payments():
    pass

def accountant_generate_income_and_outstanding_payment_reports():
    pass

def accountant_generate_monthly_financial_summary():
    pass


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