from app.fetcher import get_random_joke
from app.writer import save_joke

def main():
    joke = get_random_joke()
    print("Joke fetched:", joke)
    save_joke(joke)
    print("Joke saved to file.")

if __name__ == "__main__":
    print("skaltuch was here")
    main()
    
