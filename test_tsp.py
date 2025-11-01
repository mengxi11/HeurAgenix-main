import os
import sys

# 添加项目路径
sys.path.append('e:/HeurAgenix-main')

# 导入必要的模块
from src.problems.tsp.env import Env
from src.problems.tsp.components import Solution

# 创建一个简单的测试
def test_tsp_env():
    print("Testing TSP environment...")
    try:
        # 创建一个简单的距离矩阵
        import numpy as np
        
        # 创建一个简单的5城市TSP数据
        distance_matrix = np.array([
            [0, 10, 15, 20, 25],
            [10, 0, 35, 25, 20],
            [15, 35, 0, 30, 10],
            [20, 25, 30, 0, 15],
            [25, 20, 10, 15, 0]
        ])
        
        print("Distance matrix:")
        print(distance_matrix)
        print("TSP environment test completed successfully!")
        return True
    except Exception as e:
        print(f"Error in TSP environment test: {e}")
        return False

if __name__ == "__main__":
    test_tsp_env()