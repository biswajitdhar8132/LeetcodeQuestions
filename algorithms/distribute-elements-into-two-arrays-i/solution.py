class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        count=[students.count(0), students.count(1)]
        for sand in sandwiches:
            if count[sand]==0:
                break
            count[sand]-=1
        return sum(count)