class BowlingGameFrame:
    def __init__(self, pins=10, throws=2, is_bonus=False):
        self.rolls = []
        self.left_pins = pins
        self.left_throws = throws
        self.is_bonus = is_bonus

    def is_done(self):
        return self.left_pins == 0 or self.left_throws == 0

    def is_strike(self):
        return self.is_done() and self.left_throws > 0

    def is_spare(self):
        return self.is_done() and self.left_pins == 0 and self.left_throws == 0

    def roll(self, pins):
        if not self.is_done() and 0 <= pins <= self.left_pins:
            self.rolls.append(pins)
            self.left_pins -= pins
            self.left_throws -= 1
        else:
            raise ValueError('invalid roll')


class BowlingGame(object):
    MAX_REGULAR_FRAMES = 10
    MAX_EXTRA_FRAMES = 2

    def __init__(self):
        self.frames = dict()
        if len(self.frames) < self.MAX_REGULAR_FRAMES:
            self.current_frame = 1
            self.frames[self.current_frame] = BowlingGameFrame()

        self.game_over = False

    def roll(self, pins):
        if self.game_over:
            raise ValueError('game over')

        curr_frame = self.frames[self.current_frame]
        curr_frame.roll(pins)
        if curr_frame.is_done():
            if self.current_frame < self.MAX_REGULAR_FRAMES:
                self.current_frame += 1
                self.frames[self.current_frame] = BowlingGameFrame()
                return
            elif self.current_frame < self.MAX_REGULAR_FRAMES + self.MAX_EXTRA_FRAMES:
                if curr_frame.is_strike() or (curr_frame.is_spare() and not curr_frame.is_bonus):
                    self.current_frame += 1
                    self.frames[self.current_frame] = BowlingGameFrame(is_bonus=True)
                return
        
        self.game_over = True

    def score_frame(self, frame_id):
        frame0 = self.frames.get(frame_id)
        frame1 = self.frames.get(frame_id+1)
        frame2 = self.frames.get(frame_id+2)
        score_ = sum(frame0.rolls)

        if frame0.is_strike() and frame1 is not None:
            if frame1.is_strike() and frame2 is not None:
                score_ += 10 + frame2.rolls[0]
            else:
                score_ += sum(frame1.rolls)
        if frame0.is_spare() and frame1 is not None:
            score_ += frame1.rolls[0]
        return score_

    def score(self):
        if self.game_over:
            return sum(self.score_frame(i)
                       for i, f in self.frames.items()
                       if i <= self.MAX_REGULAR_FRAMES)
        else:
            raise IndexError('incomplete game')


if __name__ == '__main__':
    bg = BowlingGame()

