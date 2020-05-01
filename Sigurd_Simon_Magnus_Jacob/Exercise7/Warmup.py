{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Warm-up exercise - 27/03/20: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c to small\n",
      "c to small\n",
      "Success\n"
     ]
    }
   ],
   "source": [
    "from random import uniform\n",
    "\n",
    "def retry(n):\n",
    "    def _decorator(fnc):\n",
    "        def _wrapped():\n",
    "            attempts = 0\n",
    "            while attempts < n:\n",
    "                try:\n",
    "                    fnc()\n",
    "                    print('Success')\n",
    "                    break\n",
    "                except Exception as e:\n",
    "                    print(e)\n",
    "                    attempts += 1\n",
    "        return _wrapped\n",
    "    return _decorator\n",
    "\n",
    "@retry(10)\n",
    "\n",
    "def this_might_fail():\n",
    "    c = uniform(0,1) > 0.8\n",
    "    if c: return 'Success'\n",
    "    raise ValueError('c to small')\n",
    "    \n",
    "this_might_fail()"
   ]
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
