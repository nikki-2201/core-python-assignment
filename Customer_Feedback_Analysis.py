def positive_feedback_percentage(ratings):
    """Calculate the percentage of positive feedback (ratings 4 or 5)."""
    if not ratings:
        return 0 
    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100

def main():
    try:
        n = int(input("Enter the number of ratings: "))
        if n <= 0:
            print("Please enter a valid number of ratings greater than 0.")
            return

        ratings_input = input(f"Enter {n} ratings (separate with commas): ").strip()

        ratings = [int(rating) for rating in ratings_input.split(",")]

        if any(rating < 1 or rating > 5 for rating in ratings):
            print("Invalid ratings! Ratings must be between 1 and 5.")
            return
        
        positive_percentage = positive_feedback_percentage(ratings)

        print(f"Positive Feedback: {positive_percentage:.2f}%")

    except ValueError:
        print("Invalid input! Please enter valid integer values.")

if __name__ == "__main__":
    main()
