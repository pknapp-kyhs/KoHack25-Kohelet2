
import time

class InteractiveCommentSystem:
    def __init__(self):
        self.comments = []  # Stores comments as a list of dictionaries

    def display_comments(self):
        """Displays all comments in real time."""
        print("\n=== Comment Section ===")
        if not self.comments:
            print("No comments yet. Be the first to comment!")
        else:
            for idx, comment in enumerate(self.comments, start=1):
                print(f"{idx}. {comment['username']} - {comment['text']} ({comment['timestamp']})")
        print("========================\n")

    def add_comment(self):
        """Allows the user to enter a comment dynamically."""
        username = input("Enter your name: ").strip()
        if not username:
            print("Username cannot be empty.")
            return

        text = input("Enter your comment: ").strip()
        if not text:
            print("Comment cannot be empty.")
            return

        comment = {
            "username": username,
            "text": text,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")  # Adds a timestamp
        }

        self.comments.append(comment)
        print("\n✅ Comment added successfully!\n")
        self.display_comments()  # Show updated comments in real time

    def start(self):
        """Runs the interactive comment system."""
        print("💬 Welcome to the Interactive Comment System!")
        while True:
            print("\nOptions: [1] Add Comment  [2] View Comments  [3] Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_comment()
            elif choice == "2":
                self.display_comments()
            elif choice == "3":
                print("👋 Exiting comment system. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose 1, 2, or 3.")

# Run the interactive comment system
if __name__ == "__main__":
    system = InteractiveCommentSystem()
    system.start()