def min_battles(S, J, W):
    # 初始化战斗次数
    battles = 0
    
    # 只要三个部落中有两个部落的人数大于0，就继续战斗
    while (S > 0 and J > 0) or (S > 0 and W > 0) or (J > 0 and W > 0):
        # 检查哪两个部落的人数相同且最大
        if (S == J and S >= W) or (J == W and J >= S) or (S == W and S >= J):
            if S == J and S > 0 and J > 0:
                # S与J部落战斗
                S -= 1
                J -= 1
                W += 1
            elif J == W and J > 0 and W > 0:
                # J与W部落战斗
                J -= 1
                W -= 1
                S += 1
            elif S == W and S > 0 and W > 0:
                # S与W部落战斗
                S -= 1
                W -= 1
                J += 1
        else:
            # 选择人数最多的两个部落进行战斗
            if S >= J and J >= W or W >= J and J >= S:
                # S与J部落战斗
                S -= 1
                J -= 1
                W += 1
            elif J >= W and W >= S or S >= W and W >= J:
                # J与W部落战斗
                J -= 1
                W -= 1
                S += 1
            elif S >= W and W >= J or J >= W and W >= S:
                # S与W部落战斗
                S -= 1
                W -= 1
                J += 1

        # 每次战斗后，战斗次数增加
        battles += 1
    
    # 返回最小战斗次数
    return battles

# 计算最小战斗次数并输出
result = min_battles(1, 2, 3)
print(result)
