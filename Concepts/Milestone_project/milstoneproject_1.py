#creating a function and desplay the result to the users

'''def my_list(list):
    print(list)
list = [1,2,3,4]
my_list(list)
'''

# validation the input based on function .isdigit()
'''
def verify():
    get_input = "me"
    
    while not get_input.isdigit(): 
        get_input = input("Enter the Number: ")

        if get_input.isdigit() == False:
            print("wrong input!!")
    
    print(int(get_input)) 

verify()
'''
#checking with multiple input
'''
def verify():
    choice = ""
    while choice not in ['1','2','3']:
        choice = input("Enter the Number: ")

        if choice not in ['1','2','3']:
            print("sorry")
    return int(choice)
verify()
'''

#game code
def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)