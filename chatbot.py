
import re
from datetime import datetime


# -----------------------------
# Customer Service Chatbot
# -----------------------------

def get_response(user_input):
    """
    Generate a response based on keywords
    found in the user's message.
    """

    text = user_input.lower().strip()

    # Greeting
    if re.search(r"\b(hi|hello|hey|good morning|good afternoon)\b", text):
        return (
            "Hello! 👋 Welcome to Customer Service. "
            "How can I help you today?"
        )

    # Order status
    elif any(word in text for word in ["order status", "track order", "where is my order", "tracking"]):
        return (
            "You can track your order using the tracking number "
            "provided in your order confirmation email."
        )

    # Shipping
    elif any(word in text for word in ["shipping", "delivery", "deliver"]):
        return (
            "Standard shipping usually takes 3–5 business days. "
            "Express shipping usually takes 1–2 business days."
        )

    # Refund
    elif any(word in text for word in ["refund", "money back", "reimburse"]):
        return (
            "Refunds are generally processed within 5–7 business days "
            "after your return has been approved."
        )

    # Return
    elif any(word in text for word in ["return", "send back", "exchange"]):
        return (
            "You can request a return within 30 days of receiving your order. "
            "Please make sure the product is in its original condition."
        )

    # Opening hours
    elif any(word in text for word in ["hours", "open", "close", "working time"]):
        return (
            "Our customer service team is available Monday–Friday, "
            "9:00 AM–6:00 PM."
        )

    # Payment
    elif any(word in text for word in ["payment", "pay", "credit card", "debit card"]):
        return (
            "We accept major credit cards, debit cards, and online payments."
        )

    # Cancel order
    elif any(word in text for word in ["cancel order", "cancel my order", "cancel"]):
        return (
            "If your order has not been shipped yet, you may be able to cancel it. "
            "Please provide your order number to customer support."
        )

    # Contact support
    elif any(word in text for word in ["contact", "support", "agent", "representative"]):
        return (
            "You can contact our support team at support@example.com "
            "or call 1800-123-456."
        )

    # Thank you
    elif any(word in text for word in ["thank you", "thanks", "thank"]):
        return (
            "You're welcome! 😊 Is there anything else I can help you with?"
        )

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        return (
            "Thank you for contacting Customer Service. "
            "Have a great day! 👋"
        )

    # Default response
    else:
        return (
            "I'm sorry, I didn't understand your question. "
            "You can ask me about orders, shipping, returns, refunds, "
            "payments, or customer support."
        )


def chatbot():
    """Run the chatbot."""

    print("=" * 50)
    print("       CUSTOMER SERVICE CHATBOT")
    print("=" * 50)
    print("Type 'bye' or 'exit' to end the conversation.\n")

    print("Bot: Hello! 👋 How can I help you today?")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type a question.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        # End conversation
        if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
            break


# Start chatbot
if __name__ == "__main__":
    chatbot()
