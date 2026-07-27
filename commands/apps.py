import subprocess


def handle_app_command(user):
    user = user.lower()

    apps = {
        "chrome": "Google Chrome",
        "vs code": "Visual Studio Code",
        "finder": "Finder",
        "terminal": "Terminal",
        "spotify": "Spotify",
        "notes": "Notes",
        "calculator": "Calculator",
        "safari": "Safari",
    }

    for app, mac_name in apps.items():
        if f"open {app}" in user:
            print(f"Friday: Opening {mac_name}...")
            subprocess.run(["open", "-a", mac_name])
            return True

    return False