this = input("请输入一个大字符串(按end退出)：")
if this != "end":
    dot = input("请输入一个子字符串（退出按end）：")
    if dot != "end":
        beg = input("请输入开始索引的位置：")
        fin = input("请输入结束索引的位置(不含)：")
        # print("{}在{}中出现的位置是{}:{}".format(dot, this, this.index(dot), this.index(dot)+len(dot)))
        while dot != "end":
            try:
                print("{}在{}中出现的位置是[{}:{})".format(dot,
                                                   this,
                                                   this.index(dot, eval(beg), eval(fin)),
                                                   this.index(dot, eval(beg), eval(fin)) + len(dot)))
            except:
                print("开始到结束索引的位置中不包含该子字符串，")
            dot = input("请输入一个子字符串（退出按end）：")
            if dot != "end":
                beg = input("请输入开始索引的位置：")
                fin = input("请输入结束索引的位置（不含）：")

    else:
        pass

print("已退出")
