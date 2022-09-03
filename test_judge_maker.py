from judge_maker import make_judge

def test_make_judge_no1():
    
    """
    マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """

    #テスト関数の呼び出し
    result = make_judge('A', [9, 100, 100, 100, 100,100, 100, 100, 100, 100])

    #assertを使用して結果が正しいことを確認する
    assert result == 3
