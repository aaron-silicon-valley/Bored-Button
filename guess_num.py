{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled9.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMC2rvUQ5ohm7QcDS4W/vZQ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yXcuv8eP7p6p",
        "outputId": "c56073e0-498f-4885-9b3e-77af8e9189de"
      },
      "source": [
        "from random import randrange \n",
        "\n",
        "\n",
        "l = list(range(1, 11))\n",
        "num_l = random.choice(l)\n",
        "\n",
        "guess_num = num_l\n",
        "\n",
        "g = input('enter the guess number: '+ 'numbers are from {}'.format(l))\n",
        "while True:\n",
        "  if int(g) == guess_num:\n",
        "    print('you got the number congratulations')\n",
        "    print(guess_num)\n",
        "    break\n",
        "  else:\n",
        "    print('sorry try again')\n",
        "    # print(guess_num)\n",
        "    g = input('enter the guess number: ')\n",
        "    continue\n",
        "\n"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "enter the guess number: numbers are from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]4\n",
            "sorry try again\n",
            "7\n",
            "enter the guess number: 7\n",
            "you got the number congratulations\n",
            "7\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}