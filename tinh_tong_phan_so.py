def calculate_series_sum():
    try:
        n = int(input("Enter the number of terms: "))
        if n < 1:
            print("n must be >= 1")
            return
        
        s = 0
        for i in range(1, n + 1):
            term = ((-1)**(i + 1)) / (i**i)
            s += term
        
        print("OUTPUT")
        print(f"{s:.4f}")
        print("FINISH")
    except ValueError:
        print("Invalid input")
        
print(calculate_series_sum())