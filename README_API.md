# 🔬 Public API Usage Guide

Welcome to the documentation for the **Public API**. This API allows authenticated users to:

- Perform semantic searches on PubMed articles.
- Find scientific datasets (e.g., GSE series).
- Download metadata as TSV.

> ⚠️ **Authentication Required**  
> All endpoints require a valid `Bearer Token` in the `Authorization` header.

---

## 🔐 Authentication

Before accessing any protected route, authenticate with:

```python
import requests

api_url = "http://195.134.65.149:4001"

login_url = f"{api_url}/login/token"
login_data = {
    "username": "your_username",
    "password": "your_password"
}

response = requests.post(login_url, data=login_data)
token = response.json().get("access_token")

headers = {
    "Authorization": f"Bearer {token}"
}
