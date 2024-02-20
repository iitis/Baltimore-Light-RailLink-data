
import numpy as np
import argparse
import matplotlib.pyplot as plt
import pickle

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=10)



def make_files_names(our_dirs, trains_direction):

    l = len(our_dirs)-1
    days = our_dirs[0][0:2]+"-"+our_dirs[l][0:2]
    month = our_dirs[0][2:4]
    year = our_dirs[0][4:8]

    period = ""
    if "_700" in our_dirs[0]:
        period += "morning "
    if "_1500" in our_dirs[l]:
        period += "afternoon"

    if trains_direction == "s":
        direction = "south"
    elif trains_direction == "n":
        direction = "north"
    else:
        direction = "both_ways"

    json_dir = f"pics/Realdata_{period}_{days}{month}{year}{direction}.json"
    pdf_dir = f"pics/Realdata_{period}_{days}{month}{year}{direction}.pdf"

    return json_dir, pdf_dir, (days, month, year, period, direction)


def make_histograms(our_dirs, trains_direction):

    hn = []
    hs = []
    for our_dir in our_dirs:
        with open(f'outputs/{our_dir}hist_times.pkl', 'rb') as f:
            times_hist = pickle.load(f)
        print(times_hist['time_range'])

        if trains_direction != "s":
            print("len north", len(times_hist["N"]))
            hn += times_hist["N"]
        if trains_direction != "n":
            print("len south", len(times_hist["S"]))
            hs += times_hist["S"]
    h = hn + hs
    # for now cutting of to large artefacts
    #h = list(filter(lambda x : x < cutoff, h))

    json_dir, _, (days, month, year, period, direction) = make_files_names(our_dirs, trains_direction)

    results = {"hist": h, "days": days, "month": month, "year": year, "period": period, "direction": direction}

    with open(json_dir, 'wb') as fp:
        pickle.dump(results, fp)




def plot_histograms(our_dirs, trains_direction):


    json_dir, pdf_dir, (days, month, year, period, direction) = make_files_names(our_dirs, trains_direction)

    with open(json_dir, 'rb') as fp:
        results = pickle.load(fp)

    h = results["hist"]

    print("length all", len(h))

    r1 = np.ceil(max(h))
    bins = np.arange(- 0.5, r1 + 1.5, 1.)
    #print("bins", bins)
    #print("passing times", h )

    fig, ax = plt.subplots(figsize=(4, 3))
    fig.subplots_adjust(bottom=0.2, left = 0.15)
    plt.hist( h, bins = bins, color = "gray",  ec="darkblue")
    l = len(our_dirs)-1


    plt.title(f"{period}  {days}  {month}  {year}")
    plt.xlabel(f"measured passing time CS -- MR {direction}")
    plt.gca().set_xlim(left=0, right = 30)
    #plt.xticks(range(0, int(r1)+1, 2))
    plt.xticks(range(0, 30, 2))
    plt.ylabel("counts")
    plt.savefig(pdf_dir)
    plt.show()
    plt.clf()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--datafolder', type=str, default=["files/"], nargs="*",
                            help='folders data are stored')
    parser.add_argument('--direction', type=str, default="",
                            help='direction of trains possible "s" - south, "n" -north or "" both' )

    args = parser.parse_args()
    assert args.direction in ["s", "n", ""]

    make_histograms(args.datafolder, args.direction)
    plot_histograms(args.datafolder, args.direction)






