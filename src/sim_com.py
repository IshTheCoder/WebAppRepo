
import numpy as np
import scipy.stats
import pandas as pd
from scipy.stats import entropy
from numpy.linalg import norm

def JSD(P, Q):
    _P = P / norm(P, ord=1)
    _Q = Q / norm(Q, ord=1)
    _M = 0.5 * (_P + _Q)
    return 0.5 * (entropy(_P, _M) + entropy(_Q, _M))



def jensen_shannon_distance(p, q):
    """
    method to compute the Jenson-Shannon Distance 
    between two probability distributions
    """

    # convert the vectors into numpy arrays in case that they aren'



    divergence = JSD(p,q)


    # compute Jensen Shannon Divergence
    #divergence = (scipy.stats.entropy(p, m) + scipy.stats.entropy(q, m)) / 2

    # compute the Jensen Shannon Distance
    distance = np.sqrt(divergence)
    return distance




def sim_com(df1, df2, team, num_poss = 0):
	df2 = df2[df2['TEAM_NAME'] == team]

	df_temp = df1[df1["TEAM_NAME"] != team]
	#df_temp = df1
	#print(df_temp)
	pt_abrv = ['iso_freq', 'tr_freq', 'prb_freq', 'prr_freq', 'pu_freq', 'su_freq', 'ho_freq', 'cut_freq', 'os_freq', 'putback_freq', 'misc_freq']

	q = df2[pt_abrv]
	q = list(q.iloc[0])
	diff_list = []

	for index, row in df_temp.iterrows():
		p = list(row[pt_abrv])

		diff_list.append(round(jensen_shannon_distance(p,q), 4))



	# print(len(diff_list))
	#df1['Similarity Score'] = df1.apply(lambda row: jensen_shannon_distance(row[pt_abrv], df2[pt_abrv]) , axis=1)
	df_temp['Similarity Score'] = diff_list
	df_temp['Complement Score'] = df_temp.apply(lambda row: round(1-row['Similarity Score'], 4) , axis=1)

	df_temp = df_temp[df_temp['total_poss'] >= num_poss]

	return df_temp



