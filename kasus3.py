def print_reverse_lines(n):
    for i in range(n, 0, -1):
        print("baris ke -", i)

def main():
    try:
        n = int(input("Masukkan banyak pengulangan: "))
        print_reverse_lines(n)
    except ValueError:
        print("Masukkan harus berupa bilangan bulat.")

if __name__ == "__main__":
    main()
