LOWER_ORD_MODIFIER = 96
UPPER_ORD_MODIFIER = 38

class RuckSack:
    def __init__(self) -> None:
        self.common_char_dict = {}
        self.badge_group_dict = {}

    def process_file(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            payload = 0
            for line in lines:
                string_1, string_2 = self.split_string_into_two(line)
                common_chr = self.find_character_in_common(string_1, string_2)
                priority = self.determine_priority(common_chr)
                self.common_char_dict[payload] = {"items": line, "compartments": [string_1, string_2], "char": common_chr, "priority": priority}
                payload += 1

    def split_string_into_two(self, string) -> tuple[str, str]:
        part_1, part_2 = string[:len(string)//2], string[len(string)//2:]
        return part_1, part_2

    def find_character_in_common(self, string_1, string_2) -> chr:
        for letter_1 in list(string_1):
            for letter_2 in list(string_2):
                if letter_1 == letter_2:
                    return letter_1
        raise RuntimeError

    def determine_priority(self, char) -> int:
        if char.isupper():
            priority = ord(char) - UPPER_ORD_MODIFIER
        else:
            priority = ord(char) - LOWER_ORD_MODIFIER
        return priority

    def process_badge_data(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            groupings = [ [x,y,z] for x,y,z in zip(lines[0::3], lines[1::3], lines[2::3]) ]
            group_num = 0
            for group in groupings:
                badge_letter = self.find_badge(group[0], group[1], group[2])
                priority = self.determine_priority(badge_letter)
                self.badge_group_dict[group_num] = {"compartments": group, "badge_letter": badge_letter, "priority": priority}
                group_num += 1

    def find_badge(self, string_1, string_2, string_3):
        for char_1 in list(string_1):
            for char_2 in list(string_2):
                if char_1 == char_2:
                    for char_3 in list(string_3):
                        if char_1 == char_3:
                            return char_1
        raise RuntimeError

    def priority_sum_common_char(self) -> None:
        total_sum = 0
        for v in self.common_char_dict.values():
            total_sum += v.get('priority')
        print(f"The total priority sum is: {total_sum}")

    def priority_sum_badge_char(self) -> None:
        total_sum = 0
        for v in self.badge_group_dict.values():
            total_sum += v.get('priority')
        print(f"The total priority sum is: {total_sum}")

if __name__ == "__main__":
    rucksack = RuckSack()
    rucksack.process_file('input.txt')
    rucksack.priority_sum_common_char()

    rucksack.process_badge_data('input.txt')
    rucksack.priority_sum_badge_char()