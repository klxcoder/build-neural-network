# Tutorial
  - [Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)](https://www.youtube.com/watch?v=w8yWXqWQYmU)

# Create conda env

```bash
conda create -n py310 python=3.10
```

# Activate conda env

```bash
(base) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$ conda env list
# conda environments:
#
base                  *  /home/klx/miniconda3
py310                    /home/klx/miniconda3/envs/py310

(base) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$ conda activate py310

(py310) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$
```

# Check python version

```bash
(py310) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$ python -V                
Python 3.10.16

(py310) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$ poetry run python -V     
Python 3.10.16

(py310) ┌──(klx㉿kali)-[~/build-neural-network] (main)
└─$ 
```

# poetry install

```bash
poetry install
```