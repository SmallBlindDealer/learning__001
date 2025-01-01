package main

import (
	"fmt"
	"net"
)

func main() {
	// Define the UDP address and port
	address := ":8080"

	// Resolve the UDP address
	udpAddr, err := net.ResolveUDPAddr("udp", address)
	if err != nil {
		fmt.Println("Error resolving address:", err)
		return
	}

	// Start listening on the UDP address
	conn, err := net.ListenUDP("udp", udpAddr)
	if err != nil {
		fmt.Println("Error starting UDP server:", err)
		return
	}
	defer conn.Close()

	fmt.Printf("UDP server listening on %s\n", address)

	// Buffer for incoming messages
	buffer := make([]byte, 1024)

	for {
		// Read the incoming message
		n, addr, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error reading from UDP:", err)
			continue
		}

		// Print the message and client address
		fmt.Printf("Received message: %s from %s\n", string(buffer[:n]), addr)

		// Process the request in a separate goroutine
		go handleRequest(conn, addr, buffer[:n])
	}
}

func handleRequest(conn *net.UDPConn, addr *net.UDPAddr, message []byte) {
	// Example: Print and respond to the client
	fmt.Printf("Handling request from %s: %s\n", addr, string(message))

	// Respond to the client
	response := "Message received\n"
	_, err := conn.WriteToUDP([]byte(response), addr)
	if err != nil {
		fmt.Printf("Error responding to %s: %v\n", addr, err)
	}
}

//echo "Hello, UDP Server" | nc -u localhost 8080
