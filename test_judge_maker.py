from judge_maker import name

def test_make_judge_no1():
    
    """
    マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """

    #テスト関数の呼び出し
    test_object = name()
    result = test_object.make_judge('A', [9, 100, 100, 100, 100,100, 100, 100, 100, 100])

    #assertを使用して結果が正しいことを確認する
    assert result == 3

#2　成績がAからC    30点以下の回数:3以上   10点より下:なし    再テスト:2
def test_make_judge_no2():
    test_object = name()
    result = test_object.make_judge('A', [30, 30, 30, 100, 100,100, 100, 100, 100, 90])
    assert result == 2

#3　成績がAからC    30点以下の回数:1～2   10点より下:あり    不合格:3
def test_make_judge_no3():
    test_object = name()
    result = test_object.make_judge('B', [30, 30, 9, 100, 100,100, 100, 100, 100, 80])
    assert result == 3

#4　成績がAからC    30点以下の回数:1～2   10点より下:なし    合格:1
def test_make_judge_no4():
    test_object = name()
    result = test_object.make_judge('C', [30, 30, 100, 100, 100,100, 100, 100, 100, 70])
    assert result == 1    

#5　成績がD    30点以下の回数:3以上   10点より下:あり    不合格:3
def test_make_judge_no5():
    test_object = name()
    result = test_object.make_judge('D', [30, 30, 30, 9, 100,100, 100, 100, 100, 60])
    assert result == 3

def test_make_judge_no6():
    test_object = name()
    result = test_object.make_judge('F', [100, 100, 100, 100, 100,100, 100, 100, 100, 100])
    assert result == 1