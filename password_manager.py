import json
import string

language_var = 'en'

# variable that indicates the language, default language = English
# En = English
# Sp = Spanish
language = ('Spanish' if language_var == 'sp' else 'English')


text = json.load(open('Languages/'+language+'.json', 'r'))
# Text in different languages

# English = {'keyword_in1' : 'Site: ',
# 'user' : 'Username: ',
# 'password' : 'Password: ',
# 'corrUser': 'The user {} was creat correctly!',
# 'wrongUser': 'The user {} was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
# 'wrongpass': 'The password was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
# 'passAgain': 'Write a correct password: ',
# 'keyAgain': 'Write a correct site name: ',
# 'userAgain': 'Write a correct username: ',
# 'shortPass': 'The password is too short and weakness, try with minimum 6 characters',}

Spanish = {'keyword_in1' : 'Sitio : ',
'user' : 'Nombre de usuario: ',
'password' : 'Contraseña: ',
'corrUser': 'El usuario {} fue creado correctamente!',
'wrongUser': 'El usuario {} no se creó correctamente, verifique que contenga solo letras mayusculas o minusculas (a-z o A-Z), numeros (0-9) ó los siguientes simbolos ({}), sin espacios',
'wrongpass': 'La contraseña no se creó correctamente, verifique que contenga solo letras mayusculas o minusculas (a-z o A-Z), numeros (0-9) ó los siguientes simbolos ({}), sin espacios',
'passAgain': 'Escriba una contraseña correcta: ',
'keyAgain': 'Escriba el nombre del sitio de forma correcta: ',
'userAgain': 'Escriba el nombre de usuario del sitio de forma correcta: ',
'shortPass': 'La contraseña es muy corta y debil, intente con una longitud minima de 6 caracteres',
}

# Permited characters
perm_chars = list(string.ascii_letters+ string.digits+ 'ñÑ'+ string.punctuation)

# __________________________________________________________________________________________________

def verificate_password(password):
# err_status identify the error, 0= no error, 1= too short, 2= invalid characters
    err_status = 0
    if len(password) > 5:

        for letter in password:
                if letter in perm_chars: pass
                else:
                    print (text['wrongpass'].format(string.punctuation))
                    _, New_password = input_var(0,0,1,'','','passAgain')

    else:
        err_status = 1
        print(text['shortPass'])

# __________________________________________________________________________________________________
def input_var(keyword, user,password ,key_text, user_text,pas_text):
    """
    Request the keyword(Site or service) and password to the user

    Arguments:
    keyword: Boolean, the keyword input is required(1) or not(0)
    user: Boolean, the user input is required(1) or not(0)
    password: Boolean, the password input is required(1) or not(0)
    key_text: The output text shown to the user for type the keyword
    user_text: The output text shown to the user for type the user of the site
    pas_text: The output text shown to the user for type the password

    Output:
    New_keyword: The name of a Site or service wich password wants to generate or save (capitalized)
    New_user: The username of the site
    New_password: the new password entered by the user
    """
    if keyword == 1:
        New_keyword = input(text[key_text]).capitalize()

        for letter in New_keyword:
            if letter in perm_chars: pass
            else:
                print (text['wrongUser'].format(New_keyword, string.punctuation))
                New_keyword, _ = input_var(1,0,0,'keyAgain','','')
    else: New_keyword = ''

    if user ==1:
        New_user = input(text[user_text])
        if letter in perm_chars: pass
        else:
            print (text['wrongUser'].format(New_keyword, string.punctuation))
            New_keyword, _ = input_var(0,1,0, '','userAgain','')

    if password == 1:
        New_password = input(text[pas_text])


    else: New_password = ''

    return New_keyword, New_user, New_password
# __________________________________________________________________________________________________
def sign_up():
    # Creates a new user
    New_User = input('user')
    Password = input('password')

    if New_User.isidentifier():
        print('')
# __________________________________________________________________________________________________

# __________________________________________________________________________________________________
if __name__ == '__main__':
    key, user, passw = input_var(1,1,1,'keyword_in1','user','password')
    print ('Site: {}\nUser: {} \nPassword: {}'.format(key, user, passw))


