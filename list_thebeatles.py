beatles = []
beatles.extend(["John Lennon", "Paul McCartney", "George Harrison"])

# Specify the number of members to add
n_members_to_add = 2

# Loop to add new members
for i in range(n_members_to_add):
    member_name = input("Input the name of the Bandmember to add to the list\n")
    beatles.append(member_name)
    print(f"Added member: {member_name}")

print(beatles)

del beatles[-2:]
beatles.insert(0, "Ringo Starr")
print(beatles)