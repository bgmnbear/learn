package main

import "regexp"

func main() {
	// white list
	r.ParseForm()
	name := r.Form.Get("name")
	CleanMap := make(map[string]interface{}, 0)
	if name == "astaxie" || name == "herry" || name == "marry" {
		CleanMap["name"] = name
	}

	// regexp
	r.ParseForm()
	username := r.Form.Get("username")
	CleanMap := make(map[string]interface{}, 0)
	if ok, _ := regexp.MatchString("^[a-zA-Z0-9]+$", username); ok {
		CleanMap["username"] = username
	}
}
