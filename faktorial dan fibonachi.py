def faktorial(n, step=1):
    if n == 0 or n == 1:  
        print(f"Iterasi {step}: {n}! = 1")
        return 1
    else:  
        print(f"Iterasi {step}: {n}! = {n} * {n-1}!")
        return n * faktorial(n - 1, step + 1)

def fibonacci(n, step=1):
    if n == 0: 
        print(f"Iterasi {step}: F(0) = 0")
        return 0
    elif n == 1:
        print(f"Iterasi {step}: F(1) = 1")
        return 1
    else:  # Langkah rekursif
        print(f"Iterasi {step}: F({n}) = F({n-1}) + F({n-2})")
        return fibonacci(n - 1, step + 1) + fibonacci(n - 2, step + 1)

def main():
    print("Pilih fungsi yang ingin dijalankan:")
    print("1: Faktorial")
    print("2: Fibonacci")
    pilihan = input("Masukkan pilihan (1/2): ")
    
    if pilihan == "1":
        n = int(input("Masukkan angka untuk faktorial: "))
        print(f"\nHasil Faktorial dari {n} adalah: {faktorial(n)}")
    elif pilihan == "2":
        n = int(input("Masukkan angka untuk Fibonacci: "))
        print(f"\nHasil Fibonacci dari {n} adalah: {fibonacci(n)}")
    else:
        print("\nPeringatan: Anda hanya boleh memilih 1 atau 2!")

main()
