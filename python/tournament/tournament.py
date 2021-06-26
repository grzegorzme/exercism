complementary_results = {"win": "loss", "loss": "win", "draw": "draw"}


def tally(tournament_results):
    header = "Team                           | MP |  W |  D |  L |  P"

    def stringify(team, results):
        return " |".join(
            [
                team.ljust(30, " "),
                str(sum(v for k, v in results.items())).rjust(3, " "),
                str(results["win"]).rjust(3, " "),
                str(results["draw"]).rjust(3, " "),
                str(results["loss"]).rjust(3, " "),
                str(3 * results["win"] + results["draw"]).rjust(3, " "),
            ]
        )

    table = dict()
    for match in tournament_results:
        team1, team2, team1result = match.split(";")
        if team1 not in table:
            table[team1] = {"win": 0, "loss": 0, "draw": 0}
        table[team1][team1result] += 1
        if team2 not in table:
            table[team2] = {"win": 0, "loss": 0, "draw": 0}
        table[team2][complementary_results[team1result]] += 1

    table = sorted(table.items(), key=lambda x: (-3 * x[1]["win"] - x[1]["draw"], x[0]))
    return [header] + [stringify(team, result) for (team, result) in table]
