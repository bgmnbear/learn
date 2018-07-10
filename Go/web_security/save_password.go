package main

import (
	"crypto/sha256"
	"io"
	"fmt"
	"crypto/sha1"
	"crypto/md5"
)

func main() {
	// normal
	//import "crypto/sha256"
	h := sha256.New()
	io.WriteString(h, "His money is twice tainted: 'taint yours and 'taint mine.")
	fmt.Printf("% x", h.Sum(nil))

	//import "crypto/sha1"
	h := sha1.New()
	io.WriteString(h, "His money is twice tainted: 'taint yours and 'taint mine.")
	fmt.Printf("% x", h.Sum(nil))

	//import "crypto/md5"
	h := md5.New()
	io.WriteString(h, "需要加密的密码")
	fmt.Printf("%x", h.Sum(nil))

	// Advanced
	//import "crypto/md5"
	//假设用户名abc，密码123456
	h := md5.New()
	io.WriteString(h, "需要加密的密码")

	//pwmd5等于e10adc3949ba59abbe56e057f20f883e
	pwmd5 := fmt.Sprintf("%x", h.Sum(nil))

	//指定两个 salt： salt1 = @#$%   salt2 = ^&*()
	salt1 := "@#$%"
	salt2 := "^&*()"

	//salt1+用户名+salt2+MD5拼接
	io.WriteString(h, salt1)
	io.WriteString(h, "abc")
	io.WriteString(h, salt2)
	io.WriteString(h, pwmd5)

	last := fmt.Sprintf("%x", h.Sum(nil))

	// master
	dk := scrypt.Key([]byte("some password"), []byte(salt), 16384, 8, 1, 32)
}
