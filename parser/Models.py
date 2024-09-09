from bs4 import Tag


class Lesson:
    def __init__(self, div: Tag):
        self.parser(div)

    def parser(self, div: Tag):
        self.time = div.find(class_="время-подсказка").text
        self.number = div.find(class_="пара").text.replace(self.time, "")
        temp_data = div.findAll("td")
        self.title = temp_data[2].text.replace("\u00ad", "")
        self.prepod = temp_data[3].text.replace("\u00ad", "")
        self.place = temp_data[4].text
    
    def to_json(self):
        return {
            "time": self.time,
            "number": self.number,
            "title": self.title,
            "prepod": self.prepod,
            "place": self.place,
        }


class Day:
    def __init__(self, div: Tag):
        self.parser(div)
        self.lessons: list[Lesson] = []

    def parser(self, div: Tag):
        self.data = div.text

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def to_json(self):
        return {
            "data": self.data,
            "lessons": [lesson.to_json() for lesson in self.lessons]
        }


class ShedulePage:
    def __init__(self, divs: Tag):
        self.days: list[Day] = []
        self.parser(divs)

    def parser(self, divs: Tag):
        for block in divs:
            block_type = self.get_type(block)
            if block_type == "дата":
                self.new_day(block)
            if block_type == "занятие":
                self.add_lesson(block)

    def new_day(self, div: Tag):
        self.days.append(Day(div))

    def add_lesson(self, div: Tag):
        self.days[-1].add_lesson(Lesson(div))

    @staticmethod
    def get_type(div: Tag):
        return div.attrs.get('class', " ")[0]

    def to_json(self):
        return {
            "days": [day.to_json() for day in self.days]
        }
