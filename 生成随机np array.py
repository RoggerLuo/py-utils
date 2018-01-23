import numpy as np

np.random.rand(4) #随机小数，一个4位长度的一维数组
np.random.rand(4,2) #随机小数，一个4x2的二维数组，
np.random.random((3,3,4)) # 也是生成随机小数
np.random.random((3,3,4))  ===  np.random.rand(3,3,4)

# 生成随机 整数
np.random.randint(0,10,size=[3,3,3])

#正态分布 normal distribution 
np.random.randn(3,2,1) #第一个参数也是shape




我们更经常会用到的np.random.randn(size)所谓标准正态分布（μ=0,σ=1），
对应于np.random.normal(loc=0, scale=1, size)

loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值


# tf的正态分布
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),name="weights")

biases = tf.Variable(tf.zeros([200]), name="biases")

mean: 均值
stddev: 标准差