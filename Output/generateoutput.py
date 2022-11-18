import csv


def generate_csv(gen_b_rows, gen_avg_rows, gen_std_dev_rows):
    gen_best = open('./Output/gen_best.csv', 'w', newline='').close()
    gen_avg = open('./Output/gen_avg.csv', 'w', newline='').close()
    gen_std_dev = open('./Output/gen_std_dev.csv', 'w', newline='').close()
    gen_best = open('./Output/gen_best.csv', 'a', newline='')
    gen_avg = open('./Output/gen_avg.csv', 'a', newline='')
    gen_std_dev = open('./Output/gen_std_dev.csv', 'a', newline='')
    header_gb = ['Gen', 'f(x)']
    writer_gen_best = csv.writer(gen_best)
    header_ga = ['Gen', 'Avg']
    writer_gen_avg = csv.writer(gen_avg)
    header_gsd = ['Gen', "Standard Deviation"]
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
