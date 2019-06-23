import random


hand_list = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

print('出す手を選んで下さい')
print('1:グー 2:チョキ 3:パー')

# ユーザの手を入力する
player_in = input()

# 入力値の判定
if player_in not in hand_list:
    # '1': 'グー', '2': 'チョキ', '3': 'パー'以外であれば終了する
    print('入力が正しくありません')
    exit()

# 入力した値に対応した手を辞書hand_listから取得し、player_handに代入
player_hand = hand_list[player_in]
print('入力した手:' + player_hand)

# コンピュータの手をランダムで設定
com_in = random.choice(['1','2','3'])
# コンピュータの手を辞書hand_listから取得し、com_handに代入
com_hand = hand_list[com_in]
print('コンピュータの手:' + com_hand)

# 互いの手を表示する
print(player_hand + 'vs' + com_hand)

# ジャンケンの勝敗判定、結果は変数zyanken_resultに代入
# あいこ
if player_hand == com_hand:
    zyanken_result = 'あいこ'
# グー
elif player_hand == 'グー':
    if com_hand == 'チョキ':
        zyanken_result = 'あなたの勝ち'
    else:
        zyanken_result = 'コンピューターの勝ち'
# チョキ
elif player_hand == 'チョキ':
    if com_hand == 'パー':
        zyanken_result = 'あなたの勝ち'
    else:
        zyanken_result = 'コンピューターの勝ち'
# パー
else:
    if com_hand == 'グー':
        zyanken_result = 'あなたの勝ち'
    else:
        zyanken_result = 'コンピューターの勝ち'

print(zyanken_result)
