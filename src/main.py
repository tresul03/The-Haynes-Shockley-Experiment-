from brains import Brains
import time

if __name__ == "__main__":
    start_time = time.time()

    # Please allow up to 5 minutes for the program to run.
    brains = Brains()
    brains.plot_colourmaps()
    brains.plot_graphs() 
    brains.plot_videos()

    print(f"--- Runtime: {time.time() - start_time} seconds ---")