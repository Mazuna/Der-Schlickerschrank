led_display_tuple = (
    """
        ###
        # #
        # #
        # #
        ###
    """,
    """
          #
          #
          #
          #
          #
    """,
    """
        ###
          #
        ###
        #
        ###
    """,
    """
        ###
          #
        ###
          #
        ###
    """,
    """
        # #
        # #
        ###
          #
          #
    """,
    """
        ###
        #
        ###
          #
        ###
    """,
    """
        ###
        #
        ###
        # #
        ###
    """,
    """
        ###
          #
          #
          #
          #
    """,
    """
        ###
        # #
        ###
        # #
        ###
    """,
    """
        ###
        # #
        ###
          #
        ###
    """,
)
user_input = input("Input the integers to display\n")
n_to_display = []

for i in user_input:
    index = int(i)
    n_to_display.append(led_display_tuple[index])
    
for display in n_to_display:
    print(display)