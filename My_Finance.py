# HelaDevs-Sweden Python Class Practice Project 2023.03.27 At 02.06PM
# Open Learning Platform - UoM Moratuwa University
# -------------------------------------------------------------------------------------------------------------------
# This Program About To Manage Your Personal Finance Plans

import os
import datetime

# Payment List (Database)
# This List Will Stores The All The Payments You Enters To The Program
payment_list = []

# Income List (Database)
# This List Will Stores The All The Income You Recieve
income_list = []

# Future Payment Reminder List
# This List Will Stores The All The Payment Reminders You Enters
reminder_list = []

# There is a Encryption System I Developed for this program. Because It is very important to protect
# someone's financial information. So I developed a algorithem here to change actual int (numbers)
# to special charactores. I discribed how it happens before start all of my encrypt statements. 
# for a example if you input 0 as a number program will converts the "0" to ";"   
# =========================================================================================================================
# D A T A   E N C R Y P T I O N   S Y S T E M   -   B Y   J U D E   D I L A N K A
# =========================================================================================================================


# Single Encryption - This Will Encrypt Only Numbers To A Special Chracters
# ----------ENCRYPTION METHOD--------------
#   0	1	2	3	4	5	6	7	8	9   .    [RAW Date]
#   ;	#	!	^	*	~	?	[	>	/   <    [Single Encripted Data]
#-------------------------------------------------------------------------------------

def single_encrypt(encrypt_data):

    single_encryption = ''
    # First Conversation. When calles the statement it will return with the result
    for i, c in enumerate(encrypt_data):
        if(c == '0'):
            c = ';'
        if(c == '1'):
            c = '#'
        if(c == '2'):
            c = '!'
        if(c == '3'):
            c = '^'
        if(c == '4'):
            c = '*'
        if(c == '5'):
            c = '~'
        if(c == '6'):
            c = '?'
        if(c == '7'):
            c = '['
        if(c == '8'):
            c = '>'
        if(c == '9'):
            c = '/'
        if(c == '.'):
            c = '<'
        single_encryption += str(c)
    return (single_encryption)

# Double conversation checks if the same number repeats several times. For example
# if you input "00" it will converts to ";;" with the single conversation above,
# from double encryption checks if ";;" exist that means "00" and if finds them,
# it will convert to "e"
# -------------------DOUBLE ENCRYPTION----------------------------------------------------------
#===============================================================================================

# ----------ENCRYPTION METHOD--------------
#   ;;  ##  !!  ^^  **  ~~  ??  [[  >>  //    [RAW Data recives from single encryption]
#    e   n   w   h   o   i   x   v   g   q    [Double Encripted Data]
#-------------------------------------------------------------------------------------

def sigle_double_encryption(encrypt_data):
    # check repeated value
    # If repeated values find, Convert them to followings and return them when calls the statment
    is_double = False

    previous_value = ''
    dual_encryption = ''

    for i, c in enumerate(encrypt_data):
        this_value = str(c)
        if(this_value != previous_value and is_double == False):
            is_double = True

        if(c == ';' and previous_value == ';' and is_double == True):
            c = 'e'   
        if(c == '#' and previous_value == '#'and is_double == True):
            c = 'n'   
        if(c == '!' and previous_value == '!'and is_double == True):
            c = 'w'  
        if(c == '^' and previous_value == '^'and is_double == True):
            c = 'h'   
        if(c == '*' and previous_value == '*'and is_double == True):
            c = 'o'    
        if(c == '~' and previous_value == '~'and is_double == True):
            c = 'i'   
        if(c == '?' and previous_value == '?'and is_double == True):
            c = 'x'     
        if(c == '[' and previous_value == '['and is_double == True):
            c = 'v'   
        if(c == '>' and previous_value == '>'and is_double == True):
            c = 'g'   
        if(c == '/' and previous_value == '/'and is_double == True):
            c = 'q'

        if(previous_value == this_value):
            previous_value = str()
            dual_encryption = dual_encryption.rstrip(dual_encryption[-1])
            dual_encryption = (dual_encryption + c)
            is_double = False
        else:
            dual_encryption += str(c)    
            previous_value = this_value
            this_value = str()

    return (dual_encryption)

# If this finds "ee" (that means - 0000) this will converts them to followings
#-------------------------------------------------------------------------------------
#   ee 	nn	ww	hh	oo	ii	xx	vv	gg	qq  [RAW Data Comes with double encryption]
#    K	M	A	L	R	S	W	E	Y	B   [Triple Encripted Data]
#-------------------------------------------------------------------------------------

def triple_encrypt(encrypt_data):

    is_double = False

    previous_value_triple = ''
    triple_encryption = ''
    this_value = str()

    for j, cd in enumerate(str(encrypt_data)):
        this_value = str()
        if(cd != '\x08'):
            this_value = str(cd)
        if(this_value == previous_value_triple and is_double == False):
            is_double = True

        if(cd == 'e' and previous_value_triple == 'e' and is_double == True):
            cd = 'K'   
        if(cd == 'n' and previous_value_triple == 'n'and is_double == True):
            cd = 'M'   
        if(cd == 'w' and previous_value_triple == 'w'and is_double == True):
            cd = 'A'  
        if(cd == 'h' and previous_value_triple == 'h'and is_double == True):
            cd = 'L'   
        if(cd == 'o' and previous_value_triple == 'o'and is_double == True):
            cd = 'R'    
        if(cd == 'i' and previous_value_triple == 'i'and is_double == True):
            cd = 'S'   
        if(cd == 'x' and previous_value_triple == 'x'and is_double == True):
            cd = 'W'     
        if(cd == 'v' and previous_value_triple == 'v'and is_double == True):
            cd = 'E'   
        if(cd == 'g' and previous_value_triple == 'g'and is_double == True):
            cd = 'Y'   
        if(cd == 'q' and previous_value_triple == 'q'and is_double == True):
            cd = 'B'

        if(previous_value_triple == this_value):
            previous_value_triple = str()
            #triple_encryption = (triple_encryption + '\b' + cd)
            triple_encryption = triple_encryption.rstrip(triple_encryption[-1])
            triple_encryption = (triple_encryption + cd)
            is_double = False
        else:
            triple_encryption += str(cd)    
            previous_value_triple = this_value
            this_value = str()

    return (triple_encryption)

# If this finds "KK" (that means - 00000000) this will converts them to followings
#-------------------------------------------------------------------------------------
#   KK	MM	AA	LL	RR	SS	WW	EE	YY	BB   [RAW Data]
#   )	(	|	-	_	%	$	+	@	\    [Triple Encripted Data]
#-------------------------------------------------------------------------------------

def triple_plus_encrypt(encrypt_data):

    is_double = False

    previous_value_triple_plus = ''
    triple_plus_encryption = ''
    this_value = str()

    for j, cd in enumerate(str(encrypt_data)):
        this_value = str()
        if(cd != '\x08'):
            this_value = str(cd)
        if(this_value == previous_value_triple_plus and is_double == False):
            is_double = True

        if(cd == 'K' and previous_value_triple_plus == 'K' and is_double == True):
            cd = ')'   
        if(cd == 'M' and previous_value_triple_plus == 'M'and is_double == True):
            cd = '('   
        if(cd == 'A' and previous_value_triple_plus == 'A'and is_double == True):
            cd = '|'  
        if(cd == 'L' and previous_value_triple_plus == 'L'and is_double == True):
            cd = '-'   
        if(cd == 'R' and previous_value_triple_plus == 'R'and is_double == True):
            cd = '_'    
        if(cd == 'S' and previous_value_triple_plus == 'S'and is_double == True):
            cd = '%'   
        if(cd == 'W' and previous_value_triple_plus == 'W'and is_double == True):
            cd = '$'     
        if(cd == 'E' and previous_value_triple_plus == 'E'and is_double == True):
            cd = '+'   
        if(cd == 'Y' and previous_value_triple_plus == 'Y'and is_double == True):
            cd = '@'   
        if(cd == 'B' and previous_value_triple_plus == 'B'and is_double == True):
            cd = '\\'

        if(previous_value_triple_plus == this_value):
            previous_value_triple_plus = str()
            #triple_encryption = (triple_encryption + '\b' + cd)
            triple_plus_encryption = triple_plus_encryption.rstrip(triple_plus_encryption[-1])
            triple_plus_encryption = (triple_plus_encryption + cd)
            is_double = False
        else:
            triple_plus_encryption += str(cd)    
            previous_value_triple_plus = this_value
            this_value = str()

    return (triple_plus_encryption)

# When Needed To Encrypt Some Numbers, Simply Calles This Function, And All The Encryption Methods Will Calles Here
def encrypt_data(raw_data):
    # Start Primary Encryption
    x = single_encrypt(raw_data)

    # Start Secondary Encryption
    y = sigle_double_encryption(x)
            
    # Start Triple Duplication Encryption Protection Here
    z = triple_encrypt(y)

    # Start Triple Plus Duplication Encryption Protection Here
    a = triple_plus_encrypt(z)
    return a
# It is very important to Decrypt, Encrypted datas. Otherwise human cannot read them without study and knowing the
# proper meaning of them. So I developed a algorythem to revise my process back to normal. Then human can read 
# them without any truoble
# =========================================================================================================================
# D A T A   E N C R Y P T I O N   S Y S T E M   -   B Y   J U D E   D I L A N K A
# =========================================================================================================================
# ENDS HERE
# encrypt_data(Pass The Data You Want To Encrypt)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# START FROM HERE
# =========================================================================================================================
# D A T A   D E C R Y P T I O N   S Y S T E M   -   B Y   J U D E   D I L A N K A
# =========================================================================================================================

# ----------ENCRYPTION METHOD--------------
#   0	1	2	3	4	5	6	7	8	9   .    [RAW Date]
#   ;	#	!	^	*	~	?	[	>	/   <    [Single Encripted Data]
#-------------------------------------------------------------------------------------

def single_decrypt(decrypt_data):

    single_decryption = ''

    for i, c in enumerate(decrypt_data):
        if(c == ';'):
            c = '0'
        if(c == '#'):
            c = '1'
        if(c == '!'):
            c = '2'
        if(c == '^'):
            c = '3'
        if(c == '*'):
            c = '4'
        if(c == '~'):
            c = '5'
        if(c == '?'):
            c = '6'
        if(c == '['):
            c = '7'
        if(c == '>'):
            c = '8'
        if(c == '/'):
            c = '9'
        if(c == '<'):
            c = '.'
        single_decryption += str(c)
    return (single_decryption)


# -------------------DOUBLE ENCRYPTION----------------------------------------------------------
#===============================================================================================

# ----------ENCRYPTION METHOD--------------
#   ;;  ##  !!  ^^  **  ~~  ??  [[  >>  //    [RAW Date]
#    e   n   w   h   o   i   x   v   g   q    [Double Encripted Data]
#-------------------------------------------------------------------------------------

def sigle_double_decryption(decrypt_data):

    is_double = False

    previous_value = ''
    dual_decryption = ''

    for i, c in enumerate(decrypt_data):
        this_value = str(c)
        if(this_value != previous_value and is_double == False):
            is_double = True

        if(c == 'e'):
            c = ';;'   
        if(c == 'n'):
            c = '##'   
        if(c == 'w'):
            c = '!!'  
        if(c == 'h'):
            c = '^^'   
        if(c == 'o'):
            c = '**'    
        if(c == 'i'):
            c = '~~'   
        if(c == 'x'):
            c = '??'     
        if(c == 'v'):
            c = '[['   
        if(c == 'g'):
            c = '>>'   
        if(c == 'q'):
            c = '//'

        if(previous_value == this_value):
            previous_value = str()
            #dual_decryption = dual_decryption.rstrip(dual_decryption[-1])
            dual_decryption = (dual_decryption + c)
            is_double = False
        else:
            dual_decryption += str(c)    
            previous_value = this_value
            this_value = str()

    return (dual_decryption)

#-------------------------------------------------------------------------------------
#   ee 	nn	ww	hh	oo	ii	xx	vv	gg	qq  [RAW Data]
#    K	M	A	L	R	S	W	E	Y	B   [Triple Encripted Data]
#-------------------------------------------------------------------------------------

def triple_decrypt(decrypt_data):

    is_double = False

    previous_value_triple = ''
    triple_decryption = ''
    this_value = str()

    for j, cd in enumerate(str(decrypt_data)):
        this_value = str()
        if(cd != '\x08'):
            this_value = str(cd)
        if(this_value == previous_value_triple and is_double == False):
            is_double = True

        if(cd == 'K'):
            cd = 'ee'   
        if(cd == 'M'):
            cd = 'nn'   
        if(cd == 'A'):
            cd = 'ww'  
        if(cd == 'L'):
            cd = 'hh'   
        if(cd == 'R'):
            cd = 'oo'    
        if(cd == 'S'):
            cd = 'ii'   
        if(cd == 'W'):
            cd = 'xx'     
        if(cd == 'E'):
            cd = 'vv'   
        if(cd == 'Y'):
            cd = 'gg'   
        if(cd == 'B'):
            cd = 'qq'

        if(previous_value_triple == this_value):
            previous_value_triple = str()
            #triple_encryption = (triple_encryption + '\b' + cd)
            #triple_decryption = triple_decryption.rstrip(triple_decryption[-1])
            triple_decryption = (triple_decryption + cd)
            is_double = False
        else:
            triple_decryption += str(cd)    
            previous_value_triple = this_value
            this_value = str()

    return (triple_decryption)

#-------------------------------------------------------------------------------------
#   KK	MM	AA	LL	RR	SS	WW	EE	YY	BB   [RAW Data]
#   )	(	|	-	_	%	$	+	@	\    [Triple Encripted Data]
#-------------------------------------------------------------------------------------

def triple_plus_decrypt(decrypt_data):

    is_double = False

    previous_value_triple_plus = ''
    triple_plus_decryption = ''
    this_value = str()

    for j, cd in enumerate(str(decrypt_data)):
        this_value = str()
        if(cd != '\x08'):
            this_value = str(cd)
        if(this_value == previous_value_triple_plus and is_double == False):
            is_double = True

        if(cd == ')'):
            cd = 'KK'   
        if(cd == '('):
            cd = 'MM'   
        if(cd == '|'):
            cd = 'AA'  
        if(cd == '-'):
            cd = 'LL'   
        if(cd == '_'):
            cd = 'RR'    
        if(cd == '%'):
            cd = 'SS'   
        if(cd == '$'):
            cd = 'WW'     
        if(cd == '+'):
            cd = 'EE'   
        if(cd == '@'):
            cd = 'YY'   
        if(cd == '\\'):
            cd = 'BB'

        if(previous_value_triple_plus == this_value):
            previous_value_triple_plus = str()
            #triple_encryption = (triple_encryption + '\b' + cd)
            #triple_plus_decryption = triple_plus_decryption.rstrip(triple_plus_decryption[-1])
            triple_plus_decryption = (triple_plus_decryption + cd)
            is_double = False
        else:
            triple_plus_decryption += str(cd)    
            previous_value_triple_plus = this_value
            this_value = str()

    return (triple_plus_decryption)

def decryption():
    a = str()

    # Import Exported Encryption File To The System
    with open('Salary.jdl') as f:
            for line in f:
                a = (line.strip())

    f = triple_plus_decrypt(a)

    t = triple_decrypt(f)

    s = sigle_double_decryption(t)

    ss = single_decrypt(s)
    return ss

# =========================================================================================================================
# D A T A   D E C R Y P T I O N   S Y S T E M   -   B Y   J U D E   D I L A N K A
# =========================================================================================================================
# DATA DECRYPTION ENDS HERE

# Main Software Interface Logo - Header Design
# This Is The Main Interface Of My Software
def interface():
    print('                ')
    print('                         ℝ 𝕆 𝔹 𝕆   𝔹 𝔸 ℕ 𝕂   𝕊 𝕐 𝕊 𝕋 𝔼 𝕄 ') 
    print("                          Yᴏᴜʀ Tʀᴜsᴛᴇᴅ Fɪɴᴀɴᴄɪᴀʟ Aᴅᴠɪsᴇʀ  ")
    print('                        | ------------------------------- |')
    print('       =̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶')
    print('                       |𝓥𝓮𝓻𝓼𝓲𝓸𝓷 1.0 - 𝓐𝓵𝓵 𝓡𝓲𝓰𝓱𝓽 𝓡𝓮𝓼𝓮𝓻𝓿𝓮𝓭|')
    print('                          ---------------------------------    \n')

# This Is the Logo Of My Software
def software_logo():
    print(' █▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ▒█░▄▀ 　 ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▄▀█ ')
    print('▒█▄▄▀ ▒█░░▒█ ▒█▀▀▄ ▒█░░▒█ 　 ▒█▀▀▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▄░ 　 ░▀▀▀▄▄ ▒█▄▄▄█ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▒█▒█ ')
    print('▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ 　 ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ 　 ▒█▄▄▄█ ░░▒█░░ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░░▒█')
    print("           ᴰᵒⁿ'ᵗ ˢᵖᵉⁿᵈ ᵐᵒⁿᵉʸ ʳᵉᶜᵏˡᵉˢˢˡʸ⸴ ˢᵖᵉⁿᵈ ⁱᵗ ʷⁱᵗʰ ʷʰᵃᵗ ʸᵒᵘ ʰᵃᵛᵉ ˡᵉᶠᵗ ᵃᶠᵗᵉʳ ˢᵃᵛⁱⁿᵍ                 ​​​​")

# Main Menu Design
def main_menu():
# Program Dashboard
    os.system('cls')
    interface()
    software_logo()
    print('\n\n')
    print('     Your Total Amount is : ' + str(currency_type) + ' ' + str(net_salary) + '             Current Date : ' + str(date_time)+ '\n\n')
    print('                  -------------------------------------------')
    print('                  >>Add New Payment               - Press "A"')
    print('                  >>Add New Income                - Press "I"')
    print('                  >>Payment Reminders             - Press "P"')
    print('                  -------------------------------------------')
    print('                  >>Exit The Software             - Press "E"')
    print('                  -------------------------------------------')
    print('                  >>Software Instruction          - Press "R"')
    print('                  -------------------------------------------')
    print('\n\n')
    

# Payment Reminder Menu Design
def payment_reminder():
    software_logo()
    print('         --------- WELCOME TO ROBO BANK PAYMENT REMINDER SYSTEM ---------')
    print('         ================================================================')
    print('         Flexible, Fastest and Secure payment Reminder System For Personal')
    print('         Use. Create and Maintain Your Future Financial Plans With Our Secure')
    print('         Personal Financial Software')
    print('\n\n')
    print('                     To Create A Reminder      -         Press "C"')
    print('                     To View All Reminders     -         Press "V"')
    print('                     To Update A Reminder      -         Press "U" [Comming Soon]')
    print('                     To Delete A Reminder      -         Press "D" [Comming Soon]')
    print('\n\n')

# HelaDeves-Logo To Thank Them
def hela_dev_logo():
    print('██╗░░██╗███████╗██╗░░░░░░█████╗░  ██████╗░███████╗██╗░░░██╗░██████╗')
    print('██║░░██║██╔════╝██║░░░░░██╔══██╗  ██╔══██╗██╔════╝██║░░░██║██╔════╝')
    print('███████║█████╗░░██║░░░░░███████║  ██║░░██║█████╗░░╚██╗░██╔╝╚█████╗░')
    print('██╔══██║██╔══╝░░██║░░░░░██╔══██║  ██║░░██║██╔══╝░░░╚████╔╝░░╚═══██╗')
    print('██║░░██║███████╗███████╗██║░░██║  ██████╔╝███████╗░░╚██╔╝░░██████╔╝')
    print('╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░')

# Months Of the Year - It Needed To When Create Payment Plan
# When Payment Plan Creats, It Will Display The Next Payment Month.
# To Show the Next Payment Month, This Function Will Helps Them
def months(month):
    if(month == 1):
        dt = 'January'
    if(month == 2):
        dt = 'February'
    if(month == 3):
        dt = 'March'
    if(month == 4):
        dt = 'April'
    if(month == 5):
        dt = 'May'
    if(month == 6):
        dt = 'June'
    if(month == 7):
        dt = 'July'
    if(month == 8):
        dt = 'August'
    if(month == 9):
        dt = 'September'
    if(month == 10):
        dt = 'October'
    if(month == 11):
        dt = 'November'
    if(month == 12):
        dt = 'December'
    return dt

# Program Exit
# When User Press E 
def exit():
    os.system('cls')
    interface()
    print('GOOD BYE!')
    
# Clear Window
os.system('cls')

# LOADIN SCREEN ROBO BANK SYSTEM
# This Program Stores Your Salary Infromations In a File With My Encryption.
# Check If Files (Database) Exist Or Not
# This Will Check Whether You Are New To The Program Or Not
check_file = os.path.isfile('Salary.jdl')
salary_db = (check_file)
currency_code = str()

# You Are New To The Program
if(salary_db == False):
    # Salary Informations 
    my_salary = int(input('How much do you earn for a month ? '))
    print('\nCurrency Types\n--------------\nUS Dollers - Type "D"\nEuro - Type "E"\nRupees - Type "R"\n')
    currency_type = input('What is your Preferd Currency Type ? ')

    # Currency Informations
    # What Is The Users Currency Type, That means If You Are Sri Lankan And Doing Local Job Then You Will Recieve
    # Your Salary With Sri Lankan Rupees
    if(currency_type == 'D' or currency_type == 'd'):
        currency_type = "1" # One Represent Doller
    elif(currency_type == 'E' or currency_type == 'e'):
        currency_type = "2" # Two Represent Euro
    elif(currency_type == 'R' or currency_type == 'r'):
        currency_type = "3" # Three Represent Sri Lankan Rupees

    # Create Salary Database [Create Text Data & Rename It To JDL File Format Because I'm JDL - Jude Dialanka Lashan]
    try:
        my_salary = str(currency_type + str(my_salary))
        en_data = encrypt_data(str(my_salary))
        
        with open('Salary.jdl', 'w') as f:
            f.write(str(en_data))

        # Currency Code : This will Identify the salary you recieve with what currency type.
        # Currency type will help to store data safe with database. Because currency code can encrypt
        if(currency_type == '1'):
            currency_type = "$"
            currency_code = '1'  
        if(currency_type == '2'):
            currency_type = "Euro" 
            currency_code = '2' 
        if(currency_type == '3'):
            currency_type = "Rs" 
            currency_code = '3'

        my_salary = str(my_salary[1:]) 
             
    except:
        # If database File Create Fails
        # Salary Database Create Failed - Display Msg To The User
        print('=========WARNING!=========WARNING!=========WARNING!=========WARNING!=========')
        print('=============================================================================')
        print('    Database File Not Created! You Are In TRAIL Mode. Please Clean Your PC   ')
        print('=============================================================================')
        input('\n\n>>>>> Press Any Key To Continue :  ')
else:
    # If You Are Existing User
    # Getting Salary Information From The Database (.jdl File)
    # And Assign Currency Type From Currency Code That get from the file(.jdl)
    with open('Salary.jdl') as f:
        for line in f:
            salary = (decryption())
            if(salary[0] == '1'):
                currency_type = '$'
                currency_code = '1'
                my_salary = salary[1:]
            if(salary[0] == '2'):
                currency_type = 'Euro'
                currency_code = '2'
                my_salary = salary[1:]
            if(salary[0] == '3'):
                currency_type = 'Rs'
                currency_code = '3'
                my_salary = salary[1:]
           
# Append Data To Text Files-------------------------------------------------------------------
#with open("Salary.jdl","a") as file:
#    file.write("\nAnd more…")

# Clear The Screen
os.system('cls')

# Current Date & Time
date_time = datetime.datetime.now()

# Encrypt Currencycode and salary
en_data = encrypt_data(currency_code + str(my_salary))  

# Write Them To A File
# Here I Use "Salary.jdl" File As A Database
with open('Salary.jdl', 'w') as f:
    f.write(str(en_data))   

# Salary Information Converts To A String And Stores Them In A New Variable
net_salary = str(my_salary)
main_menu()

# Program Functioning & Navigation Instructions (Until Press E While Loop Continuasly Run)
user_option=True
while user_option:
    main_menu()

    user_option = input('                 𝑹𝑶𝑩𝑶 𝑩𝑨𝑵𝑲 𝑺𝒀𝑺𝑻𝑬𝑴 - 𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑪𝒉𝒐𝒊𝒄𝒆 𝑯𝒆𝒓𝒆' +' \n                         ')
    if(user_option == 'A' or user_option == 'a'):
        os.system('cls')
        # Program Dashboard
        # Payment Informations
        interface()
        payment_name = input('Title Of The Payment ?  ')
        payment_date = str(datetime.datetime.now())
        Payment_amount = input('Enter The Payment Amount -  ')
        my_salary = float(my_salary) - float(Payment_amount)
        payment_list.append(str('Payment Title : '+payment_name + ' | Payment Date : ' + payment_date + ' | Payment Amount : ' + currency_type + ' ' + Payment_amount + ' | Total Salary Amount : '  + currency_type + ' ' +str(my_salary)))
        print('\nYour Payment Info\n-----------------\n' + str(payment_list) + '\n') 
        input('Press Any Key To Main Menu')

        # Update Salary Database And Write Them To The File
        en_data = encrypt_data(str(currency_code + str(my_salary)))
        with open('Salary.jdl', 'w') as f:
            f.write(str(en_data))
        net_salary = my_salary
        main_menu()

    if(user_option == 'I' or user_option == 'i'):
        os.system('cls')

        # Program Dashboard
        # Income Infromations
        interface()
        income_name = input('Title Of Your Income ?  ')
        payment_date = str(datetime.datetime.now())
        income_amount = input('Enter The Income Amount -  ')
        my_salary = float(my_salary) + float(income_amount)
        income_list.append(str('Income Title : '+income_name + ' | Income Date : ' + payment_date + ' | Income Amount : ' + currency_type + ' ' + income_amount + ' | Total Salary Amount : '  + currency_type + ' ' +str(my_salary)))
        print('\nYour Total Amount Info\n-----------------\n' + str(income_list) + '\n') 
        input('Press Any Key To Main Menu')

        # Update Salary Database
        en_data = encrypt_data(str(currency_code + str(my_salary)))
        # Write Updated Information To The Database (Export Data)
        with open('Salary.jdl', 'w') as f:
            f.write(str(en_data))
        net_salary = my_salary
        main_menu()

    # When User Press R (Readme) - This Is The Readme Area
    if(user_option == 'R' or user_option == 'r'):
        os.system('cls')
        print('                 SOFTWARE INSTRUCTION - HOW TO USE THIS SOFTWARE')
        print('                 -----------------------------------------------')
        print('\n\n     ROBO BANK SYSTEM is a application software developed with Python language. \nThis application will help you to track your financial informations such as your \nSalaries, Incomes and all your Expenditures. \nThis software has a friendly graphical user interface that can easily understand \nits behavior and every functions of this software.')
        print('\n\nProgram Started Date : 2023.03.27 At 02.06PM\nDeveloped Language : Python Beginer Guide\nSpecial Thanks To HELADEVS-SWEEDEN TEAM & MORATUWA UNIVERSITY')
        print('\n')
        hela_dev_logo()
        input('\n\nPress Any Key To Main Menu')
        main_menu()

    # Program Exit Here
    if(user_option == 'E' or user_option == 'e'):
        user_option = False
        exit()

    # Payment Reminder Section
    if(user_option == 'P' or user_option == 'p'):
        os.system('cls')
        # Program Dashboard
        interface()
        payment_reminder()
        reminder_option = input('         𝑹𝑶𝑩𝑶 𝑩𝑨𝑵𝑲 𝑺𝒀𝑺𝑻𝑬𝑴 - 𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑪𝒉𝒐𝒊𝒄𝒆 𝑯𝒆𝒓𝒆' +' \n                 ')

        # Payment Reminder Option Controls
        # This Will Shows The User To Payment Reminder Interface & And It's Options
        if(reminder_option == 'C' or reminder_option == 'c'):
            os.system('cls')
            # Program Dashboard
            # Introduction
            interface()
            print('--------- WELCOME TO ROBO BANK PAYMENT REMINDER SYSTEM ---------')
            print('================================================================')
            print('\n')
            print('It Is Very Helpful When You Have A Title For Your Payment')
            remind_header = input('Please Enter Reminder Title - ')
            op1 = ('Payment Title : ' + remind_header)
            print('-------------------------------------------------------------')
            # Display User Input - Payment Title
            print(op1)
            print('-------------------------------------------------------------')
            print('It Is Very Helpful To Track, How Much Do You Want To Pay For This Payment')
            remind_amount = input('Please Enter The Amount - ')
            op2 = ('Payment Amount : ' + remind_amount)
            print('-------------------------------------------------------------')
            # Display User Input - Payment Amount
            print(op2)
            print('-------------------------------------------------------------')
            print('Type Here Everything You Wanted To Remember Including Special Notes')
            remind_note = input('Enter Discription About Your Payment - ')
            op3 = ('Payment Note : ' + remind_note)
            print('-------------------------------------------------------------')
            # Display User Input - Payment Note
            print(op3)
            print('-------------------------------------------------------------') 
            print('\n')
            # Displays The Payment Plans That Program Supports
            print('It is Very Important To Plan When You Can Pay Your Payments. Is It')
            print('>>>>>> Yearly Payment     -   Type "Y"')
            print('>>>>>> Monthly Payment    -   Type "M"')
            print('>>>>>> Daily Payment      -   Type "D"')
            print('\n')

            # Payment Reminder System - If Player Choose Yealy Plan
            # Program Will Show The Next Year As Next Payment Date
            p_date = input('What is Your Payment Type - ')
            if(p_date == "Y" or p_date == 'y'):
                next_payment = 'Yealy Payment '
                this_year = datetime.date.today().year
                next_year = int(this_year) + 1
                print('-------------------------------------------------------------')
                print('Your Next Payment Will Be In : ' + str(next_year))
                print('-------------------------------------------------------------')
                reminder_list.append(op1 + " | " + op2 + " | " + op3 + ' | ' + next_payment + " Next Payment " + str(next_year) + ' Year')
                input('\nPress AnyKey >>>>>>>>>>>>>>>>  ')
            # Payment Reminder System - If Player Choose Monthly Plan
            # Program Will Show The Next Month As Next Payment Date
            if(p_date == "M" or p_date == 'm'):
                next_payment = 'Monthly Payment '
                this_month = datetime.date.today().month
                next_month = int(this_month) + 1
                next_month = months(next_month)
                print('-------------------------------------------------------------')
                print('Your Next Payment Will Be In : ' + str(next_month) + ' Month')
                print('-------------------------------------------------------------')
                reminder_list.append(op1 + " | " + op2 + " | " + op3 + ' | ' + next_payment + " Next Payment " + str(next_month) + ' Month')
                input('\nPress AnyKey >>>>>>>>>>>>>>>>  ')
            # Payment Reminder System - If Player Choose Daily Plan
            # Program Will Show The Next Year As Next Date (Tommorow)
            if(p_date == "D" or p_date == 'd'):
                next_payment = 'Daily Payment '
                this_day = datetime.date.today().day
                next_day = int(this_day) + 1
                print('-------------------------------------------------------------')
                print('Your Next Payment Will Be In : ' + str(next_day) + ' (Tommorow)')
                print('-------------------------------------------------------------')
                reminder_list.append(op1 + " | " + op2 + " | " + op3 + ' | ' + next_payment + " Next Payment " + str(next_day) + ' Day')
                input('\nPress AnyKey >>>>>>>>>>>>>>>>  ')

            # Display Payment Reminders
            os.system('cls')
            interface()
            print('            ------YOͦUͧRͬ РⷬAͣYMⷨEͤNᴛⷮ RͬEͤMⷨIͥNDͩEͤRͬ S͛UͧMⷨMⷨEͤRͬIͥEͤS͛------')
            print('\n')
            print(reminder_list)
            print('\n')
            input('Press Any Key To Navigate To Main Window : ')
        
        if(reminder_option == 'V' or reminder_option == 'v'):
            os.system('cls')
            interface()
            print('===================================================================')
            print('------------------YOͦUͧRͬ РⷬAͣYMⷨEͤNᴛⷮ RͬEͤMⷨIͥNDͩEͤRͬ S͛UͧMⷨMⷨEͤRͬIͥEͤS͛------------------')
            print('===================================================================')
            print('\n')
            #print(reminder_list)
            print(*reminder_list, sep = "\n---------------------------------------------------------------------------------------------------------------\n")
            print('\n')
            input('Press Any Key To Navigate To Main Window : ')

        # Still Not Programmed But I Planed To Implement
        if(reminder_option == 'U' or reminder_option == 'u'):
            os.system('cls')
            interface()
            print('\n\n===================================================================')
            print('--------------------C O M M I N G   S O O N------------------------')
            print('===================================================================\n\n')
            input('Press Any Key To Navigate To Main Window : ')

        # Still Not Programmed But I Planed To Implement
        if(reminder_option == 'D' or reminder_option == 'd'):
            os.system('cls')
            interface()
            print('\n\n===================================================================')
            print('--------------------C O M M I N G   S O O N------------------------')
            print('===================================================================\n\n')
            input('Press Any Key To Navigate To Main Window : ')
