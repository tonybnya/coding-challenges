/*
 * Challenge 2: JavaScript - Real-World Problem
 *
 * Task: Write a JavaScript function that takes an array of objects
 * representing products and returns the total price of all products.
 * Each object has keys name, price, and quantity.
 *
*/
const products = [
    { name: "Laptop", price: 1000, quantity: 2 },
    { name: "Phone", price: 500, quantity: 3 },
    { name: "Tablet", price: 300, quantity: 1 }
];

const totalPrice = (products) => {
    // Your code here
    let totalPrice = 0;
    for (let i = 0; i < products.length; ++i) {
        totalPrice += products[i].price;
    }
    return totalPrice;
}

console.log(totalPrice(products));
