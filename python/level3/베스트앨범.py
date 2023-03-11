def solution(genres, plays):
    answer = []
    genres_total_play = dict()
    genres_plays = dict()
    
    for i in range(len(plays)):
        genre, play = genres[i], plays[i]
        if genre not in genres_total_play:
            genres_total_play[genre] = play
            genres_plays[genre] = [(-play, i)]
        else:
            genres_total_play[genre] += play
            genres_plays[genre].append((-play, i))
    
    for genre, _ in sorted(genres_total_play.items(), key = lambda item: item[1], reverse = True):
        for song in sorted(genres_plays[genre])[:2]:
            answer.append(song[1])
            
    return answer
