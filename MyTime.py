import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MyTime():
    def __init__(self, name):
        now = time.time()
        self.name = name
        self.paused = False
        self.start_time = now
        self.laps = []  # Running time at each lap
        self.lap_duration = [] # Duration of each lap
        self.lap_start = now
        self.running_time = None
        self.paused_running_time = 0  # The length of time that it's been paused
        self.paused_time = 0  # The time that the instance was paused

    def stop(self):
        if not self.paused:
            self.pause()
        self.laps = np.asarray(self.laps)
        self.lap_duration = np.asarray(self.lap_duration)
        self.running_time = self.laps[-1]

    def pause(self):
        now = time.time()
        self.laps.append(now - self.start_time - self.paused_running_time)
        self.lap_duration.append(now - self.lap_start)
        self.paused_time = now

        self.paused = True

    def resume(self):
        now = time.time()
        assert self.paused is True
        self.paused = False
        self.paused_running_time = self.paused_running_time + (now - self.paused_time)
        self.lap_start = now

    def __getitem__(self, idx):
        """Return the lap at idx
        """
        return self.lap_duration[idx]

    def print(self):
        if self.running_time is None:
            self.stop()
        print(f'{self.name}: {self.running_time:.5}')

    def max_lap(self):
        assert self.running_time != None
        idx = np.argmax(self.lap_duration)
        print(f'  max_lap({self.name}): ({idx}){self.lap_duration[idx]:.5}')
        return

    def min_lap(self):
        assert self.running_time != None
        idx = np.argmin(self.lap_duration)
        print(f'  min_lap({self.name}): ({idx}){self.lap_duration[idx]:.5}')
        return

    def mean_lap(self):
        assert self.running_time != None
        mean = self.lap_duration.mean()
        print(f'  mean_lap({self.name}): {mean:.5}')
        return

    def len_lap(self):
        assert self.running_time != None
        print(f'  len(laps): {len(self.laps)}')

    def lap_stats(self):
        self.mean_lap()
        self.max_lap()
        self.min_lap()
        self.len_lap()

    def plot_laps(self):
        series = pd.Series(self.lap_duration)
        series.plot(grid=True, marker='', ylabel='Seconds', xlabel='Lap')
        plt.savefig(f'/home/will/Documents/period_transformer/code/stuff/timing/{self.name}',
                    bbox_inches='tight')
        plt.close()

