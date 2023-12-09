import time as t
import random

#seznamy
souhlasky = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
samohlasky = ["a","e","i","o","u"]
vsechno = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", ". ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(" ")

print("(jeden odstavec se skládá ze čtyř řádků)")
otazka = int(input("zadejte kolik chcete řádků: "))

odstavec = 0
count = 0

print(" ")

#cyklus
while count != otazka:

    #randomy
    one = random.choice(vsechno)
    one2 = random.choice(vsechno)
    one3 = random.choice(souhlasky)
    one4 = random.choice(samohlasky)
    one5 = random.choice(pismena)
    one6 = (" ", one5)
    one7 = random.randint(0,1)

    #prvni_moznost
    if one5 in samohlasky:
        two = one5 + one3 
        three = two + one4
        four = three + random.choice(souhlasky)
        five = four + random.choice(vsechno)
        six = five + random.choice(pismena)
        seven = six + random.choice(samohlasky)
        eight = seven + random.choice(souhlasky) + random.choice(samohlasky)
        nine = eight + random.choice(vsechno) + random.choice(samohlasky)
        ten = nine + random.choice(souhlasky)
        eleven = ten + random.choice(samohlasky)
        twelve = eleven + random.choice(souhlasky) + random.choice(samohlasky)
        thirteen = twelve + random.choice(vsechno)
        fourteen = thirteen + random.choice(samohlasky) + random.choice(souhlasky) + " "
        fiveteen = fourteen + random.choice(pismena) + random.choice(samohlasky)
        sixteen = fiveteen + random.choice(souhlasky) + random.choice(pismena)
        seventeen = sixteen + random.choice(samohlasky) + random.choice(souhlasky) + " "
        eighteen = seventeen + random.choice(samohlasky) + random.choice(souhlasky)
        nineteen = eighteen + random.choice(samohlasky) + random.choice(vsechno) + random.choice(pismena)
        twenty = nineteen + random.choice(samohlasky) + random.choice(souhlasky) + random.choice(vsechno)
        twentyone = twenty + random.choice(pismena) + random.choice(souhlasky) + one6[one7] +random.choice(samohlasky)
        twentytwo = twentyone + random.choice(souhlasky) + random.choice(samohlasky) + random.choice(pismena)
        twentythree = twentytwo + random.choice(vsechno)
        print(twentythree)
        
    #druha_moznost
    elif one5 in souhlasky:
        two = one5 + one4
        three = two + one2
        four = three + random.choice(souhlasky)
        five = four + random.choice(vsechno)
        six = five + random.choice(pismena)
        seven = six + random.choice(samohlasky)
        eight = seven + random.choice(souhlasky) + random.choice(samohlasky)
        nine = eight + random.choice(vsechno) + random.choice(samohlasky)
        ten = nine + random.choice(souhlasky)
        eleven = ten + " " + random.choice(samohlasky)
        twelve = eleven + random.choice(souhlasky) + random.choice(samohlasky)
        thirteen = twelve + random.choice(vsechno)
        fourteen = thirteen + random.choice(samohlasky) + random.choice(souhlasky) + " "
        fiveteen = fourteen + random.choice(pismena) + random.choice(samohlasky)
        sixteen = fiveteen + random.choice(souhlasky) + random.choice(pismena)
        seventeen = sixteen + random.choice(samohlasky) + random.choice(souhlasky) + " "
        eighteen = seventeen + random.choice(samohlasky) + random.choice(souhlasky)
        nineteen = eighteen + random.choice(samohlasky) + random.choice(vsechno) + random.choice(pismena)
        twenty = nineteen + random.choice(samohlasky) + random.choice(souhlasky) + random.choice(vsechno)
        twentyone = twenty + random.choice(pismena) + one6[one7] +random.choice(samohlasky) + random.choice(souhlasky)
        twentytwo = twentyone + random.choice(samohlasky) + random.choice(souhlasky) + random.choice(pismena)
        twentythree = twentytwo + random.choice(vsechno)
        print(twentythree)

    odstavec += 1
    count += 1

    if odstavec % 4 == 0:
        print(" ")
        
    t.sleep(1)
