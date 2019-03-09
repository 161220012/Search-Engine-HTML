#同理我们来看一下鬼切
x=18
y=20
attack=x
strike=y
damage1=(x*0.06*3350+3350+486)*(y*0.07+1.6)
print('常规认为的爆伤拉满伤害为',damage1)

while x<30:
    x=x+1
    y=y-1
    damage2=(x*0.06*3350+3350+486)*(y*0.07+1.6)
    if(damage2>damage1):
        damage1=damage2
        attack=x
        strike=y
print('最科学的搭配方案伤害，攻击点数，爆伤点数分别为',damage1,attack,strike)