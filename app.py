from flask import Flask

app = Flask(__name__)

# The complete HTML for the page is stored in this multiline string.
# It includes your specific Vertex AI agent details.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Buddy</title>

    <!-- Dialogflow Messenger scripts and styles -->
    <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
    <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>

    <style>
      /* Basic styles for the page content */
      body {
        font-family: 'Google Sans', sans-serif;
        margin: 0;
        padding: 2em;
        background-color: #f8f9fa;
        color: #3c4043;
      }
      h1 {
        color: #1a73e8;
      }
      p {
        font-size: 1.1em;
        line-height: 1.6;
      }

      /* Styles for the Dialogflow Messenger chat widget */
      df-messenger {
        z-index: 999;
        position: fixed;
        bottom: 16px;
        right: 16px;
        --df-messenger-font-color: #000;
        --df-messenger-font-family: Google Sans;
        --df-messenger-chat-background: #f3f6fc;
        --df-messenger-message-user-background: #d3e3fd;
        --df-messenger-message-bot-background: #fff;
      }
    </style>
</head>
<body>
    <h1>Welcome to your Travel Buddy!</h1>
    <p>Your personal AI assistant is ready to help you plan your next adventure.</p>
    <p>Click the chat icon in the bottom-right corner to get started.</p>

    <!-- Dialogflow Messenger component with your agent's details -->
    <df-messenger
      location="us-central1"
      project-id="hpgcp-474419"
      agent-id="f738cea0-d361-4c01-af93-a89b112bd137"
      language-code="en"
      max-query-length="-1">
      <df-messenger-chat-bubble
        chat-title="Travel Buddy">
      </df-messenger-chat-bubble>
    </df-messenger>

</body>
</html>
"""

@app.route("/")
def index():
    """Serves the HTML page with the embedded chatbot."""
    return html_content

if __name__ == "__main__":
    # To run this application:
    # 1. Save the code as app.py
    # 2. Install Flask: pip install Flask
    # 3. Run the script: python app.py
    # 4. Open your browser to http://127.0.0.1:8080
    # The port is set to 8080 to match the Dockerfile and Cloud Run's default.
    app.run(host='0.0.0.0', port=8080, debug=True)