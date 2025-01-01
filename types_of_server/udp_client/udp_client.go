package main

import (
	"fmt"
	"net"
)

func main() {
	// Resolve server address
	serverAddr, err := net.ResolveUDPAddr("udp", "localhost:8080")
	if err != nil {
		fmt.Println("Error resolving address:", err)
		return
	}

	// Create a UDP connection
	conn, err := net.DialUDP("udp", nil, serverAddr)
	if err != nil {
		fmt.Println("Error creating UDP connection:", err)
		return
	}
	defer conn.Close()

	// Send a message to the server
	message := []byte("Hello, UDP Server")
	_, err = conn.Write(message)
	if err != nil {
		fmt.Println("Error sending message:", err)
		return
	}
	fmt.Println("Message sent to server.")

	// Receive a response from the server
	buffer := make([]byte, 1024)
	n, addr, err := conn.ReadFrom(buffer)
	if err != nil {
		fmt.Println("Error receiving response:", err)
		return
	}
	fmt.Printf("Received response from %s: %s\n", addr, string(buffer[:n]))
}
