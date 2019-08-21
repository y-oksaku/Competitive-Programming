package main
import "fmt"
// import "sort"

func main()  {
    var S string

    fmt.Scan(&S)

    var ans int
    ans = 0
    for digit := 0; digit < 3; digit++ {
        ans *= 10
        if S[digit] == '9' {
            ans += 1
        } else {
            ans += 9
        }
    }

	fmt.Println(ans)
}
