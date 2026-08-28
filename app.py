import os
from google import genai
from google.genai import types
import sys
import time
import re
import requests
# 1. Initialize Gemini client
ai_client = genai.Client(api_key="AQ.Ab8RN6JQNjfe28Gs9SMahId21HV-OPqJucToDpac0pA_bEgY7w")
def animated_input(prompt_text, delay=0.03):
  for char in prompt_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  return input()
def animated_output(text, delay=0.03):
  formatted_text = re.sub(r"\*\*(.*?)\*\*", r"\033[1m\1\033[0m", text)
  for char in formatted_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()
def start_tutor_chat():
    print("=== Welcome to the AI School Tutor Chat! ===")
   
    # 2. Collect inputs from the user
    student_class = animated_input("Enter your class (e.g., Class-8): ").lower().strip()
    subject = animated_input("Enter your subject (e.g., Science): ").lower().strip()
    chapter = animated_input("Enter your chapter (e.g., Chapter-1): ").lower().strip()
    class_1_inputs = [
        "1",          # String Digit (Integer converted to string)
        "class-1",    # Hyphenated format
        "class1",     # Connected format
        "class 1",    # Spaced format
        "i",          # Roman numeral
        "class i",    # Roman numeral with space
        "class-i",    # Roman numeral with hyphen
        "one",        # Text word
        "first",      # Ordinal word
        "1st"         # Ordinal number
    ]
    class_2_inputs = [
        "2",          # String Digit
        "class-2",    # Hyphenated format
        "class2",     # Connected format
        "class 2",    # Spaced format
        "ii",         # Roman numeral
        "class ii",   # Roman numeral with space
        "class-ii",   # Roman numeral with hyphen
        "two",        # Text word
        "second",     # Ordinal word
        "2nd"         # Ordinal number
    ]
    class_3_inputs = [
    "3",          # String Digit
    "class-3",    # Hyphenated format
    "class3",     # Connected format
    "class 3",    # Spaced format
    "iii",        # Roman numeral
    "class iii",  # Roman numeral with space
    "class-iii", # Roman numeral with hyphen
    "three",      # Text word
    "third",      # Ordinal word
    "3rd"         # Ordinal number
    ]
    class_4_inputs = [
    "4",          # String Digit
    "class-4",    # Hyphenated format
    "class4",     # Connected format
    "class 4",    # Spaced format
    "iv",         # Roman numeral
    "class iv",   # Roman numeral with space
    "class-iv",   # Roman numeral with hyphen
    "four",       # Text word
    "fourth",     # Ordinal word
    "4th"         # Ordinal number
    ]
    class_5_inputs = [
    "5",          # String Digit
    "class-5",    # Hyphenated format
    "class5",     # Connected format
    "class 5",    # Spaced format
    "v",          # Roman numeral
    "class v",    # Roman numeral with space
    "class-v",    # Roman numeral with hyphen
    "five",       # Text word
    "fifth",      # Ordinal word
    "5th"         # Ordinal number
    ]
    class_6_inputs = [
    "6",          # String Digit
    "class-6",    # Hyphenated format
    "class6",     # Connected format
    "class 6",    # Spaced format
    "vi",         # Roman numeral
    "class vi",   # Roman numeral with space
    "class-vi",   # Roman numeral with hyphen
    "six",        # Text word
    "sixth",      # Ordinal word
    "6th"         # Ordinal number
    ]
    class_7_inputs = [
    "7",          # String Digit
    "class-7",    # Hyphenated format
    "class7",     # Connected format
    "class 7",    # Spaced format
    "vii",        # Roman numeral
    "class vii",  # Roman numeral with space
    "class-vii", # Roman numeral with hyphen
    "seven",      # Text word
    "seventh",    # Ordinal word
    "7th"         # Ordinal number
    ]
    class_8_inputs = [
    "8",          # String Digit
    "class-8",    # Hyphenated format
    "class8",     # Connected format
    "class 8",    # Spaced format
    "viii",       # Roman numeral
    "class viii", # Roman numeral with space
    "class-viii",# Roman numeral with hyphen
    "eight",      # Text word
    "eighth",     # Ordinal word
    "8th"         # Ordinal number
    ]
    class_9_inputs = [
    "9",          # String Digit
    "class-9",    # Hyphenated format
    "class9",     # Connected format
    "class 9",    # Spaced format
    "ix",         # Roman numeral
    "class ix",   # Roman numeral with space
    "class-ix",   # Roman numeral with hyphen
    "nine",       # Text word
    "ninth",      # Ordinal word
    "9th"         # Ordinal number
    ]
    class_10_inputs = [
    "10",          # String Digit
    "class-10",    # Hyphenated format
    "class10",     # Connected format
    "class 10",    # Spaced format
    "x",           # Roman numeral
    "class x",     # Roman numeral with space
    "class-x",     # Roman numeral with hyphen
    "ten",         # Text word
    "tenth",       # Ordinal word
    "10th"         # Ordinal number
    ]
    all_class_imputs={
        1:class_1_inputs,
        2:class_2_inputs,
        3:class_3_inputs,
        4:class_4_inputs,
        5:class_5_inputs,
        6:class_6_inputs,
        7:class_7_inputs,
        8:class_8_inputs,
        9:class_9_inputs,
        10:class_10_inputs
    }
    # Subject variations mapped to standardized names
    subject_validation = {
        "Science": ["science", "sci", "general science"],
        "Maths": ["maths", "math", "mathematics", "geometry", "algebra"],
        "English": ["english", "eng", "english literature", "english grammar"],
        "Social-science": ["social science", "sst", "history", "geography", "civics", "social studies"]
    }

    # Chapter 1 to 10 variations (Generated dynamically to keep code clean)
    chapter_validation = {
        i: [str(i), f"chapter-{i}", f"chapter{i}", f"chapter {i}", f"ch-{i}", f"ch{i}", f"ch {i}"]
        for i in range(1, 11)
    }

    for class_key,class_checker in all_class_imputs.items():
       if student_class in class_checker:
          student_class = f"Class-{class_key}"

    for subject_name, allowed_inputs in subject_validation.items():
        if subject in allowed_inputs:
            subject = subject_name
            break

    for chapter_num, allowed_inputs in chapter_validation.items():
        if chapter in allowed_inputs:
            chapter = f"Chapter-{chapter_num}"
            break
    base_url=f"https://raw.githubusercontent.com/nesar-innovations/AI-creation/main/{student_class}/{subject}/{chapter}.pdf"
    url_response=requests.get(base_url)
    if url_response.status_code==200:
        print("Success")
    else:
        print("Could not found your pdf on Cloud,please check your Class,Subject,Chapter")
    # 3. Dynamic absolute path selection


    
    try:
        
        pdf_attachment = types.Part.from_bytes(
            data=url_response.content,
            mime_type="application/pdf"
        )
        
        # 5. Core behavior prompt for your tutor agent
        system_instruction = (
            f"You are an expert school tutor for {student_class} {subject}. "
            f"You are discussing {chapter} with a student. Use the attached PDF to answer questions. "
            "Keep answers simple, encouraging, and clear for a school student. "
            "If they ask something not in the chapter, politely let them know."
        )
        
        animated_output("🤖 Initializing AI Tutor Chat Session...")
        
        # 6. Start the chat loop using gemini-3.5-flash-lite
        chat = ai_client.chats.create(
            model="gemini-3.5-flash-lite", # Correct current model name
            history=[
                types.Content(
                    role="user", 
                    parts=[
                        pdf_attachment, 
                        # Fixed structure type requirement
                        types.Part.from_text(text="Hi tutor, please analyze this chapter file so I can ask you questions about it.")
                    ]
                )
            ],
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.4
            )
        )
        
        animated_output("\n✨ Chat Started! Type your questions below. (Type 'exit' to quit) ✨\n")
        
        # 7. Running Chat Interface
        while True:
            user_msg = input("You: ").strip()
            
            if user_msg.lower() == 'exit':
                print("\n👋 Goodbye! Happy studying!")
                break
                
            if not user_msg:
                continue
                
            response = chat.send_message(user_msg)
            animated_output(f"\nAI: {response.text}\n")
            
    except Exception as e:
        print(f"❌ Error during chat execution: {str(e)}")

if __name__ == "__main__":
    start_tutor_chat()
