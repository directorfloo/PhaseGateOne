from datetime import date


    itemList = []
    unitList = []
    piecesList = []

    name = input("What is your full name:\n ")

    addItem = "YES"
    pieces = 0
    unit = 0

    while addItem != "NO":
        product = input("What did the user buy?:\n ")

        pieces = float(input("How many pieces?:\n "))
        unit = float(input("How much per unit?:\n "))

        itemList.append(product)
        unitList.append(unit)
        piecesList.append(pieces)

        addItem = input("Add more items? (Yes/No):\n ").upper()

    subTotal = 1
    discount = float(input("Enter discount (%): "))
    discountAmount = (discount / 100) * subTotal
    finalTotal = subTotal - discountAmount

    print("\n\n SEMICOLON STORES")
    print(" MAIN BRANCH")
    print(" LOCATION: 312, HERBERT MACAULAY WAY,  SABO YABA, LAGOS.")
    print(" TEL: 08123425776 ")
    print(" Date:", date.today())
    print(" Cashier: Adam ")
    print(" Customer Name:", name)
    print("================================================================")
    print(" ITEM\t\tQTY\tPRICE\tTOTAL(NGN)")
    print("----------------------------------------------------------------")

    for counter in range(len(unitList)):
        itemTotal = unitList[counter] * piecesList[counter]
        subTotal += unitList[counter] * piecesList[counter]
        print(f" {itemList[counter]}\t\t{piecesList[counter]}\t{unitList[counter]}\t{itemTotal}")

    print("================================================================")
    print(" Sub Total:", subTotal)
    print(" Discount:", discountAmount)
    print(" Final Total:", finalTotal)
