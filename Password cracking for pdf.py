

#with open('C:/Users/User/OneDrive/Desktop/__pycache__/textfile for cracking.txt','w') as file:
#    for x in range(1000,10000):
#        file.write(f'{x}\n')
#    else:
#        print('Done!')    
import pikepdf

passwords_filename = 'C:/Users/User/OneDrive/Desktop/Game1/word2.txt'

locked_pdf_file = "C:/Users/User/Downloads/A strategic plan AFCF-protected.pdf"

# load passwords file
with open(passwords_filename) as file:

    passwords_list = file.readlines()
    total_passwords = len(passwords_list)

    for index,password in enumerate(passwords_list):
        #try if passworc  is correct
        try:
            with pikepdf.open(locked_pdf_file, password = password.strip()) as pdf_file:
            # Strip means return me the password alone.    
                print('\n+++++++++success+++++++++')
                print('success--------File is Unblocked and the password is: ', password)
                break
        #if password fail
        except:
            print('\n===========')
            print(f'Trying Password {password} --- Fail!!!')
            scanning = (index/total_passwords)*100
            print('Scanning passwords complete:', round(scanning,2))
            continue    
 













































