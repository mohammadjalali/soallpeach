package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func main() {
	var path string = os.Args[1]
	str, _ := ioutil.ReadFile(path)

	tmp := string(str)

	shit := strings.SplitN(tmp, "\n", len(tmp))

	for _, line := range shit {
		it, _ := strconv.Atoi(line)
		fmt.Println(isPrime(it))
	}

}

func isPrime(n int) int {
	if n == 2 {
		return 1
	} else if n%2 == 0 {
		return 0
	}

	for i := 3; i < n; i = i + 2 {
		if n%i == 0 {
			return 0
		}
	}

	return 1
}
