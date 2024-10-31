import sys

def find_max_min_size(file_name, min_size=False):
    users = []
    with open(file_name, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[1] == 'inbox':  # Ajuste para verificar 5 partes na linha
                user = parts[0]
                size = int(parts[4])  # O valor de 'size' está na 5ª parte da linha
                users.append((user, size))

    if not users:
        print("Nenhum dado encontrado")
        return

    if min_size:
        user_min = min(users, key=lambda x: x[1])
        print(f"{user_min[0]} inbox size {user_min[1]:09}")
    else:
        user_max = max(users, key=lambda x: x[1])
        print(f"{user_max[0]} inbox size {user_max[1]:09}")

if __name__ == "__main__":
    file_name = sys.argv[1]
    min_size = len(sys.argv) > 2 and sys.argv[2] == "-min"
    find_max_min_size(file_name, min_size)