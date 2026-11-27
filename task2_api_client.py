import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    logging.info("Starting API request.")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        posts = response.json()

        logging.info("API request successful.")

        return posts[:5]

    except requests.exceptions.Timeout:
        logging.error("The API request timed out.")

    except requests.exceptions.ConnectionError:
        logging.error("Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        logging.error(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:
        logging.error(f"API request failed: {error}")

    return None


def transform_posts(posts):
    documents = []

    for post in posts:
        document = {
            "doc_id": post["id"],
            "title": post["title"].strip(),
            "content": post["body"].replace("\n", " ").strip(),
            "word_count": len(post["body"].split())
        }

        documents.append(document)

    return documents


def get_mock_documents():
    logging.warning("Using fallback mock documents.")

    return [
        {
            "doc_id": 101,
            "title": "VPN Password Reset",
            "content": "Contact IT support to reset your VPN password.",
            "word_count": 9
        },
        {
            "doc_id": 102,
            "title": "Remote Work Policy",
            "content": "Employees can work remotely according to company policy.",
            "word_count": 9
        }
    ]


# Main execution

posts = fetch_posts()

if posts:
    documents = transform_posts(posts)
    logging.info(f"Successfully processed {len(documents)} API documents.")
else:
    documents = get_mock_documents()
    logging.info(f"Successfully processed {len(documents)} fallback documents.")

print(documents[0])