
import numpy as np
import argparse
import matplotlib.pyplot as plt
import pickle

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=10)

def plot_histograms(our_dirs, south = True, north = True):

    hn = []
    hs = []
    for our_dir in our_dirs:
        with open(f'outputs/{our_dir}hist_times.pkl', 'rb') as f:
            times_hist = pickle.load(f)
        print(times_hist['time_range'])

        if north:
            print("len north", len(times_hist["N"]))
            hn += times_hist["N"]
        if south:
            print("len south", len(times_hist["S"]))
            hs += times_hist["S"]
    h = hn + hs

    print("length all", len(h))

    r1 = np.ceil(max(h))
    bins = np.arange(- 0.5, r1 + 1.5, 1.)
    #print("bins", bins)
    #print("passing times", h )

    fig, ax = plt.subplots(figsize=(4, 3))
    fig.subplots_adjust(bottom=0.2, left = 0.15)
    plt.hist( h, bins = bins, color = "gray",  ec="darkblue")
    l = len(our_dirs)-1
    days = our_dirs[0][0:2]+"-"+our_dirs[l][0:2]
    month = our_dirs[0][2:4]
    year = our_dirs[0][4:8]
    period = ""
    if "_700" in our_dirs[0]:
        period += "morning "
    if "_1500" in our_dirs[l]:
        period += "afternoon"
    plt.title(f"{period}  {days}  {month}  {year}")
    if south and (not north):
        direction = "south"
    elif north and (not south):
        direction = "north"
    else:
        direction = "both_ways"
    plt.xlabel(f"measured passing time CS -- MR {direction}")
    plt.gca().set_xlim(left=0)
    plt.xticks(range(0, int(r1)+1, 2))
    plt.ylabel("counts")
    plt.savefig(f"pics/Realdata_{period}_{days}{month}{year}{direction}.pdf")
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
    if args.direction == "s":
        plot_histograms(args.datafolder, south = True, north = False)
    elif args.direction == "n":
        plot_histograms(args.datafolder, south = False, north = True)
    else:
        plot_histograms(args.datafolder, south = True, north = True)






