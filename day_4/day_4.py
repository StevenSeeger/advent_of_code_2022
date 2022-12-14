def process_file(filename) -> int:
    contains = 0
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            group_1, group_2 = line.split(',')
            min_1, max_1 = [int(s) for s in group_1.split('-')]
            min_2, max_2= [int(s) for s in group_2.split('-')]
            if ((min_1 <= min_2) and (max_1 >= max_2)):
                contains +=1
            elif ((min_2 <= min_1) and (max_1 <= max_2)):
                contains +=1
    return contains

def overlaps_process_file(filename) -> int:
    contains = 0
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            group_1, group_2 = line.split(',')
            min_1, max_1 = [int(s) for s in group_1.split('-')]
            min_2, max_2= [int(s) for s in group_2.split('-')]
            if (min_2 >= min_1) and (min_2 <= max_1):
                contains += 1
            elif (min_1 >= min_2) and (min_1 <= max_2):
                contains += 1
            elif (max_2 >= min_1) and (max_2 <= max_1):
                contains += 1
            elif (max_1 >= min_2) and (max_1 <= max_2):
                contains += 1
    return contains


if __name__ == "__main__":
    num_contained = process_file('input.txt')
    print(num_contained)

    num_contained = overlaps_process_file('input.txt')
    print(num_contained)