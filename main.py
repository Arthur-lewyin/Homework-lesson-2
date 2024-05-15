name = input("create username-")
passwords = input("create password-")
print('thanks for creating account')

users = {
    'user_1' : {
        'name' : 'me',
        'password' : 'yea'
    },
    'user_2': {
        'name': name,
        'password' : passwords
    }
}

print('verify account')

test1 = input("username-")
test2 = input('password-')

if (test1==name) and (test2==passwords) :
    print("Logged in")
    print(users['user_2'])

else:
    print('ERROR, try again')

