math=input("score:")
Eng=input("score:")
math=float(math)
Eng=float(Eng)
if math>=90 and Eng>=90:
    print("prize")
elif math<=89 and Eng<=89:
    print("study hard")
else:
    print("very good")