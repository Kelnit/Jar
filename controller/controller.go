package controller

import "net/http"

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	// Hello Handler
	w.Write([]byte("Hallo !"))
}
