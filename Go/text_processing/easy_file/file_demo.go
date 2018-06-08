package main

import (
	"fmt"
	"os"
)

func main() {
	os.Mkdir("whister", 0777)
	os.MkdirAll("whister/test1/test2", 0777)
	err := os.Remove("whister")
	if err != nil {
		fmt.Println(err)
	}
	os.RemoveAll("whister")
}