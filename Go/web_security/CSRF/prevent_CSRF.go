package CSRF

import (
	"crypto/md5"
	"io"
	"strconv"
	"fmt"
	"html/template"
)

func main() {
	// GET,POST
	mux.Get("/user/:uid", getuser)
	mux.Post("/user/:uid", modifyuser)

	//create token
	h := md5.New()
	io.WriteString(h, strconv.FormatInt(crutime, 10))
	io.WriteString(h, "hey")
	token := fmt.Sprintf("%x", h.Sum(nil))

	t, _ := template.ParseFiles("web_security//CSRF//login.gtpl")
	t.Execute(w, token)

	// confirm token
	r.ParseForm()
	token := r.Form.Get("token")
	if token != "" {
		//验证token的合法性
	} else {
		//不存在token报错
	}
}
