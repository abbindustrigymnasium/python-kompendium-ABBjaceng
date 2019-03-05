male = [
" Erik ",
" Lars ",
" Karl ",
" Anders ",
" Johan "
]
female = [
" Maria ",
" Anna ",
" Margareta ",
" Elisabeth ",
" Eva "
]

print(male [0])
print(female [0])
print(female [3])
print(male [1])

del male [1]
del male [2]
del female [0]

print()
print(male [0])
print(female [0])
print(female [3])
print(male [1])

male.append("Jacob")

male.sort()
female.sort()

print ("Män:", male )
print ("Kvinnor :", female )

