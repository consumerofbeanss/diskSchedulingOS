import sys

def fcfs(requests, initialPos):
    totalHeadMovements = 0
    currentPos = initialPos
    for request in requests:
        totalHeadMovements += abs(request - currentPos)
        currentPos = request
    return totalHeadMovements

def scan(requests, initialPos, totalCylinders):
    requests.sort()
    totalHeadMovements = 0
    currentPos = initialPos
    headDirection = -1
    while requests:
        if currentPos in requests:
            requests.remove(currentPos)
        if currentPos == 0 or currentPos == totalCylinders - 1:
            headDirection *= -1
        currentPos += headDirection
        totalHeadMovements += 1
    return totalHeadMovements

def cscan(requests, initialPos, totalCylinders):
    requests.sort()
    totalHeadMovements = 0
    currentPos = initialPos
    while requests:
        if currentPos in requests:
            requests.remove(currentPos)
        if currentPos == totalCylinders - 1:
            currentPos = 0
        else:
            currentPos += 1
        totalHeadMovements += 1
    return totalHeadMovements

def main():
    if len(sys.argv) != 3:
        print("Usage: python program_name.py initial_position input_file.txt")
        return

    initialPos = int(sys.argv[1])
    request = sys.argv[2]

    with open(request, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]


    totalCylinders = 5000

    # Task 1
    print("Task 1:")
    print("FCFS Head Movements:", fcfs(requests.copy(), initialPos))
    print("SCAN Head Movements:", scan(requests.copy(), initialPos, totalCylinders))
    print("C-SCAN Head Movements:", cscan(requests.copy(), initialPos, totalCylinders))

    # Task 2
    print("Task 2:")
    print("FCFS Head Movements:", fcfs(sorted(set(requests)), initialPos))
    print("SCAN Head Movements:", scan(sorted(set(requests)), initialPos, totalCylinders))
    print("C-SCAN Head Movements:", cscan(sorted(set(requests)), initialPos, totalCylinders))


if __name__ == "__main__":
    main()
