"""
임의의 텍스트를 불러와서 n-gram을 바탕으로 학습하여
새로운 텍스트를 생성하는 모델 만들기
"""
from collections import Counter, defaultdict
import numpy as np
import string

def unzip(pairs):
    return tuple(zip(*pairs))

#정규화시키는 코드, 내림차순으로 (most_common() 활용)
#counter는 {"char": cnt}의 dict형태
def normalize(counter):
    ans = []
    total = sum(counter.values())

    return [(char, cnt / total) for char, cnt in counter.most_common()]

#텍스트를 입력받아 n-gram형식으로 빈도수 리턴함수
def train_lm(text, n):
    raw_lm = defaultdict(Counter)
    history = "~" * (n-1)

    for char in text:
        raw_lm[history][char] += 1
        history = history[1:] + char
    
    lm = {history : normalize(counter) for history, counter in raw_lm.items()}
    return lm
    #리턴형태 - dict{history, defaultdict(char, frequency)}


#데이터로 학습된 모델 바탕으로 랜덤(확률에 따른)으로 char생성하기
def generate_letter(lm, history):
    if not history in lm:
        return "~"
    
    letters, probs = unzip(lm[history])
    chr = np.random.choice(letters, p = probs)
    return chr


#위의 함수를 바탕으로 자동 텍스트 생성 구현
def generate_text(lm, n, nletters):
    text = []
    history = "~" * (n-1)

    for i in range(nletters):
        c = generate_letter(lm, history)
        text.append(c)
        history = history[1:] + c

    return "".join(text)

if __name__ == "__main__":
    with open("korean_national_anthem.txt", "rb") as f:
        lyrics = f.read().decode()
        lyrics = lyrics.lower()
    
    lm = train_lm(lyrics, 5)
    new_text = generate_text(lm, 5, 100)
    print(new_text)