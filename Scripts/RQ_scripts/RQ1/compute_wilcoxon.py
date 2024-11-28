import numpy as np
import pandas as pd
from scipy.stats import wilcoxon


class SciStats:

    @classmethod
    def stats_obvious_greater(cls, data1, data2):
        w_value,p_value = wilcoxon(np.array(data1), np.array(data2), alternative="greater")
        return p_value

    @classmethod
    def stats_increase(cls, data1: list, data2):
        total = 0
        for d1, d2 in zip(data1, data2):
            total += (d1 - d2) / d2
        return total / len(data1)


def computeWilcoxon(metric_df):
    def compute_measure(measure):
        aff_col = f'avg_{measure}_aff'
        nonaff_col = f'avg_{measure}_nonaff'

        aff_data = metric_df[aff_col].values
        nonaff_data = metric_df[nonaff_col].values

        p_value = SciStats.stats_obvious_greater(aff_data, nonaff_data)
        increase = SciStats.stats_increase(aff_data, nonaff_data)

        return [measure, p_value, increase]

    measures = ['#author', '#changeCmt', '#changeLoc', '#issue', '#issueCmt', '#issueLoc']

    results = [compute_measure(measure) for measure in measures]

    # Convert results to DataFrame
    results_df = pd.DataFrame(results, columns=['measure', 'P-value', 'increase'])

    print("output Wilcoxon-output.csv")
    # Write DataFrame to CSV file
    print(results_df)
    results_df.to_csv('sample-wilcoxon-output.csv', index=False)

if __name__ == '__main__':
    metric = pd.read_csv("sample-metrics.csv")
    computeWilcoxon(metric)
