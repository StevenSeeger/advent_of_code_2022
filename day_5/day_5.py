import copy
FILENAME = "input.txt"
CHAR_GAP = 4

def process_file(filename):
    crates = dict()
    with open(filename) as f:
        lines = f.read().splitlines()
        for j, line in enumerate(lines):
            if line == '':
                moves = lines[j+1:]
                break
            items = [line[i:i+CHAR_GAP] for i in range(0, len(line), CHAR_GAP)]
            counter = 1
            for item in items:
                letter = ''.join(filter(str.isalpha, item))
                if letter != '':
                    crates.setdefault(counter, []).append(letter)
                counter += 1

        for i in range(1, 10):
            crates[i] = crates[i][::-1]

        crates_og = {key: value[:] for key, value in crates.items()}

        # 9000 series
        for move in moves:
            num_box, f_pos, t_pos = [int(x) for x in move.split(' ') if x.isdigit()]
            for i in range(num_box):
                box = crates[f_pos].pop()
                crates[t_pos].append(box)

        # 9001 series
        for move in moves:
            num_box, f_pos, t_pos = [int(x) for x in move.split(' ') if x.isdigit()]
            old_lst = crates_og[f_pos][:-num_box]
            mv_lst = crates_og[f_pos][-num_box:]
            crates_og[f_pos] = old_lst
            crates_og[t_pos] = crates_og[t_pos] + mv_lst

    output = ''
    for i in range(1, 10):
        output += crates[i][-1]
    print("9000 series:", output)

    output = ''
    for i in range(1, 10):
        output += crates_og[i][-1]
    print("9001 series:", output)

if __name__ == "__main__":
    process_file(FILENAME)