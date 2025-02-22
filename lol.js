function hello() {
    console.log("Hello, JavaScript!")
}

hello();

// Unused variable (ESLint will flag this)
let unusedVar = 42;

// Indentation issue (ESLint will flag this)
if(true){
console.log("Indentation issue detected!");
}

// Missing semicolon (ESLint will flag this)
console.log("Linting Test")
