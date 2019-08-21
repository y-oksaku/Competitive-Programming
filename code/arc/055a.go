package main

import (
    "fmt"
)

func main()  {
    var N int
    fmt.Scan(&N)

    fmt.Print("1")
    for digit := N - 1; digit > 0; digit-- {
        fmt.Print("0")
    }
    fmt.Println("7")
}
