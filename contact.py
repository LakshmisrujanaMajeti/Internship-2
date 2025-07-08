contacts={}
while True:
    print("\n1.ADD CONTACT ")
    print("\n2.VIEW ALL")
    print("\n3.SEARCH")
    print("\n4.DELETE")
    print("\n6.EXIT")
    choice=input("Enter Choice").strip()
    if choice=='1':
        name=input("Name :")
        phone=input("Phone : ")
        contacts[name]=phone
        print("Contact Saved!")
    elif choice=='2':
        for name,phone in contacts.items():
            print(f"{name}:{phone}")
    elif choice=='3':
        name=input("Enter the Name:")
        if name in contacts:
            print(f"{name}'s phone:{contacts[name]}")
        else:
            print("contact is not found")
    elif choice=='4':
        name=input("Enter the Name to delete:")
        if name in contacts:
            del contacts[name]
            print("Deleted successfully")
        else:
            print("no such contact.")
    elif choice == '6':  # Fixed this line
        print("Exiting contact manager.")
        break

    else:
        print("Invalid Contact")

class Solution:
    def addTwoNumbers(self, l1:[ListNode], l2:  [ListNode]) -> Optional[l1]:
        l1: Optional[ListNode]
        l2: Optional[ListNode]
        l1.reverse()
        l2.reverse()
        add=l1+l2
        reversed_nums = add[::-1]
        print(reversed_nums)


