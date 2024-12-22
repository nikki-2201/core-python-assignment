def available_seats(total_seats, booked_seats):
    avail = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return avail

def reserve_seat(total_seats, booked_seats, book_seat):
    if book_seat < 1 or book_seat > total_seats:
        return "Invalid seat number"
    if book_seat in booked_seats:
        return f"Seat {book_seat} is already reserved"
    booked_seats.append(book_seat)
    return f"Seat {book_seat} reserved successfully"

def cancel_seat(booked_seats, cancel_seat_num):
    if cancel_seat_num not in booked_seats:
        return f"Seat {cancel_seat_num} is not reserved"
    booked_seats.remove(cancel_seat_num)
    return f"Seat {cancel_seat_num} canceled successfully"

def main():
    try:
        total_seats = int(input("Enter total number of seats: "))
        if total_seats <= 0:
            print("Please enter a positive number for total seats.")
            return
        
        booked_seats = list(map(int, input("Enter booked seats, separated by commas: ").split(",")))
        
        booked_seats = [seat for seat in booked_seats if 1 <= seat <= total_seats]
        
        book_seat = int(input("Enter seat number to reserve: "))
        print(reserve_seat(total_seats, booked_seats, book_seat))
        
        cancel_seat_num = int(input("Enter seat number to cancel: "))
        print(cancel_seat(booked_seats, cancel_seat_num))
        
        available = available_seats(total_seats, booked_seats)
        print("Available seats:", available)
        print(f"Total booked seats: {len(booked_seats)}")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers for seats.")

if __name__ == "__main__":
    main()
