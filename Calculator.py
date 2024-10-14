{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMVYzkth34CiA6CnA1XWjq4",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/usmangul23/123/blob/master/Calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-rRk3oh69_n9",
        "outputId": "a1f2a856-8524-4cfa-853e-121dd8846411"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-10-14 17:04:42.786 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.791 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.793 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.795 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.797 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.805 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.807 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.809 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.813 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.814 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.824 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-14 17:04:42.825 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "#!pip install streamlit\n",
        "#!pip install pyngrok\n",
        "\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "# Simple Calculator in Streamlit\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# Inputs\n",
        "num1 = st.number_input(\"Enter the first number\", value=0.0)\n",
        "num2 = st.number_input(\"Enter the second number\", value=0.0)\n",
        "\n",
        "# Operations\n",
        "operation = st.selectbox(\"Select an operation\", [\"Add\", \"Subtract\", \"Multiply\", \"Divide\"])\n",
        "\n",
        "# Perform calculation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = num1 + num2\n",
        "    elif operation == \"Subtract\":\n",
        "        result = num1 - num2\n",
        "    elif operation == \"Multiply\":\n",
        "        result = num1 * num2\n",
        "    elif operation == \"Divide\":\n",
        "        if num2 != 0:\n",
        "            result = num1 / num2\n",
        "        else:\n",
        "            result = \"Error! Division by zero.\"\n",
        "\n",
        "    st.write(f\"The result is: {result}\")\n"
      ]
    }
  ]
}