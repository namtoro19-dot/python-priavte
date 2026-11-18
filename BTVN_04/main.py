#bài 1: Chuẩn hóa tên
def normalize_name(text: str) -> str:
    return " ".join(text.split())


#bài 2: Tính điểm trung bình và số đạt
def average_score(scores: list[float]) -> float | None:
    """tính điểm tb(average) của list scores, nếu list rỗng thì trả về None"""
    if not scores: #note :3 : if len(scores) == 0:  or if scores == []:
        return None
    return sum(scores) / len(scores)
def count_passed(scores: list[float], threshold: float = 5) -> float:
    """đếm số lượng phần tử trong list scores >= threshold"""
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count


#bài 3: Sắp xếp dict bằng lambda
def rank_students(score_by_name: dict[str, float]) -> dict[str, float]:
    sorted_items = sorted(
        score_by_name.items(),
        key=lambda item: (-item[1], item[0])
    )
    return dict(sorted_items)




print("bài 1")
print(normalize_name("  Nguyễn   An  "))  
print((normalize_name("minh")))             
print((normalize_name("   ")))             

print("\nbài 2")
test_scores_1 = [8, 4, 9, 5]
print("[8, 4, 9, 5]:", average_score(test_scores_1), "| Đạt (>=5):", count_passed(test_scores_1), "| Đạt (>=8):", count_passed(test_scores_1, 8))
test_scores_2 = [5]
print("[5]:", average_score(test_scores_2), "| Đạt (>=5):", count_passed(test_scores_2), "| Đạt (>=8):", count_passed(test_scores_2, 8))
test_scores_3 = []
print("[]:", average_score(test_scores_3), "| Đạt (>=5):", count_passed(test_scores_3), "| Đạt (>=8):", count_passed(test_scores_3, 8))

print("\nbài 3")
score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
ranked = rank_students(score_by_name)
empty_ranked = rank_students({})
print("bảng xếp hạng:", ranked)
print("Dict rỗng:", empty_ranked)