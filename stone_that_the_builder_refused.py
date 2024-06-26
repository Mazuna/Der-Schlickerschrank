def builder(blocks):
    current_step = 0
    built_rows = 0

    while blocks >= current_step + 1:
        current_step += 1
        built_rows += 1
        blocks -= current_step

    print("The height of the Pyramid:", built_rows)

n_blocks = int(input("Enter the number of Blocks:\n"))
builder(n_blocks)