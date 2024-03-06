
def all_sequences(n, sequence=""):
    if n == 0:
        txtfile=open("airtel_password_possibilities.txt",'a')
        txtfile.write("air"+sequence)
        txtfile.write("\n")
        txtfile.close()
        #print(sequence)
    else:
        for i in range(10):
            all_sequences(n - 1, sequence + str(i))

# Example usage
n = 5

all_sequences(n)

