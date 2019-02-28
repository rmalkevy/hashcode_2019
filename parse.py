
def parse_data(file_name):
    with open(file_name, 'r') as fhr:
        file_list = fhr.readlines()
        H = {}
        V = {}
        for item in range(1, len(file_list)):
            j, count, *tag = file_list[item].rstrip().split(" ")
            if j == "H":
                H[item] = (int(count), set(tag))
            if j == "V":
                V[item] = (int(count), set(tag))
    print("H = ", H)
    print("V = ", V)
    return H, V


file1 = "a_example.txt"
file2 = "b_lovely_landscapes.txt"
file3 = "c_memorable_moments.txt"
file4 = "d_pet_pictures.txt"
file5 = "e_shiny_selfies.txt"


H, V = parse_data(file1)
