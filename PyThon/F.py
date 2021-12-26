# Double queue task

line = input()
queue = dict()
served = list()

while line != "0":
    command = line[0]
    if command == "1":
        command, identifier, priority = map(int, line.split())
        queue[identifier] = priority
    else:
        info = 0
        if queue and command == "2":
            info = max(queue, key=queue.get)
            del queue[info]
        elif queue and command == "3":
            info = min(queue, key=queue.get)
            del queue[info]
        served.append(info)

    line = input()

print("\n".join(map(str, served)))