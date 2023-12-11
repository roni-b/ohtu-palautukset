from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    # m1 = (
    #     query
    #     .playsIn("NYR")
    #     .hasAtLeast(10, "goals")
    #     .hasFewerThan(20, "goals")
    #     .build()
    # )

    # m2 = (
    #     query
    #     .playsIn("EDM")
    #     .hasAtLeast(50, "points")
    #     .build()
    # )

    # matcher = query.oneOf(m1, m2)
    matcher = (
    query
        .oneOf(
        query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals"),
        query.playsIn("EDM")
            .hasAtLeast(50, "points")
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
