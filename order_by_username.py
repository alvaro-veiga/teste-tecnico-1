import sys

def order_users(file_name, descending=False):
    users = []
    with open(file_name, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[1] == 'inbox':  # Verifica o formato correto
                users.append(line.strip())

    users.sort(reverse=descending)

    try:
        for user in users:
            print(user)
    except BrokenPipeError:
        sys.stderr.close()

if __name__ == "__main__":
    file_name = sys.argv[1]
    descending = len(sys.argv) > 2 and sys.argv[2] == "-desc"
    order_users(file_name, descending)
