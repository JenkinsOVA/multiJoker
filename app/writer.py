def save_joke(joke, file_path="joke.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(joke)
