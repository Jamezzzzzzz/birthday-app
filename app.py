import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'birthday_suprise'


MESSAGES = [
    "葉明佳菲貓加油 ❤️",
    "21歲了 加油一點啦! 🎂",
    "這題算難，你在想一下",
    "你確定嗎? 錢錢要不見了喔",
    "這個錢比niko and難賺喔 加油加油",
    "呂紹群超帥 :D"
]
PRIZES = {
    'letter1': {'name': '卡通都是騙人的', 'price': 100, 'content': 'ㄟ~~~ 是卡 片'},
    'mysterybox1': {'name': '你頭上有海報', 'price': 150, 'content': '鴨子瓜瓜'},
    'picture': {'name': '你的美照', 'price': 50, 'content': '我好愛這張'},
    'mysterybox2': {'name': '米老鼠手提袋', 'price': 150, 'content': '米三米吃提拉米蘇'},
    'mysterybox3': {'name': '金雨好煩', 'price': 50, 'content': '手殘可用'}

}

def reset_game():
    session['money'] = 0
@app.route('/')
def index():
    if 'lives' not in session:
        reset_game()
    return render_template('index.html')

@app.route('/quiz/<int:q_idx>', methods=['GET', 'POST'])
def quiz(q_idx):
    questions = [
        {'q': '我們的紀念日是...(日期 ex: 2026/03/20)?', 'a': '2024/02/29', 'reward': 20},
        {'q': '葉明佳是不是很可愛? (是/不是)', 'a': '是', 'reward': 20},
        {'q': '西索是幻影旅團幾號成員？', 'a': '4', 'reward': 20},
        {'q': '幻影旅團總共有多少成員？', 'a': '13', 'reward': 20},
        {'q': '讓我們紅塵作伴 活得瀟瀟灑灑 ______ 共享人世繁華', 'a': '策馬奔騰', 'reward': 20},
        {'q': '呂紹群不喜歡哪一家韓式料理店?', 'a': '娘子家', 'reward': 20},
        {'q': '馬戲團公約 劇本由你來寫 燈光是點綴 ________', 'a': '音樂是調味', 'reward': 20},
        {'q': 'BTS有幾個成員？', 'a': '7', 'reward': 20},
        {'q': '試問這裡有幾個三角形？', 'a': '8', 'reward': 20},
        {'q': 'GRTF stands for？', 'a': 'golden rain tree festival', 'reward': 20},
        {'q': '甄嬛總共懷孕過幾次?', 'a': '4', 'reward': 20},
        {'q': 'ACE stands for？', 'a': 'adult and continuing education', 'reward': 20},
        {'q': '隆科多騙太后康熙爺最討厭＿＿色，並叫當時的她穿那個顏色去選秀，殊不知其實是康熙爺最喜歡的顏色，因而讓她入選？ a.粉紫 b.粉紅 c.粉藍 d.粉紫', 'a': 'b', 'reward': 20},
        {'q': '去年你生日我們搭到哪一站捷運站吃你的生日餐？', 'a': '永安市場', 'reward': 20},
        {'q': '呂紹群是不是很帥? )', 'a': '超帥', 'reward': 20},
        {'q': '單點大麥克多少錢', 'a': '81', 'reward': 20},
        {'q': '小雞逛超市裡的小雞有幾隻？', 'a': '5', 'reward': 20},
        {'q': 'team Cole or team Alex?', 'a': 'alex', 'reward':20},
        {'q': '葉明佳有幾劃？', 'a': '29', 'reward': 20},
        {'q': '清水祖師爺', 'a': '溫水煮青蛙', 'reward': 20},
        {'q': 'BTS 隊長是 ？', 'a': 'rm', 'reward': 20},
        {'q': '17 隊長是 ？', 'a': 's.coups', 'reward': 20},
        {'q': '36返服大默契: 注意  _____', 'a': '美樂地', 'reward': 20},
        {'q': '葉明佳生日快樂，Love you~', 'a': 'love you too', 'reward': 20},
        {'q': 'love you more', 'a': 'love you most', 'reward': 20},
        {'q': 'love you moo', 'a': 'love you mooooooo', 'reward': 20}


    ]

    error_msg = None

    if q_idx >= len(questions):
        return redirect(url_for('shop'))

    if request.method == 'POST':
        user_answer = request.form.get('answer').lower().strip()
        
        if user_answer == questions[q_idx]['a']:
            session['money'] += questions[q_idx]['reward']
            if q_idx + 1 >= len(questions):
                return redirect(url_for('shop'))
            else:
                return redirect(url_for('quiz', q_idx=q_idx + 1))
        else:
            
            error_msg = random.choice(MESSAGES)

    return render_template('quiz.html', question=questions[q_idx], q_idx=q_idx, error_msg=error_msg)

@app.route('/skip/<int:q_idx>')
def skip(q_idx):
    questions = [
        {'q': '我們的紀念日是...(日期 ex: 2026/03/20)?', 'a': '2024/02/29', 'reward': 20},
        {'q': '葉明佳是不是很可愛? (是/不是)', 'a': '是', 'reward': 20},
        {'q': '西索是幻影旅團幾號成員？', 'a': '4', 'reward': 20},
        {'q': '幻影旅團總共有多少成員？', 'a': '13', 'reward': 20},
        {'q': '讓我們紅塵作伴 活得瀟瀟灑灑 ______ 共享人世繁華', 'a': '策馬奔騰', 'reward': 20},
        {'q': '呂紹群不喜歡哪一家韓式料理店?', 'a': '娘子家', 'reward': 20},
        {'q': '馬戲團公約 劇本由你來寫 燈光是點綴 ________', 'a': '音樂是調味', 'reward': 20},
        {'q': 'BTS有幾個成員？', 'a': '7', 'reward': 20},
        {'q': '試問這裡有幾個三角形？', 'a': '8', 'reward': 20},
        {'q': 'GRTF stands for？', 'a': 'golden rain tree festival', 'reward': 20},
        {'q': '甄嬛總共懷孕過幾次?', 'a': '4', 'reward': 20},
        {'q': 'ACE stands for？', 'a': 'adult and continuing education', 'reward': 20},
        {'q': '隆科多騙太后康熙爺最討厭＿＿色，並叫當時的她穿那個顏色去選秀，殊不知其實是康熙爺最喜歡的顏色，因而讓她入選？ a.粉紫 b.粉紅 c.粉藍 d.粉紫', 'a': 'b', 'reward': 20},
        {'q': '西索是幻影旅團幾號成員？', 'a': '4', 'reward': 20},
        {'q': '呂紹群是不是很帥? )', 'a': '超帥', 'reward': 20},
        {'q': '單點大麥克多少錢', 'a': '81', 'reward': 20},
        {'q': '小雞逛超市裡的小雞有幾隻？', 'a': '5', 'reward': 20},
        {'q': 'team Cole or team Alex?', 'a': 'alex', 'reward':20},
        {'q': '葉明佳有幾劃？', 'a': '29', 'reward': 20},
        {'q': '清水祖師爺', 'a': '溫水煮青蛙', 'reward': 20},
        {'q': 'BTS 隊長是 ？', 'a': 'rm', 'reward': 20},
        {'q': '17 隊長是 ？', 'a': 's.coups', 'reward': 20},
        {'q': '36返服大默契: 注意  _____', 'a': '美樂地', 'reward': 20},
        {'q': '葉明佳生日快樂，Love you~', 'a': 'love you too', 'reward': 20},
        {'q': 'love you more', 'a': 'love you most', 'reward': 20},
        {'q': 'love you moo', 'a': 'love you mooooooo', 'reward': 20}
    ]
    if q_idx + 1 >= len(questions):
        return redirect(url_for('shop'))
    
    return redirect(url_for('quiz', q_idx=q_idx + 1))


@app.route('/shop')
def shop():
    if 'purchased_items' not in session:
        session['purchased_items'] = []
    return render_template('shop.html', prizes=PRIZES)

@app.route('/buy/<item_id>')
def buy(item_id):
    prize = PRIZES.get(item_id)
    
    if 'purchased_items' not in session:
        session['purchased_items'] = []

    if prize and session['money'] >= prize['price']:
        if item_id not in session['purchased_items']:
            session['money'] -= prize['price']
            session['purchased_items'].append(item_id)
            session.modified = True 
            
    return redirect(url_for('shop'))


if __name__ == '__main__':
    app.run(debug=True)