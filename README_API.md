# 🔬 Public API Usage Examples

Below are examples of how to use the available API endpoints.

> ⚠️ All requests require a valid **Bearer Token** in the `Authorization` header.

---

## ⚠️ Important Notes

- 🔐 **Tokens expire after 24 hours**. It is recommended to request a new token with each API call.
- 🐢 **Rate limit**: 1 request every **4 seconds**.

---

## 📍 Endpoint: Search PubMed Using Semantic Search

Search PubMed abstracts based on **vector similarity** using **FAISS**.

**GET** `http://195.134.65.149:4001/public/search_pubmed_from_faiss`

---

### 🔎 Request Body Examples

#### 🧪 Search for oxidative stress (no extra filters)

```json
{
  "query_text": "oxidative stress",
  "date_query": null,
  "organisms": [],
  "library_strategy": [],
  "experiment_type": [],
  "extracted_molecule": [],
  "top_k": 3,
  "model": "BioBERT"
}
```

#### 🧪 Search for oxidative stress in Homo sapiens organism:

```json
{
    "query_text": "oxidative stress",
    "date_query": None,
    "organisms": ['Homo sapiens'],
    "library_strategy": [],
    "experiment_type": [],
    "extracted_molecule": [],
    "top_k": 3,
    "model": 'BioBERT'
}
```

| Parameter            | Type           | Required | Description                                                                            |
| -------------------- | -------------- | -------- | -------------------------------------------------------------------------------------- |
| `query_text`         | `string`       | ✅        | Main search phrase (e.g. `"oxidative stress"`).                                        |
| `date_query`         | `integer`      | ❌        | Filter by publication year (e.g. `2010`).                                              |
| `organisms`          | `list[string]` | ❌        | E.g. `["Homo sapiens"]`.                                                               |
| `library_strategy`   | `list[string]` | ❌        | E.g. `["RNA-Seq"]`.                                                                    |
| `experiment_type`    | `list[string]` | ❌        | E.g. `["expression profiling by array"]`.                                              |
| `extracted_molecule` | `list[string]` | ❌        | E.g. `["total RNA"]`.                                                                  |
| `top_k`              | `integer`      | ✅        | Number of top results to return (e.g. `10`). Max: `10000`.                             |
| `model`              | `string`       | ❌        | Embedding model to use: `BioBERT`, `S-BioBERT`, or `MiniLM`.<br>**Default**: `BioBERT` |

💡 Notes
- Filters are applied after retrieving top vectors using L2 distance.
- query_text is the primary input and should be used like a smart PubMed search.
- Results are returned based on semantic similarity to the query.

### Example with python
Here's how to authenticate and use the API from Python using therequests library:

```python
import requests
import json

api_url = "http://195.134.65.149:4001"

# Step 1: Authenticate and get token
login_url = f"{api_url}/login/token"
login_data = {
    "username": "your_username",
    "password": "your_password"
}

login_response = requests.post(login_url, data=login_data)
token = login_response.json().get("access_token")

# Step 2: Use token to access protected route
headers = {
    "Authorization": f"Bearer {token}"
}

# Step 3: Call the semantic search endpoint
search_url = f"{api_url}/public/search_pubmed_from_faiss"
payload = {
    "query_text": "oxidative stress",
    "organisms": ["Homo sapiens"],
    "top_k": 20,
    "model": "BioBERT"
}

response = requests.get(search_url, json=payload, headers=headers)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
```
