import csv
import pandas as pd
import matplotlib.pyplot as plt
def generate_csv(gen_b_rows, gen_avg_rows, gen_std_dev_rows):
    gen_best = open('./Output/gen_best.csv', 'w', newline='').close()
    gen_avg = open('./Output/gen_avg.csv', 'w', newline='').close()
    gen_std_dev = open('./Output/gen_std_dev.csv', 'w', newline='').close()
    gen_best = open('./Output/gen_best.csv', 'a', newline='')
    gen_avg = open('./Output/gen_avg.csv', 'a', newline='')
    gen_std_dev = open('./Output/gen_std_dev.csv', 'a', newline='')
    header_gb = ['Gen', 'Best']
    writer_gen_best = csv.writer(gen_best)
    header_ga = ['Gen', 'Avg']
    writer_gen_avg = csv.writer(gen_avg)
    header_gsd = ['Gen', "StandardDeviation"]
    writer_gen_std_dev = csv.writer(gen_std_dev)

    writer_gen_best.writerow(header_gb)
    writer_gen_best.writerows(gen_b_rows)
    writer_gen_avg.writerow(header_ga)
    writer_gen_avg.writerows(gen_avg_rows)
    writer_gen_std_dev.writerow(header_gsd)
    writer_gen_std_dev.writerows(gen_std_dev_rows)

    gen_best.close()
    gen_avg.close()
    gen_std_dev.close()


def generate_plot():
    cols_gen_best = ['Gen', 'Best']
    cols_gen_avg = ['Gen', 'Avg']
    cols_gen_std_dev = ['Gen', 'StandardDeviation']
    gen_best = pd.read_csv('./Output/gen_best.csv', sep=',', usecols=cols_gen_best)
    gen_avg = pd.read_csv('./Output/gen_avg.csv', sep=',', usecols=cols_gen_avg)
    gen_std_dev = pd.read_csv('./Output/gen_std_dev.csv', sep=',', usecols=cols_gen_std_dev)
    plt.plot(gen_best.Gen, gen_best.Best)
    plt.savefig('./Output/gen_to_best.png')
    plt.close()
    plt.plot(gen_avg.Gen, gen_avg.Avg)
    plt.savefig('./Output/gen_to_avg.png')
    plt.close()
    plt.plot(gen_std_dev.Gen, gen_std_dev.StandardDeviation)
    plt.savefig('./Output/gen_to_std_dev.png')
