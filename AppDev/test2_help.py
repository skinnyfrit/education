class Person:
    def __init__(self, pid = str, name = str):
        self.pid = pid
        self.name = name
    def _start(self):
        return f"{self.name}"

class Professor(Person):
    def __init__(self, pid, name):
        super().__init__(pid, name)

class Student(Person):
    def __init__(self, pid, name):
        super().__init__(pid, name)

class TeachingAssistant(Student):
    def __init__(self, pid, name):
        super().__init__(pid, name)

class TutorialGroup():
    N = 3
    def __init__(self, ta):
        self.ta = ta
        self.__students = list() #initialise private attribute as list
    def add_student(self, student = None):
        self.__students.append(student)
    def _start(self):
        ta_name = self.ta._start()
        if len(self.__students) == 0:
            class_names = "No one"
        else:
            class_names = ",".join(s._start() for s in self.__students)
        return f"{ta_name}'s Class - {class_names}"
    def get_students(self):
        return self.__students
    def grp_size(self):
        return self.__students
    
class Course():
    def __init__(self, cid, title, professors):
        self.cid = cid
        self.title = title
        self.__professors = professors
        self.__groups = list() #initialise private attribute as list
    def find_smallest_group(self): # helper function
        min_size = float("inf") #setting min_size to become infinity, so that it goes away when you call min function
        smallest_g = None
        for g in self.__groups:
            curr_size = g.grp_size()
            if curr_size < min_size:
                min_size = curr_size
                smallest_g = g
        return smallest_g
    def allocate(self, students):
        for s in students:
            smallest_g = self.find_smallest_group()
            smallest_g.add_student()
        self.__groups
    def start(self): # main calls course, course calls tutorial group
        if len(self.__groups) == 0:
            return "No Tutorial Groups"
        # for tg in self.__groups:
        #     tg._start() # TutorialGroup class start func
        return "\n".join(tg._start() for tg in self.__groups) # refer to above 2 lines (merged)
    def add_tutorialgroup(self, ta):
        self.__groups.append(TutorialGroup(ta))
    def get_professors(self):
        return self.__professors
    def get_tutorialgroups(self):
        return self.__groups


if __name__ == "__main__":
    # Example usage as per sequence diagram
    # ===================================================
    p = Professor("P001", "Prof. Ada")
    ta = TeachingAssistant("TA001", "Bob")
    c = Course("CS101", "Intro to CS", [p])
    s1 = Student("S001", "Stu One")
    s2 = Student("S002", "Stu Two")

    c.add_tutorialgroup(ta)
    assert(c.start() == "Bob's Class - No one")
    c.allocate([s1, s2])
    print(s1._start())
    assert(c.start() == "Bob's Class - Stu One,Stu Two")
    assert(s1._start() == "Stu One")
    assert(s2._start() == "Stu Two")
    # ===================================================
    
    # Additional test cases, not part of the seq diagram
    bob = TeachingAssistant("TA002", "Bob")
    bob_tg = TutorialGroup(bob)
    assert(bob_tg._start() == "Bob's Class - No one")
    
    alice = TeachingAssistant("TA003", "Alice")
    alice_tg = TutorialGroup(alice)
    alice_tg.add_student(Student("S003", "Stu One"))
    alice_tg.add_student(Student("S005", "Stu Three"))
    alice_tg.add_student(Student("S004", "Stu Two"))
    assert(alice_tg._start() == "Alice's Class - Stu One,Stu Three,Stu Two")

    c2 = Course("CS102", "Data Structures", [Professor("P002", "Prof. Bob")])
    assert(c2.start() == "No tutorial groups")
    c2.add_tutorialgroup(alice)
    c2.add_tutorialgroup(bob)
    assert(c2.start() == "Alice's Class - No one\nBob's Class - No one")