import pulp
import sys

def preprocessing_for_mp(df):
    """データの整形をする関数"""

    task_name_list = df['業務名'].tolist()[:-1]
    
    weight_list = df['重要度'].tolist()[:-1]
    weight_limit = df['重要度'].tolist()[-1]
    
    df_const = df.iloc[:-1, 2:]
    const_limits = df.iloc[-1, 2:].tolist()

    return task_name_list, weight_list, weight_limit, df_const, const_limits

def resource_maximize(df, isBinary=True):
    """リソースを最大化する数理計画問題"""
    
    # データの整形
    task_name_list, \
    alpha_list, \
    _, \
    df_resource, \
    resource_limits = preprocessing_for_mp(df)
    
    # 問題定義
    problem = pulp.LpProblem(sense=pulp.LpMaximize)

    # 変数定義
    if isBinary:
        tasks = [pulp.LpVariable('t{}'.format(idx), cat=pulp.LpBinary) for idx in range(len(task_name_list))]
    else:
        tasks = [pulp.LpVariable('t{}'.format(idx), cat=pulp.LpContinuous, lowBound=0, upBound=1) for idx in range(len(task_name_list))]

    # 目的関数定義
    demands_each_task = [row.values.sum()*alpha for (_, row), alpha in zip(df_resource.iterrows(), alpha_list)]
    problem += pulp.lpDot(demands_each_task, tasks)

    # 制約条件定義 
    for (_, demands_each_resource), resource_limit in zip(df_resource.iteritems(), resource_limits):
        problem += pulp.lpDot(demands_each_resource, tasks) <= resource_limit

    # 解く
    status = problem.solve()

    if pulp.LpStatus[status] != 'Optimal':
        sys.stderr.write('Error!: この問題は最適化不可能です．以下に作成した問題を示します．')
        sys.stderr.write(problem)
    
    result = {task_name_list[idx]: pulp.value(tasks[idx]) for idx, _ in enumerate(tasks)}
    
    return result
