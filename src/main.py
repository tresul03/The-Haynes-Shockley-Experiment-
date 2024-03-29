from brains import Brains
import time

if __name__ == "__main__":

    # Please allow up to 5 minutes for the program to run.
    brains = Brains()
    start_time = time.time()
    brains.plot_videos()
    brains.plot_graphs()
    brains.plot_colourmaps()
    print(f"--- Runtime: {time.time() - start_time} seconds ---")
