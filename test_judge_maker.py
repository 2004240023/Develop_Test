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


"""

実行結果:一回目はインデントミスで失敗
        二回目は修正後実行想定内の結果が帰ってきたため成功
        
(venv) root@605-14:~/Develop_Test# pytest test_judge_maker.py
================================================= test session starts ==================================================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /root/Develop_Test
collected 1 item

test_judge_maker.py F                                                                                            [100%]

======================================================= FAILURES =======================================================
_________________________________________________ test_make_judge_no1 __________________________________________________

    def test_make_judge_no1():

        
        マトリックスNo1 ←テストを行うマトリックスの番号
        10点より下の点数がある場合 ←テストの内容
        

        #テスト関数の呼び出し
        test_object = name()
        result = test_object.make_judge('A', [9, 100, 100, 100, 100,100, 100, 100, 100, 100])

        #assertを使用して結果が正しいことを確認する
>       assert result == 3
E       assert 1 == 3

test_judge_maker.py:15: AssertionError
=============================================== short test summary info ================================================
FAILED test_judge_maker.py::test_make_judge_no1 - assert 1 == 3
================================================== 1 failed in 0.01s ===================================================
(venv) root@605-14:~/Develop_Test# pytest test_judge_maker.py
================================================= test session starts ==================================================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /root/Develop_Test
collected 1 item

test_judge_maker.py .                                                                                            [100%]

================================================== 1 passed in 0.00s ===================================================

"""