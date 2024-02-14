# Print the program title
print("Calculate the hotel bill.")

# Define constants
STD_RM_RATE_1 = 155
STD_RM_RATE_2 = 160
STD_RM_RATE_3 = 165

DEL_RM_RATE_1 = 195
DLX_RM_RATE_2 = 210
DLX_RM_RATE_4 = 225

ROOM_TAX = 0.12

BREAKFAST = 15
PARKING = 25

DISCOUNT_5_NIGHTS = 0.9

# Get user inputs
room_type = input("Enter room type (Standard or Deluxe): ").lower()
num_nights = int(input("Enter number of nights: "))
num_people = int(input("Enter number of people: "))
breakfast = input("Would you like breakfast? (y/n)").lower()
parking = input("Do you need parking? (y/n)").lower()

# Figure out the room rate
if room_type == "standard":
    if num_people == 1:
        room_rate = STD_RM_RATE_1
    elif num_people == 2:
        room_rate = STD_RM_RATE_2
    else:
        room_rate = STD_RM_RATE_3
else:
    if num_people <= 2:
        room_rate = DEL_RM_RATE_1
    elif num_people == 3:
        room_rate = DLX_RM_RATE_2
    else:
        room_rate = DLX_RM_RATE_4

# Calculate the room charges
if room_rate is not None:
    room_charges = room_rate * num_nights
    if num_nights > 5:
        room_charges *= DISCOUNT_5_NIGHTS
    
    # Calculate the breakfast charge
    if breakfast == 'y':
        breakfast_charge = BREAKFAST * num_people * num_nights
    else:
        breakfast_charge = 0

    # Calculate the parking charge
    if parking == 'y':
        parking_charge = PARKING * num_nights
    else:
        parking_charge = 0
    # Calculate subtotal before tax
    subtotal = room_charges + breakfast_charge + parking_charge
    # Calculate tax
    tax = subtotal * ROOM_TAX

    # Calculate total charges
    total_charges = subtotal + tax

    # Generate the bill
    print("\n------------")
    print(f"Room Charges ({room_type} room, {num_people} people, {num_nights} nights): ${room_charges}")

    print(f"Breakfast Charges ({num_people} people, {num_nights} nights): ${breakfast_charge}")

    print(f"Parking Charges ({num_nights} nights): ${parking_charge}")

    print(f"Subtotal (before tax): ${subtotal}")
    print(f"Tax (12%): ${tax}")
    print("------------------------")
    print(f"Total Amount is: ${total_charges}")
else:
    print("Invalid room type or number of people.")
