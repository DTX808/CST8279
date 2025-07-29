

import sqlite3

def delete_grade(lastName,firstName,province):
    try:
        conn = sqlite3.connect('lab11.db')
        cursor = conn.cursor()
        cursor.execute('''
                DELETE FROM Grades 
                WHERE lname = ? AND fname = ? AND Province = ?
            ''', (lastName, firstName, province))
        rows_deleted = cursor.rowcount
        conn.commit()
        conn.close()
        if rows_deleted > 0:
            print(f"Successfully deleted {rows_deleted} record(s) for {firstName} {lastName} from {province}")
            return True
        else:
            print(f"No record found for {firstName} {lastName} from {province}")
            return False
                
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    
def displayGrade(lastName, firstName, province):
    
    try:
        # Connect to the database
        conn = sqlite3.connect('lab11.db')
        cursor = conn.cursor()
        
        # Query using LIKE function for partial matching
        cursor.execute('''
            SELECT lname, fname, Province, Grade 
            FROM Grades 
            WHERE lname LIKE ? AND fname LIKE ? AND Province LIKE ?
        ''', (f'%{lastName}%', f'%{firstName}%', f'%{province}%'))
        
        results = cursor.fetchall()
        conn.close()
        
        if results:
            print(f"\nFound {len(results)} matching record(s):")
            print("-" * 70)
            print(f"{'Last Name':<15} {'First Name':<15} {'Province':<20} {'Grade':<10}")
            print("-" * 70)
            
            grades_list = []
            for row in results:
                print(f"{row[0]:<15} {row[1]:<15} {row[2]:<20} {row[3]:<10}")
                grades_list.append(row[3])  # Add grade to the list
            print("-" * 70)
            
            return grades_list
        else:
            print(f"No records found matching: {firstName} {lastName} from {province}")
            return []
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_user_input():
    """Get user input for student information"""
    print("\nEnter student information:")
    print("(You can use % as wildcard for partial matches in display mode)")
    
    lastName = input("Last name: ").strip()
    firstName = input("First name: ").strip()
    province = input("Province: ").strip()
    
    return lastName, firstName, province

def main():
    """Main program loop"""
    print("=" * 50)
    print("    STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)
    
    while True:
        print("\nPlease select an option:")
        print("1. Display a grade")
        print("2. Delete a grade")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n--- DISPLAY GRADE ---")
            lastName, firstName, province = get_user_input()
            grades = displayGrade(lastName, firstName, province)
            
        elif choice == '2':
            print("\n--- DELETE GRADE ---")
            lastName, firstName, province = get_user_input()
            
            # Confirm deletion
            confirm = input(f"\nAre you sure you want to delete the record for {firstName} {lastName} from {province}? (y/n): ")
            if confirm.lower() == 'y':
                deleteGrade(lastName, firstName, province)
            else:
                print("Deletion cancelled.")
                
        elif choice == '3':
            print("\nThank you for using the Student Grade Management System!")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
