stochastic gradient descent
随机梯度下降

1. 批量放入
2. 传统
 
   ``` 
   W +=-Learning_rate * dx
   ```
    
3. momentum 动量更新

   ``` 
   m = b1*m - learning_rate *dx
   W +=m
   ```
    
4. Adagrad

   ``` 
   v += dx^2
    W += -learning_rate *dx/根号v 
    ```
    
5. RMSProp
    ```
    v = b1*v+(1-b1)*dx^2
    W +=-learning_rate *dx/根号v
    ```
6. Adam
    ```
    m = b1*m - (1-b1) *dx
    v = b1*v+(1-b1)*dx^2
    W +=-learning_rate *dx/根号v
    ``` 
    



