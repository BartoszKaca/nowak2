imie = str(input("Imie:"))
nazwisko = str(input("nazwisko:"))
print("incjaly:", imie[0],nazwisko[0], sep = "")
imie =imie.lower()
nazwisko =nazwisko.lower()
if(imie.find("an")==-1 and nazwisko.find("an")==-1 and imie.find("na")==-1 and nazwisko.find("na")==-1):
    print("nie znaleziono na lub an w danych")
else:
    print("znaleziono na lub an w danych")


