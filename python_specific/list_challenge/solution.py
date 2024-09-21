def main(commands):
    work_list = []
    for cmd in commands:
        execute_command(cmd, work_list)


def execute_command(cmd, work_list):
    try:
        if 'insert' in cmd[0].lower():
            work_list.insert(int(cmd[1]), int(cmd[2]))
        elif 'print' in cmd[0].lower():
            print(work_list)
        elif 'remove' in cmd[0].lower():
            work_list.remove(int(cmd[1]))
        elif 'append' in cmd[0].lower():
            work_list.append(int(cmd[1]))
        elif 'sort' in cmd[0].lower():
            work_list.sort()
        elif 'pop' in cmd[0].lower():
            work_list.pop()
        elif 'reverse' in cmd[0].lower():
            work_list.reverse()
    except Exception as e:
        pass


if __name__ == '__main__':
    N = int(input())
    commands = []
    for i in range(N):
        cmd = input().split(' ')
        commands.append(cmd)
    
    main(commands)
