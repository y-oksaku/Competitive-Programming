package main

import (
    "fmt"
    "math"
)

func main()  {
    var L, X, Y, S, D float64
    fmt.Scan(&L, &X, &Y, &S, &D)

    var back, front float64
    if D >= S {
        front = (D - S) / (X + Y)
        back = (L - (D - S)) / (Y - X)
    } else {
        front = (L - (S - D)) / (X + Y)
        back = (S - D) / (Y - X)
    }

    if Y <= X {
        fmt.Println(front)
    } else {
        fmt.Println(math.Min(front, back))
    }
}

func abs(a int) int {
    return int(math.Abs(float64(a)))
}

func fabs(a float64) float64 {
    return math.Abs(a)
}

func pow(p, q int) int {
    return int(math.Pow(float64(p), float64(q)))
}

func min(nums ...int) int {
    if len(nums) == 0 {
        panic("funciton min() requires at least one argument.")
    }
    res := nums[0]
    for i := 0; i < len(nums); i++ {
        res = int(math.Min(float64(res), float64(nums[i])))
    }
    return res
}

func max(nums ...int) int {
    if len(nums) == 0 {
        panic("funciton max() requires at least one argument.")
    }
    res := nums[0]
    for i := 0; i < len(nums); i++ {
        res = int(math.Max(float64(res), float64(nums[i])))
    }
    return res
}
