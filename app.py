import pandas as pd

def main():
    # Initialize DataFrame for member data
    member_data = pd.DataFrame(columns=['Name', 'Age', 'Membership', 'Cost'])

    membership_types = {
        1: ("daily", 100),
        2: ("monthly", 1000),
        3: ("3 months", 3000),
        4: ("6 months", 6000),
        5: ("yearly", 9000)
    }

    while True:
        print("1. Add member")
        print("2. Remove member")
        print("3. Display members")
        print("4. Display number of members")
        print("5. Display average age of members")
        print("6. Display membership type distribution")
        print("7. Display total revenue")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter member name: ")
            age = int(input("Enter member age: "))

            print("Enter 1 for daily")
            print("Enter 2 for monthly subscription")
            print("Enter 3 for 3 months subscription")
            print("Enter 4 for 6 months subscription")
            print("Enter 5 for yearly subscription")
            membership_choice = int(input("Enter your choice: "))

            if membership_choice in membership_types:
                membership_type, total_cost = membership_types[membership_choice]
                print(f"\nThe total cost is: {total_cost}\n")
                member_data = member_data.append({'Name': name, 'Age': age, 'Membership': membership_type, 'Cost': total_cost}, ignore_index=True)
            else:
                print("Invalid choice. Please try again.")

        elif choice == 2:
            name_to_remove = input("Enter name of the member to be removed: ")
            member_data = member_data[member_data['Name'] != name_to_remove]
            print("Member has been removed\n")

        elif choice == 3:
            if not member_data.empty:
                print("Members:")
                print(member_data)
            else:
                print("No members to display.")
            print()

        elif choice == 4:
            print(f"Number of members: {len(member_data)}\n")

        elif choice == 5:
            if not member_data.empty:
                average_age = member_data['Age'].mean()
                print(f"Average age of members: {average_age:.2f}\n")
            else:
                print("No members to display.\n")

        elif choice == 6:
            if not member_data.empty:
                membership_distribution = member_data['Membership'].value_counts()
                print("Membership type distribution:")
                print(membership_distribution)
                print()
            else:
                print("No members to display.\n")

        elif choice == 7:
            if not member_data.empty:
                total_revenue = member_data['Cost'].sum()
                print(f"Total revenue: {total_revenue}\n")
            else:
                print("No members to display.\n")

        elif choice == 8:
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
