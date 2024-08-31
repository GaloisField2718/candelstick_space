# Understanding the space of Candelstick charts

In mathematics I always loved [Topology](https://en.wikipedia.org/wiki/Topology) and [Fundamental algebra](https://en.wikipedia.org/wiki/Algebra). 

When I discovered the trading and [Candelstick charts](https://en.wikipedia.org/wiki/Candlestick_chart) I was fascinated by the idea of understanding the space of the charts. More precisely, when we are looking a candelstick chart what is the underlying space that we are looking at?

## Introduction

In this repository I want to try some ideas to understand the space of candelstick charts. I'll use mainly Python to stay in something easy to implement. 

First we can remark that each candle is a tuple of 4 elements: `(high, low, open, close)`. This tuple can be seen as a point in a 4-dimensional space over the real numbers[^1]. I'll make constant use of real numbers property. To consider this space over $\mathbb{Q}^4$ would change everything. i

Each candle is indexed by it's timestamp. We can view one full candle as: `[Time, (high, low, open, close)]`. At a given time we have a vector of 4 elements.

So, the **space of candelstick charts** can be described by: $\mathcal{T} \times \mathbb{R}^4$ where $\mathcal{T}$ is the *time domain*. 
The space $\mathbb{R}^4$, is well known by mathematicians since a pretty long time. It's the 4-dimensional space over the real numbers. What is interesting with this space is that we can make a lot of computation over it and we have a lot of theorem that can be applied to it.
The *time domain* is more tricky. We are considering a discrete space (because we move from one candle to another) but not containing numbers (or at least not only). This space will be considered and studied thereafter. 

[^1]: We can also consider the space of Decimals numbers (floats) or even the space of rational numbers. But for now we will stick to the real numbers. Some interesting considerations can come out from this choice. If we stick to Rational numbers we should consider polynomials as the underlying space.

[^2]: TODO -> Study consequences of the choice of $p$ on the space of candelstick charts.

## Distance considerations

A small reminder about distances in $\mathbb{R}^4$. The most common distance is the Euclidean distance. It's defined as:
$\forall X \in \mathbb{R}^4, \forall Y \in \mathbb{R}^4, d(X,Y) = \sqrt{\sum_{i=1}^4 (x_i - y_i)^2}$, where $X = (x_1, x_2, x_3, x_4)$ and $Y = (y_1, y_2, y_3, y_4)$.
The Euclidean distance is built over the Norm 2, defined as: $\|X\|_2 = \sqrt{\sum_{i=1}^4 x_i^2}$.

The distance can be rewritten as: $d(X,Y) = \|X - Y\|_2$.

In general we can define any $p$-norm[^2] where $p$ is a integer greater than 1. The $p$-norm is defined as: $\|X\|_p = \left(\sum_{i=1}^4 |x_i|^p\right)^{1/p}$.

We can define: $\|X\|_1 = \sum_{i=1}^4 |x_i|$ and $\|X\|_{\infty} = \max_{i=1}^4 |x_i|$.

Each norm defines a distance. The $p$-norm defines the $p$-distance as: $d_p(X,Y) = \|X - Y\|_p$.

*Remark*: The $p$-distance is a metric on $\mathbb{R}^4$. We can compute the norm through: $\|X\|_p = d_p(X,0)$. In this repo I choose to define the distance and compute the norm from the distance. Inversion of this calculus is possible. 


### Implementation

The Euclidean distance, Euclidean norm (2-norm) and the $3$-norm are implemented in the file `distances.py`.

To implement such distances we need to define the vectors operations $(-(x), +,~\text{and}~\times)$. This is done at the beginning of `distances.py`.
Useful functions as `power` and `sub` (substraction) are also defined.

To practice on real data, there is the file `data.py`. This script has mainly 2 functions: `extract_tuples` and `extract` which is extracting data from a ticker and create a list of tuples indexed by timestamp[^3]. I'm using [`yfinance`](https://pypi.org/project/yfinance/) to get market data. 

The file `main.py` is the main file to run. It's a simple script that will load the data from a ticker and compute the Euclidean distance between each candle with providing some information about the data (in the standard output, `print`).

[^3]: To stay simple I haven't built in from Pandas dataframe. If it's necessary in the future it can be done, but it will be a bit more complex and heavy. 

### First results

```
Between :  2024-08-01  and  2024-08-02  the distance is:  2713.579
Between :  2024-08-01  and  2024-08-02  the distance3 is:  2165.69
( 61618.9258 , 59605.7344 , 61208.7695 , 59700.8203 )  ➡️  ( 60792.9336 , 57700.4727 , 59706.9102 , 60592.8086 )
Norm2 of X0 is:  121080.2915354364
Norm2 of X1 is:  119421.64336988732
🔴 ➡️  💚 

Between :  2024-08-02  and  2024-08-03  the distance is:  4747.585
Between :  2024-08-02  and  2024-08-03  the distance3 is:  4423.613
( 60792.9336 , 57700.4727 , 59706.9102 , 60592.8086 )  ➡️  ( 60758.832 , 56027.5586 , 60589.0977 , 56238.3281 )
Norm2 of X0 is:  119421.64336988732
Norm2 of X1 is:  116895.30057390696
💚 ➡️  🔴 

Between :  2024-08-03  and  2024-08-04  the distance is:  5957.094
Between :  2024-08-03  and  2024-08-04  the distance3 is:  5199.151
( 60758.832 , 56027.5586 , 60589.0977 , 56238.3281 )  ➡️  ( 56930.707 , 54812.9531 , 56238.0938 , 55585.6992 )
Norm2 of X0 is:  116895.30057390696
Norm2 of X1 is:  111794.71533517641
🔴 ➡️  🔴 

Between :  2024-08-04  and  2024-08-05  the distance is:  3547.235
Between :  2024-08-04  and  2024-08-05  the distance3 is:  3024.044
( 56930.707 , 54812.9531 , 56238.0938 , 55585.6992 )  ➡️  ( 55936.4453 , 52407.6719 , 55582.0312 , 53266.5352 )
Norm2 of X0 is:  111794.71533517641
Norm2 of X1 is:  108637.63597993355
🔴 ➡️  🔴 

Between :  2024-08-05  and  2024-08-06  the distance is:  9043.694
Between :  2024-08-05  and  2024-08-06  the distance3 is:  7889.525
( 55936.4453 , 52407.6719 , 55582.0312 , 53266.5352 )  ➡️  ( 53407.9844 , 45038.3789 , 53260.4141 , 49304.3516 )
Norm2 of X0 is:  108637.63597993355
Norm2 of X1 is:  100739.56108903051
🔴 ➡️  🔴 

Between :  2024-08-06  and  2024-08-07  the distance is:  6251.19
Between :  2024-08-06  and  2024-08-07  the distance3 is:  -2752.445
( 53407.9844 , 45038.3789 , 53260.4141 , 49304.3516 )  ➡️  ( 52206.2305 , 49287.7461 , 49304.25 , 51285.4648 )
Norm2 of X0 is:  100739.56108903051
Norm2 of X1 is:  101073.63843481512
🔴 ➡️  💚 

Between :  2024-08-07  and  2024-08-08  the distance is:  2398.671
Between :  2024-08-07  and  2024-08-08  the distance3 is:  -1973.969
( 52206.2305 , 49287.7461 , 49304.25 , 51285.4648 )  ➡️  ( 52864.1992 , 50001.5273 , 51291.2461 , 50356.4531 )
Norm2 of X0 is:  101073.63843481512
Norm2 of X1 is:  102280.69507337733
💚 ➡️  🔴 

Between :  2024-08-08  and  2024-08-09  the distance is:  7724.11
Between :  2024-08-08  and  2024-08-09  the distance3 is:  -6901.146
( 52864.1992 , 50001.5273 , 51291.2461 , 50356.4531 )  ➡️  ( 57400.8945 , 50099.9453 , 50358.8047 , 56537.1602 )
Norm2 of X0 is:  102280.69507337733
Norm2 of X1 is:  107411.94953428752
🔴 ➡️  💚 

Between :  2024-08-09  and  2024-08-10  the distance is:  7707.752
Between :  2024-08-09  and  2024-08-10  the distance3 is:  -6869.068
( 57400.8945 , 50099.9453 , 50358.8047 , 56537.1602 )  ➡️  ( 56575.3906 , 54538.6836 , 56553.7188 , 55731.7852 )
Norm2 of X0 is:  107411.94953428752
Norm2 of X1 is:  111712.12030058283
💚 ➡️  🔴 

Between :  2024-08-10  and  2024-08-11  the distance is:  1093.224
Between :  2024-08-10  and  2024-08-11  the distance3 is:  674.599
( 56575.3906 , 54538.6836 , 56553.7188 , 55731.7852 )  ➡️  ( 56266.7656 , 55189.3477 , 55732.8086 , 55783.0938 )
Norm2 of X0 is:  111712.12030058283
Norm2 of X1 is:  111488.62058067034
🔴 ➡️  💚 

Between :  2024-08-11  and  2024-08-12  the distance is:  2641.509
Between :  2024-08-11  and  2024-08-12  the distance3 is:  2343.488
( 56266.7656 , 55189.3477 , 55732.8086 , 55783.0938 )  ➡️  ( 56545.3906 , 53458.4336 , 55782.25 , 53807.8906 )
Norm2 of X0 is:  111488.62058067034
Norm2 of X1 is:  109827.74616168832
💚 ➡️  🔴 

Between :  2024-08-12  and  2024-08-13  the distance is:  2366.457
Between :  2024-08-12  and  2024-08-13  the distance3 is:  2076.338
( 56545.3906 , 53458.4336 , 55782.25 , 53807.8906 )  ➡️  ( 55526.2031 , 52791.1094 , 53807.8125 , 54274.4219 )
Norm2 of X0 is:  109827.74616168832
Norm2 of X1 is:  108217.62343074982
🔴 ➡️  💚 

Between :  2024-08-13  and  2024-08-14  the distance is:  1365.578
Between :  2024-08-13  and  2024-08-14  the distance3 is:  -1108.307
( 55526.2031 , 52791.1094 , 53807.8125 , 54274.4219 )  ➡️  ( 56103.043 , 53564.6992 , 54275.9688 , 55119.6719 )
Norm2 of X0 is:  108217.62343074982
Norm2 of X1 is:  109548.10566042917
💚 ➡️  💚 

Between :  2024-08-14  and  2024-08-15  the distance is:  2031.269
Between :  2024-08-14  and  2024-08-15  the distance3 is:  1724.288
( 56103.043 , 53564.6992 , 54275.9688 , 55119.6719 )  ➡️  ( 55959.7383 , 53082.8438 , 55121.0234 , 53342.2539 )
Norm2 of X0 is:  109548.10566042917
Norm2 of X1 is:  108779.61154690293
💚 ➡️  🔴 

Between :  2024-08-15  and  2024-08-16  the distance is:  3126.337
Between :  2024-08-15  and  2024-08-16  the distance3 is:  2544.468
( 55959.7383 , 53082.8438 , 55121.0234 , 53342.2539 )  ➡️  ( 54466.4531 , 51189.1562 , 53338.6133 , 52458.4883 )
Norm2 of X0 is:  108779.61154690293
Norm2 of X1 is:  105753.60461587431
🔴 ➡️  🔴 
...

Between :  2024-08-25  and  2024-08-26  the distance is:  574.168
Between :  2024-08-25  and  2024-08-26  the distance3 is:  -521.402
( 57583.5898 , 56839.0508 , 57222.3203 , 57338.5391 )  ➡️  ( 58089.5742 , 57029.8867 , 57336.1914 , 57494.3086 )
Norm2 of X0 is:  114493.01077680534
Norm2 of X1 is:  114977.56726162547
💚 ➡️  💚 

Between :  2024-08-26  and  2024-08-27  the distance is:  1470.792
Between :  2024-08-26  and  2024-08-27  the distance3 is:  1283.143
( 58089.5742 , 57029.8867 , 57336.1914 , 57494.3086 )  ➡️  ( 57628.9688 , 56290.1406 , 57502.0664 , 56321.1367 )
Norm2 of X0 is:  114977.56726162547
Norm2 of X1 is:  113878.16319720492
💚 ➡️  🔴 

Between :  2024-08-27  and  2024-08-28  the distance is:  5539.725
Between :  2024-08-27  and  2024-08-28  the distance3 is:  4836.327
( 57628.9688 , 56290.1406 , 57502.0664 , 56321.1367 )  ➡️  ( 56603.8125 , 51962.1875 , 56320.2852 , 53237.3359 )
Norm2 of X0 is:  113878.16319720492
Norm2 of X1 is:  109134.0871499784
🔴 ➡️  🔴 

Between :  2024-08-28  and  2024-08-29  the distance is:  3980.882
Between :  2024-08-28  and  2024-08-29  the distance3 is:  3558.767
( 56603.8125 , 51962.1875 , 56320.2852 , 53237.3359 )  ➡️  ( 54091.1875 , 52101.2031 , 53240.7305 , 53060.8203 )
Norm2 of X0 is:  109134.0871499784
Norm2 of X1 is:  106256.3784660014
🔴 ➡️  🔴 

Between :  2024-08-29  and  2024-08-30  the distance is:  643.04
Between :  2024-08-29  and  2024-08-30  the distance3 is:  -525.983
( 54091.1875 , 52101.2031 , 53240.7305 , 53060.8203 )  ➡️  ( 53942.1406 , 52377.9336 , 53585.6133 , 53503.2695 )
Norm2 of X0 is:  106256.3784660014
Norm2 of X1 is:  106710.91912565904
🔴 ➡️  🔴 

Last Distance is:  643.0398030809143
```

The emojis Green and Red are used to show if the price goes up or down (candle color). Emojis are used to make the output more readable and a bit funnier.

### What to understand from this?

The Euclidean distance can be seen as a kind of volatility measure. The higher the distance the higher the volatility. The 3-norm distance is a bit more stable. Some tests with different norms can be done to see if we can have a better understanding of the space of candelstick charts.

Implement $p$-norms and compute the distance for $p=1,2,3,\infty$.

Something interesting to do could be to take mean of distances or to compute distances between candles involves in big distances. 
For example, between :  2024-08-05  and  2024-08-06 the distance is pretty high ~9000. If we take the distance between each candle and each candle between 2024-08-08  and  2024-08-09, can we conclude something?

## Sequences of candles

As the time is moving ahead with constant steps[^4] (defined by Timeframe unit in trading), we can consider the space of candelstick charts as a sequence of points in $\mathbb{R}^4$. This sequence can be seen as a path in the space? Is it possible for such sequences to be convergent? 

### Definitions & elementary results

**Definition**: A sequence of points in $\mathbb{R}^4$ is said to be convergent if there exists a point $X \in \mathbb{R}^4$ such that for all $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that for all $n \geq N$ we have $d(X_n, X) < \epsilon$.

**Definition**: A sequence of points in $\mathbb{R}^4$ is said to be Cauchy if for all $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that for all $n,m \geq N$ we have $d(X_n, X_m) < \epsilon$.

**Proposition**: Any convergent sequence is Cauchy.
One proof can be find here: [SML_LFJO_2.pdf](https://www.math.nagoya-u.ac.jp/~richard/teaching/f2021/SML_LFJO_2.pdf)

**Definition**: We say that a Space is **complete** if every Cauchy sequence is convergent.
For example $\mathbb{R}$ is complete. 
*Remark*: Any cartesian product of complete spaces is complete.

An example of non-complete space is $\mathbb{Q}$, the set of rational numbers. You can find details in previous link.

### Propositions and intuitions

**Proposition**: No sequence from candelstick charts can be Cauchy.
**Proof**: Indeed let's suppose that a sequence of candelstick charts is convergent. Then the sequence is Cauchy. But we can have a Black Swan event or any unpredictable event that can make the sequence not bounded. 
*Cauchy*: $\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n,m \geq N, d(X_n, X_m) < \epsilon$. But if there is a Black Swann, we can have $d(X_n, X_m) > M$ where $M$ is a real number, for $n,m$ big enough. Indeed, a big gap in the price will make the distance between two points very high. We can just take one candle before the event and one candle after the event to have a distance bigger than $M$.

**Proposition**: No sequence from candelstick charts can be convergent.
**Proof**: Any convergent sequence is Cauchy. But we have shown that no such sequences can be Cauchy.

This proposal is a counter argument to the fact that the free Market will create a price stability over time.

Study: $$(\mathcal{T} \times \mathbb{R}^4)^{\mathbb{N}}$$


[^4]: By default on `yfinance` the Timeframe unit is 1 day.
