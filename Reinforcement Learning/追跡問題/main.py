from service.gameservice import GameService
import numpy as np
import cv2
from matplotlib import pyplot

if __name__ == '__main__':

    # init
    h = 24
    w = 24
    area_shape = (h, w)
    mergin = 2
    epsilon = 0.3
    alpha = 0.3
    gamma = 0.7
    image_shape = (200, 200)

    # count
    total_plays = 300
    total_steps = np.zeros(total_plays).astype('int')
    play = 0
    steps = 0

    # construct
    gameservice = GameService()
    area, agent1, agent2, target = gameservice.construct(area_shape, mergin)

    # video writer
    #writer = cv2.VideoWriter('q-learning.mv4', cv2.cv.FOURCC('m', 'p', '4', 'v'), 20, image_shape)
    writer = cv2.VideoWriter('q-learning.mv4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 20, image_shape)

    while True:
        # disp
        print( u'play: %d, steps: %d' % (play, steps))

        # act
        gameservice.turn(area, agent1, agent2, target, epsilon)

        # update area and agents' q talbe
        agent1.update_q(area, alpha, gamma)
        agent2.update_q(area, alpha, gamma)

        # show image
        image = cv2.resize(area.state[mergin:h - mergin, mergin:w - mergin], image_shape, interpolation = cv2.INTER_NEAREST)
        writer.write(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))
        cv2.imshow('', image)
        if cv2.waitKey() == 27:
            break

        # refresh state if agents catch the taget
        steps += 1
        if agent1.reward == 3:
            print ('\033[32m' + '!!!catch the target!!!' + '\033[0m')
            gameservice.reset(area, agent1, agent2, target)
            agent1.save_q('q1.npy')
            agent2.save_q('q2.npy')
            total_steps[play] = steps
            steps = 0
            play += 1

        # count
        if play == total_plays:
            break

    pyplot.plot(np.arange(0, total_plays), total_steps)
    pyplot.savefig('graph.png')
    cv2.destroyAllWindows()
    print ('!!!finish!!!')