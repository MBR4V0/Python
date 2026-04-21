{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "ir",
      "display_name": "R"
    },
    "language_info": {
      "name": "R"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 611
        },
        "id": "a3OB-u6drgKa",
        "outputId": "79a316a5-9639-4517-e94c-9f9a48092af7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Loading required package: ggplot2\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Testando função e coletando dados para o gráfico...\n",
            "\n",
            "Tamanho:        10 | Tempo: 0.005799 segundos\n",
            "Tamanho:       100 | Tempo: 0.000021 segundos\n",
            "Tamanho:      1000 | Tempo: 0.000072 segundos\n",
            "Tamanho:     10000 | Tempo: 0.000713 segundos\n",
            "Tamanho:    100000 | Tempo: 0.006821 segundos\n",
            "Tamanho:   1000000 | Tempo: 0.066631 segundos\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "plot without title"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAMAAADKOT/pAAADAFBMVEUAAAABAQECAgIDAwME\nBAQFBQUGBgYHBwcICAgJCQkKCgoLCwsMDAwNDQ0ODg4PDw8QEBARERESEhITExMUFBQVFRUW\nFhYXFxcYGBgZGRkaGhobGxscHBwdHR0eHh4fHx8gICAhISEiIiIjIyMkJCQlJSUmJiYnJyco\nKCgpKSkqKiorKyssLCwtLS0uLi4vLy8wMDAxMTEyMjIzMzM0NDQ1NTU2NjY3Nzc4ODg5OTk6\nOjo7Ozs8PDw9PT0+Pj4/Pz9AQEBBQUFCQkJDQ0NERERFRUVGRkZHR0dISEhJSUlKSkpLS0tM\nTExNTU1OTk5PT09QUFBRUVFSUlJTU1NUVFRVVVVWVlZXV1dYWFhZWVlaWlpbW1tcXFxdXV1e\nXl5fX19gYGBhYWFiYmJjY2NkZGRlZWVmZmZnZ2doaGhpaWlqampra2tsbGxtbW1ubm5vb29w\ncHBxcXFycnJzc3N0dHR1dXV2dnZ3d3d4eHh5eXl6enp7e3t8fHx9fX1+fn5/f3+AgICBgYGC\ngoKDg4OEhISFhYWGhoaHh4eIiIiJiYmKioqLi4uMjIyNjY2Ojo6Pj4+QkJCRkZGSkpKTk5OU\nlJSVlZWWlpaXl5eYmJiZmZmampqbm5ucnJydnZ2enp6fn5+goKChoaGioqKjo6OkpKSlpaWm\npqanp6eoqKipqamqqqqrq6usrKytra2urq6vr6+wsLCxsbGysrKzs7O0tLS1tbW2tra3t7e4\nuLi5ubm6urq7u7u8vLy9vb2+vr6/v7/AwMDBwcHCwsLDw8PExMTFxcXGxsbHx8fIyMjJycnK\nysrLy8vMzMzNzc3Ozs7Pz8/Q0NDR0dHS0tLT09PU1NTV1dXW1tbX19fY2NjZ2dna2trb29vc\n3Nzd3d3e3t7f39/g4ODh4eHi4uLj4+Pk5OTl5eXm5ubn5+fo6Ojp6enq6urr6+vs7Ozt7e3u\n7u7v7+/w8PDx8fHy8vLz8/P09PT19fX29vb39/f4+Pj5+fn6+vr7+/v8/Pz9/f3+/v7////i\nsF19AAAACXBIWXMAABJ0AAASdAHeZh94AAAgAElEQVR4nO3dd2AUdfrH8ScJoSWAKEUQxC4q\nIIhyCCqCiHoKqAgoSLGAnCAq4IEVEQUP8AdnO8F2nGeDOwtFEbE3FBVUzg42EDAkQOglmd/O\n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\nRK5CYII="
          },
          "metadata": {
            "image/png": {
              "width": 420,
              "height": 420
            }
          }
        }
      ],
      "source": [
        "# Carregando a biblioteca para gráficos (equivalente ao matplotlib)\n",
        "if (!require(ggplot2)) install.packages(\"ggplot2\")\n",
        "library(ggplot2)\n",
        "\n",
        "# 1. Definição da função de média ponderada\n",
        "weighted_mean_custom <- function(list_of_numbers, weights) {\n",
        "  running_total <- 0\n",
        "  for (i in 1:length(list_of_numbers)) {\n",
        "    running_total <- running_total + (list_of_numbers[i] * weights[i])\n",
        "  }\n",
        "  return(running_total / sum(weights))\n",
        "}\n",
        "\n",
        "# 2. Função auxiliar para medir tempo\n",
        "medir_tempo <- function(tamanho) {\n",
        "  numeros <- runif(tamanho, min = 1, max = 100)\n",
        "  pesos <- runif(tamanho, min = 1, max = 10)\n",
        "\n",
        "  inicio <- Sys.time()\n",
        "  resultado <- weighted_mean_custom(numeros, pesos)\n",
        "  fim <- Sys.time()\n",
        "\n",
        "  # Retorna a diferença em segundos\n",
        "  return(as.numeric(difftime(fim, inicio, units = \"secs\")))\n",
        "}\n",
        "\n",
        "# 3. Listas (Vetores) para guardar os tamanhos e tempos\n",
        "tamanhos <- c(10, 100, 1000, 10000, 100000, 1000000)\n",
        "tempos <- c()\n",
        "\n",
        "cat(\"Testando função e coletando dados para o gráfico...\\n\\n\")\n",
        "\n",
        "for (tamanho in tamanhos) {\n",
        "  tempo_execucao <- medir_tempo(tamanho)\n",
        "  tempos <- c(tempos, tempo_execucao)\n",
        "\n",
        "  # Formatando a saída no console\n",
        "  cat(sprintf(\"Tamanho: %9d | Tempo: %.6f segundos\\n\", tamanho, tempo_execucao))\n",
        "}\n",
        "\n",
        "# 4. Criando o gráfico\n",
        "df_plot <- data.frame(tamanhos = tamanhos, tempos = tempos)\n",
        "\n",
        "ggplot(df_plot, aes(x = tamanhos, y = tempos)) +\n",
        "  geom_line() +\n",
        "  geom_point() +\n",
        "  scale_x_log10() + # Escala logarítmica para o eixo X\n",
        "  labs(title = \"Complexidade de Tempo da Função Média Ponderada\",\n",
        "       x = \"Tamanho da Lista (n)\",\n",
        "       y = \"Tempo de execução (segundos)\") +\n",
        "  theme_minimal()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aa838fc5"
      },
      "source": [
        "### Configurando R no Google Colab com `rpy2`\n",
        "\n",
        "Primeiro, precisamos instalar a biblioteca `rpy2`, que permite a interação entre Python e R."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "99ace72e"
      },
      "source": [
        "%%capture\n",
        "!pip install rpy2\n"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bbda2999"
      },
      "source": [
        "Agora podemos carregar a extensão `rpy2.ipython` e usar a *magic command* `%%R` para executar código R em uma célula Python. Dentro de uma célula `%%R`, você pode instalar pacotes R da mesma forma que faria em um ambiente R normal."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d6380c7e",
        "outputId": "61922451-0342-40ae-caa0-dfbb749ad830"
      },
      "source": [
        "%%R\n",
        "# Carregando a biblioteca para gráficos (equivalente ao matplotlib)\n",
        "# Verifique se o pacote já está instalado e, se não, instale-o.\n",
        "if (!require(ggplot2)) {\n",
        "  install.packages(\"ggplot2\", repos = \"http://cran.us.r-project.org\")\n",
        "}\n",
        "library(ggplot2)\n",
        "\n",
        "# Exemplo: Instalar outro pacote R (se necessário)\n",
        "# if (!require(dplyr)) {\n",
        "#   install.packages(\"dplyr\", repos = \"http://cran.us.r-project.org\")\n",
        "# }\n",
        "# library(dplyr)\n",
        "\n",
        "print(\"Pacotes R carregados com sucesso!\")"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "UsageError: Cell magic `%%R` not found.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b338dc05"
      },
      "source": [
        "Com `ggplot2` (ou qualquer outro pacote R) instalado e carregado usando `%%R`, você pode usar as funções do R em suas células `%%R` subsequentes. O código original que você forneceu estava em R e, ao executá-lo em uma célula `%%R`, ele deverá funcionar corretamente."
      ]
    }
  ]
}