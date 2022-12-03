SHAPE_POINT_DICT = {"X": 1, "Y": 2, "Z": 3}
TRANSLATE_DICT = {"X": "A", "Y": "B", "Z": "C"}
REVERSE_TRANSLATE_DICT = {"A": "X", "B": "Y", "C": "Z"}
LOST_TRANSLATE_DICT = {"A": "Z", "B": "X", "C": "Y"}
WIN_TRANSLATE_DICT = {"A": "Y", "B": "Z", "C": "X"}

class StrategyScoreSheet:
    def __init__(self) -> None:
        self.score_sheet_dictionary = {}
        self.final_score = 0
        pass

    def process_strategy_guide(self, filename, column_two_round_status=False) -> None:
        with open(filename) as f:
            lines = f.read().splitlines()
            round = 0
            for line in lines:
                shape_1, shape_2 = line.split(" ")
                if column_two_round_status:
                    shape_2 = self.convert_shape_to_round_status(shape_1, shape_2)
                round_points = self.get_round_points(shape_1, shape_2)
                
                round_dictionary = {
                    "shape_1": shape_1,
                    "shape_2": shape_2,
                    "shape_points": SHAPE_POINT_DICT[shape_2],
                    "round_points": round_points - SHAPE_POINT_DICT[shape_2]
                }
                self.score_sheet_dictionary[round] = round_dictionary
                round += 1
                self.final_score += round_points

    def get_round_points(self, shape_1, shape_2) -> int:
        shape_point = SHAPE_POINT_DICT[shape_2]
        # draw
        if shape_1 == TRANSLATE_DICT[shape_2]:
            win_points = 3
        # user loss
        elif (shape_1 == 'A' and shape_2 == 'Z') or (shape_1 == 'C' and shape_2 == 'Y') or (shape_1 == 'B' and shape_2 == 'X'):
            win_points = 0
        # user win
        else:
            win_points = 6

        round_points = shape_point + win_points
        return round_points

    def get_final_score(self) -> None:
        print(f"Final Score for Strategy Guide is: {self.final_score}")

    def convert_shape_to_round_status(self, shape_1, shape_2) -> str:
        if shape_2 == "Y":
            shape_2 = REVERSE_TRANSLATE_DICT[shape_1]
        elif shape_2 == "X":
            shape_2 = LOST_TRANSLATE_DICT[shape_1]
        else:
            shape_2 = WIN_TRANSLATE_DICT[shape_1]
        return shape_2

if __name__ == "__main__":
    # Part 1
    startegy_guide = StrategyScoreSheet()
    startegy_guide.process_strategy_guide('input.txt')
    startegy_guide.get_final_score()

    # Part 2
    startegy_guide_round_status = StrategyScoreSheet()
    startegy_guide_round_status.process_strategy_guide('input.txt', True)
    startegy_guide_round_status.get_final_score()