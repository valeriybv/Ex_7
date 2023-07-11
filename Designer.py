from Employee import Employee


class Designer(Employee):
    def __init__(self, name, awards, score):
        super().__init__(name, awards, score)
        self.grade = self.get_grade()
        pass

    def get_grade(self):
        """Вычисляет грейд по очкам"""
        if self.score >= 7:
            self.grade = self.score // 7
        else:
            self.grade = 1
        return self.grade

    def pass_qualification(self):
        """Прохождеие квалификации"""
        self.score = self.add_scores()
        self.grade = self.get_grade()
        self.publish_grade()


    def add_scores(self):
        """Прибавляет очки квалификации"""
        self.score +=1
        return self.score


    def publish_grade(self):
        print("Текущий грейд", self.grade)

