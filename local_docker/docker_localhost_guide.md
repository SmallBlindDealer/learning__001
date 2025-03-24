# How to Use `localhost` in Docker

## 1. Access Services Running on the Host from a Docker Container
By default, `localhost` inside a Docker container refers to the container itself, not the host machine.  
To access your **host machine** from inside the container, use `host.docker.internal`:

```python
redis_client = redis.Redis(host="host.docker.internal", port=6379, decode_responses=True)
```

This allows your Docker container to access services (like Redis, Postgres, etc.) running directly on your Mac/PC.

---

## 2. Enable `host.docker.internal` on Linux
If you are using Docker on **Mac/Windows**, `host.docker.internal` works out of the box.  
However, for **Linux**, you need to run:

```sh
docker run --add-host=host.docker.internal:host-gateway my_container
```

Or, modify `docker-compose.yml`:

```yaml
services:
  flask_app:
    build: .
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

---

## 3. When to Use `localhost` vs. Service Name

| Scenario | What to Use? |
|-------------|------------------|
| **Container to Container (Inside Docker)** | Use the **service name** (`my_redis`, `postgres`, etc.) |
| **Container to Host Machine (Access Local Services)** | Use `host.docker.internal` |
| **Host Machine to Docker Container** | Use `localhost` with mapped ports (`6379:6379`, `5432:5432`, etc.) |
| **Inside a Container (`localhost`)** | Refers to the **same container** |

---

## Example 1: Using `host.docker.internal`
If **Redis is running on your Mac (outside Docker)**, update your **Flask app**:

```python
redis_client = redis.Redis(host="host.docker.internal", port=6379)
```

---

## Example 2: Using a Custom Network (Without `localhost`)
If Redis **is running in Docker**, connect using the **service name** (`my_redis`):

```python
redis_client = redis.Redis(host="my_redis", port=6379)
```

---

## 🔥 Final Takeaway
- **For services running inside Docker** → Use the **service name** (e.g., `my_redis`)
- **For services running on your local machine** → Use `host.docker.internal`
- **Do NOT use `localhost` inside Docker** unless the service is running in the same container.
