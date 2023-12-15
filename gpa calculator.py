def all_results():   
        midterm_score = float(input("Enter your midterm score: "))
        final_score = float(input("Enter your final score: "))
        quiz_scores = []
        for i in range(4):
            quiz = float(input("Enter your quiz score: "))
            quiz_scores.append(quiz)
            i+=1
        homework_scores = []
        for j in range(4):
            homework = float(input("Enter your homework score: "))
            homework_scores.append(homework)
            j+=1

        print("Scores are saved.")
        return[midterm_score, quiz_scores, homework_scores, final_score]

def calculates_scores(all_results):
    midterm_score = all_results[0]
    quiz_scores = all_results[1]
    homework_scores = all_results[2]
    final_scores = all_results[3]

    total_score = midterm_score * 0.25 + (sum(quiz_scores)/len(quiz_scores))  * 0.20 + (sum(homework_scores)/len(homework_scores)) * 0.20 + final_scores * 0.35

    return total_score

def calculate_absenteeism_rate():
    absences = int(input("How many classes have you missed? "))
    total_num_of_weeks = 14
    absent_rate = absences/total_num_of_weeks
    return absent_rate

def letter_grade(total_score, absent_rate):
    if absent_rate>0.25:
        print("Your grade is NA")
    elif 90 <= total_score <= 100:
        print("AA")
    elif 85 <= total_score <= 89:
        print("BA")
    elif 80 <= total_score <= 84:
        print("BB")
    elif 75 <= total_score <= 79:
        print("CB")
    elif 70 <= total_score <= 74:
        print("CC")
    elif 65 <= total_score <= 69:
        print("DC")
    elif 60 <= total_score <= 64:
        print("DD")
    elif 50 <= total_score <= 60:
        print("FD")
    elif 0 <=total_score<= 49:
        print("FF")



def main():
    score = all_results()
    total_score = calculates_scores(score)
    absent_rate = calculate_absenteeism_rate()

    letter_grade(total_score, absent_rate)

main()
