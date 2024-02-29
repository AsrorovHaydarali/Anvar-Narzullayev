kocha = input("Ko`changizni kiriting: ").strip().capitalize()
mahalla = input("Mahallangizni kiriting: ").strip().capitalize()
tuman = input("Tumaningizni kiriting: ").strip().capitalize()
viloyat = input("Viloyatingizni kiriting: ").strip().capitalize()

print(kocha, "ko`chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati.")
print(
    kocha
    + " ko`chasi, "
    + mahalla
    + " mahallasi, "
    + tuman
    + " tumani, "
    + viloyat
    + " viloyati."
)
print(f"{kocha} ko`chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")
