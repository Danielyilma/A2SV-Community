if __name__ == '__main__':
    N = int(input())
    
    result_list = []
    
    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            result_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(result_list)
        elif command[0] == 'remove':
            result_list.remove(int(command[1]))
        elif command[0] == 'append':
            result_list.append(int(command[1]))
        elif command[0] == 'sort':
            result_list.sort()
        elif command[0] == 'pop':
            result_list.pop()
        else:
            result_list.reverse()
