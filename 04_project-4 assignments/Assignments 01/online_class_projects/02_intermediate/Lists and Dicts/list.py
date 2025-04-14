def list_practice():
    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of the list:", len(fruit_list))
    
    # Add 'mango' to the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range!"

def slice_list(lst, start, end):
    return lst[start:end]

def index_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']
    
    while True:
        print("\nOptions:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Element at index", index, ":", access_element(my_list, index))
        
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        
        elif choice == '4':
            print("Exiting game...")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

def main():
    print("--- List Practice ---")
    list_practice()
    print("\n--- Index Game ---")
    index_game()

if __name__ == "__main__":
    main()
