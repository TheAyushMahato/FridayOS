import webbrowser
import urllib.parse


def handle_web_command(user):
    user = user.lower()

    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "chatgpt": "https://chat.openai.com",
        "github": "https://github.com",
    }

    # Open websites
    for site, url in websites.items():
        if f"open {site}" in user:
            print(f"Friday: Opening {site.title()}...")
            webbrowser.open(url)
            return True

    # Google Search
    if user.startswith("search "):
        query = user.replace("search", "", 1).strip()

        encoded_query = urllib.parse.quote(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        print(f"Friday: Searching Google for '{query}'...")
        webbrowser.open(url)
        return True

    return False