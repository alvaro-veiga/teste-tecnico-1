import sys

def find_between_msgs(file_name, min_msgs, max_msgs):
    users = []
    with open(file_name, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[1] == 'inbox':  # Verifica o formato correto
                msgs = int(parts[2])  # A quantidade de mensagens está na 3ª parte
                if min_msgs <= msgs <= max_msgs:
                    users.append(line.strip())

    for user in users:
        print(user)

if __name__ == "__main__":
    file_name = sys.argv[1]
    min_msgs = int(sys.argv[2])
    max_msgs = int(sys.argv[3])
    find_between_msgs(file_name, min_msgs, max_msgs)