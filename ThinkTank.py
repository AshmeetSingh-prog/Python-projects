import tkinter
import pymysql as m
import threading 

def main():
    while True:
        print("\n===== QUESTION DATABASE MENU =====")
        print("1. Add Question")
        print("2. View All Questions")
        print("3. Update Question")
        print("4. Delete Question")
        print("5. Display all users")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_question()
        elif choice == '2':
            view_questions()
        elif choice == '3':
            update_question()
        elif choice == '4':
            delete_question()
        elif choice == "5":
            display_all_users()
        elif choice == '6':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Try again!")
def create_database_and_table():
    try:
        
        connection = m.connect(
            host='localhost',      
            user='root',           
            password='admin1234', 
            cursorclass=m.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            # Create database if not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS MindMM12")
            print("Database 'MindMM12' created or already exists.")

            # Select the database
            cursor.execute("USE MindMM12")

            # Create table if not exists
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT PRIMARY KEY,
                name VARCHAR(100),
                score INT DEFAULT 0
            )
            """
            cursor.execute(create_table_sql)
            print("Table 'users' created or already exists.")
        
        connection.commit()

    except m.MySQLError as e:
        print(f"MySQL Error: {e}")
    finally:
        connection.close()


# Call the function to create the database and table
create_database_and_table()

root = tkinter.Tk()
root.geometry("850x650")
root.configure(bg="#FFFFE0")
root.title("Student Form")

# Role flags
admin_role = False
user_role = False
all_user_details = False
questions = []
hints= []
options = []
answers = []
current_question_index = 0
score = 0
hint_used = 0

# Connect to MySQL
def get_connection():
    return m.connect(host="localhost", user="root", password="admin1234", database="MindMM12")

# Clear all widgets from root
def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

# Set admin role
def set_admin():
    global admin_role, user_role
    admin_role = True
    user_role = False
    print("Admin selected:", admin_role, user_role)

# Set user role
def set_user():
    global admin_role, user_role
    admin_role = False
    user_role = True
    print("admin : ", admin_role, "user : ", user_role)

def insert_user(user_id, name):
    try:
        con = get_connection()
        cur = con.cursor()
        query = "INSERT INTO users (user_id, name) VALUES ({},'{}')".format(user_id,name)
        cur.execute(query)
        con.commit()
        con.close()
        print("User inserted successfully.")
        return True

    except Exception as e:
        print("Insert error: {}".format(e))
        return False
    
def id_exists(user_id):
    try:
        con = get_connection()
        cur = con.cursor()

        query = "SELECT * FROM users WHERE user_id = {}".format(user_id)
        cur.execute(query)
        
        result = cur.fetchone()
        con.close()
        
        return result is not None

    except Exception as e:
        print("Database error: {}".format(e))
        return False


# Show second screen for user input
name_user=""
id_user=""
def show_user_screen():
    def validate_user_input():
        global all_user_details
        global name_user
        global id_user
        print(all_user_details)
        name_user = name_textbox.get()
        id_user = id_textbox.get()
        valid = True

        if not name_user:
            n_warn_label.config(text="*Required")
            valid = False
        else:
            n_warn_label.config(text="")

        if not id_user:
            i_warn_label.config(text="*Required")
            valid = False
        elif not id_user.isdigit():
            i_warn_label.config(text="*Only numeric ID allowed")
            valid = False
        elif id_exists(id_user):
            i_warn_label.config(text="*ID already registered")
            valid = False
        else:
            i_warn_label.config(text="")

        if valid:
            print("Name Entered:", name_user)
            print("ID Entered:", id_user)
            insert_user(id_user,name_user)
            all_user_details = True
            print(all_user_details)
            name_textbox.delete(0, tkinter.END)
            id_textbox.delete(0, tkinter.END)
            """Third Screen - USer Questions """
            ques_screen()

    name_label = tkinter.Label(root, text="Enter name", font=("nyala", 20), bg="#FFFFE0")
    name_label.pack(anchor=tkinter.W, padx=20, pady=(20, 0))

    name_frame = tkinter.Frame(root, bg="#FFFFE0")
    name_frame.pack(anchor=tkinter.W, padx=20, pady=(10, 20))

    name_textbox = tkinter.Entry(name_frame, font=("aerial", 20))
    name_textbox.pack(side=tkinter.LEFT)

    n_warn_label = tkinter.Label(name_frame, text="", fg="red", bg="#FFFFE0", font=("aerial", 20))
    n_warn_label.pack(side=tkinter.LEFT, padx=10)

    id_label = tkinter.Label(root, text="Enter ID", font=("nyala", 20), bg="#FFFFE0")
    id_label.pack(anchor=tkinter.W, padx=20, pady=(20, 0))

    id_frame = tkinter.Frame(root, bg="#FFFFE0")
    id_frame.pack(anchor=tkinter.W, padx=20, pady=(10, 20))

    id_textbox = tkinter.Entry(id_frame, font=("aerial", 20))
    id_textbox.pack(side=tkinter.LEFT)

    i_warn_label = tkinter.Label(id_frame, text="", fg="red", bg="#FFFFE0", font=("aerial", 20))
    i_warn_label.pack(side=tkinter.LEFT, padx=10)

    # Instructions for the MindMM12
    inst0_label = tkinter.Label(root, text="""📝 Instructions:
- The Quiz contains 20 questions in total.
- Difficulty increases with each question.
- You will get +4 points for every correct answer.
- You will lose 1 point for every wrong answer.
- A total of 5 hints are available for the entire quiz. Use them wisely!
- In the entry box type "hint" and submit to get hint
- Try to score as high as possible. Good luck!""", fg="red", bg="#FFFFE0", font=("aerial", 20), justify=tkinter.LEFT)
    inst0_label.pack(anchor=tkinter.W, padx=20, pady=(10, 20))

    # Submit button
    submit_button = tkinter.Button(root, text="Submit", font=("aerial", 20), command=validate_user_input)
    submit_button.pack(anchor=tkinter.W, padx=20)
    
"""Third Screen - USer Questions """
def create_questions_table():
    try:
        con = get_connection()
        cur = con.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS questions (
            question_id INT PRIMARY KEY AUTO_INCREMENT,
            question_text TEXT NOT NULL,
            option1 VARCHAR(255) NOT NULL,
            option2 VARCHAR(255) NOT NULL,
            option3 VARCHAR(255) NOT NULL,
            option4 VARCHAR(255) NOT NULL,
            correct_option INT NOT NULL,
            hint TEXT
        )
        """
        cur.execute(create_table_sql)
        con.commit()
        print("Table 'questions' created or already exists.")
    except m.MySQLError as e:
        print("MySQL Error:", e)
    finally:
        con.close()
        
def insert_question(question_id, question_text, option1, option2, option3, option4, correct_option, hint):
    try:
        con = m.connect(host='localhost', user='root', password='admin1234', database='MindMM12')
        cur = con.cursor()

        # Check if question already exists
        check_sql = "SELECT COUNT(*) FROM questions WHERE question_id = %s"
        cur.execute(check_sql, (question_id,))
        exists = cur.fetchone()[0]

        if exists:
            print(f"Question with ID {question_id} already exists. Skipping insertion.")
        else:
            insert_sql = """
            INSERT INTO questions (question_id, question_text, option1, option2, option3, option4, correct_option, hint)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(insert_sql, (question_id, question_text, option1, option2, option3, option4, correct_option, hint))
            con.commit()
            print(f"Question {question_id} inserted successfully.")
    except m.MySQLError as e:
        print("Insert error:", e)
def load_questions():
    global questions
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT question_text FROM questions ORDER BY question_id")
        questions = cur.fetchall()
        con.close()
        return questions
    except Exception as e:
        print("Error loading questions:", e)

def load_hints():
    global hints
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT hint FROM questions ORDER BY question_id")
        hints = cur.fetchall()
        con.close()
        return hints
    except Exception as e:
        print("Error loading hints:", e)
        return []
    
def load_options():
    global options
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT option1, option2, option3, option4 FROM questions ORDER BY question_id")
        options = cur.fetchall()
        con.close()
        return options
    except Exception as e:
        print("Error loading options:", e)
        return []
def load_correct_answers():
    global answers
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT correct_option FROM questions ORDER BY question_id")
        answers = cur.fetchall()
        con.close()
        return answers
    except Exception as e:
        print("Error loading correct answers:", e)
        return []

question_label=""
option1_label = ""
option2_label = ""
option3_label = ""
option4_label = ""
answer_entry = ""
w_answer_entry = ""
def ques_screen():
    global all_user_details
    global questions
    global question_label
    global option1_label
    global option2_label
    global option3_label
    global option4_label
    global hints
    global answer_entry
    global w_answer_entry
    global hint_used
    print(all_user_details)
    if all_user_details :
        clear_root(root)
        create_questions_table()
        insert_question(1, "What is the output of: print(2 * 3 + 4)?", "10", "14", "12", "18", 1, "Follow the order of operations (PEMDAS).")

        insert_question(2, "Which of the following is a valid variable name in Python?", "2var", "var_1", "var-2", "var 3", 2, "Variable names cannot start with digits or contain special characters or spaces.")

        insert_question(3, "Which keyword is used to define a function in Python?", "func", "define", "def", "function", 3, "Functions are defined using 'def'.")

        insert_question(4, "What is the result of: len('Hello')?", "5", "4", "6", "None", 1, "Count the number of characters in the string.")

        insert_question(5, "What does the 'range(3)' function return?", "[1, 2,  3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[3, 2, 1]", 2, "range(n) returns numbers from 0 to n-1.")

        insert_question(6, "Which data type is mutable in Python?", "Tuple", "String", "List", "Integer", 3, "Mutable means changeable after creation.")

        insert_question(7, "What is the output of: 'Hello'.lower()?", "hello", "HELLO", "Hello", "error", 1, "The method .lower() converts all characters to lowercase.")

        insert_question(8, "What is the output of: print(3 == 3.0)?", "True", "False", "Error", "None", 1, "Python considers int and float with same value as equal in comparison.")

        insert_question(9, "Which of the following will create a dictionary?", "{}", "[]", "()", "set()", 1, "{} creates an empty dictionary unless context says otherwise.")

        insert_question(10, "What is the correct syntax to import the math module?", "import.math", "include math", "import math", "math import", 3, "Use the 'import module' syntax.")

        insert_question(11, "What is the output of: print(type({1,2,3}))?", "<class 'list'>", "<class 'tuple'>", "<class 'set'>", "<class 'dict'>", 3, "Curly braces with values create a set.")

        insert_question(12, "Which method is used to add an item to a list?", "append()", "add()", "push()", "insert()", 1, "Use list.append() to add to the end.")

        insert_question(13, "Which keyword is used for exception handling?", "try", "catch", "handle", "except", 4, "Python uses 'try' and 'except' blocks.")

        insert_question(14, "What is the output of: bool([])?", "True", "False", "None", "Error", 2, "Empty containers are considered False in boolean context.")

        insert_question(15, "Which of these is used to read a file in Python?", "read()", "input()", "load()", "open()", 4, "Use 'open()' to work with files.")

        insert_question(16, "What will be the result of: 10//3?", "3.33", "3", "4", "Error", 2, "// is floor division.")

        insert_question(17, "Which Python keyword is used for creating a class?", "def", "function", "class", "struct", 3, "Use 'class' to define a class.")

        insert_question(18, "What will be the output of: list('abc')?", "['abc']", "['a','b','c']", "('a','b','c')", "{'a','b','c'}", 2, "list(string) splits it into characters.")

        insert_question(19, "Which module in Python is used for regular expressions?", "re", "regex", "match", "string", 1, "The module is called 're'.")

        insert_question(20, "What is the output of: print({i:i**2 for i in range(3)})?", "{0:0, 1:1, 2:4}", "[0,1,2]", "{0,1,4}", "{0:1,1:2,2:3}", 1, "This is a dictionary comprehension.")
    
        # Question Label
        question_label = tkinter.Label(root, text="Question", font=("Nyala", 20), bg="#FFFFE0", wraplength=800, justify="left")
        question_label.pack(anchor=tkinter.W, padx=30, pady=(30, 20))

        # Option Labels
        option1_label = tkinter.Label(root, text="opt1", font=("Arial", 18), bg="#FFFFE0", anchor="w")
        option1_label.pack(anchor=tkinter.W, padx=50, pady=5)

        option2_label = tkinter.Label(root, text="opt2", font=("Arial", 18), bg="#FFFFE0", anchor="w")
        option2_label.pack(anchor=tkinter.W, padx=50, pady=5)

        option3_label = tkinter.Label(root, text="opt3", font=("Arial", 18), bg="#FFFFE0", anchor="w")
        option3_label.pack(anchor=tkinter.W, padx=50, pady=5)

        option4_label = tkinter.Label(root, text="opt4", font=("Arial", 18), bg="#FFFFE0", anchor="w")
        option4_label.pack(anchor=tkinter.W, padx=50, pady=5)

        # Entry for user's answer
        answer_entry = tkinter.Entry(root, font=("Arial", 18), width=5)
        answer_entry.pack(anchor=tkinter.W, padx=50, pady=(20, 10))
        w_answer_entry = tkinter.Label(root,text="",font=("Arial", 18))
        w_answer_entry.pack(anchor=tkinter.W)
        
        # Submit Button
        """TO remove the error that was coming, see that error after removing this function from here"""
        ques_ans_log()
        submit_button = tkinter.Button(root, text="Submit", font=("Arial", 18), bg="#4CAF50", fg="white",command=ques_ans_log)
        submit_button.pack(anchor=tkinter.W, padx=50, pady=10)
        

def ques_ans_log():
    global questions
    global answers
    global hints
    global options
    global current_question_index
    global score
    global answer_entry
    global w_answer_entry
    global hint_used

    if current_question_index == 0:
        questions = load_questions()
        answers = load_correct_answers()
        options = load_options()
        hints = load_hints()

    if current_question_index < len(questions):
        # Check the previous answer only if it's not the first question
        if current_question_index > 0:
            user_sel_ans = answer_entry.get().strip().lower()

            if user_sel_ans == "hint":
                if hint_used < 5:
                    hint_text = hints[current_question_index - 1][0]
                    print(f"Hint: {hint_text}")
                    w_answer_entry.config(text=hint_text)
                    hint_used+=1
                    return  # Do not proceed to next question or score update
                else :
                    w_answer_entry.config(text="All 5 hints used")
                    return
            if user_sel_ans not in ('1', '2', '3', '4'):
                w_answer_entry.config(text="kindly enter only (1, 2, 3, 4) or 'hint'")
                return

            user_sel_ans = int(user_sel_ans)
            correct_ans = answers[current_question_index - 1][0]

            if user_sel_ans == correct_ans:
                score += 4
            else:
                score -= 1
            print(score)

        # Load the current question and options
        q = questions[current_question_index][0]
        opt1 = options[current_question_index][0]
        opt2 = options[current_question_index][1]
        opt3 = options[current_question_index][2]
        opt4 = options[current_question_index][3]

        # Display question and options
        question_label.config(text=f"{current_question_index + 1}) {q}")
        option1_label.config(text=f"1) {opt1}")
        option2_label.config(text=f"2) {opt2}")
        option3_label.config(text=f"3) {opt3}")
        option4_label.config(text=f"4) {opt4}")

        w_answer_entry.config(text="")  # Clear warning
        answer_entry.delete(0, 'end')   # Clear input
        current_question_index += 1

    else:
        # Check final question answer
        user_sel_ans = answer_entry.get().strip().lower()
        if user_sel_ans == "hint":
            if hint_used<5:
                hint_text = hints[current_question_index - 1][0]
                print(f"Hint: {hint_text}")
                w_answer_entry.config(text=hint_text)
                hint_used+=1
                return
            else : 
                w_answer_entry.config(text="All 5 hints used")
                return

        if user_sel_ans in ('1', '2', '3', '4'):
            user_sel_ans = int(user_sel_ans)
            correct_ans = answers[current_question_index - 1][0]
            if user_sel_ans == correct_ans:
                score += 4
            else:
                score -= 1
        show_final_screen()
def show_final_screen():
    global questions
    global id_user
    global score

    # Update score in the database using format()
    con = get_connection()
    cur = con.cursor()
    update_query = "UPDATE users SET score = {} WHERE user_id = {}".format(score, id_user)
    cur.execute(update_query)
    con.commit()
    con.close()

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFFFE0")

    # Display Final Score
    final_label = tkinter.Label(root, text="🎉 Quiz Finished! 🎉", font=("Nyala", 28, "bold"), bg="#FFFFE0", fg="#008000")
    final_label.pack(pady=(100, 20))

    score_label = tkinter.Label(root, text=f"{name_user}'s Final Score: {score} out of {len(questions)*4}", font=("Nyala", 22), bg="#FFFFE0", fg="#000080")
    score_label.pack(pady=(0, 40))

    # Exit Button
    exit_button = tkinter.Button(root, text="Exit", command=root.destroy, font=("Nyala", 16), bg="#FF6961", fg="white", padx=20)
    exit_button.pack()

# Entry point after role is selected
def start():
    print("Current roles - Admin:", admin_role, "User:", user_role)
    if admin_role and not user_role:
        root.destroy()
        threading.Thread(target=main).start()
    elif user_role and not admin_role:
        clear_root(root)
        show_user_screen()
    else:
        war_select.config(text="*Kindly choose your role", fg="red")
# First screen - role selection

m_title = tkinter.Label(root, text="ThinkTank", font=("aerial", 34, "bold"), bg="#FFFFE0")
m_title.pack(pady=(20, 0))

mm_label = tkinter.Label(root, text="You Are acting as -:", font=("nyala", 27), bg="#FFFFE0")
mm_label.pack(anchor=tkinter.W, padx=20, pady=(80, 0))

ch_frame = tkinter.Frame(bg="#FFFFE0")
ch_frame.pack(anchor=tkinter.W, fill='x', pady=(40, 0))

button_frame = tkinter.Frame(ch_frame, bg="#FFFFE0")
button_frame.pack(anchor='center')

ad_button = tkinter.Button(button_frame, text="Administrator", font=("aerial", 20), height=4, width=12, command=set_admin)
ad_button.pack(side=tkinter.LEFT, padx=70)

user_button = tkinter.Button(button_frame, text="Player", font=("aerial", 20), height=4, width=12, command=set_user)
user_button.pack(side=tkinter.LEFT, padx=70)

war_select = tkinter.Label(root, text="", bg="#FFFFE0", font=("aerial", 12))
war_select.pack()

sub_button = tkinter.Button(root, text="Submit", font=("aerial", 18), bg="#FF0000", fg="#FFFFFF", command=start)
sub_button.pack(pady=(20, 0))

root.mainloop()


#-------------------------administrator----------------------------------#


def add_question():
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Add New Question ---")
    question_text = input("Enter question text: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correct_option = int(input("Enter correct option number (1-4): "))
    hint = input("Enter hint (optional, press Enter to skip): ")

    query = """
        INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option, hint)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (question_text, option1, option2, option3, option4, correct_option, hint if hint else None))
    conn.commit()
    print("✅ Question added successfully!")
    cur.close()
    conn.close()

def view_questions():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM questions")
    rows = cur.fetchall()

    print("\n--- All Questions ---")
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Question: {row[1]}")
        print(f"1: {row[2]} | 2: {row[3]} | 3: {row[4]} | 4: {row[5]}")
        print(f"Correct Option: {row[6]}")
        print(f"Hint: {row[7]}")
    
    cur.close()
    conn.close()

def update_question():
    conn = get_connection()
    cur = conn.cursor()

    question_id = input("\nEnter the Question ID to update: ")
    print("Leave field empty to keep existing value.")
    
    # Fetch current values
    cur.execute("SELECT * FROM questions WHERE question_id = %s", (question_id,))
    result = cur.fetchone()
    if not result:
        print("❌ No such question ID found.")
        return

    print(f"Current question: {result[1]}")
    new_question_text = input("New question text: ") or result[1]
    new_option1 = input("New option 1: ") or result[2]
    new_option2 = input("New option 2: ") or result[3]
    new_option3 = input("New option 3: ") or result[4]
    new_option4 = input("New option 4: ") or result[5]
    new_correct_option = input("New correct option (1-4): ") or result[6]
    new_hint = input("New hint: ") or result[7]

    query = """
        UPDATE questions
        SET question_text=%s, option1=%s, option2=%s, option3=%s, option4=%s,
            correct_option=%s, hint=%s
        WHERE question_id=%s
    """
    cur.execute(query, (
        new_question_text, new_option1, new_option2, new_option3,
        new_option4, int(new_correct_option), new_hint, question_id
    ))
    conn.commit()
    print("✅ Question updated successfully!")
    cur.close()
    conn.close()

def delete_question():
    conn = get_connection()
    cur = conn.cursor()

    question_id = input("\nEnter the Question ID to delete: ")
    cur.execute("DELETE FROM questions WHERE question_id = %s", (question_id,))
    conn.commit()

    if cur.rowcount > 0:
        print("✅ Question deleted.")
    else:
        print("❌ No question found with that ID.")

    cur.close()
    conn.close()

def display_all_users():
    connection = get_connection()
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, score FROM users")
        users = cursor.fetchall()
        
        if users:
            print(f"{'User ID':<10} {'Name':<30} {'Score':<10}")
            print("-" * 50)
            for user in users:
                user_id, name, score = user
                print(f"{user_id:<10} {name:<30} {score:<10}")
        else:
            print("No users found in the database.")
        
        cursor.close()
    except Exception as e:
        print("Error fetching users:", e)
    finally:
        connection.close()
"""administrator function is on the top function name -: "main" """
