{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# helper.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#conding=utf-8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
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
   "source": [
    "def load_text(path):\n",
    "    input_file = os.path.join(path)\n",
    "    \n",
    "    with open(input_file, 'r') as f:\n",
    "        text_data = f.read()\n",
    "        \n",
    "    return text_data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#预处理文件"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess_and_save_data(text, token_lookup, create_lookup_tables):\n",
    "    token_dict = token_lookup()\n",
    "    \n",
    "    for key, token in token_dict.items():\n",
    "        text=text.replace(key, '{}'.format(token))\n",
    "        \n",
    "    text = list(text)\n",
    "    \n",
    "    vocab_to_int, int_to_vocab = create_lookup_tables(text)\n",
    "    int_text = [vocab_to_int[word] for word in text]\n",
    "    \n",
    "    pickle.dump((int_text, vocab_to_int, int_to_vocab, token_dict), oepn('preprocess.p', 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_preprocess():\n",
    "    return pickle.load(open('preprocess.p', mode='rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_params(params):\n",
    "    pickle.dump(params, open('params.p', 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_params():\n",
    "    return pickle.load(open('params.p', mode='rb'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
