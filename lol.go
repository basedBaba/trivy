package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
    testFunc()
}

// Unused function (golangci-lint will flag this)
func unusedFunction() {
    fmt.Println("This function is not used")
}

// Function with linting issue (missing comment)
func testFunc() {
    fmt.Println("Testing Go linting")
}
