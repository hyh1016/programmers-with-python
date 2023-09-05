def solution(plans):
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        h, m = map(int, start.split(':'))
        plans[i] = [name, h*60+m, int(playtime)]
    plans.sort(key=lambda x: x[1])
    
    end = []
    stop = []
    for i in range(len(plans)-1):
        name, start, playtime = plans[i]
        next_start = plans[i+1][1]
        while True:
            # 끝나거나 멈추거나
            if start+playtime > next_start: # 멈추고 새로운 과제 시작
                rest = start+playtime - next_start
                stop.append((name, rest))
                break
            else: # 끝냈으면 다음 과제 시작하기 전까지 멈춘 과제 진행
                end.append(name)
                if not stop: # 멈춘 과제 없으면 다음 과제 시작까지 아무 일도 하지 않음
                    break
                start = start+playtime
                name, playtime = stop.pop()
    end.append(plans[-1][0])
    while stop:
        end.append(stop.pop()[0])
    return end