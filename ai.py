import subprocess

def ask_ai(message):
    result = subprocess.run(
        ["ollama", "run", "qwen3:4b", message],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    if "...done thinking." in output:
        output = output.split("...done thinking.")[-1].strip()

    return output