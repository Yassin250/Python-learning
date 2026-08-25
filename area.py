def area(length, width):
    print(str(length * width) + " square feet")
    return length * width

def main():
   house_area = area(10,20)
   yard_area = area(10,10)
   total_area = house_area + yard_area
   print(str(total_area) + " total square feet")

main()