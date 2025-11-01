import os
import sys

# 添加项目路径
sys.path.append('e:/HeurAgenix-main')

# 导入必要的模块
import numpy as np
from src.problems.tsp.components import Solution

# 创建一个模拟的环境来测试启发式算法
class MockEnv:
    def __init__(self):
        # 创建一个简单的5城市TSP数据
        self.instance_data = {
            "node_num": 5,
            "distance_matrix": np.array([
                [0, 10, 15, 20, 25],
                [10, 0, 35, 25, 20],
                [15, 35, 0, 30, 10],
                [20, 25, 30, 0, 15],
                [25, 20, 10, 15, 0]
            ])
        }
        self.current_solution = Solution(tour=[])
        self.key_item = "current_cost"
        
    def get_key_value(self, solution=None):
        """计算当前解的成本"""
        if solution is None:
            solution = self.current_solution
        if len(solution.tour) < 2:
            return 0
        current_cost = sum([
            self.instance_data["distance_matrix"][solution.tour[index]][solution.tour[index + 1]] 
            for index in range(len(solution.tour) - 1)
        ])
        if len(solution.tour) > 2:
            current_cost += self.instance_data["distance_matrix"][solution.tour[-1]][solution.tour[0]]
        return current_cost

# 测试最近邻启发式算法
def test_nearest_neighbor():
    print("Testing nearest neighbor heuristic...")
    
    # 导入最近邻启发式算法
    sys.path.append('e:/HeurAgenix-main/src/problems/tsp/heuristics/basic_heuristics')
    from nearest_neighbor_f91d import nearest_neighbor_f91d
    
    # 创建模拟环境
    env = MockEnv()
    
    # 创建问题状态（符合启发式算法要求的格式）
    problem_state = {
        "distance_matrix": env.instance_data["distance_matrix"],
        "current_solution": env.current_solution,
        "unvisited_nodes": list(range(env.instance_data["node_num"])),
        "last_visited": -1  # -1表示还没有访问任何节点
    }
    
    # 运行启发式算法
    try:
        operator, info = nearest_neighbor_f91d(problem_state, {})
        print(f"Operator: {operator}")
        print(f"Info: {info}")
        
        # 应用操作符到解决方案
        if operator:
            new_solution = operator.run(env.current_solution)
            print(f"New solution: {new_solution.tour}")
            
            # 计算解的成本
            env.current_solution = new_solution
            cost = env.get_key_value()
            print(f"Solution cost: {cost}")
        else:
            print("No operator returned")
        
        print("Nearest neighbor heuristic test completed successfully!")
        return True
    except Exception as e:
        print(f"Error in nearest neighbor heuristic test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_nearest_neighbor()