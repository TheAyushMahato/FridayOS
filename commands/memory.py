from brain import (
    remember,
    get_memories,
    get_name,
    get_favourite_anime,
    save_favourite_anime,
)


def handle_memory_command(user, memory):
    # Save favourite anime
    if "my favourite anime is" in user.lower():
        anime = user.lower().replace("my favourite anime is", "").strip()

        save_favourite_anime(memory, anime)
        print("Friday: I'll remember that.")
        return True

    # Recall favourite anime
    if "what is my favourite anime" in user.lower():
        print("Friday: Your favourite anime is " + get_favourite_anime(memory))
        return True

    # Recall name
    if "what is my name" in user.lower() or "who am i" in user.lower():
        print("Friday: Your name is " + get_name(memory))
        return True

    # Remember anything
    if "remember that" in user.lower():
        fact = user[14:].strip()

        remember(memory, fact)
        print("Friday: I'll remember that.")
        return True

    # Show memories
    if "what do you remember about me" in user.lower():
        memories = get_memories(memory)

        if len(memories) == 0:
            print("Friday: I don't remember anything yet.")
        else:
            print("Friday: Here's what I remember:")
            for item in memories:
                print("- " + item)

        return True

    return False