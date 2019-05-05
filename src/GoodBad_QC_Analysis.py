import pandas as pd
import matplotlib.pyplot as plt


def get_bad_workers_pct(df):
    bad_set = set()
    total_set = set()
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']
        total_set.add(worker_id)
        for i in range(1,11):
            input_img = row['Input.img'+str(i)]
            img_good_answer = row['Answer.img'+str(i)+'.good']
            if input_img.find('neg', input_img.rfind('/')) > -1 and img_good_answer:
                bad_set.add(worker_id)
    return len(bad_set)/len(total_set) * 100


def main():
    files = ["Budapest_GoodBad.csv", "California_GoodBad.csv",
    "CostaRica_GoodBad.csv", "Greece_GoodBad.csv",
    "Singapore_GoodBad.csv", "SouthAfrica_GoodBad.csv"]
    d = {}

    for file in files:
        input = '../data/good_bad_input/' + file
        df = pd.read_csv(input)
        pct = get_bad_workers_pct(df)
        d[file] = pct
    print(d)

    sizes = [50, 220, 360, 220, 50, 440]
    dqdf = pd.DataFrame(list(zip(d.values(), sizes)),
        columns=['percentages','sizes'])
    print(dqdf.corr())


    checkbox = [15.0, 2.649, 8.2192, 4.5045, 1.8868, 10.1124]
    checkbox_goodbad_df = pd.DataFrame(list(zip(d.values(), checkbox)),
        columns=['Good/Bad', 'CheckBox'])
    print(checkbox_goodbad_df.corr())


    d1 = {k[:-12]:v for k,v in d.items()}
    series = pd.Series(d1)
    mean = series.mean()
    std = series.std()
    print("Mean: " + str(mean))
    print("Standard Deviation: " + str(std))

    ax = series.plot(kind="bar")
    t2 = ax.set_title("Percentage of Workers Disqualified in Good/Bad HIT")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
