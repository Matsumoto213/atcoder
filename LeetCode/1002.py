N = int(input())
words = [input() for _ in range(N)]
# words = input().split()

from collections import Counter

def common_characters(words):
    # すべての文字列をカウントする
    counter = Counter(''.join(words))
    
    # 重複を含む文字のリストを作成する
    common_chars = [char for char, count in counter.items() if count >= len(words)]
    
    # 結果を返す
    return common_chars

    # 結果を返す
    return common_chars
print(common_characters(words))