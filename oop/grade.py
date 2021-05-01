'''
클래스에 학생의 이름을 입력하면
해당 학생이 얻은 3과목의 평균점수에 따라 A부터 F까지 출력하시오
해당 문제를 해결하기 위해서는 72페이지의 리스틀 참조하세요
'''

class Grade:
    def __init__(self, name):
        self.name = name
        self.marks = [] # list type

    def addMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def main():
        student = Grade(input("학생이름입력:"))
        for subject in ['국어', '영어', '수학']:
            student.addMarks(int(input(subject+"점수입력:")))
        avg = student.avg()

        if avg >= 90 :
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else:
            grade = "F"

        print(f'{student.name}의 과목 평균은{int(avg)}입니다. 학점은{grade} 입니다.')


if __name__ == '__main__':
    Grade.main()