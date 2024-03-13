import ROOT
h = ROOT.TH1D(name = "h", title = "My histo", nbinsx = 100, xlow = -5, xup = 5)

h.FillRandom("gaus", ntimes = 5000)
h.Draw()
