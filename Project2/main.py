from functions1 import *


saved_chats = {
    "chat1": {
        "users": ["Alice", "Bob"],
        "messages": [
            ("Alice", "Hello"),
            ("Bob", "Hi Alice"),
            ("Alice", "How are you?"),
            ("Bob", "I am fine"),
            ("Alice", "What are you doing?")
        ]
    },

    "chat2": {
        "users": ["Sai", "Kiran", "Rahul"],
        "messages": [
            ("Sai", "Good morning"),
            ("Kiran", "Good morning Sai"),
            ("Rahul", "How is everyone?"),
            ("Sai", "I am good"),
            ("Kiran", "Let's meet today"),
            ("Rahul", "Sure, what time?")
        ]
    }
}


def build_data(chat, users):

    z = {}
    messages = []

    for user in users:
        z[user] = []

    for user, message in chat:
        z[user].append(message)
        messages.append(message)

    return z, messages


def run_function(choice, chat, users, z, messages,
                 original_total, deleted_chat):

    if choice == 1:
        total_messages(
            chat,
            original_total,
            deleted_chat
        )

    elif choice == 2:
        unique_users(chat)

    elif choice == 3:
        total_words(chat)

    elif choice == 4:
        average_words(chat)

    elif choice == 5:
        longest_message(chat)

    elif choice == 6:
        most_active_user(chat)

    elif choice == 7:
        message_count(z)

    elif choice == 8:
        frequent_word(z)

    elif choice == 9:
        first_last(z)

    elif choice == 10:
        check_user(users)

    elif choice == 11:
        repeated_words(chat)

    elif choice == 12:
        longest_average(z)

    elif choice == 13:
        mention_count(chat)

    elif choice == 14:
        remove_duplicates(messages)

    elif choice == 15:
        sort_messages(messages)

    elif choice == 16:
        questions(chat)

    elif choice == 17:
        reply_ratio(chat)

    elif choice == 18:
        deleted_messages(deleted_chat)


while True:

    print("\n====================================")
    print("        CHAT DATA SELECTION")
    print("====================================")
    print("1. Use Saved Dictionary Data")
    print("2. Enter Data Manually")
    print("3. Exit")

    try:
        data_choice = int(
            input("Enter your choice (1-3): ")
        )
    except ValueError:
        print("Enter a valid number.")
        continue

    if data_choice == 3:
        print("Thank You!")
        exit()

    elif data_choice == 1:

        chat_names = list(saved_chats.keys())

        print("\n========== AVAILABLE CHATS ==========")

        for i in range(len(chat_names)):
            print(
                f"{i + 1}. {chat_names[i]}"
            )

        print(
            f"{len(chat_names) + 1}. Back"
        )

        try:
            chat_choice = int(
                input("Select Chat: ")
            )
        except ValueError:
            print("Enter a valid number.")
            continue

        if chat_choice == len(chat_names) + 1:
            continue

        if chat_choice < 1 or chat_choice > len(chat_names):
            print("Invalid Chat.")
            continue

        selected_chat_name = (
            chat_names[chat_choice - 1]
        )

        selected_chat = saved_chats[
            selected_chat_name
        ]

        users = selected_chat["users"].copy()
        chat = selected_chat["messages"].copy()

        original_total = len(chat)

        deleted_chat = []

        while True:

            print("\n====================================")
            print("           SAVED CHAT")
            print("====================================")

            print("\nUsers:")

            for user in users:
                print("-", user)

            print("\nMessages:")

            for user, msg in chat:
                print(f"{user}: {msg}")

            print("\n====================================")
            print("       SAVED CHAT OPTIONS")
            print("====================================")
            print("1. Delete Message")
            print("2. Replace Message")
            print("3. Continue")

            try:
                option = int(
                    input("\nEnter option (1-3): ")
                )
            except ValueError:
                print("Enter a valid number.")
                continue

            if option == 1:

                print(
                    "\n========== DELETE MESSAGE =========="
                )

                duser = input(
                    "Enter user name: "
                )

                found_user = None

                for user in users:
                    if user.lower() == duser.lower():
                        found_user = user
                        break

                if found_user is None:
                    print("User not found.")
                    continue

                duser = found_user

                user_indexes = []
                count = 0

                print(
                    f"\nMessages of {duser}:"
                )

                for i in range(len(chat)):

                    if chat[i][0] == duser:

                        count += 1
                        user_indexes.append(i)

                        print(
                            f"{count}. {chat[i][1]}"
                        )

                if count == 0:
                    print("No messages found.")
                    continue

                try:
                    d = int(
                        input(
                            "\nEnter message number to delete: "
                        )
                    )
                except ValueError:
                    print("Enter a valid number.")
                    continue

                if d < 1 or d > count:
                    print("Invalid message number.")
                    continue

                actual_index = user_indexes[d - 1]
                old_message = chat[actual_index][1]

                if old_message == "This message was Deleted":
                    print(
                        "This message is already deleted."
                    )
                    continue

                deleted_chat.append(
                    (
                        duser,
                        old_message,
                        actual_index
                    )
                )

                chat[actual_index] = (
                    duser,
                    "This message was Deleted"
                )

                selected_chat["messages"] = chat.copy()

                print(
                    "\nMessage deleted successfully."
                )

            elif option == 2:

                print(
                    "\n========== REPLACE MESSAGE =========="
                )

                ruser = input(
                    "Enter user name: "
                )

                found_user = None

                for user in users:
                    if user.lower() == ruser.lower():
                        found_user = user
                        break

                if found_user is None:
                    print("User not found.")
                    continue

                ruser = found_user

                user_indexes = []
                count = 0

                print(
                    f"\nMessages of {ruser}:"
                )

                for i in range(len(chat)):

                    if chat[i][0] == ruser:

                        count += 1
                        user_indexes.append(i)

                        print(
                            f"{count}. {chat[i][1]}"
                        )

                if count == 0:
                    print("No messages found.")
                    continue

                try:
                    r = int(
                        input(
                            "\nEnter message number to replace: "
                        )
                    )
                except ValueError:
                    print("Enter a valid number.")
                    continue

                if r < 1 or r > count:
                    print("Invalid message number.")
                    continue

                actual_index = user_indexes[r - 1]
                old_message = chat[actual_index][1]

                new_message = input(
                    "Enter new message: "
                )

                chat[actual_index] = (
                    ruser,
                    new_message
                )

                if old_message == "This message was Deleted":

                    for i in range(
                        len(deleted_chat) - 1,
                        -1,
                        -1
                    ):

                        if deleted_chat[i][2] == actual_index:
                            del deleted_chat[i]
                            break

                selected_chat["messages"] = chat.copy()

                print(
                    "\nMessage replaced successfully."
                )
                print("Old message:", old_message)
                print("New message:", new_message)

            elif option == 3:
                break

            else:
                print("Invalid Option.")

        z, messages = build_data(
            chat,
            users
        )

        break

    elif data_choice == 2:

        try:
            n = int(
                input(
                    "\nEnter Number of Messages: "
                )
            )

            a = int(
                input(
                    "Enter Number of Users: "
                )
            )

        except ValueError:
            print("Enter valid numbers.")
            continue

        users = []

        for i in range(a):

            while True:

                name = input(
                    f"Enter user {i + 1} name: "
                )

                if name == "":
                    print(
                        "User name cannot be empty."
                    )
                    continue

                duplicate = False

                for old_name in users:

                    if old_name.lower() == name.lower():
                        duplicate = True
                        break

                if duplicate:
                    print(
                        "User already exists."
                    )
                else:
                    users.append(name)
                    break

        chat = []

        for i in range(n):

            while True:

                user = input(
                    f"\nChoose User for Message {i + 1}: "
                )

                found_user = None

                for name in users:

                    if name.lower() == user.lower():
                        found_user = name
                        break

                if found_user is None:
                    print("Invalid User.")
                    continue

                message = input(
                    f"Enter Message {found_user}: "
                )

                chat.append(
                    (
                        found_user,
                        message
                    )
                )

                break

        original_total = len(chat)
        deleted_chat = []

        z, messages = build_data(
            chat,
            users
        )

        break

    else:
        print("Invalid Choice.")


print("\n====================================")
print("          FINAL CHAT DATA")
print("====================================")

print("\nUsers:")

for user in users:
    print("-", user)

print("\nMessages:")

for user, msg in chat:
    print(f"{user}: {msg}")


while True:

    print("\n====================================")
    print("       CHAT ANALYSIS MENU")
    print("====================================")

    print("1. Total Messages")
    print("2. Unique Users")
    print("3. Total Words")
    print("4. Average Words")
    print("5. Longest Message")
    print("6. Most Active User")
    print("7. Message Count of User")
    print("8. Most Frequent Word by User")
    print("9. First & Last Message")
    print("10. Check User")
    print("11. Repeated Words")
    print("12. Longest Average Message")
    print("13. Messages Mentioning User")
    print("14. Remove Duplicate Messages")
    print("15. Sort Messages")
    print("16. Extract Questions")
    print("17. Reply Ratio")
    print("18. Deleted Messages")
    print("19. Exit")

    try:
        choice = int(
            input(
                "\nEnter your choice (1-19): "
            )
        )
    except ValueError:
        print("Enter a valid number.")
        continue

    if choice == 19:
        print("\nThank You!")
        break

    if choice < 1 or choice > 18:
        print("Invalid Choice!")
        continue

    run_function(
        choice,
        chat,
        users,
        z,
        messages,
        original_total,
        deleted_chat
    )

    while True:

        print()
        print("1. Continue same function")
        print("2. Display Chat")
        print("3. Edit Chat")
        print("4. Back to Functions Options")
        print("5. Exit")

        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Enter 1, 2, 3, 4 or 5.")
            continue

        # 1. Continue same function
        if option == 1:

            run_function(
                choice,
                chat,
                users,
                z,
                messages,
                original_total,
                deleted_chat
            )

        # 2. Display Chat
        elif option == 2:

            display_chat(chat)

        # 3. Edit Chat
        elif option == 3:

            while True:

                print("\n========== EDIT CHAT ==========")
                print("1. Delete Message")
                print("2. Replace Message")
                print("3. Back")

                try:
                    edit_choice = int(
                        input("Enter option: ")
                    )
                except ValueError:
                    print("Enter 1, 2 or 3.")
                    continue

                if edit_choice == 1:

                    delete_message(
                        chat,
                        users,
                        deleted_chat
                    )

                    z, messages = build_data(
                        chat,
                        users
                    )

                elif edit_choice == 2:

                    replace_message(
                        chat,
                        users,
                        deleted_chat
                    )

                    z, messages = build_data(
                        chat,
                        users
                    )

                elif edit_choice == 3:

                    break

                else:

                    print("Invalid option.")

        # 4. Back to Functions Options
        elif option == 4:

            break

        # 5. Exit
        elif option == 5:

            print("\nThank You!")
            exit()

        else:

            print("Invalid option.")