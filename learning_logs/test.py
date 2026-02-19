# phone = input('전화번호를 입력하시오 >>> ')
# if len(phone) != 13:
#     print('유효하지 않은 전화번호 형식입니다.')
# elif len(phone) == 13:
#     print(f'{phone} 전화번호의 중간 4자리는 {phone[4:8]}입니다.')
# class Student :
#     def __init__(self,name,student_id,grade) :
#         self.name = name
#         self.student_id = student_id
#         self.grade = {}
#         print(f'학생 이름 : {self.name}')
#
#     def add_grade(self, subject, score) :
#         self.grade[subject] = score
#
#     def get_average_grade(self) :
#         avg = sum(self.grade.values()) / len(self.grade)
#         print(f'평균 성적 : {avg}점')
#
# student = Student('김일', 2026, grade='')
# student.add_grade('수학', 90)
# student.add_grade('국어', 90)
# student.add_grade('영어', 90)
# student.get_average_grade()
# check_num = int(input('몇 개의 숫자를 입력하시겠습니까? >>> '))
# numbers = []
# positive_num = 0
# negative_num = 0
# zero_num = 0
# for i in range(check_num):
#     input_num = int(input(f'{i+1}번째 숫자를 입력하시오 >>> '))
#     if input_num == 0:
#         numbers.append(input_num)
#         zero_num += 1
#     elif input_num > 0:
#         numbers.append(input_num)
#         positive_num += 1
#     elif input_num < 0:
#         numbers.append(input_num)
#         negative_num += 1
# print(f'양수: {positive_num}개\n음수: {negative_num}개\n0: {zero_num}개')
# num_of_persons = int(input('후보자 수를 입력하시오 >>> '))
# candidates = []
# for i in range(num_of_persons):
#     person_name = input(f'{i+1}번째 후보자의 이름을 입력하시오 >>> ')
#     candidates.append(person_name)
# votes_dict = {}
# for letter in candidates:
#     votes_dict[letter] = 0
# votes= int(input('전체 투표 횟수를 입력하시오 >>> '))
# for i in range(votes):
#     vote = int(input(f'{i+1}번째 투표 (1: {candidates[0]}, 2: {candidates[1]}, 3: {candidates[2]}) >>> '))
#     if vote == 1:
#         votes_dict[candidates[0]] += 1
#     elif vote == 2:
#         votes_dict[candidates[1]] += 1
#     elif vote == 3:
#         votes_dict[candidates[2]] += 1
# list_keys = list(votes_dict.keys())
# list_values = list(votes_dict.values())
# print(f'---투표 결과---\n{list_keys[0]} : {list_values[0]}\n{list_keys[1]} : {list_values[1]}\n{list_keys[2]} : {list_values[2]}')