
// this is how you print("") in javascript
console.log("THIS WAS PRINTED FROM WITHIN index.js")

// this just adds a listener to any HTML element with the id smelly text, so that when its clicked, it will change the 
// Inner html
document.getElementById("smelly-text").addEventListener("click", () => {
    document.getElementById("smelly-text").innerHTML = "and that bish dont shower"
})