# MapReducer: traballando con MapReduce

## Exercicio 1.1

A función do  mapper executarase sobre todas e cada unhas liñas do ficheiro de datos. O código do mapper anterior non funcionará correctamente se se encontra algunha liña que non encaixa co número exacto de valores separados por tabulador.
Mellora o código de xeito que se encontra algunha liña cun formato non axeitado a descarte e siga traballando coa liña seguinte.

Non esquezas darlle permiso de execución aos scripts mapper.py e reducer.py:

chmod +x mapper.py reducer.py
Executa o código mellorado sobre o ficheiro de proba:

executa o mapper e o reducer sobre o ficheiro de proba
cat testfile.txt | ./mapper | sort | ./reducer

Execución desde Hadoop
Como se pode ver no código, non se trata dun algoritmo complexo e ademais pode executarse desde a consola lanzando os scripts de xeito manual.
A vantaxe que ofrece Hadoop é que poden utilizarse os mesmos algoritmos sobre ficheiros moito máis grandes, repartidos nun sistema de ficheiros distribuído e utilizar múltiples computadores para procesar os datos.

Antes de continuar asegúrate de colocar o ficheiro purchases.txt no almacenamento distribuído.

hdfs dfs -put purchases.txt input/

Para lanzar o proceso en Hadoop é necesario utilizar a ferramenta Streaming, que permite executar scripts noutras linguaxes diferentes a java. A sintaxe sería a seguinte:

$ mapred streaming 
    -files mapper.py,reducer.py
    -input myInputDirs \
    -output myOutputDir \
    -mapper script_mapper
    -reducer script_reducer
Documentación de Hadoop Streaming: https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html


Executa a tarefa con hadoop:

mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA -mapper "python mapper.py" -reducer "python reducer.py"

## Exercicicio 1.2

Redefine o mapper e o reducer de xeito que devolvan un ficheiro co total de vendas por categoría.

Fai as probas cun extracto do ficheiro de vendas.

Executa o traballo desde Hadoop sobre purchases.txt almacenado en HDFS.

## Exercicio 1.3

Redefine o mapper e o reducer de xeito que se obteña a venda máis alta para cada tipo de pago das rexistradas en todo o ficheiro.

Fai as probas cun extracto do ficheiro de vendas.

Executa o traballo desde Hadoop sobre purchases.txt almacenado en HDFS.

Consulta o resultado: a que  pode ser debido?


## Exercicio 1.4

Modifica o exercicio anterior para que o resultado da execución sexa o máximo absoluto de todas as vendas rexistradas.


## Exercicio 1.5

Redefine o mapper e o reducer de xeito que se obteña o total de vendas.

Fai as probas cun extracto do ficheiro de vendas.

Executa o traballo desde Hadoop sobre purchases.txt almacenado en HDFS.

Entrega
A partir do código inicial do mapper e reducer vistos na clase deben realizarse os diferentes exercicios modificando o código que sexa necesario.

Crea unha nova carpeta para cada exercicio: exercicio1_1, exercicio1_2, ... dentro dunha carpeta xeral "mapreduce". Sube todo o código a un repositorio da túa creación e copia o enlace na entrega da tarefa unha vez estea listo.

O repositorio pode estar en github, gitlab ou naquel que consideres oportuno.
