
BERTHS = ["SU", "LB", "MB", "UB", "LB", "MB", "UB", "SL"]


def parse_pnr(pnr):
    if not isinstance(pnr, str):
        raise ValueError("PNR must be a string")

    if len(pnr) != 10 or not all(ch in "0123456789" for ch in pnr):
        raise ValueError("PNR must contain exactly 10 digits")

    return int(pnr[0]), int(pnr[1:])


def journey_distance(distances_csv):
    if not isinstance(distances_csv, str):
        raise ValueError("Distances must be provided as a CSV string")

    parts = distances_csv.split(',')

    if len(parts) < 2:
        raise ValueError("At least two station distances are required")

    try:
        distances = [int(d.strip()) for d in parts]
    except ValueError:
        raise ValueError("All station distances must be integers")

    return distances[-1] - distances[0]


def berth_type(seat):
    if not isinstance(seat, str):
        raise ValueError("Seat must be a string")

    if seat.count('-') != 1:
        raise ValueError("Seat must be in COACH-NUMBER format")

    coach, number = seat.split('-')

    coach = coach.strip()

    if not coach:
        raise ValueError("Coach cannot be empty")

    if not number.isdigit():
        raise ValueError("Seat number must be a positive integer")

    number = int(number)

    if number <= 0:
        raise ValueError("Seat number must be positive")

    return coach.upper(), BERTHS[number % 8]


def main():
    print("==== Running parse_pnr ====")
    user_input = input("Enter a 10 digit PNR (e.g. 4521367890): ")
    result = parse_pnr(user_input)
    print("Zone and Number:", result)

    print("\n==== Running journey_distance ====")
    user_input = input("Enter station distances as CSV (e.g. 0,120,340): ")
    result = journey_distance(user_input)
    print("Total Distance:", result)

    print("\n==== Running berth_type ====")
    user_input = input("Enter coach and seat (e.g. S3-45): ")
    result = berth_type(user_input)
    print("Coach and Berth:", result)


if __name__ == "__main__":
    main()
