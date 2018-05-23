package main

import "fmt"

func main() {
	var user, age = "Whister", 21
	fmt.Printf("Hello, %s, a %d years old young man.\n", user, age)

	a := [3]string{"a", "b", "c",}

	for i := 0; i < 3; i++ {
		fmt.Printf("Let's have a count %d %s.\n", i, a[i])
	}

	type coder struct {
		name string
		age  int
	}

	var C coder

	C.name = "Whister"
	C.age = 21
	fmt.Printf("The coder's name is %s and he is %d years old.\n", C.name, C.age)
}
