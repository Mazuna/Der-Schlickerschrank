standard_input = "778"
led_display_tuple = (
    [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    [
        "  #",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    [
        "###",
        "  #",
        "###",
        "#  ",
        "###"
    ],
    [
        "###",
        "  #",
        "###",
        "  #",
        "###"
    ],
    [
        "# #",
        "# #",
        "###",
        "  #",
        "  #"
    ],
    [
        "###",
        "#  ",
        "###",
        "  #",
        "###"
    ],
    [
        "###",
        "#  ",
        "###",
        "# #",
        "###"
    ],
    [
        "###",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    [
        "###",
        "# #",
        "###",
        "  #",
        "###"
    ]
)

user_input = input("Input the integers to display\n")
n_to_display = []

# Collect the lines for each digit
for digit in user_input:
    index = int(digit)
    n_to_display.append(led_display_tuple[index])

# Print the digits side by side
for i in range(5):  # Each digit has 5 lines
    line = ""
    for digit in n_to_display:
        line += digit[i] + " "  # Adjust spaces between digits
    print(line)
