package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// Define the address and port to listen on
	address := ":8080" // Listen on all available IPs, port 8080

	// Start listening on the specified address
	listener, err := net.Listen("tcp", address)
	if err != nil {
		fmt.Println("Error starting TCP server:", err)
		os.Exit(1)
	}
	defer listener.Close()

	fmt.Printf("TCP server listening on %s\n", address)

	for {
		// Accept a new connection| blocking call
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}

		// Handle the connection in a separate goroutine
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close() // Ensure the connection is closed when the function ends

	// Set a timeout for the connection
	// conn.SetDeadline(time.Now().Add(10 * time.Second)) // 10-second timeout


	fmt.Printf("New client connected: %s\n", conn.RemoteAddr().String())

	// Create a buffer to read client messages
	reader := bufio.NewReader(conn)
	for {
		// Read data from the client
		message, err := reader.ReadString('\n')
		if err != nil {
			fmt.Printf("Client disconnected: %s\n", conn.RemoteAddr().String())
			return
		}

		// Print the received message
		fmt.Printf("Received message from %s: %s", conn.RemoteAddr().String(), message)

		// Send a response back to the client
		response := "Message received\n"
		_, err = conn.Write([]byte(response))
		if err != nil {
			fmt.Printf("Error sending response to %s: %v\n", conn.RemoteAddr().String(), err)
			return
		}
	}
}

// In Go, you can implement timeouts for both TCP and UDP using 
//the SetDeadline, SetReadDeadline, or SetWriteDeadline methods 
//provided by the net.Conn or net.UDPConn interfaces

// echo "Hello, TCP Server" | nc localhost 8080
