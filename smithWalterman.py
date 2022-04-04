{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "smithWalterman.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMRYpTxMhrwZTixf4oqHxNI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Blarissa/DisciBioInformatica/blob/main/smithWalterman.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Adkz93Ssssql"
      },
      "source": [
        "\n",
        "a=\"USP-CURSO DE EXTENSÃO\"\n",
        "print(a.split)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ql3TUlfAxY4O"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "_rEn_Vtt9dBs"
      }
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5hUaDPTUnKV2"
      },
      "source": [
        "def smithWalterman():           \n",
        "        \n",
        "    sequencia1='ATCGTCTTTA'\n",
        "    sequencia2='GTCGTCATTT'\n",
        "    linhas=len(sequencia2)+1\n",
        "    colunas=len(sequencia1)+1\n",
        "    matriz=espelho=[]\n",
        "    gap=-2\n",
        "    match=1\n",
        "    mismatch=-1\n",
        "    esquerda=topo=diagonal=valor=score=0\n",
        "    \n",
        "    def validaSequencia(sequencia):\n",
        "        for i in range(len(sequencia)):\n",
        "            if sequencia[i] not in ['A', 'T', 'C', 'G']:                \n",
        "                return False\n",
        "        \n",
        "        return True\n",
        "\n",
        "    def inicializaMatriz():            \n",
        "        for i in range(linhas):\n",
        "            matriz[i][0]=gap*i\n",
        "        \n",
        "        for j in range(colunas):\n",
        "            matriz[0][j]=gap*j    \n",
        "\n",
        "    def match(letra1,letra2):\n",
        "        if(letra1==letra2):\n",
        "            return True\n",
        "        else:\n",
        "            False\n",
        "\n",
        "    def preencheMatriz():\n",
        "        for i in range(1,linhas):      \n",
        "            for j in range (1,colunas):\n",
        "                if(match(sequencia1[j-1],sequencia2[i-1])==True):\n",
        "                    valor=match\n",
        "                else:\n",
        "                    valor=mismatch\n",
        "                \n",
        "                diagonal=matriz[i-1][j-1]+valor\n",
        "                topo=matriz[i-1][j]+gap\n",
        "                esquerda=matriz[i][j-1]+gap\n",
        "\n",
        "                matriz[i][j]=max(diagonal,topo,esquerda)\n",
        "                preencheEspelho(i,j)\n",
        "                \n",
        "    def preencheEspelho(i,j):\n",
        "        num=max(diagonal,topo,esquerda)\n",
        "        \n",
        "        if(num==diagonal):\n",
        "            espelho[i-1][j-1]=\"diagonal\"\n",
        "        elif(num==topo):\n",
        "            espelho[i-1][j-1]=\"topo\"\n",
        "        elif(num==esquerda):    \n",
        "            espelho[i-1][j-1]=\"esquerda\"\n",
        "\n",
        "    def backtrace():\n",
        "        sequencia=[]\n",
        "        coluna=colunas-1\n",
        "        linha=0\n",
        "        \n",
        "        for i  in range(linhas):\n",
        "            if score <= matriz[i][coluna]:\n",
        "                pontuacao=matriz[i][coluna]\n",
        "                linha=i\n",
        "\n",
        "        linha-=1\n",
        "        coluna-=1\n",
        "\n",
        "        while(True):\n",
        "            \n",
        "            if(espelho[linha][coluna]==\"diagonal\"):\n",
        "                sequencia[0]+=sequencia2[coluna]\n",
        "                sequencia[1]+=sequencia1[linha]\n",
        "                linha-=1\n",
        "                coluna-=1\n",
        "            \n",
        "            elif(espelho[linha][coluna]==\"topo\"):\n",
        "                sequencia[0]+=sequencia2[coluna]\n",
        "                sequencia[1]+='-'\n",
        "                coluna-=1\n",
        "            \n",
        "            elif(espelho[linha][coluna]==\"diagonal\"):    \n",
        "                sequencia[0]+='-'\n",
        "                sequencia[1]+=sequencia1[linha]\n",
        "                linha-=1\n",
        "\n",
        "            if((not linha and not coluna) or (not espelho[linha][coluna])):\n",
        "                break                    \n",
        "\n",
        "        sequencia[0]=inverte(sequencia[0])\n",
        "        sequencia[1]=inverte(sequencia[1])\n",
        "\n",
        "        return sequencia\n",
        "\n",
        "    def inverte(sequencia):\n",
        "        str=\"\"               \n",
        "\n",
        "        for i in range(len(sequencia),0):\n",
        "            str+=sequencia[i]\n",
        "        return str   \n",
        "\n",
        "    def imprime():\n",
        "        print('>Sequencia 1 = ',sequencia1,\n",
        "            '\\n>Sequencia 2 = ',sequencia2)\n",
        "\n",
        "        sequencia=backtrace()\n",
        "\n",
        "        print('\\n',sequencia[0],\n",
        "            '\\n',sequencia[1],\n",
        "            '\\nScore = ',score)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}