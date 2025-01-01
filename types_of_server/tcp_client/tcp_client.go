package main

import (
	"bufio"
	"net"
	"testing"
)

func TestTCPServer(t *testing.T) {
	// Connect to the server
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		t.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	// Send a message
	message := "Hello, Server\n"
	_, err = conn.Write([]byte(message))
	if err != nil {
		t.Fatalf("Failed to send message: %v", err)
	}

	// Read the response
	response, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		t.Fatalf("Failed to read response: %v", err)
	}

	expected := "Message received\n"
	if response != expected {
		t.Errorf("Expected %q but got %q", expected, response)
	}
}
