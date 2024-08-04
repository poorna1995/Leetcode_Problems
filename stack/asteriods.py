asteroids = [8,-8]
# [5,10,-5]

def asteroidCollision(asteroids):
    notExploded=[]
    stack=[]
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1]>0:
                top_asteriod =stack[-1]
                if top_asteriod < -asteroid:
                    stack.pop()
                elif top_asteriod == -asteroid:
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
    return stack


    # for i in range(len(asteroids)):
    #     if asteroids[i] <0 and asteroids[i+1]>0:
    #         explode = min(asteroids[i], asteroids[i + 1])
    #     notExploded.append(max(-explode, -asteroids[i + 1]


print(asteroidCollision(asteroids))