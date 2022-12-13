# def find_second_index(list_strings: List[str], search_word:str) -> int:
#     count = 0
#     for k, item in enumerate(list_strings):
#         if item == search_word:
#             count+=1
#         if count == 2:
#             return k
#     return -1

# def find_second_index2(list_strings: List[str], search_word:str) -> int:
#     list_indexes = [i for i, string in enumerate(list_strings) if search_word in string]
#     try:
#         return list_indexes[1]
#     except IndexError:
#         return -1
