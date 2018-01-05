# coding: utf-8
"""
Q学習-最良経路を学習するスクリプト書いた (powered by Python)
http://d.hatena.ne.jp/Kshi_Kshi/20111227/1324993576
https://gist.github.com/peace098beat/4901950ec11596d948a9
Greedy法:学習結果をGreedy法で行動選択
11:00-
"""

import sys
import copy
import random
import numpy as np


# 環境: State
# 環境の状態: S
# エージェントの行動:a
# 方策: Plan -> a = Plan(S)
# S' = State(S,a)
# 報酬: r = Reward(S')

GAMMA = 0.9
ALPHA = 0.9
GREEDY_RATIO = 0.5

MAX_ITERATE = 150000

NUM_COL = 10  # 横
NUM_ROW = 10  # 縦

GOAL_REWORD = 100

ACTION = [0, 1, 2, 3]
ACTION_NAME = ['UP', 'RIGHT', 'DOWN', 'LEFT']
NUM_ACTION = 4

START_COL = 1
START_ROW = 1
GOAL_COL = NUM_COL-2
GOAL_ROW = NUM_ROW-2

# 道:0 壁:1 ゴール:2 エージェント:3
# WALL = 1
# GOAL = 2
# ROAD = 0
# AGENT = 3
ROAD,WALL,GOAL,AGENT = 0,1,2,3
# FIELD = np.array([
#     [1, 1, 1, 1, 1, 1],
#     [1, 0, 3, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1]
# ])
FIELD = np.zeros((NUM_ROW,NUM_COL))
for row in range(NUM_ROW):
    for col in range(NUM_COL):
        if row in (0, NUM_ROW-1):
            FIELD[row,col]=WALL
        if col in (0, NUM_COL-1):
            FIELD[row, col]=WALL
FIELD[START_ROW, START_COL] = AGENT




def fieldDisplay(S):
    print('*** Field ***')
    Sprint = np.copy(S)
    Sprint[GOAL_ROW, GOAL_COL] = GOAL
    for row in range(NUM_ROW):
        print (Sprint[row, :])


def plan(S):
    n = 1
    n = np.random.randint(0, 3 + 1)
    print ('>> Plan(), Return Action:', ACTION_NAME[n])
    return ACTION[n]


def State(aSnow, a):
    Snow = np.copy(aSnow)
    # 2. 環境StateはエージェントAgentから受け取った行動aと、現在の状態Sにもとづいて、次の状態S'に変化
    Agent_row, Agent_col = np.where(Snow == 3)
    row1 = Agent_row[0]
    col1 = Agent_col[0]
    if a == ACTION[0]:
        row2 = row1 - 1
        col2 = col1
    elif a == ACTION[1]:
        row2 = row1
        col2 = col1 + 1
    elif a == ACTION[2]:
        row2 = row1 + 1
        col2 = col1
    elif a == ACTION[3]:
        row2 = row1
        col2 = col1 - 1

    Stmp = Snow[row2, col2]
    if Stmp == WALL:
        # print 'Agent next WALL'
        S_next = np.copy(Snow)
    else:

        Snow[row1, col1] = ROAD
        Snow[row2, col2] = AGENT
        S_next = Snow

    return S_next


def Reward(Snext):
    # 2. 環境StateはエージェントAgentから受け取った行動aと、現在の状態Sにもとづいて、次の状態S'に変化
    Agent_row, Agent_col = np.where(Snext == AGENT)
    row1 = Agent_row[0]
    col1 = Agent_col[0]

    # if (row1, col1) == (GOAL_ROW, GOAL_COL):
    if row1 == GOAL_ROW and col1 == GOAL_COL:
        r = GOAL_REWORD
    else:
        r = 0

    return r


def QLearn(Q, S, a, r, S_next):
    row, col = np.where(S == AGENT)
    row = row[0]
    col = col[0]

    row_next, col_next = np.where(S_next == AGENT)
    row_next = row_next[0]
    col_next = col_next[0]

    # q_value = Q[row, col, a]
    # q = (1.0 - ALPHA) * q_value + ALPHA * (r + GAMMA * max(Q[row_next, col_next, :]))
    # Q[row, col, a] = q
    max_Q = max(Q[row_next, col_next, :])
    Q[row, col, a] = Q[row, col, a] + ALPHA * (r + GAMMA * max_Q - Q[row, col, a])

    return Q


def displayQ(Q):
    for row in range(NUM_ROW):
        c = [max(Q[row, col, :]) for col in range(NUM_COL)]
        # print '%5.1f,'*6 % tuple(c)
    for a in ACTION:
        print( 'action', a)
        for row in range(NUM_ROW):
            c = [Q[row, col, a] for col in range(NUM_COL)]
            print( '%8.1f,' * NUM_COL % tuple(c))


def planQ(Q, S):
    Agent_row, Agent_col = np.where(S == AGENT)
    Agent_row = Agent_row[0]
    Agent_col = Agent_col[0]
    # print 'Q:', Q[Agent_row, Agent_col, :]
    a = 1
    max_Q = -10000
    best_action = []
    for i in range(NUM_ACTION):
        q = Q[Agent_row, Agent_col, ACTION[i]]
        if q > max_Q:
            max_Q = q
            best_action = [ACTION[i]]
        elif q == max_Q:
            best_action.append(ACTION[i])

    # print '>> Best Action,', best_action
    a = np.random.choice(best_action)

    if GREEDY_RATIO < random.random():
        return a
    else:
        return np.random.choice([0, 1, 2, 3])


def main():
    # ********* main ********* #
    #  0. 初期状態
    # AgentのAI
    Q = np.zeros((NUM_ROW, NUM_COL, NUM_ACTION))

    goal_num = 0

    t = 0;
    S = np.copy(FIELD)
    fieldDisplay(S)

    while t < MAX_ITERATE:
        # print '//////////// Itarate %d ///////////////' % (t)
        # print 'Goal Number : %d' % (goal_num)
        # fieldDisplay(S)

        # 1. エージェントは環境から受け取った観測Sを受け取り、方策planに基づいて環境に行動aを渡す
        # a = plan(S)
        a = planQ(Q, S)
        # print '>> Action :', ACTION_NAME[a]

        # 2. 環境StateはエージェントAgentから受け取った行動aと、現在の状態Sにもとづいて、次の状態S'に変化
        S_next = State(S, a)

        #   その遷移に基づいて報酬r = Reward(S')をエージェントに返す
        r = Reward(S_next)
        # print '>> Reward Value :', r

        # 4. Agentに学習させる
        Q = QLearn(np.copy(Q), np.copy(S), a, r, np.copy(S_next))

        if r == GOAL_REWORD:
            # fieldDisplay(S)
            S = np.copy(FIELD)
            goal_num += 1

        S = np.copy(S_next)
        # 3. 時間進行t=t+1
        t = t + 1

    print ('//////////// Itarate %d ///////////////' % (t))
    print ('Goal Number : %d' % (goal_num))
    displayQ(Q)


if __name__ == '__main__':
    main()