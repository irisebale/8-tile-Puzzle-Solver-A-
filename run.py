from flask import Flask, render_template
import main
import time

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main1():

    main.shuffler()
    initialState = main.initial_state
    print initialState
    sec = time.time()
    a, b = main.astarsearch(initialState)
    sec_astar = round(time.time()-sec, 6)
    moves = main.backtrace2()
    print str(moves)+": astar"
    sec2 = time.time()
    c, d = main.bfs(initialState)
    sec_bfs = round(time.time()-sec2, 6)
    moves2 = main.backtrace()
    print str(moves2)+": bfs"
    print(sec_astar)
    print(sec_bfs)

    return render_template('front.html', initial=initialState, moves=moves, moves2=moves2, main=b, bfs=d, sec_astar=sec_astar, sec_bfs=sec_bfs)

app.run(debug=True)

