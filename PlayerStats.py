class PlayerStats:
    def __init__(self, name, date, matchup, fg_pct, reb, assists, stl, blocks, tov, pts):
        self.name = name
        self.date = date
        self.matchup = matchup
        self.fg_pct = fg_pct
        self.reb = reb
        self.assists = assists
        self.stl = stl
        self.blocks = blocks
        self.tov = tov
        self.pts = pts


    def __str__(self):
        return self.name + ": " + str(self.pts)
