package main

import (
	"application/controller"
	"log"
	"net/http"
)

func main() {
	// Router & Controller
	http.HandleFunc("/", controller.HelloHandler)
	// On Server
	log.Println("Port 5000 !")
	fail := http.ListenAndServe(":5000", nil)
	// Fail Server
	if fail != nil {
		log.Fatal(fail.Error())
	}
}
