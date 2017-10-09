#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from pandas import DataFrame
import copy

class BranchAndBound:
    def __init__(self, weights, values, max_weight, answer_val):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.max_weight = max_weight
        self.answer_val = answer_val
        self.evaluates = self.values/self.weights
        self.index_list = []
        for index in range(1, len(weights) + 1):
            self.index_list.append('x' + str(index))
        self.target_df = DataFrame(np.c_[self.evaluates, self.weights, self.values, np.array(self.answer_val)], index=self.index_list, columns=["evaluate", "weight", "value", "ans"])
        self.target_df = self.target_df.sort_values('evaluate', ascending=False)
        self.answer_val = list(self.target_df['ans']) #answer_valを評価値の高い順にソートされたものに変更
        del self.target_df['ans'] # DataFrameにはもう必要ないので「ans」カラムを削除

        self.target_ans = np.dot(np.array(answer_val), values)
        self.index_list = self.target_df.index #indexの順番変更

    def __judgeValue(self, fixed_list): # fixed_listで渡されたxの固定値における緩和問題を解き、分岐継続を判定する。また、よりよい解が見つかれば暫定解の交換を行う。
        sum_weight = 0 # 採択したxのweightの合計値
        evaluate_list = [] # 採択の判定を格納
        evaluate_list.extend(fixed_list)
        for index, val in enumerate(fixed_list):
            sum_weight += self.target_df.ix[self.index_list[index]]['weight']*val #  fixed_listで渡されたxの値でのweightの合計値

        for index in range(len(fixed_list), len(self.index_list)):
            if sum_weight > self.max_weight: #max_weightを超えた場合は分岐終了
                return False # 分岐終了
            elif sum_weight == self.max_weight: #max_weightに達しているので他のxは0
                evaluate_list.append(0)
                continue
            else:
                if sum_weight + self.target_df.ix[self.index_list[index]]['weight'] < self.max_weight:#x=1にしてもmax_weightに到達しないとき
                    sum_weight += self.target_df.ix[self.index_list[index]]['weight']
                    evaluate_list.append(1)
                else:# 0 < x <= 1 となるとき
                    evaluate_list.append((self.max_weight - sum_weight)/self.target_df.ix[self.index_list[index]]['weight'])
                    sum_weight = self.max_weight
                    if (self.max_weight - sum_weight) == self.target_df.ix[self.index_list[index]]['weight']: # x=1のとき、暫定解を入れ替える
                        evaluate_list_count = len(evaluate_list)
                        for i in range(evaluate_list_count, len(self.index_list)): # 決まっていないxは全部0を入れる
                            evaluate_list.append(0)
                        self.target_ans = np.dot(np.array(evaluate_list), np.array(self.target_df.value)) # 暫定解 target_ansの入れ替え
                        self.answer_val = evaluate_list # 暫定解 answer_valの入れ替え
                        return False # 分岐終了

        if len(fixed_list) == len(self.index_list):  # 全てのxの値が固定されているとき 暫定解との比較
            if (sum_weight <= self.max_weight) and (np.dot(np.array(fixed_list), np.array(self.target_df.value)) > self.target_ans): # 暫定解との比較
                self.target_ans = np.dot(np.array(fixed_list), np.array(self.target_df.value)) # 暫定解 target_ansの入れ替え
                self.answer_val = fixed_list  # 暫定解 answer_valの入れ替え
            return False

        if np.dot(np.array(evaluate_list), np.array(self.target_df.value)) > self.target_ans: # 緩和問題の解が暫定解を超えた時
            return True# 分岐継続
        else:  # 暫定解を超えていないとき
            return False  # 分岐終了
    def depthFirstSearch(self):  #深さ優先探索
        search_lists = [[0], [1]]  # 要素 [0]、[1]は先に入れておく
        while len(search_lists) != 0:  # search_listsが空になるまで続ける
            first_list = search_lists[0]  # Stachで考える、上から１つ取得
            search_lists.pop(0)  # 取得した要素は削除
            if self.__judgeValue(first_list):  # 探索が継続かどうか
                new_list_cp = copy.deepcopy(first_list)  # 次要素に「1」を追加するために深いコピー
                new_list_cp.append(1)  # 1を末尾に追加
                search_lists.insert(0, new_list_cp)  # 新たな要素を search_listsの先頭に格納
                new_list_cp = copy.deepcopy(first_list)  # 次要素に「0」を追加するために深いコピー
                new_list_cp.append(0)  # 0を末尾に追加
                search_lists.insert(0, new_list_cp)  # 新たな要素をsearch_listsの先頭に格納

        print("-----深さ優先探索-----")
        for index, val in enumerate(self.index_list):
            print(val + ": " + str(self.answer_val[index]))
        print("ans: " + str(self.target_ans))

# BranchAndBound(weight_list(a1, a2, a3, a4), value_list(c1, c2, c3, c4), max_weight(a_max), first_values(x1, x2, x3, x4))
# first_valuesは何でもよいが、ここではgreedy-algorithmで求めた解を初期値として与えた。
bb = BranchAndBound([2, 3, 5, 6], [4, 5, 12, 14], 9, [1, 0, 0, 1])
bb.depthFirstSearch()