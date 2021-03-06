from Ganga.GPI import *
import inspect
import os


local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

j = Job(application=Gauss(
        version="v47r2",
        optsfile=local_dir + "/gauss-job.py",
        ))

j.name = "SciFi-tracking"
j.outputfiles = [DiracFile("*.sim")]

j.backend = Dirac()
#j.backend.settings['BannedSites'] = ['LCG.RRCKI.ru']

events = 1000
eventsperjob = 50

j.splitter = GaussSplitter(numberOfJobs=int(round(events*1.1/eventsperjob)),
                           eventsPerJob=eventsperjob)

#j.do_auto_resubmit = True

#j.prepare()
j.submit()
