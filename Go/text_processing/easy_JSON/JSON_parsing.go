package main

import (
	"encoding/json"
	"fmt"
)

type Server1 struct {
	ServerName string
	ServerIP   string
}

type Serverslice1 struct {
	Servers []Server1
}

func main() {
	var s Serverslice1
	str := `{"servers":[{"serverName":"Shanghai_VPN","serverIP":"127.0.0.1"},{"serverName":"Beijing_VPN","serverIP":"127.0.0.2"}]}`
	json.Unmarshal([]byte(str), &s)
	fmt.Println(s)
}