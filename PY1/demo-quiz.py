class Question:
    def __init__(self,text,choices,answer) :
        self.text=text
        self.choices=choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions) :
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input ("cevap :")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def displayProgress(self):
            totalQuestion = len(self.questions)
            questionNumber = self.questionIndex +1
        
            if questionNumber >totalQuestion:
                print("Quiz bitti")

            else:
                print(f"quesiton {questionNumber} of {totalQuestion}".center(80,"*"))

    
    def showScore(self):
        print("score" + str(self.score))


q1 = Question("1 soru : nedir ?",["a","b","c"],"a")
q2 = Question("2 soru : nedir ?",["a","b","c"],"a")
q3 = Question("3 soru : nedir ?",["a","b","c"],"a")
questions = [q1,q2,q3]

quiz =Quiz(questions)

quiz.loadQuestion()


