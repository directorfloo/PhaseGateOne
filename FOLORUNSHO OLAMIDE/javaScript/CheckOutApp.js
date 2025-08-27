const prompt = require("prompt-sync")();

    let itemList = [];
    let unitList = [];
    let piecesList = [];

    let name = prompt("What is your full name:\n ");

    let addItem = "YES";
    let pieces = 0;
    let unit = 0;

    while (addItem !== "NO") {
        let product = prompt("What did the user buy?:\n ");

        pieces = parseFloat(prompt("How many pieces?:\n "));
        unit = parseFloat(prompt("How much per unit?:\n "));

        itemList.push(product);
        unitList.push(unit);
        piecesList.push(pieces);

        addItem = prompt("Add more items? (Yes/No):\n ").toUpperCase();
    }

    let subTotal = 1;
    let discount = parseFloat(prompt("Enter discount (%): "));
    let discountAmount = (discount / 100) * subTotal;
    let finalTotal = subTotal - discountAmount;

    console.log("\n\n SEMICOLON STORES");
    console.log(" MAIN BRANCH");
    console.log(" LOCATION: 312, HERBERT MACAULAY WAY,  SABO YABA, LAGOS.");
    console.log(" TEL: 08123425776 ");
    console.log(" Date:", new Date().toLocaleDateString());
    console.log(" Cashier: Adam ");
    console.log(" Customer Name:", name);
    console.log("================================================================");
    console.log(" ITEM\t\tQTY\tPRICE\tTOTAL(NGN)");
    console.log("----------------------------------------------------------------");

    for (let counter = 0; counter < unitList.length; counter++) {
        let itemTotal = unitList[counter] * piecesList[counter];
        subTotal += unitList[counter] * piecesList[counter];
        console.log(` ${itemList[counter]}\t\t${piecesList[counter]}\t${unitList[counter]}\t${itemTotal}`);
    }

    console.log("================================================================");
    console.log(" Sub Total:", subTotal);
    console.log(" Discount:", discountAmount);
    console.log(" Final Total:", finalTotal);
}

