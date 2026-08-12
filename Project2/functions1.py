def total_messages(chat, original_total, deleted_chat):

    active_count = 0

    for user, msg in chat:

        if msg != "This message was Deleted":
            active_count += 1

    print("\n========== MESSAGE COUNT ==========")
    print("Before deletion:", original_total)
    print("After deletion:", active_count)
    print("Deleted messages:", len(deleted_chat))


def unique_users(chat):

    users = []

    for user, msg in chat:

        if user not in users:
            users.append(user)

    print("\n========== UNIQUE USERS ==========")

    for user in users:
        print("-", user)

    print("Total unique users:", len(users))


def total_words(chat):

    count = 0

    for user, msg in chat:

        if msg != "This message was Deleted":
            count += len(msg.split())

    print("\n========== TOTAL WORDS ==========")
    print("Total words:", count)


def average_words(chat):

    total = 0
    count = 0

    for user, msg in chat:

        if msg != "This message was Deleted":

            total += len(msg.split())
            count += 1

    print("\n========== AVERAGE WORDS ==========")

    if count == 0:

        print("Average words: 0")

    else:

        average = total / count

        print(
            "Average words:",
            round(average, 2)
        )


def longest_message(chat):

    longest = ""
    longest_user = ""

    for user, msg in chat:

        if msg == "This message was Deleted":
            continue

        if len(msg) > len(longest):

            longest = msg
            longest_user = user

    print("\n========== LONGEST MESSAGE ==========")

    if longest == "":

        print("No messages found.")

    else:

        print(f"{longest_user}: {longest}")
        print("Characters:", len(longest))


def most_active_user(chat):

    count = {}

    for user, msg in chat:

        if msg == "This message was Deleted":
            continue

        if user not in count:
            count[user] = 0

        count[user] += 1

    print("\n========== MOST ACTIVE USER ==========")

    if len(count) == 0:

        print("No messages found.")
        return

    active_user = max(
        count,
        key=count.get
    )

    print(
        "Most Active User:",
        active_user
    )

    print(
        "Messages:",
        count[active_user]
    )


def message_count(z):

    user = input("\nEnter user name: ")

    found_user = None

    for name in z:

        if name.lower() == user.lower():

            found_user = name
            break

    if found_user is None:

        print("User not found.")
        return

    count = 0

    for msg in z[found_user]:

        if msg != "This message was Deleted":
            count += 1

    print(
        f"\n{found_user} sent {count} active messages."
    )


def frequent_word(z):

    user = input("\nEnter user name: ")

    found_user = None

    for name in z:

        if name.lower() == user.lower():

            found_user = name
            break

    if found_user is None:

        print("User not found.")
        return

    words = {}

    for msg in z[found_user]:

        if msg == "This message was Deleted":
            continue

        for word in msg.lower().split():

            word = word.strip(".,!?")

            if word == "":
                continue

            if word not in words:
                words[word] = 0

            words[word] += 1

    print(
        "\n========== MOST FREQUENT WORD =========="
    )

    if len(words) == 0:

        print("No words found.")
        return

    most_word = max(
        words,
        key=words.get
    )

    print("User:", found_user)
    print("Word:", most_word)
    print("Count:", words[most_word])


def first_last(z):

    user = input("\nEnter user name: ")

    found_user = None

    for name in z:

        if name.lower() == user.lower():

            found_user = name
            break

    if found_user is None:

        print("User not found.")
        return

    valid_messages = []

    for msg in z[found_user]:

        if msg != "This message was Deleted":

            valid_messages.append(msg)

    print(
        "\n========== FIRST & LAST MESSAGE =========="
    )

    if len(valid_messages) == 0:

        print("No active messages found.")
        return

    print(
        "First message:",
        valid_messages[0]
    )

    print(
        "Last message:",
        valid_messages[-1]
    )


def check_user(users):

    user = input("\nEnter user name: ")

    for name in users:

        if name.lower() == user.lower():

            print(
                f"{name} is present in the chat."
            )

            return

    print(
        f"{user} is not present in the chat."
    )


def repeated_words(chat):

    words = {}

    for user, msg in chat:

        if msg == "This message was Deleted":
            continue

        for word in msg.lower().split():

            word = word.strip(".,!?")

            if word == "":
                continue

            if word not in words:
                words[word] = 0

            words[word] += 1

    print(
        "\n========== REPEATED WORDS =========="
    )

    found = False

    for word, count in words.items():

        if count > 1:

            print(
                f"{word}: {count}"
            )

            found = True

    if not found:

        print("No repeated words found.")


def longest_average(z):

    averages = {}

    for user in z:

        total_words = 0
        count = 0

        for msg in z[user]:

            if msg == "This message was Deleted":
                continue

            total_words += len(msg.split())
            count += 1

        if count > 0:

            averages[user] = (
                total_words / count
            )

    print(
        "\n========== LONGEST AVERAGE MESSAGE =========="
    )

    if len(averages) == 0:

        print("No messages found.")
        return

    user = max(
        averages,
        key=averages.get
    )

    print("User:", user)

    print(
        "Average words:",
        round(averages[user], 2)
    )


def mention_count(chat):

    search_user = input(
        "\nEnter user name to search in messages: "
    )

    count = 0

    print(
        "\n========== MESSAGES =========="
    )

    for sender, msg in chat:

        if msg == "This message was Deleted":
            continue

        if search_user.lower() in msg.lower():

            print(
                f"{sender}: {msg}"
            )

            count += 1

    print(
        f"\nMessages mentioning {search_user}: {count}"
    )


def remove_duplicates(messages):

    unique = []

    for msg in messages:

        if msg not in unique:

            unique.append(msg)

    print(
        "\n========== REMOVE DUPLICATES =========="
    )

    print(
        "Original message count:",
        len(messages)
    )

    print(
        "After removing duplicates:",
        len(unique)
    )

    print("\nUnique messages:")

    for msg in unique:

        print(msg)


def sort_messages(messages):

    active_messages = []

    for msg in messages:

        if msg != "This message was Deleted":

            active_messages.append(msg)

    sorted_messages = sorted(
        active_messages,
        key=len
    )

    print(
        "\n========== SORTED MESSAGES =========="
    )

    for msg in sorted_messages:

        print(msg)


def questions(chat):

    count = 0

    print(
        "\n========== QUESTIONS =========="
    )

    for user, msg in chat:

        if msg == "This message was Deleted":
            continue

        if "?" in msg:

            print(
                f"{user}: {msg}"
            )

            count += 1

    print(
        "\nTotal questions:",
        count
    )


def reply_ratio(chat):

    replies = 0
    active_pairs = 0

    if len(chat) < 2:

        print("\nNot enough messages.")
        return

    for i in range(1, len(chat)):

        previous_user = chat[i - 1][0]
        previous_msg = chat[i - 1][1]

        current_user = chat[i][0]
        current_msg = chat[i][1]

        if previous_msg == "This message was Deleted":
            continue

        if current_msg == "This message was Deleted":
            continue

        active_pairs += 1

        if previous_user != current_user:

            replies += 1

    print(
        "\n========== REPLY RATIO =========="
    )

    if active_pairs == 0:

        print("Reply messages: 0")
        print("Reply ratio: 0.0 %")

        return

    ratio = (
        replies / active_pairs
    ) * 100

    print(
        "Reply messages:",
        replies
    )

    print(
        "Reply ratio:",
        round(ratio, 2),
        "%"
    )


def deleted_messages(deleted_chat):

    print(
        "\n========== DELETED MESSAGES =========="
    )

    if len(deleted_chat) == 0:

        print("No deleted messages found.")

        return

    for item in deleted_chat:

        user = item[0]
        msg = item[1]

        print(
            f"{user}: {msg}"
        )

    print(
        "\nDeleted messages found:",
        len(deleted_chat)
    )


def display_chat(chat):

    print(
        "\n===================================="
    )

    print(
        "             CHAT DATA"
    )

    print(
        "===================================="
    )

    for user, msg in chat:

        print(
            f"{user}: {msg}"
        )
def delete_message(chat, users, deleted_chat):

    print("\n========== DELETE MESSAGE ==========")

    duser = input("Enter user name: ")

    found_user = None

    for user in users:

        if user.lower() == duser.lower():
            found_user = user
            break

    if found_user is None:

        print("User not found.")
        return

    duser = found_user

    user_indexes = []
    count = 0

    print(f"\nMessages of {duser}:")

    for i in range(len(chat)):

        if chat[i][0] == duser:

            count += 1
            user_indexes.append(i)

            print(
                f"{count}. {chat[i][1]}"
            )

    if count == 0:

        print("No messages found.")
        return

    try:

        d = int(
            input(
                "Enter message number to delete: "
            )
        )

    except ValueError:

        print("Enter a valid number.")
        return

    if d < 1 or d > count:

        print("Invalid message number.")
        return

    actual_index = user_indexes[d - 1]

    old_message = chat[actual_index][1]

    if old_message == "This message was Deleted":

        print("Message already deleted.")
        return

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

    print("\nMessage deleted successfully.")
def replace_message(chat, users, deleted_chat):

    print("\n========== REPLACE MESSAGE ==========")

    ruser = input("Enter user name: ")

    found_user = None

    for user in users:

        if user.lower() == ruser.lower():
            found_user = user
            break

    if found_user is None:

        print("User not found.")
        return

    ruser = found_user

    user_indexes = []
    count = 0

    print(f"\nMessages of {ruser}:")

    for i in range(len(chat)):

        if chat[i][0] == ruser:

            # Don't show deleted messages
            if chat[i][1] == "This message was Deleted":
                continue

            count += 1
            user_indexes.append(i)

            print(
                f"{count}. {chat[i][1]}"
            )

    if count == 0:

        print("No active messages available to replace.")
        return

    try:

        r = int(
            input(
                "Enter message number to replace: "
            )
        )

    except ValueError:

        print("Enter a valid number.")
        return

    if r < 1 or r > count:

        print("Invalid message number.")
        return

    actual_index = user_indexes[r - 1]

    old_message = chat[actual_index][1]

    new_message = input(
        "Enter new message: "
    )

    chat[actual_index] = (
        ruser,
        new_message
    )

    print("\nMessage replaced successfully.")
    print("Old message:", old_message)
    print("New message:", new_message)