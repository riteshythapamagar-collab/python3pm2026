# # data=['ram','sita','hari']
# # # data.insert(0,'shyam')
# # # data.pop()
# # # data.remove('sita')
# # # # data.sort()
# # # # data.sort(reverse=True)
# # # # data.append('laxman')
# # # # data.extend('ritesh')
# # print(data)

# # data=[
# #     {
# #         'name':'shopia',
# #         'country':[
# #             {
# #                 'name': 'nepal',
# #             }
# #         ]
# #     }
# # ]
# # print(data[0]['name'],data[0]['country'][0]['name'])

# # data=[
# #     'name':'ram',
# #     'age':20,
# #     'course':'python'
# # ]
# # # print(data.get('names','keys not found'))
# # # print('we are learning python')
# # data.clear()
# # print(data)

# ## ATM Machine Program 

# balance = 5000
# pin = "1234"

# entered_pin = input("Enter ATM PIN: ")

# if entered_pin == pin:

#     print("\n===== ATM MENU =====")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     # Check Balance
#     if choice == "1":
#         print("Your balance is:", balance)

#     # Deposit Money
#     elif choice == "2":
#         deposit = float(input("Enter amount to deposit: "))
#         balance = balance + deposit
#         print("Deposit successful.")
#         print("New balance is:", balance)

#     # Withdraw Money
#     elif choice == "3":
#         withdraw = float(input("Enter amount to withdraw: "))

#         if withdraw <= balance:
#             balance = balance - withdraw
#             print("Please collect your cash.")
#             print("Remaining balance is:", balance)
#         else:
#             print("Insufficient balance!")

#     # Exit
#     elif choice == "4":
#         print("Thank you for using ATM.")

#     else:
#         print("Invalid choice!")

# else:
#     print("Incorrect PIN!")