def count_task_assignments(n, x, y, z):
    total_ways = 0
    # 遍历员工x可以承担的任务数
    for tasks_x in range(min(x, n) + 1):
        # 遍历员工y可以承担的任务数
        for tasks_y in range(min(y, n - tasks_x) + 1):
            tasks_z = n - tasks_x - tasks_y
            # 检查员工z的任务数是否超过其上限
            if tasks_z <= z:
                total_ways += 1
    return total_ways

# 示例输入
n, x, y, z = 10, 5, 5, 5
# 输出结果
print(count_task_assignments(n, x, y, z))
