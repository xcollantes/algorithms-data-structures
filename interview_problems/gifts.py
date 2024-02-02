"""Each person at a party gets a gift."""


def main():
    gifts = ["book", "chocolate"]
    people = ["A", "B", "C"]

    # print(getRoundRobin(people, gifts))
    print(getRoundRobinAnswer(people, gifts))


def getRoundRobin(people: str, gifts: str) -> dict[str, str]:
    result = {}
    for person in people:
        result[person] = []
        print("PERSON: ", person)

        for gift in gifts:
            print(f"Adding {gift} to {person}")
            result[person].append(gift)

    return result


def getRoundRobinAnswer(people: str, gifts: str) -> dict[str, str]:
    result = {}
    for receiver in people:
        gift_idx = 0  # Use index since gifts correspond to sender.
        for sender in people:
            if receiver is not sender:
                result[receiver].append(gifts[gift_idx])
                gift_idx += 1

    return result


def getRoundRobinClean(people: str, gifts: str) -> dict[str, str]:
    pass


if __name__ == "__main__":
    main()
