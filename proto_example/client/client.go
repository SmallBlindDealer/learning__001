

package main

import (
	"context"
	"io"
	"log"
	"time"

	pb "github.com/shiv.s.keshari/proto_example/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	conn, err := grpc.NewClient("localhost:9001", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err!=nil {
		log.Fatalf("failed to connect to gRPC server")
	}
	defer conn.Close()

	c:=pb.NewCoffeeShopClient(conn)
	ctx, cancel:=context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	menuStream, err := c.GetMenu(ctx, &pb.MenuRequest{})
	if err !=nil {
		log.Fatal("error calling function getMenu")
	}
	done :=make(chan bool)
	var items []*pb.Item

	go func() {
		for {
			res, err :=menuStream.Recv()
			if err == io.EOF {
				done<- true
				return
			}
			if err!=nil {
				log.Fatalf("can not reveieve %v", err)
			}
			items = res.Items
			log.Printf("Res receieved: %v", res.Items)
		}	
	}()
	<-done
	receipt, err := c.PlaceOrder(ctx, &pb.Order{Items:  items})
	log.Printf("%v", receipt)

	status, err := c.GetOrderStatus(ctx, receipt)
	log.Printf("%v", status)
	
}