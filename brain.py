import json


def load_memory():
    with open("memory.json", "r") as file:
        return json.load(file)


def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)


def get_name(memory):
    return memory["name"]


def get_favourite_anime(memory):
    return memory["favourite_anime"]


def save_favourite_anime(memory, anime):
    memory["favourite_anime"] = anime
    save_memory(memory)


def remember(memory, fact):
    memory["memories"].append(fact)
    save_memory(memory)


def get_memories(memory):
    return memory["memories"]