package main

import "fmt"

type User struct {
	name string
	age  int
}

type Whister struct {
	User
	hobby string
}

type Unknown struct {
	User
}

func (w Whister) hello() {
	fmt.Printf("Hello %s, a %d years old young man like playing %s.\n", w.name, w.age, w.hobby)
}

func (u *Unknown) SetNameAndAge(name string, age int) {
	u.name = name
	u.age = age
}

func (u Unknown) hello() {
	fmt.Printf("Who r u? Oh, %s. How old r u? M %d.\n", u.name, u.age)
}

func (u User) hello_all() {
	fmt.Printf("Hello every one!\n")
}

func (w Whister) hello_all() {
	fmt.Printf("Oh, hello to Whister and others!\n")
}

func main() {
	w := Whister{User{"Whister", 21}, "soccer"}
	w.hello()

	u := Unknown{}
	u.SetNameAndAge("Anny", 20)
	u.hello()

	u.hello_all()
	w.hello_all()
}
