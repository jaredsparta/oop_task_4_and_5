class DNA:
    def __init__(self):
        self.user()

    def count(self, dna_string):
        A_count = 0
        C_count = 0
        G_count = 0
        T_count = 0
        for letter in dna_string:
            if letter == "A":
                A_count += 1

            elif letter == "C":
                C_count += 1

            elif letter == "T":
                T_count += 1

            elif letter == "G":
                G_count += 1
            else:
                continue

        return (A_count, C_count, T_count, G_count)


    def user(self):
        while True:
            dna = input("""\nPlease input a DNA sequence or X to stop:
                    > """).upper()
            if dna == "X":
                break
            tuple = self.count(dna)
            print("\nResults:")
            print(f"A : {tuple[0]}, C : {tuple[1]}, T : {tuple[2]}, G : {tuple[3]}")

DNA()          