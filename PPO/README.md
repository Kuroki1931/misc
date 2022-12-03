# PPO

# 流れ
**trajectory listの取得**  
input-state-箱の位置、箱の速度、ポールの角度、角速度  
→  
Network (4, 256)-relu-(256, 2)-softmax-Categorical  
→  
actionを得る  
→  
env.step(action)で次のstepへ。  
T_horizon回学習を進めて、trajectory listを得る。  

**最適化**  
更新前と更新後のstateからdeltaを計算する。  
→  
報酬を計算する。  
→  
Networkを最適化する。

# 参考
https://github.com/seungeunrho/minimalRL
