# 執行過程
### Docker
1. 開啟 Docker Desktop

2. 跑 docker 指令

    docker build -t dctmusicgensentimentbackend . 
    
    docker run -d -p 80:80 dctmusicgensentimentbackend

3. 確認是否有在跑

    docker container ls -a

4. 印出訊息

    docker logs (container ID)

5. 移除容器

    docker rm (container ID)
    
    docker volume prune -a
    
    docker system prune -a
