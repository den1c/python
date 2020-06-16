import json
info = [
    {
        'foto':'hero.jpeg',
        'name':'Алоди',
        'attack': 25,
        'protection': 40,
        'force': 38,
        'energy': 60,
        'info': ' Алоди (англ. Alodi) – поступивший на обучение в Даларан сирота\n'
                ', родители которого были высшим эльфом и человеком\n'
                '. Алоди продемонстрировал удивительные возможности по отслеживанию\n'
                ' и передаче потоков тайной магии, из-за чего получил предложение присоединиться\n'
                ' к Совету Тирисфаля. Он лично разработал новое заклинание\n'
                ', позволяющее передать силы магов на расстоянии,'
    }
    ,
    {
        'foto':'hero1.jpeg',
        'name':'Глю пукин',
        'attack': 25,
        'protection': 40,
        'force': 38,
        'energy': 60,
        'info': ' fgfgfgfgfdfdfdf'

    }
    ,
    {
        'foto':'hero2.jpg',
        'name':'Глюкин',
        'attack': 25,
        'protection': 40,
        'force': 38,
        'energy': 60,
        'info': ' fgfgfgfgfdfdfdf'
    }
    ,
    {
        'foto':'hero3.jpg',
        'name':'пукин',
        'attack': 25,
        'protection': 40,
        'force': 38,
        'energy': 60,
        'info': ' fgfgfgfgfdfdfdf'
    }
]





with open('info_hero.json','w',encoding= 'UTF-8')as f:
    json.dump(info,f)



with open('info_hero.json','r')as fr:
    text = json.load(fr)
    print(text)