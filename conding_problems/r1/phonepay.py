

import enum
from typing import List

class DifficultyType:
    easy   = "easy"
    medium = "medium"
    hard   = "hard"
    

class Question:
    def __init__(self, id: str, name: str, description: str, tag: str, difficulty: DifficultyType, score: int):
        self.id: str                    = id
        self.name: str                  = name
        self.description: str           = description
        self.tag: str                   = tag
        self.difficulty: DifficultyType = difficulty
        self.score: int                 = score
        self.solve_by: List[str]        = []
        self.average_time: float          = 0
    
    def update_average(self, time_taken: int):
        total_solver = len(self.solve_by)
        self.average_time = ((self.average_time*(total_solver-1) + time_taken)/total_solver)
         
    
class Contestant:
    def __init__(self, id: str, name: str, department: str):
        self.id: str                         = id
        self.name: str                       = name
        self.department: str                 = department
        self.solved_problems: list[Question] = []
        self.total_score: int                = 0
        
    
    def solve_problem(self, problem: Question, time_taken: int):
        if problem.id not in [p.id for p in self.solved_problems]:
            self.solved_problems.append(problem)
            self.total_score+=problem.score

            problem.solve_by.append(self.id)
            problem.update_average(time_taken)
    

class LeaderBoard:
    def __init__(self):
        self.leader = []
    
    def update_leader(self, contestants: list[Contestant]):
        # self.leader = max(contestants, key=lambda x:x.total_score)
        self.leader = sorted(contestants, key=lambda x:x.total_score)[:3]
    
    # [
    #     0: [1, 2],
    #     0: [],
    #     100: [0],--->pop--user_id3
    #     1000: [3],--->append user_id3
    # ]
    # [
    #     0: 2,
    #     0: 0,
    #     0: 2,--> -1
    #     1000: 0-->+1,
    # ]

    
    
    
class HackathonPlatform:
    def __init__(self):
        self.problems: dict[str, Question]       = {}
        self.contestents: dict[str, Contestant]  = {}
        self.leader_board: LeaderBoard           = LeaderBoard()
    
    
    def addProblem(self, id: str, name: str, description: str, tag: str, difficulty: DifficultyType, score: int):
        if id in self.problems:
            raise Exception("problem id already exist")
        self.problems[id] = Question(id, name, description, tag, difficulty, score)
    
    def addUser(self, id: str, name: str, department: str):
        if id in self.contestents:
            raise Exception("contestent id already exist")
        self.contestents[id] = Contestant(id, name, department)
    
    def fetchProblems(self, filter_by: dict=None, sort_by: str=None):
        problems = list(self.problems.values())
        if filter_by:
            for key, val in filter_by.items():
                problems = [p for p in problems if getattr(p, key)==val]
        
        if sort_by:
            problems.sort(key=lambda x: getattr(p, sort_by))
        
        return problems
    
    def solve(self, contestant_id: str, problem_id: str, time_taken: int):
        if contestant_id not in self.contestents:
            raise ValueError("Invalid contestant_id")
            
        if problem_id not in self.problems:
            raise ValueError("Invalid problem_id")
        
        contestant = self.contestents[contestant_id]
        problem = self.problems[problem_id]
        contestant.solve_problem(problem, time_taken)
        self.leader_board.update_leader(list(self.contestents.values()))
    
    def fetchSolvedProblems(self, contestant_id: str):
        if contestant_id not in self.contestents:
            raise ValueError("Invalid contestant_id")
        
        return self.contestents[contestant_id].solved_problems
    
    def getLeader(self):
        leader = self.leader_board.leader
        if not leader:
            return
        
        return {
            "name": leader.name,
            "department": leader.department,
            # "score": leader.total_score
        }
    
        
        

        
        
platform =HackathonPlatform()

platform.addProblem(0, "sum 1", "desc", "algorithms", DifficultyType.easy, 50)

platform.addProblem(1, "sum 2 number", "desc", "algorithms", DifficultyType.easy, 50)
platform.addProblem(2, "sum 3 number", "desc", "algorithms", DifficultyType.medium, 90)


platform.addUser(1, "shiv", "IT")
platform.addUser(2, "shankar", "Consulting")


platform.solve(1, 1, 300)
print("current_leader: ", platform.getLeader())
platform.solve(2, 2, 300)
print("current_leader: ", platform.getLeader())
platform.solve(1, 1, 300)
print("current_leader: ", platform.getLeader())
platform.solve(1, 2, 300)
print("current_leader: ", platform.getLeader())

#filter easy problems
print("\n"*3)


diff_type = DifficultyType.medium
print(f"filter {diff_type} problems")

problems = platform.fetchProblems(filter_by={"difficulty": diff_type})
for p in problems:
    print(f"{p.id} title: {p.name}")


    


