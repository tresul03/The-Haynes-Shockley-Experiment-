from brains import Brains
import time

if __name__ == "__main__":
    start_time = time.time()

    brains = Brains()
    brains.plot_graphs() 
    brains.produce_videos()

    print(f"--- Runtime: {time.time() - start_time} seconds ---")