def main():
    spacecraft = {"name": " Yassin webb space telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun", "length": 0.12, "width": 0.1})
    print (create_report(spacecraft))




def create_report(spacecraft):
    return f"""""
    ========REPORT========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} million km
    orbit: {spacecraft["orbit"]}
    Length: {spacecraft["length"]} 
    Width: {spacecraft["width"]} 

    ==================

    """""


main()
    