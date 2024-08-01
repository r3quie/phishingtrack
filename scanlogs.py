def scanLogs(file):
    abc = "abcdefghijklmnopqrstuvwxyz"
    with open(file, "r") as f:
        lines = f.readlines()
        return ["".join([abc[(abc.find(c)+13)%26] for c in line.split("?id=")[1].split(" ")[0]]) for line in lines if "?id=" in line]

if __name__ == "__main__":
    path = input("Enter file name or path:\n")
    print("Scanning logs...\n----------------")
    print(scanLogs(path))