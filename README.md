AI Intern Take Home Assignment

## Project Overview:

This project demonstrates Python data cleaning, basic NLP preprocessing, API integration, and introductory concepts related to LLMs, RAG, and AI safety.

The project consists of three main parts.

1. Data Cleaning and NLP: Cleans support tickets, removes duplicates and invalid records, preprocesses text, and extracts frequent keywords.

2. API Integration: Fetches posts from JSONPlaceholder, transforms the response into structured documents, and handles API errors using fallback mock data.

3. LLM, RAG, and AI Safety: Covers prompt engineering, retrieval strategies, and prompt injection prevention.

## Project Structure

ai-intern-assignment/
|
|-- data/
|   |-- support_tickets.json
|   |-- cleaned_tickets.json
|
|-- task1_nlp_cleaner.py
|-- task2_api_client.py
|-- ANSWERS.md
|-- README.md
|-- requirements.txt
|-- .gitignore

## Requirements:

1. Python 3.10 or higher
2. pip
3. Internet connection for API requests
Setup Instructions
1. Clone the repository using the following command:

git clone YOUR_GITHUB_REPOSITORY_URL

2. Enter the project directory:

cd ai-intern-assignment

3. Create a virtual environment:

python -m venv .venv

4. Activate the virtual environment:

source .venv/bin/activate

5. Install the required dependencies:

python -m pip install -r requirements.txt

Running the Project
Part 1: Data Cleaning and NLP
Run the following command:

python task1_nlp_cleaner.py

This script performs the following operations:
1. Removes duplicate ticket IDs while keeping the first occurrence.
2. Rejects invalid or empty queries.
3. Removes HTML tags and surrounding whitespace.
4. Converts text to lowercase and removes punctuation.
5. Tokenizes text and removes common English stop words.
6. Counts tickets by category.
7. Extracts the five most frequent keywords.
8. Saves processed records to data/cleaned_tickets.json.

Part 2: API Integration

Run the following command:

python task2_api_client.py

This script performs the following operations:
1. Fetches posts from JSONPlaceholder.
2. Retrieves the first five posts.
3. Transforms the response into structured documents.
4. Handles timeout, connection, and HTTP errors.
5. Uses mock documents when the API request fails.
Assumptions and Challenges
1. The first occurrence of a duplicate ticket ID is retained.
2. Tickets with null, empty, or whitespace only queries are rejected.
3. English stop words are removed using a predefined list.
4. The API is expected to return JSON data in the documented format.
5. If the API is unavailable, predefined mock documents are used.
6. An internet connection is required for successful live API requests.

Assignment Answers:

Refer to ANSWERS.md for explanations covering HR chatbot prompt engineering, temperature and top p, RAG chunking and embeddings, and prompt injection prevention.

## Submitted by : Sujan Pokhrel
