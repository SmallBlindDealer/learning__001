https://www.youtube.com/playlist?list=PLBm4OGt1_S7aKTFWL2nKbyLcu6H2pRi2Q

https://support.konghq.com/support/s/article/How-to-setup-Kong-to-serve-an-SSL-certificate-for-API-requests#:~:text=The%20installation%20of%20Kong%20provides,the%20clients%20known%20CA%20list.&text=Now%20that%20we%20have%20a,points%20to%20the%20Certificate%20entity.&text=6)%20It%20is%20now%20possible,pem).



docker-compose up

curl http://127.0.0.1:8001/services
curl http://127.0.0.1:8001/routes

docker-compose logs kong
