class name:

    def make_judge(self, grade, points):
        
        isout = False   #不合格
        isretest = False    #再テスト
        count = 0

        #10点がないかチェックor30点以下が何回かチェック
        for point in points:
            if point < 10:
                isout = True
            if point <= 30:
                count += 1
        
        #
        if count >= 3:
            isretest = True

            if isout == True:

                result = 3
                return result

        #
        elif isretest == True:

                result = 2
                return result

        #
        else:
            if grade == "A" or grade == "B" or grade == "C":

                result = 1
                return result

            elif grade == "D":

                result = 2
                return result

            elif grade == "E":

                result = 3
                return result

# points = [0,10,20,30,40,50,60,70,80,90]
# judge = ["A","B","C","D","E"]
# grade = judge[0]
# print()