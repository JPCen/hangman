def hangerman2(word):
    num = len(word)
    life = 6
    throt =["_"]*num
    point =["_"]*num
    print(throt)
    stage = ["|_________         ",
             "|         |        ",
             "|         0        ",
             "|        /|>       ",
             "|        /(        ",
             ]

    while life > 0:
        chara = input("文字を1つにゅうりょくしてください")
        if chara in word:
            print("正解")
            ch_num = word.index(chara)
            throt[ch_num]=chara
            point[ch_num]="$"
            if "_" not in point:
                print("あなたの勝ち")
                break
            
        else:
            print("不正解")
            life = life - 1
        show_stage = stage[0:6-life]
        print("\n".join(show_stage))
        print(throt)
        if life >0:
            continue
        print("あなたの負け")
        print("正解は{}".format(word))

        
        

hangerman2("cat")
