# Tensorflow
Tensorflow ML

## Tensorboard
To run tensorboard examples
First uncomment the Lesson 5 region and comment the rest. 
In Emacs
```bash
M-x comment-region 
M-x uncomment-region
```
M-x can be obtained in Ubuntu by:
```bash
Alt + X
```


```python
	python3 SGD/sgd_benchmark.py
```

Then on another terminal 

```bash
	cd SGD
	tensorboard --logdir=output_sgd_benchmark
```

Then go to the ip address shown in the console window ...
In my case it is 

```bash
	http://vibhatha-ThinkPad-p50:6006
```
