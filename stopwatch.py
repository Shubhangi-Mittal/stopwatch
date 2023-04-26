import time
import tkinter as tk

class Stopwatch(tk.Frame):
    # create a stopwatch frame
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        # make the time label
        l = tk.Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

        # make the buttons
        f = tk.Frame(self)
        self._startButton= tk.Button(f, text='Start',fg='green',command=self.Start)
        self._startButton.pack(side=tk.LEFT)
        self._stopButton = tk.Button(f, text='Stop', fg='red',command=self.Stop)
        self._stopButton.pack(side=tk.LEFT)
        self._resetButton= tk.Button(f, text='Reset', fg='orange',command=self.Reset)
        self._resetButton.pack(side=tk.LEFT)
        self.pack(side=tk.TOP)
        f.pack(side=tk.BOTTOM)

    def _update(self):
        # update the label with elapsed time
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        # set the time string to Minutes:Seconds:Hundreths
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        # Start the stopwatch, ignore if running.
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
            self._startButton.config(state=tk.DISABLED)
            self._stopButton.config(state=tk.NORMAL)
            self._resetButton.config(state=tk.NORMAL)


    def Stop(self):
        # Stop the stopwatch, ignore if stopped.
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0
            self._stopButton.config(text='Resume')
            self._startButton.config(state=tk.NORMAL)
            self._resetButton.config(state=tk.NORMAL)

        else:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
            self._stopButton.config(text='Stop')
            self._startButton.config(state=tk.DISABLED)
            self._resetButton.config(state=tk.DISABLED)

    def Reset(self):
        # Reset the stopwatch.
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
        self._running = 0
    # Enable the Start button
        self._startButton.config(state=tk.NORMAL)
        self._stopButton.config(text='Stop')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Stopwatch")
    sw = Stopwatch(root)
    sw.pack(side=tk.TOP)

    root.mainloop()

# The code is pretty straightforward. The Stopwatch class is a subclass of Frame and has a constructor that calls makeWidgets() to create the widgets. The makeWidgets() method creates a Label widget to display the time and a Frame widget to hold the three buttons. The buttons are created using the Button widget and the command argument is used to specify the method to call when the button is pressed. The Start() method is called when the Start button is pressed, the Stop() method is called when the Stop button is pressed, and the Reset() method is called when the Reset button is pressed.