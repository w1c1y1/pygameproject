def levels(level):
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)

    level[0].append([0, 660, 1080, 60, GREEN, True, None])
    level[0].append([360, 280, 360, 120, GREEN, True, None])
    level[0].append([0, 180, 120, 540, GREEN, True, None])
    level[0].append([780, 540, 300, 120, GREEN, True, None])
    level[0].append([900, 420, 180, 120, GREEN, True, None])
    level[0].append([510, 140, 60, 120, YELLOW, True, "finish"])

    level[1].append([0, 660, 1080, 60, GREEN, True, None])
    level[1].append([420, 240, 360, 60, GREEN, True, None])
    level[1].append([360, 300, 360, 60, GREEN, True, None])
    level[1].append([300, 360, 360, 60, GREEN, True, None])
    level[1].append([1080 - 60, 0, 60, 720, GREEN, True, None])
    level[1].append([1080 - 300, 600, 240, 60, GREEN, True, None])
    level[1].append([1080 - 240, 540, 180, 60, GREEN, True, None])
    level[1].append([1080 - 180, 480, 120, 60, GREEN, True, None])
    level[1].append([1080 - 120, 420, 60, 60, GREEN, True, None])
    level[1].append([1080 - 360, 0, 360, 60, GREEN, True, None])
    level[1].append([1080 - 240, 60, 240, 60, GREEN, True, None])
    level[1].append([1080 - 120, 120, 120, 60, GREEN, True, None])
    level[1].append([450, 100, 60, 120, YELLOW, True, "finish"])

    level[2].append([0, 660, 1080, 60, GREEN, True, None])
    level[2].append([600, 480, 60, 180, GREEN, True, None])
    level[2].append([180, 480, 420, 60, GREEN, True, None])
    level[2].append([180, 300, 60, 180, GREEN, True, None])
    level[2].append([180, 180, 720, 120, GREEN, True, None])
    level[2].append([840, 300, 60, 240, GREEN, True, None])
    level[2].append([270, 340, 60, 120, YELLOW, True, "finish"])

    level[3].append([0, 660, 1080, 60, GREEN, True, None])
    level[3].append([0, 120, 60, 540, GREEN, True, None])
    level[3].append([1020, 120, 60, 540, GREEN, True, None])
    level[3].append([240, 420, 600, 60, GREEN, True, None])
    level[3].append([240, 210, 60, 120, RED, True, None])
    level[3].append([780, 210, 60, 120, RED, True, None])
    level[3].append([240, 600, 120, 60, RED, True, "kill"])
    level[3].append([720, 600, 120, 60, RED, True, "kill"])
    level[3].append([510, 280, 60, 120, YELLOW, True, "finish"])

    level[4].append([0, 660, 1080, 60, GREEN, True, None])
    level[4].append([630, 480, 60, 180, RED, True, None])
    level[4].append([630, 300, 60, 180, RED, True, "kill"])
    level[4].append([390, 300, 60, 180, RED, True, None])
    level[4].append([390, 480, 60, 180, RED, True, "kill"])
    level[4].append([540, 110, 60, 120, RED, True, "kill"])
    level[4].append([210, 150, 180, 60, RED, True, None])
    level[4].append([690, 300, 120, 60, RED, True, "kill"])
    level[4].append([0, 0, 60, 720, RED, True, None])
    level[4].append([720, 510, 60, 120, YELLOW, True, "finish"])

    level[5].append([210, 570, 120, 120, RED, True, "kill"])
    level[5].append([660, 270, 60, 540, RED, True, "kill"])
    level[5].append([0, 660, 720, 60, GREEN, True, None])
    level[5].append([120, 120, 60, 600, RED, True, None])
    level[5].append([180, 480, 60, 60, RED, True, None])
    level[5].append([360, 360, 480, 60, GREEN, True, None])
    level[5].append([780, 300, 60, 120, RED, True, None])
    level[5].append([1020, 120, 60, 600, RED, True, None])
    level[5].append([180, 120, 420, 60, GREEN, True, None])
    level[5].append([960, 120, 60, 60, GREEN, True, None])
    level[5].append([360, 30, 120, 60, GREEN, True, "finish"])

    level[6].append([630, 570, 60, 120, GREEN, True, "kill"])
    level[6].append([780, 390, 60, 180, GREEN, True, "kill"])
    level[6].append([0, 660, 1080, 60, GREEN, True, None])
    level[6].append([150, 510, 540, 60, GREEN, True, None])
    level[6].append([840, 510, 120, 60, GREEN, True, None])
    level[6].append([0, 330, 300, 60, GREEN, True, None])
    level[6].append([300, 330, 180, 60, GREEN, True, "kill"])
    level[6].append([480, 330, 360, 60, GREEN, True, None])
    level[6].append([1020, 0, 60, 360, GREEN, True, None])
    level[6].append([180, 150, 840, 60, GREEN, True, None])
    level[6].append([600, 60, 120, 60, GREEN, True, "finish"])

    level[7].append([0, 660, 1080, 60, GREEN, True, None])
    level[7].append([120, 480, 180, 60, GREEN, True, None])
    level[7].append([450, 480, 180, 60, GREEN, True, None])
    level[7].append([780, 480, 180, 60, GREEN, True, None])
    level[7].append([285, 300, 180, 60, GREEN, True, None])
    level[7].append([615, 300, 180, 60, GREEN, True, None])
    level[7].append([120, 120, 180, 60, GREEN, True, None])
    level[7].append([450, 120, 180, 60, GREEN, True, None])
    level[7].append([780, 120, 180, 60, GREEN, True, None])
    level[7].append([480, 30, 120, 60, GREEN, True, "finish"])
    level[7].append([195, 300, 60, 60, GREEN, True, "kill"])
    level[7].append([825, 300, 60, 60, GREEN, True, "kill"])
    level[7].append([15, 300, 60, 60, GREEN, True, None])
    level[7].append([1005, 300, 60, 60, GREEN, True, None])

    level[8].append([0, 660, 1080, 60, GREEN, True, None])
    level[8].append([420, 300, 60, 360, GREEN, True, "kill"])
    level[8].append([480, 300, 360, 60, GREEN, True, "kill"])
    level[8].append([600, 240, 60, 60, GREEN, True, "kill"])
    level[8].append([600, 60, 60, 60, GREEN, True, "kill"])
    level[8].append([0, 0, 1080, 60, GREEN, True, None])
    level[8].append([600, 480, 60, 180, GREEN, True, None])
    level[8].append([780, 360, 60, 180, GREEN, True, "kill"])
    level[8].append([840, 480, 120, 60, GREEN, True, None])
    level[8].append([960, 300, 120, 60, GREEN, True, None])
    level[8].append([120, 480, 180, 60, GREEN, True, None])
    level[8].append([240, 60, 60, 420, GREEN, True, None])
    level[8].append([150, 330, 60, 120, GREEN, True, "finish"])

    level[9].append([240, 630, 180, 60, GREEN, True, "kill"])
    level[9].append([390, 300, 60, 60, GREEN, True, "kill"])
    level[9].append([540, 180, 60, 60, GREEN, True, "kill"])
    level[9].append([0, 660, 1080, 60, GREEN, True, None])
    level[9].append([600, 480, 60, 180, GREEN, True, None])
    level[9].append([720, 180, 60, 420, GREEN, True, None])
    level[9].append([0, 0, 1080, 60, GREEN, True, None])
    level[9].append([120, 120, 660, 60, GREEN, True, None])
    level[9].append([300, 360, 480, 60, GREEN, True, None])
    level[9].append([120, 480, 480, 60, GREEN, True, None])
    level[9].append([0, 0, 60, 660, GREEN, True, None])
    level[9].append([180, 180, 60, 300, GREEN, True, None])
    level[9].append([60, 300, 60, 60, GREEN, True, None])
    level[9].append([810, 180, 60, 60, GREEN, True, "kill"])
    level[9].append([990, 150, 60, 60, GREEN, True, None])
    level[9].append([900, 270, 60, 60, GREEN, True, None])
    level[9].append([870, 480, 240, 180, GREEN, True, "kill"])
    level[9].append([630, 210, 60, 120, GREEN, True, "finish"])
    return level