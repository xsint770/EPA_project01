'''
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author = xsint770
email: -
discord: -
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
########################################################
pocet_textu = len(TEXTS)

users = {
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123'
}
oddelovac = '-' * 40

# prihlasovaci jmeno a heslo
jmeno = input('username:')
heslo = input('password:')
print(oddelovac)

# je to nekdo z registrovanych?
# neni registrovany
if jmeno not in list(users.keys()) or heslo != users.get(jmeno): 
    print('Unregistered user, terminating the program.')
    quit()
# je registrovany
print(f'''Welcome to the app, {jmeno}. 
We have {pocet_textu} texts to be analyzed.\n''' + oddelovac)      
volba_textu = input(f'Enter a number btw. 1 and {pocet_textu} to select: ')
print(oddelovac)

# je volba textu ok?
if not volba_textu.isdigit():
    print('Incorrect input, terminating the program.')
    quit()
elif int(volba_textu) not in range(1, (pocet_textu + 1)):
    print('Your selection does not exist, terminating the program.')
    quit()
###############################################################
# analyza textu
# Klic k zarazeni stringu do skupiny:
# * slova zacinajici velkym pismenem - prvni znak je pismeno 
#   a to pismeno je velke, druh ostatnich znaku nezjistuju 
# * vsechna pismena velka/mala - vsechny znaky jsou pismena a jsou velka/mala,
#   slova obsahujici jine znaky nez pismena do skupiny nepatri 
 
vybrany_text = TEXTS[int(volba_textu) - 1]

delka_slov = {}

pocet_slov = 0
prvni_velke_pismeno = 0
velka_pismena = 0
mala_pismena = 0
jine_slovo = 0
jine_slovo_list = []
cisla = 0
suma_cisel = 0

for slovo in vybrany_text.split():
    ciste_slovo = slovo.strip('.,;:!?-_/\\')
    pocet_slov += 1 
    if ciste_slovo[0].isalpha() and ciste_slovo.istitle(): 
        prvni_velke_pismeno += 1
    elif ciste_slovo.isalpha() and ciste_slovo.isupper(): 
        velka_pismena += 1
    elif ciste_slovo.isalpha() and ciste_slovo.islower():  
        mala_pismena += 1 
    elif ciste_slovo.isdigit() or ciste_slovo.isdecimal(): 
        cisla +=1
        suma_cisel = suma_cisel + float(ciste_slovo)
    else:
        jine_slovo += 1
        jine_slovo_list.append(ciste_slovo) 

    if len(ciste_slovo) not in delka_slov:
        delka_slov[len(ciste_slovo)] = 1
    else:
        delka_slov[len(ciste_slovo)] +=1

# tisk statistik
print(f'There are {pocet_slov} words in the selected text.')
print(f'There are {prvni_velke_pismeno} titlecase words.')
print(f'There are {velka_pismena} uppercase words.')
print(f'There are {mala_pismena} lowercase words.')
print(f'There are {cisla} numeric strings.')
print(f'The sum of all the numbers is {suma_cisel}')
if jine_slovo > 0:
    print(f'''-\n(There are {jine_slovo} other words/strings 
       outside the above categories: 
       {', '.join(jine_slovo_list)})''')
print(oddelovac)

# tisk grafu
print(f'len'.upper() + '|',  
      'occurences'.upper().center(20), 
      '|' + 'nr.'.upper())
print(oddelovac)
serazena_delka_slov = sorted(delka_slov.items())
for i in range(len(serazena_delka_slov)):
    print(str(serazena_delka_slov[i][0]).ljust(3) + '|', 
          str('*' * serazena_delka_slov[i][1]).ljust(20), 
          '|' + str(serazena_delka_slov[i][1]))
print(oddelovac)  
