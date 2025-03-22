# Tutorial
  - [Neural Networks from Scratch - P.1 Intro and Neuron Code)](https://youtu.be/Wo5dMEP_BbI?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3) by [sentdex](https://www.youtube.com/@sentdex)

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