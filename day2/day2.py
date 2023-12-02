from dataclasses import dataclass
import string
import re

@dataclass
class Game:
    id: int
    pulls: list[[int, int, int]]

games = []
powers = []
with open("input.txt") as file:
    for line in file:
        #line_digits = ''.join(filter(lambda x : x in [';', ':', ','] or x in string.digits, line))
        #print(line_digits)
        first_split = line.split(":")
        print(first_split)
        id = int(re.findall(r'\d+', first_split[0])[0])
        game_pulls = []
        for pull in first_split[1].split(";"):
            pull_list = [0,0,0]
            pull_split = pull.split(",")
            for component in pull_split:
                if ("red" in component):
                    pull_list[0]=int(re.findall(r'\d+', component)[0])
                if ("green" in component):
                    pull_list[1]=int(re.findall(r'\d+', component)[0])
                if ("blue" in component):
                    pull_list[2]=int(re.findall(r'\d+', component)[0])
            game_pulls.append(pull_list)
        game = Game(id, game_pulls)

        minimum = game.pulls[0]
        #print(game.pulls)
        for pull in game.pulls:
            for idx, component in enumerate(pull):
                minimum[idx] = max([minimum[idx], component])
        print(f"Minimum: {minimum}")
        powers.append(minimum)

        possible = True
        for pull in game.pulls:
            #12 red cubes, 13 green cubes, and 14 blue cubes
            if pull[0] > 12 or pull[1] > 13 or pull[2] > 14:
                    possible = False
        if possible:
            games.append(game)
        #print(game)

    print(games)
    sum = 0
    for game in games:
        sum = sum + game.id
    print(f"Sum: {sum}")
    power_sum = 0
    for minimum in powers:
        power_sum = power_sum + (minimum[0] * minimum[1] * minimum[2])
    print(f"Power sum = {power_sum}")