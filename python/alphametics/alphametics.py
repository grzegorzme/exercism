from itertools import combinations, permutations

def solve(puzzle):
    words, result = puzzle.split("==")
    words = [w.strip() for w in words.split("+")]
    result = result.strip()
    letters = set("".join(words) + result)
    first_letters = set("".join(word[0] for word in words if len(word) > 1) + result[0])

    for comb in combinations('0123456789', len(letters)):
        for perm in permutations(comb):
            solution = {l: v for l, v in zip(letters, perm)}
            if all(solution[l] != '0' for l in first_letters):
                numbers = [int("".join(solution[l] for l in word)) for word in words]
                outcome = int("".join(solution[l] for l in result))
                if sum(numbers) == outcome:
                    return {l: int(v) for l, v in solution.items()}
