'''def sprawdz_numer_telefonu(numer):
    if len(numer) == 9 and numer.isdigit():
        return "Numer telefonu jest poprawny."
    else:
        return "Numer telefonu jest niepoprawny."

numer = input("Podaj numer telefonu: ")
print(sprawdz_numer_telefonu(numer))'''

import re

def sprawdz_numer_telefonu(tel):

    wzorzec = r'^\d{9}$'
    
    if re.match(wzorzec, tel):
        return "Numer telefonu jest poprawny."
    else:
        return "Numer telefonu jest niepoprawny."

tel = input("Podaj numer telefonu: ")
print(sprawdz_numer_telefonu(tel))