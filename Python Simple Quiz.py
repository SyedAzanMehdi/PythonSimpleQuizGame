questions = [
    {
        "q": "Who is considered the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam Muhammad Ali Jinnah", "Sir Syed Ahmad Khan"],
        "answer": "C"
    },
    {
        "q": "When was the Lahore Resolution passed?",
        "options": ["1930", "1940", "1947", "1929"],
        "answer": "B"
    },
    {
        "q": "Who presented the Lahore Resolution?",
        "options": ["Allama Iqbal", "Quaid-e-Azam", "Maulvi Fazlul Haq", "Liaquat Ali Khan"],
        "answer": "C"
    },
    {
        "q": "Pakistan came into being on:",
        "options": ["15th August 1947", "14th August 1947", "23rd March 1940", "27th Ramadan 1947"],
        "answer": "B"
    },
    {
        "q": "Who was the first Governor General of Pakistan?",
        "options": ["Quaid-e-Azam Muhammad Ali Jinnah", "Liaquat Ali Khan", "Khawaja Nazimuddin", "Iskander Mirza"],
        "answer": "A"
    },
    {
        "q": "Who was the first Prime Minister of Pakistan?",
        "options": ["Liaquat Ali Khan", "Khawaja Nazimuddin", "Muhammad Ali Bogra", "Chaudhry Muhammad Ali"],
        "answer": "A"
    },
    {
        "q": "What was the title of Allama Iqbal’s Allahabad Address (1930)?",
        "options": ["Pakistan Resolution", "Khilafat Movement", "Vision of a Separate Muslim State", "Muslim League Manifesto"],
        "answer": "C"
    },
    {
        "q": "Who was the first President of Pakistan?",
        "options": ["Liaquat Ali Khan", "Iskander Mirza", "Ayub Khan", "Khawaja Nazimuddin"],
        "answer": "B"
    },
    {
        "q": "Objective Resolution was passed in:",
        "options": ["1949", "1956", "1962", "1973"],
        "answer": "A"
    },
    {
        "q": "The Indus Water Treaty was signed between Pakistan and India in:",
        "options": ["1948", "1951", "1960", "1965"],
        "answer": "C"
    },
    {
        "q": "Who was the first Muslim President of All India National Congress?",
        "options": ["Quaid-e-Azam", "Sir Syed Ahmad Khan", "Badruddin Tyabji", "Maulana Azad"],
        "answer": "C"
    },
    {
        "q": "The Simla Agreement between Pakistan and India was signed in:",
        "options": ["1947", "1965", "1972", "1999"],
        "answer": "C"
    },
    {
        "q": "The capital of Pakistan was shifted from Karachi to Islamabad in:",
        "options": ["1959", "1960", "1967", "1970"],
        "answer": "B"
    },
    {
        "q": "Who was the first Chief Martial Law Administrator of Pakistan?",
        "options": ["Iskander Mirza", "Ayub Khan", "Yahya Khan", "Zia-ul-Haq"],
        "answer": "B"
    },
    {
        "q": "When did General Zia-ul-Haq take over Pakistan?",
        "options": ["1969", "1971", "1977", "1988"],
        "answer": "C"
    },
    {
        "q": "Which political party was founded by Zulfikar Ali Bhutto in 1967?",
        "options": ["Muslim League", "Pakistan People’s Party", "Awami League", "Jamaat-e-Islami"],
        "answer": "B"
    },
    {
        "q": "Who was the first woman Prime Minister of Pakistan?",
        "options": ["Fatima Jinnah", "Benazir Bhutto", "Hina Rabbani Khar", "Begum Ra’ana Liaquat Ali Khan"],
        "answer": "B"
    },
    {
        "q": "The first constitution of Pakistan was enforced in:",
        "options": ["1949", "1956", "1962", "1973"],
        "answer": "B"
    },
    {
        "q": "The 1973 Constitution of Pakistan was passed during the government of:",
        "options": ["Ayub Khan", "Yahya Khan", "Zulfikar Ali Bhutto", "General Zia-ul-Haq"],
        "answer": "C"
    },
    {
        "q": "When did Pakistan conduct its first nuclear tests?",
        "options": ["1974", "1984", "1998", "2001"],
        "answer": "C"
    }
]

score = 0

print("\n===== Pakistan History Quiz =====\n")
print("\n===== Made By: Azan Mehdi :) =====\n")
for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['q']}")
    for j, option in zip(["A", "B", "C", "D"], q["options"]):
        print(f"  {j}) {option}")
    answer = input("Your answer (A/B/C/D): ").upper().strip()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"wrong! Correct answer: {q['answer']}) {q['options'][ord(q['answer'])-65]}\n")

print("===== Quiz Finished =====")
print(f"Your Score: {score}/{len(questions)} ({(score/len(questions))*100:.1f}%)")
