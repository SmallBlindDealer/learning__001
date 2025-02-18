package main

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "github.com/shiv.s.keshari/proto_example/proto"
	"google.golang.org/grpc"
)
type server struct {
	pb.UnimplementedCoffeeShopServer
}


func (s *server) GetMenu(menuRequest *pb.MenuRequest, srv grpc.ServerStreamingServer[pb.Menu]) error {
	items :=[]*pb.Item {
		&pb.Item{
			Id: "1",
			Name: "shiv",
		},
		&pb.Item{
			Id: "2",
			Name: "shankar",
		}, 
		&pb.Item{
			Id: "3",
			Name: "keshari",
		}, 
	}
	for i, _:=range items {
		srv.Send(
			&pb.Menu{
				Items: items[0:i+1],
			})
	}
	return nil
}
func (s *server) PlaceOrder(context context.Context, order *pb.Order) (*pb.Receipt, error) {
	return &pb.Receipt{Id: "sasas",}, nil
}
func (s *server) GetOrderStatus(context context.Context, recipt *pb.Receipt) (*pb.OrderStatus, error) {
	return &pb.OrderStatus{Orderid: recipt.Id, Status: "status1"}, nil
}


func main() {
	lis, err:=net.Listen("tcp", ":9001")
	if err!=nil {
		log.Fatalf("failed to listen: %v", err)
	}
	grpcServer :=grpc.NewServer()
	pb.RegisterCoffeeShopServer(grpcServer, &server{})
	fmt.Println("->>--->")

	if err:=grpcServer.Serve(lis); err!=nil {
		log.Fatalf("failed to serve :%s", err)
	}
	fmt.Println("->>--->")

}

