"""

Design a distributed order tracking system for an e-commerce platform that can handle:
 - Real-time order status updates
 - Scalability to process 10,000 orders per minute
 - Fault tolerance and data consistency
 - Integration with multiple warehouse and logistics providers


 
warehouse

 


logistic_service
    collect warehouse order
    
    --create_assign



logistics_providers(driver-app)

 Agents

 


user_place_order--->notify_fulfilment--->ok-->logistic_

"""

from datetime import timedelta, datetime