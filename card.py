import random

card_turple = ('武则天','嬴政','诸葛亮','宫本武藏','李白')

package = [ ]


while 1:
    choose = int(input('''
    充值能让你变强!
    请选择指令:
    1.抽卡
    2.查看背包
    3.整理背包
    4.离开
    '''))

    if choose == 1:
        num = int(input('请输入抽卡次数: '))
        for i in range(0,num):
            n = random.randint(0,4)
            print('你抽到了: {}'.format(card_turple[n]))
            package.append(card_turple[n])
        print('卡已存入背包')
        print('___________________')

    if choose == 2:
        if len(package) == 0:
            print('背包暂无英雄,快去抽卡吧')
            print('__________________')
        else:
            for i in package:
                print(i)
            print('_________________')

    if choose == 3:
        if len(package) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('_________________')
        else:
            package.sort()
            for i in package:
                print(i)
            print('_________________')

    if choose == 4:
        break

