#funcion
def kerucut(rk):
    return 1/3*22/7*rk**2*t
def bola (r):
    return 4/3*22/7*r**3
if __name__ == "__main__":

    print("Menghitung Volume Kerucut dalam Bola \n")
    
    r = int(input("Masukkan jari-jari bola: "))
    rk = int(input("Masukkan jari-jari alas kerucut: "))
    t = int(input("Masukkan tinggi kerucut: "))
    

# variable
    a = kerucut(rk)
    b = bola (r)
    
    
    print("\n")

    print("Volume kerucut adalah = {}".format(a))
    print("Volume bola adalah = {}".format(b))


#loop
    selisih = [a, b]
    sum = 0
#iterasi
    for each in selisih:
        sum = b-a

    print("Selisih volume bola dan volume kerucut adalah = {}".format(sum))


# branching 
    threshold = 2*r
    
    if (t and 2*rk < (threshold-1)):
      print("karena jari-jari dan tinggi kerucut lebih kecil dari jari-jari bola, maka kerucut dapat masuk seluruhnya kedalam bola".format(r, threshold))
    elif( 2*rk and 2*t == threshold):
      print("maka kerucut dapat masuk seluruhnya kedalam bola, dan menyinggung sisi bola.".format(r, threshold))
    else:
      print("karena jari-jari kerucut atau tinggi kerucut lebih besar dari jari-jari bola, maka kerucut tidak dapat masuk seluruhnya kedalam bola".format(r, threshold)) 
   
