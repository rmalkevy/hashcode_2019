#Shyshkin Konstantin

H = {"0": (3, {"cat", "beach", "sun"}), "3": (2, {"garden", "cat"})}
V = {"1": (2, {"selfie", "smile"}), "2": (2, {"garden", "selfie"})}

list = ["1", ("2", "3"), "4", ("5")]

def output(index,list):
    with open('result' + index + '.txt', 'w') as fhw:
        fhw.write(str(len(list)) + '\n')
        for i in list:
            if type(i) == str:
                fhw.write(i + "\n")
            else:
                if len(i) == 2:
                    fhw.write(i[0] + " " + i[1] + "\n")
                else:
                    fhw.write(i[0] + "\n")
