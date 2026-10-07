"""
Outreach & Instant Lead Handoff Engine (100% Telegram-Free)
Handles outbound outreach and triggers WhatsApp click-to-chat links mapped to Manish (+918299206433).
"""
import logging
from config import MANISH_PHONE_NUMBER

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class OutreachNotifier:
    def __init__(self, owner_phone=MANISH_PHONE_NUMBER):
        self.owner_phone = owner_phone

    def trigger_hot_lead_alert(self, lead_info, client_reply):
        """
        Triggers an instant Hot Lead hand-off alert with WhatsApp direct click-to-chat link for Manish.
        """
        client_phone = lead_info.get('phone', 'N/A')
        clean_client_phone = ''.join(filter(str.isdigit, str(client_phone)))

        wa_direct_link = f"https://wa.me/{clean_client_phone}?text=Namaste%20{lead_info.get('name')}%20ji,%20Aapne%20website%20ke%20liye%20contact%20kiya%20tha."

        logging.info(f"\n==================================================================")
        logging.info(f"🔥 HOT LEAD ALERT FOR MANISH ({self.owner_phone}) 🔥")
        logging.info(f"🏢 Business: {lead_info.get('name')}")
        logging.info(f"📍 City: {lead_info.get('city')}")
        logging.info(f"📞 Client Phone: {client_phone}")
        logging.info(f"💬 Client Said: '{client_reply}'")
        logging.info(f"👉 Direct WhatsApp Link: {wa_direct_link}")
        logging.info(f"==================================================================\n")

        return wa_direct_link

    def process_incoming_reply(self, lead_info, reply_text):
        """
        Detects if client is positive/interested. If yes, alerts Manish (+918299206433) and ends automated sequence.
        """
        positive_keywords = ["yes", "call", "interested", "ha", "haan", "batao", "price", "kitna", "details", "contact", "sample"]
        reply_lower = reply_text.lower()
        if any(keyword in reply_lower for keyword in positive_keywords):
            logging.info(f"🎉 Lead '{lead_info.get('name')}' is INTERESTED! Triggering handoff to Manish...")
            self.trigger_hot_lead_alert(lead_info, reply_text)
            return True
        return False

if __name__ == "__main__":
    notifier = OutreachNotifier()
    print(f"OutreachNotifier ready for Manish ({notifier.owner_phone}).")
