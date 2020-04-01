{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "class Clock:\n",
    "\n",
    "    def __init__(self, hours):\n",
    "        self.hours = hours\n",
    "        self.cycles = 0\n",
    "        self.time = 0\n",
    "\n",
    "    def tick(self):\n",
    "        self.time += 1\n",
    "        if self.time == self.hours:\n",
    "        \tself.time = 0\n",
    "        \tself.cycles += 1\n",
    "\n",
    "    def __eq__(self, other):\n",
    "    \treturn (self.time + self.hours*self.cycles) == (other.time + other.hours*other.cycles)\n",
    "\n",
    "\n",
    "clock1 = Clock(12)\n",
    "clock2 = Clock(9)\n",
    "\n",
    "clock1.tick()\n",
    "clock1.tick()\n",
    "clock1.tick()\n",
    "clock2.tick()\n",
    "clock2.tick()\n",
    "print(clock1 == clock2)\n",
    "clock2.tick()\n",
    "print(clock1 == clock2)"
   ]
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
