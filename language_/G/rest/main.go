package main

import (
	"github.com/gin-gonic/gin"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"net/http"
	"sync"
)

type Order struct {
	ID     uint   `gorm:"primaryKey"`
	Item   string `json:"item"`
	Amount int    `json:"amount"`
}

var (
	db   *gorm.DB
	mux  sync.Mutex
)

func initDB() {
	dsn := "host=localhost user=postgres password=yourpassword dbname=orders_db port=5432 sslmode=disable"
	var err error
	db, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("Failed to connect to database")
	}
	db.AutoMigrate(&Order{})
}

func createOrder(c *gin.Context) {
	var order Order
	if err := c.ShouldBindJSON(&order); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	mux.Lock()
	db.Create(&order)
	mux.Unlock()

	c.JSON(http.StatusCreated, order)
}

func getOrders(c *gin.Context) {
	var orders []Order
	db.Find(&orders)
	c.JSON(http.StatusOK, orders)
}

func getOrder(c *gin.Context) {
	var order Order
	id := c.Param("id")

	if err := db.First(&order, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Order not found"})
		return
	}
	c.JSON(http.StatusOK, order)
}

func updateOrder(c *gin.Context) {
	var order Order
	id := c.Param("id")

	if err := db.First(&order, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Order not found"})
		return
	}

	var updatedOrder Order
	if err := c.ShouldBindJSON(&updatedOrder); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	mux.Lock()
	db.Model(&order).Updates(updatedOrder)
	mux.Unlock()

	c.JSON(http.StatusOK, order)
}

func deleteOrder(c *gin.Context) {
	var order Order
	id := c.Param("id")

	if err := db.First(&order, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Order not found"})
		return
	}

	mux.Lock()
	db.Delete(&order)
	mux.Unlock()

	c.JSON(http.StatusOK, gin.H{"message": "Order deleted"})
}

func main() {
	// initDB()
	r := gin.Default()
	r.POST("/orders", createOrder)
	r.GET("/orders", getOrders)
	r.GET("/orders/:id", getOrder)
	r.PUT("/orders/:id", updateOrder)
	r.DELETE("/orders/:id", deleteOrder)

	r.Run(":8080")
}
