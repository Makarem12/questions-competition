import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)
        
        # Default values
        amount = 10
        category = None

        # Check for 'amount' parameter
        if 'amount' in query_params:
            try:
                amount = int(query_params['amount'][0])
                if amount > 50:
                    amount = 50  # Cap the amount to the maximum allowed
            except ValueError:
                amount = 10  # Default to 10 if the provided amount is invalid

        # Check for 'category' parameter
        if 'category' in query_params:
            category = query_params['category'][0]

        # Base URL for the trivia API
        url = f"https://opentdb.com/api.php?amount={amount}"
        if category:
            url += f"&category={category}"

        # Fetch questions from the Open Trivia Database API
        response = requests.get(url)
        data = response.json()

        # Construct the response message
        questions = data.get('results', [])
        msg = f"Here are your {len(questions)} questions:\n\n"
        for i, question in enumerate(questions, start=1):
            msg += f"{i}. {question['question']} (Answer: {question['correct_answer']})\n\n"

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(msg.encode())

        return
