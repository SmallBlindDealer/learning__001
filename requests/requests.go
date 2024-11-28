package requests

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)



func main() {
	res, err:= http.Get("https://jsonplaceholder.typicode.com/posts")
	if err!=nil {
		panic(err)
	}
	defer res.Body.Close() // close the connection
	dataBytes, _:=ioutil.ReadAll(res.Body)
	fmt.Println(string(dataBytes))
	logger := log.New(os.Stdout, "INFO: ", log.Ldate|log.Ltime)
	logger.Println("This is an info message.")

}