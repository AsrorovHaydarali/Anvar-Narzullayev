kocha = input("Ko`changizni kiriting: ").strip().capitalize()
mahalla = input("Mahallangizni kiriting: ").strip().capitalize()
tuman = input("Tumaningizni kiriting: ").strip().capitalize()
viloyat = input("Viloyatingizni kiriting: ").strip().capitalize()

print(
    "\n",
    kocha,
    "ko`chasi,\n",
    mahalla,
    "mahallasi,\n",
    tuman,
    "tumani,\n",
    viloyat,
    "viloyati.",
)

print(
    "\n"
    + kocha
    + " ko`chasi,\n"
    + mahalla
    + " mahallasi,\n"
    + tuman
    + " tumani,\n"
    + viloyat
    + " viloyati."
)

print(
    f"\n{kocha} ko`chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati."
)
