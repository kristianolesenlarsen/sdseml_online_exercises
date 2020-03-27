{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Clock:\n",
    "    def __init__(self, hours, mins, secs, cycles):\n",
    "        self.hours = hours\n",
    "        self.mins = mins\n",
    "        self.secs = secs\n",
    "        self.cycles = cycles\n",
    "    \n",
    "    def Tick(self):\n",
    "        self.cycles == 0\n",
    "        self.secs += 1\n",
    "        if self.secs == 60:\n",
    "            self.secs = 0\n",
    "            self.mins += 1 \n",
    "\n",
    "        if self.mins == 60:\n",
    "            self.mins = 0\n",
    "            self.hours += 1\n",
    "\n",
    "        if self.hours == 24:\n",
    "            self.hours = 0\n",
    "            self.cycles += 1\n",
    "        yield self.cycles\n",
    "\n",
    "#I think a yield statement should be used to store number of cycles but I'm not sure this is how"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
