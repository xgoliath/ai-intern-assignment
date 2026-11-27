import json
import re
from collections import Counter

with open("data/support_tickets.json", "r") as file:
    tickets = json.load(file)


def clean_tickets(tickets):
    seen_ids = set()
    cleaned = []

    for ticket in tickets:
        ticket_id = ticket["ticket_id"]

        # Skip duplicate ticket IDs
        if ticket_id in seen_ids:
            continue

        seen_ids.add(ticket_id)

        query = ticket["query"]

        if not isinstance(query, str) or not query.strip():
            continue

        # Remove HTML tags and surrounding whitespace
        query = re.sub(r"<[^>]+>", "", query).strip()

        if not query:
            continue

        # Create a cleaned copy of the ticket
        cleaned_ticket = ticket.copy()
        cleaned_ticket["query"] = query

        cleaned.append(cleaned_ticket)

    return cleaned



def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-z0-9\s]", "", text)

    # Split text into individual words
    tokens = text.split()

    # Common English stop words
    stop_words = {
        "the", "is", "a", "an", "and", "or", "to",
        "of", "in", "on", "for", "my", "how", "do",
        "i", "can", "what", "after", "from", "it",
        "are", "this", "that", "with", "be", "get"
    }

    # Remove stop words
    tokens = [word for word in tokens if word not in stop_words]

    return tokens


def analyze_tickets(cleaned_tickets):
    # Count tickets in each category
    category_counts = Counter(
        ticket["category"] for ticket in cleaned_tickets
    )

    processed_tickets = []
    all_keywords = []

    for ticket in cleaned_tickets:
        tokens = preprocess_text(ticket["query"])

        # Create a copy and attach processed tokens
        processed_ticket = ticket.copy()
        processed_ticket["tokens"] = tokens

        processed_tickets.append(processed_ticket)
        all_keywords.extend(tokens)

    # Find the five most frequent keywords
    top_keywords = Counter(all_keywords).most_common(5)

    # Save processed tickets to JSON
    with open("data/cleaned_tickets.json", "w") as file:
        json.dump(processed_tickets, file, indent=4)

    print("\nCategory counts:")
    print(dict(category_counts))

    print("\nTop 5 keywords:")
    print(top_keywords)

    print("\nCleaned tickets saved to data/cleaned_tickets.json")

    return processed_tickets


# Run the cleaning and analysis pipeline
cleaned_tickets = clean_tickets(tickets)

analyze_tickets(cleaned_tickets)

