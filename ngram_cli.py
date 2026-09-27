# ====================================================================
# Name: ngram_cli.py
# Description: Simple program to demonstrate n-gram concept
# Author: Aaran Rajadurai
# Date: 20260208
# ====================================================================

import random
import math


END_TOKEN = "<END>"
DEFAULT_FILE_PATH = "data/alice-in-wonderland.txt"
PUNCTUATION_END = [".", "!", "?", ";"]
PUNCTUATION_DELETE = [",", "_", "“", "”", "(", ")", ":", "-"]


# =========================
# TASK 1: File reading
# =========================
def read_file(path):
    read_path = open(path, "rt")
    contents = read_path.read()
    read_path.close()
    return contents
    # """
    # Parameters:
    #     path (str): file path to read
    # Returns:
    #     text (str): entire contents of the file as a
    #     single string
    # """
    # TODO: implement
    # pass


# =========================
# TASK 2: Tokenisation
# =========================
def tokenize(text, end_token=END_TOKEN):
    tokens = []
    word = ""
    
    for letter in text:
        # print("[" + letter + "]")
        
        if letter.isalpha() or letter == "'" or letter == "’":
            word = word + letter.lower()
            

        elif letter in PUNCTUATION_END:
            if word != "":
                tokens.append(word)
                tokens.append(end_token)
                word = ""
                
        elif letter in PUNCTUATION_DELETE:
            continue
            
        elif word != "":
            # print("{" + word + "}")
            tokens.append(word)
            word = ""

    if word != "":
        tokens.append(word)
    
    return tokens
                
    # """
    # Parameters:
    #     text (str): raw text from the book
    #     end_token (str): token to use for sentence
    #     endings, default "<END>"
    # Returns:
    #     tokens (list of str): tokenised text

    # Token rules:
    #   - lowercase
    #   - replace . ! ? with end_token
    #   - keep letters a-z and apostrophe '
    #   - everything else becomes spaces
    #   - split on whitespace
    #   - remove empty tokens
    # """
    # TODO: implement
    # pass


# =========================
# TASK 3: Build n-gram model
# =========================
def build_ngram_model(tokens, n):
    model = {}
    for seed in range(0, len(tokens) - n + 1):
        token = tuple(tokens[seed:seed + n - 1])
        if '<END>' not in token:
            if (token not in model):
                model[token] = {}
            # print(f"seed {seed}")
            following_token = tokens[seed + n - 1]
                    # print(f"following_token {following_token}")
                    # print(f"Tokens[seed] {tokens[seed]}")
            if following_token not in model[token]:
                model[token][following_token] = 0
            model[token][following_token] += 1
                    
    return(model)

    # """
    # Parameters:
    #     tokens (list of str): token list from tokenize()
    #     n (int): size of n-gram, e.g. 2=bigram, 3=trigram
    # Returns:
    #     model (dict):
    #         key: state (tuple of n-1 tokens)
    #         value: dict of { next_token: count }

    # Example (n=3):
    #     state = ("alice", "was")
    #     model[state] might be {"beginning": 2, "not": 1,
    #    "<END>": 1}
    # """
    # TODO: implement
    # pass


# =========================
# TASK 4: Weighted choice
# =========================
def weighted_choice(next_counts, temperature):
    # print(next_counts)
    for word_token, word_weight in next_counts.items():
        word_weight = math.exp(math.log(word_weight) / temperature)
    total_count = sum(next_counts.values())
    # print(total_count)
    choice = random.uniform(1, total_count+1)
    # print(choice)
    next_word = ""
    remainder = choice
    for word, count in next_counts.items():
        remainder = remainder - count
        # print(remainder)
        if remainder <= 0:
            # print(word)
            next_word = word
            break
    print(next_word)
    return next_word
    
    
    
    # """
    # Parameters:
    #     next_counts (dict): {token: count}
    # Returns:
    #     chosen_token (str): randomly chosen based on
    #     weights

    # Example:
    #   {"cat": 10, "dog": 2} should pick "cat" about 5x
    #   more than "dog".
    # """
    # TODO: implement
    # pass


# =========================
# TASK 5: Choose start state
# =========================
def choose_start_state(model, seed_tokens, n):
    token = ""
    # print(f"seed_tokens: {seed_tokens}")
    
    words = seed_tokens.lower().split()
    if len(words) == n-1:
        # print(words)
        token = tuple(words)
        # print(token)
    else:
        print("Error: invalid number of seed words")
    return token
    
    # """
    # Parameters:
    #     model (dict): trained n-gram model
    #     seed_tokens (list of str): tokenised seed words
    #     n (int): n-gram size
    # Returns:
    #     state (tuple): a valid starting state (length
    #     n-1)

    # Rules:
    #   1) If seed_tokens has >= n-1 tokens, try using the
    #      LAST n-1 as the state.
    #   2) Else if seed_tokens has at least 1 token, find
    #      states that start with seed_tokens[0].
    #   3) Else choose a random state from model.
    # """
    # TODO: implement
    # pass


# =========================
# TASK 6: Generate sentence
# =========================
def generate_sentence(model, n, seed_text, temperature, max_words = 25, end_token=END_TOKEN):
    # print(model)
    sentence = seed_text
    for word_count in range(n, max_words):
        new_seed = sentence.split()
        # print(f"length of new_seed: {len(new_seed)}")
        new_seed = new_seed[len(new_seed) - n + 1:]
        # print(f"new_seed: {new_seed}")
        seed_token = choose_start_state(model, " ".join(new_seed), n)
        if seed_token != "":
            # print(seed_token)
            if seed_token in model:
                next_word = weighted_choice(next_counts = model[seed_token], temperature = temperature)
                sentence = sentence + " " + next_word
                if next_word == end_token:
                    break
            else:
                sentence = sentence + " " + end_token
                break
        else:
            sentence = ""
            break
    
        
    return sentence
            

    
    # """
    # Parameters:
    #     model (dict): trained model
    #     n (int): n-gram size used to train
    #     seed_text (str): user input seed, e.g. "alice"
    #     or "alice was"
    #     max_words (int): max words to generate
    #     end_token (str): "<END>" token
    # Returns:
    #     sentence (str): generated sentence

    # Stop generating when:
    #   - next token is end_token, OR
    #   - max_words reached, OR
    #   - the state has no next words
    # """
    # TODO: implement
    # pass


# =========================
# Console UI helpers
# =========================
def print_menu():
    print("\n=== N-Gram Text Generator ===")
    print("1) Train model")
    print("2) Generate sentence")
    print("3) Show model info")
    print("4) Quit")


def main():
    file_path = DEFAULT_FILE_PATH

    tokens = []
    model = {}
    n = 3
    max_words = 25

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            n_text = input("Choose n (2, 3, 4...): ").strip()
            if n_text.isdigit():
                n = int(n_text)
            else:
                print("Invalid n. Keeping:", n)

            print("Reading:", file_path)
            text = read_file(file_path)
            print("Tokenising...")
            tokens = tokenize(text)
            print("Tokens:", len(tokens))

            print("Building model...")
            model = build_ngram_model(tokens, n)
            print("States:", len(model))
            print("Training complete.")

        elif choice == "2":
            if not model:
                print("Train the model first (option 1).")
                continue

            seed = input("Enter seed word(s): ").strip()
            mw = input("Max words (Enter for default 25): ").strip()
            if mw.isdigit():
                max_words = int(mw)
            temperature = float(input("Temperature: ").strip())

            sentence = generate_sentence(model, n, seed, temperature, max_words)
            if sentence != "":
                print("\nGenerated:")
                print(sentence)

        elif choice == "3":
            print("\n--- Model info ---")
            print("n:", n)
            print("Tokens loaded:", len(tokens))
            print("States:", len(model))
            if model:
                example_state = random.choice(list(model.keys()))
                print("Example state:", example_state)
                next_counts = model[example_state]
                # top 10 next tokens by count
                sorted_next = sorted(next_counts.items(), key=lambda x: x[1], reverse=True)
                print("Top next tokens:")
                for token, count in sorted_next[:10]:
                    print(" ", token, "->", count)

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    if True:
        main()
    else:
        # path = DEFAULT_FILE_PATH
        path = "data/test.txt"
        contents = read_file(path)
        tokenised = tokenize(contents)
        # for token in tokenised:
        #     print(token)
        print(len(tokenised))
        model = build_ngram_model(tokenised, 3)
        # print(model)
        for token in model:
            print(f"token {token}: {model[token]}")
        # next_word = weighted_choice(model[('is', 'a')])
        # print(next_word)
        # token = choose_start_state(model, "is a", 3)
        # print(token)
        sentence = generate_sentence(model=model, n=3, seed_text="is", max_words = 25, end_token=END_TOKEN)
        print(f"sentence: {sentence}")