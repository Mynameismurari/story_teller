import random

# Define lists of possible genres, themes, and character types
genres = [
    "Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", 
    "Adventure", "Historical Fiction", "Thriller", "Comedy", "Drama"
]

themes = [
    "Redemption", "Love and Loss", "Identity", "Power and Corruption", 
    "Exploration", "Survival", "Betrayal", "Growth", "Justice", "Freedom"
]

character_types = [
    "A young orphan", "A seasoned detective", "A powerful sorcerer", 
    "A rebellious teenager", "An alien explorer", "A time-traveling historian", 
    "A cunning thief", "A wise mentor", "A misunderstood villain", "A heroic warrior"
]

# Function to generate a story idea
def generate_story_idea(genre, theme, character):
    # Templates for combining inputs into a coherent prompt
    templates = [
        f"In a world of {genre.lower()}, {character.lower()} embarks on a journey centered around the theme of {theme.lower()}. What challenges will they face, and how will they change?",
        f"Write a story in the {genre} genre where {character.lower()} grapples with {theme.lower()}. Explore the conflicts and resolutions that arise.",
        f"Imagine {character.lower()} in a {genre.lower()} setting, dealing with the theme of {theme.lower()}. Craft a narrative that builds tension and leads to a surprising twist.",
        f"Create a tale where {character.lower()} navigates {theme.lower()} within the realm of {genre.lower()}. How do their actions shape the world around them?"
    ]
    
    # Randomly select a template
    selected_template = random.choice(templates)
    return selected_template

# Main function to run the generator
def main():
    print("Welcome to the Story Idea Generator!")
    print("This tool helps you create creative writing prompts based on your chosen genre, theme, and character type.")
    
    # Ask user for inputs
    print("\nAvailable Genres:", ", ".join(genres))
    genre = input("Choose a genre (or type 'random' for a surprise): ").strip()
    if genre.lower() == 'random':
        genre = random.choice(genres)
    
    print("\nAvailable Themes:", ", ".join(themes))
    theme = input("Choose a theme (or type 'random' for a surprise): ").strip()
    if theme.lower() == 'random':
        theme = random.choice(themes)
    
    print("\nAvailable Character Types:", ", ".join(character_types))
    character = input("Choose a character type (or type 'random' for a surprise): ").strip()
    if character.lower() == 'random':
        character = random.choice(character_types)
    
    # Generate a collection of prompts (e.g., 3 ideas)
    num_ideas = 3
    print(f"\nGenerating {num_ideas} story ideas based on: Genre - {genre}, Theme - {theme}, Character - {character}")
    print("\nHere are your creative writing prompts:")
    
    for i in range(num_ideas):
        idea = generate_story_idea(genre, theme, character)
        print(f"{i+1}. {idea}")
    
    print("\nUse these prompts to inspire your creative writing! Feel free to run the program again for more ideas.")

# Run the program
if __name__ == "__main__":
    main()
