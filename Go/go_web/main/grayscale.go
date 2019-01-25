package main

func passed() bool {
	key := hashFunctions(userID) % 1000
	if key <= 2 {
		return true
	}

	return false
}

func isTrue() bool {
	return true/false according to the rate provided by user
}

func isTrue(phone string) bool {
	if hash of phone matches {
		return true
	}

	return false
}


var cityID2Open = [12000]bool{}

func init() {
	readConfig()
	for i:=0;i<len(cityID2Open);i++ {
		if city i is opened in configs {
			cityID2Open = true
		}
	}
}

func isPassed(cityID int) bool {
	return cityID2Open[cityID]
}