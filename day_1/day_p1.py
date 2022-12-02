class CalorieCounting:
    def __init__(self) -> None:
        self.cal_dict = {}

    def process_input_calories(self, filename) -> None:
        elf_num = 0
        cal_total = 0
        with open(filename) as f:
            for line in f:
                if line =='\n':
                    self.cal_dict[elf_num] = cal_total
                    elf_num += 1
                    cal_total = 0
                else:
                    cal_total += int(line)
        self.cal_dict = dict(sorted(self.cal_dict.items(), key=lambda item: item[1], reverse=True))

    def most_calories(self) -> None:
        top_calorie = list(self.cal_dict.items())[0]
        print(f"Elf {top_calorie[0]} had the most calories: {top_calorie[1]}")

    def top_n_elves_calories(self, n) -> None:
        sum = 0
        for i in range(0, n):
            sum += list(self.cal_dict.items())[i][1]
        print(f"The total calories for the top {n} elves is: {sum}")

if __name__ == "__main__":
    elf_calories = CalorieCounting()
    elf_calories.process_input_calories('input.txt')
    elf_calories.most_calories()
    elf_calories.top_n_elves_calories(3)