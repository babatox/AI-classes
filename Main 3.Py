
import datetime

def analyze_sentiment(text):
    blob = ("text")
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "POSITIVE"
        mission_status = "Mission Accomplished ✅"
        intel = "Target mood is optimistic and cooperative."
    elif polarity < -0.2:
        sentiment = "NEGATIVE"
        mission_status = "Mission Compromised ⚠️"
        intel = "Target mood is hostile or distressed."
    else:
        sentiment = "NEUTRAL"
        mission_status = "Mission Inconclusive 🕵️"
        intel = "Target mood is ambiguous or reserved."

    return {
        "Sentiment": sentiment,
        "Polarity Score": round(polarity, 2),
        "Mission Status": mission_status,
        "Intel Summary": intel
    }

def generate_report(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = analyze_sentiment(text)

    print("\n🛰️ SENTIMENT SPY: MISSION REPORT 🛰️")
    print(f"Timestamp: {timestamp}")
    print(f"Analyzed Text: \"{text}\"")
    print(f"Sentiment Detected: {result['Sentiment']}")
    print(f"Polarity Score: {result['Polarity Score']}")
    print(f"Mission Status: {result['Mission Status']}")
    print(f"Intel Summary: {result['Intel Summary']}")
    print("--------------------------------------------------")

# Example usage
sample_text = input("Enter intercepted message: ")
generate_report(sample_text)
